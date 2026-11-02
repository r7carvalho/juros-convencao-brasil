#!/usr/bin/env python3
"""Sistema de Contas Nacionais 2023 (IBGE) e séries de capital do Ipeadata (páginas 5.2, 5.4.1, 5.4.2, 5.4.3).

Lê as planilhas .ods do FTP do IBGE (zipfile + content.xml, só biblioteca padrão) e os JSON do Ipeadata
gravados pelo coletor, confere os números das páginas e, com --gravar, refaz
dados/5.4.2-financeiras-x-transformacao.json (SCN anual em 2000–2023, SIDRA 1846 nos outros anos).

Uso: python3 tools/analises/5.4_scn2023.py [--gravar]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  scn/..._sinoticas__tabNN.ods           tabelas sinóticas do SCN 2023 (títulos impressos na seção 1)
  scn/..._tabelas_de_recursos_e_usos__*  TRU 2023 em 12 atividades x 12 produtos (12_tab1 a 12_tab4, resumo)
  scn/..._PIBReal_1947_2023.ods          PIB real, variação anual
  sidra-pib_trimestral_correntes.json    SIDRA 1846, valores correntes por trimestre
  sgs-4390.json, sgs-433.json            Selic e IPCA mensais (juro real ex-post dezembro a dezembro)
  ipea-*.json, ipea-metadados-selecionados.json   Ipeadata (taxa de investimento, FBCF trimestral,
                                         depreciação de construção e de máquinas)
  insumos/frente-L.json                  estoque de máquinas do Ipeadata (DIMAC_CFELCMQEQ, consulta em
                                         28/10/2026), só para a taxa implícita de depreciação

Observações sobre as planilhas
  - 12_tab2_2023 e 12_tab4_2023 trazem abas antigas (2m02, 2n02, 2o02) com a TRU de 2001 em 55 atividades;
    o script só lê as abas de 2023 (CI, demanda, VA).
  - A edição de 2023 saiu reduzida (transição para a referência 2021): remunerações e excedente nas
    TRU vêm zerados, e a ótica da renda da tabela 5 está vazia em 2022–2023.
"""
import json
import math
import os
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
SCN = os.path.join(BRUTOS, "scn")
PREF = "Sistema_de_Contas_Nacionais__2023__tabelas_ods__"
CONSULTA = "2026-11-02"

NS_T = "{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
NS_O = "{urn:oasis:names:tc:opendocument:xmlns:office:1.0}"
NS_X = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"


# ---------------------------------------------------------------- leitura de .ods
def _valor(c):
    if c.get(NS_O + "value-type") in ("float", "percentage", "currency"):
        return float(c.get(NS_O + "value"))
    s = "\n".join("".join(p.itertext()) for p in c.iter(NS_X + "p")).strip()
    return s or None


def ler_ods(caminho, max_cols=200):
    """Devolve {aba: [linhas]} com células numéricas como float e texto como str."""
    with zipfile.ZipFile(caminho) as z:
        raiz = ET.fromstring(z.read("content.xml"))
    abas = {}
    for tb in raiz.iter(NS_T + "table"):
        linhas = []
        for r in tb.iter(NS_T + "table-row"):
            linha = []
            for c in r:
                if c.tag not in (NS_T + "table-cell", NS_T + "covered-table-cell"):
                    continue
                n = int(c.get(NS_T + "number-columns-repeated", "1"))
                linha.extend([_valor(c)] * min(n, max_cols))
            while linha and linha[-1] is None:
                linha.pop()
            rep = int(r.get(NS_T + "number-rows-repeated", "1"))
            linhas.extend([list(linha) for _ in range(rep if linha else 1)])
        while linhas and not linhas[-1]:
            linhas.pop()
        abas[tb.get(NS_T + "name")] = linhas
    return abas


def sinotica(nome):
    return ler_ods(os.path.join(SCN, PREF + "sinoticas__" + nome + ".ods"))["Plan1"]


def tru(nome):
    return ler_ods(os.path.join(SCN, PREF + "tabelas_de_recursos_e_usos__" + nome + ".ods"))


def linha_rotulo(linhas, rotulo, col=0):
    for r in linhas:
        if len(r) > col and isinstance(r[col], str) and r[col].strip().startswith(rotulo):
            return r
    raise KeyError(rotulo)


# ---------------------------------------------------------------- outras fontes
def sidra_anual(ano_ini=1996):
    """SIDRA 1846: soma dos trimestres por ano e componente; 2026 = 1º semestre."""
    with open(os.path.join(BRUTOS, "sidra-pib_trimestral_correntes.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"][1:]
    s = defaultdict(float)
    n = defaultdict(set)
    for x in dados:
        a = int(x["D3C"][:4])
        if a >= ano_ini and x["V"] not in ("", "...", "-"):
            s[(a, x["D4N"])] += float(x["V"])
            n[a].add(x["D3C"])
    return s, {a: len(q) for a, q in n.items()}


def sgs(cod):
    with open(os.path.join(BRUTOS, f"sgs-{cod}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = {}
    for r in dados:
        if r["valor"] in ("", None):
            continue
        _, m, a = r["data"].split("/")
        out[(int(a), int(m))] = float(r["valor"])
    return out


def juro_real_dez(ano, selic, ipca):
    fs = math.prod(1 + selic[(ano, m)] / 100 for m in range(1, 13))
    fi = math.prod(1 + ipca[(ano, m)] / 100 for m in range(1, 13))
    return (fs / fi - 1) * 100


def ipea(cod):
    with open(os.path.join(BRUTOS, f"ipea-{cod}.json"), encoding="utf-8") as f:
        d = json.load(f)["dados"]
    return {x["VALDATA"][:7]: x["VALVALOR"] for x in d if x["VALVALOR"] is not None}


def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy)


# ---------------------------------------------------------------- 1. títulos das sinóticas
def secao_sinoticas():
    print("== 1. Tabelas sinóticas coletadas (título na primeira linha) ==")
    nomes = sorted(f.split("sinoticas__")[1][:-4] for f in os.listdir(SCN)
                   if f.startswith(PREF + "sinoticas__") and f.endswith(".ods"))
    setorial = []
    for n in nomes:
        linhas = sinotica(n)
        titulo = " ".join(str(r[0]) for r in linhas[:2] if r and isinstance(r[0], str))
        print(f"  {n:8s} {titulo}")
        texto = " ".join(str(c) for r in linhas for c in r if isinstance(c, str)).lower()
        # "juros" sozinho pegaria a linha da Selic na tabela 1; procura os termos das contas por setor
        if any(k in texto for k in ("setor institucional", "setores institucionais", "renda de propriedade",
                                    "juros pagos", "juros recebidos", "d.41", "sociedades financeiras")):
            setorial.append(n)
    print("  Tabelas com setor institucional, renda de propriedade ou juros:", setorial or "nenhuma")
    t1 = sinotica("tab01")
    anos = [int(a) for a in t1[4][1:]]
    cap = linha_rotulo(t1, "Capacidade (+)")
    pou = linha_rotulo(t1, "Poupança/PIB")
    print("  Tab. 1, economia como um todo, 2023: capacidade(+)/necessidade(-) de financiamento/PIB =",
          cap[1 + anos.index(2023)], "; poupança/PIB =", round(pou[1 + anos.index(2023)], 2))
    print()


# ---------------------------------------------------------------- 2. TRU 2023
def secao_tru():
    print("== 2. TRU 2023 (SCN anual) contra as Contas Trimestrais (SIDRA 1846, soma de 2023) ==")
    t1 = tru("12_tab1_2023")
    t2 = tru("12_tab2_2023")
    prod = linha_rotulo(t1["producao"], "Total")
    ofer = linha_rotulo(t1["oferta"], "Total")
    imp = linha_rotulo(t1["importacao"], "Total")
    ci = linha_rotulo(t2["CI"], "Total")
    dem = linha_rotulo(t2["demanda"], "Total")
    va = linha_rotulo(t2["VA"], "Valor adicionado bruto")
    ativ = [str(c).split("\n", 1)[1].replace("\n", " ") for c in t1["producao"][3][2:14]]
    P, CI, M, T = prod[14], ci[14], imp[2], ofer[9]
    VA = va[13]
    X, G, ISFL, C, FBCF, DE = dem[2:8]
    PIB = VA + T
    print(f"  Produção {P:,.1f}  CI {CI:,.1f}  VA {VA:,.1f}  (P - CI = {P - CI:,.1f})")
    print(f"  Impostos líquidos s/ produtos {T:,.1f} (imp. importação {ofer[5]:,.1f}, IPI {ofer[6]:,.1f}, "
          f"ICMS {ofer[7]:,.1f}, outros {ofer[8]:,.1f})  Importações {M:,.1f}")
    print(f"  Margens: comércio {ofer[3]:,.1f}, transporte {ofer[4]:,.1f} (somam zero no total)")
    print(f"  Recursos P+M+T = {P + M + T:,.1f}; oferta a preço de consumidor = {ofer[2]:,.1f}")
    usos = CI + C + ISFL + G + FBCF + DE + X
    print(f"  Usos CI+C+G+FBCF+DE+X = {usos:,.1f}; PIB = {PIB:,.1f}")
    print(f"  CI/produção = {CI / P * 100:.1f}%; VA/produção = {VA / P * 100:.1f}%; M/oferta = "
          f"{M / (P + M + T) * 100:.1f}%; T/PIB = {T / PIB * 100:.1f}%")
    print("  Por atividade (R$ bi): produção, CI, VA, VA/produção")
    for i, a in enumerate(ativ):
        p, c, v = t2["VA"][17][1 + i], ci[2 + i], va[1 + i]
        print(f"    {a[:45]:45s} {p / 1e3:9.1f} {c / 1e3:9.1f} {v / 1e3:9.1f} {v / p * 100:5.1f}%")
    s, _ = sidra_anual(2023)
    pares = [("VA", VA, "Valor adicionado a preços básicos"), ("Impostos", T, "Impostos líquidos sobre produtos"),
             ("PIB", PIB, "PIB a preços de mercado"), ("C famílias", C, "Despesa de consumo das famílias"),
             ("G", G, "Despesa de consumo da administração pública"), ("FBCF", FBCF, "Formação bruta de capital fixo"),
             ("Var. estoque", DE, "Variação de estoque"), ("X", X, "Exportação de bens e serviços"),
             ("M", M, "Importação de bens e serviços (-)"),
             ("VA financeiras", va[9], "Atividades financeiras, de seguros e serviços relacionados"),
             ("VA transformação", va[3], "Indústrias de transformação")]
    print("  Componente: anual (TRU) | trimestral (SIDRA 1846) | diferença, R$ milhões")
    for nome, anual, chave in pares:
        tri = s[(2023, chave)]
        print(f"    {nome:18s} {anual:14,.1f} {tri:14,.1f} {anual - tri:8,.1f}")
    # conta de bens e serviços 2000-2023 (tab. 2) e PIB real
    t2s = sinotica("tab02")
    anos = [int(a) for a in t2s[4][:24]]
    i23 = anos.index(2023)
    print("  Tab. 2 (conta de bens e serviços), 2023: produção", round(t2s[5][i23], 1), "; CI",
          round(t2s[9][25 + i23], 1), "; importação", round(t2s[6][i23], 1), "; impostos", round(t2s[7][i23], 1))
    for a in (2000, 2010, 2022, 2023):
        j = anos.index(a)
        print(f"    {a}: CI/produção = {t2s[9][25 + j] / t2s[5][j] * 100:.1f}%; "
              f"importação/PIB = {t2s[6][j] / (t2s[5][j] - t2s[9][25 + j] + t2s[7][j] + (t2s[8][j] or 0)) * 100:.1f}%")
    pr = ler_ods(os.path.join(SCN, PREF + "PIBReal_1947_2023.ods"))["Dados"]
    print("  PIB real 2023 (PIBReal_1947_2023):", [round(r[1], 2) for r in pr if r and r[0] == 2023.0][0], "%")
    t6 = sinotica("tab06")
    r23 = [r for r in t6 if r and r[0] == 2023.0][0]
    print(f"  Tab. 6, 2023: PIB {r23[1]:,.2f}; volume {r23[3]:.2f}%; deflator {r23[4]:.2f}%; per capita {r23[6]:,.2f}")
    t9 = sinotica("tab09")
    print("  Tab. 9, 2023 (variação em volume %, contribuição p.p.):")
    for r in t9[6:21]:
        print(f"    {str(r[1] if isinstance(r[1], str) else r[0])[:50]:50s} {r[-2]:6.2f} {r[-1]:6.2f}")
    print()


# ---------------------------------------------------------------- 3. participação no VA
def serie_tab13():
    t = sinotica("tab13_1")
    anos = [int(a) for a in t[4][2:]]
    fin = linha_rotulo(t, "Atividades financeiras", col=1)[2:]
    tra = linha_rotulo(t, "Indústrias de transformação", col=1)[2:]
    return dict(zip(anos, fin)), dict(zip(anos, tra))


def secao_va(gravar):
    print("== 3. Participação no VA: SCN anual (tab. 13.1) contra SIDRA 1846 ==")
    fin_a, tra_a = serie_tab13()
    s, nq = sidra_anual(1996)
    anos_s = sorted(nq)
    fin_s = {a: s[(a, "Atividades financeiras, de seguros e serviços relacionados")]
             / s[(a, "Valor adicionado a preços básicos")] * 100 for a in anos_s}
    tra_s = {a: s[(a, "Indústrias de transformação")] / s[(a, "Valor adicionado a preços básicos")] * 100
             for a in anos_s}
    difmax = 0.0
    for a in sorted(fin_a):
        d1, d2 = fin_a[a] - fin_s[a], tra_a[a] - tra_s[a]
        difmax = max(difmax, abs(d1), abs(d2))
        marca = "" if round(fin_a[a], 1) == round(fin_s[a], 1) and round(tra_a[a], 1) == round(tra_s[a], 1) else "  <- arredonda diferente"
        print(f"  {a}: financeiras {fin_a[a]:.3f} x {fin_s[a]:.3f}; transformação {tra_a[a]:.3f} x {tra_s[a]:.3f}{marca}")
    print(f"  Maior diferença absoluta 2000-2023: {difmax:.4f} ponto")
    # série combinada: SIDRA 1846 em 1996-1999 e 2024-2026; SCN anual em 2000-2023
    fin = {a: (fin_a[a] if a in fin_a else fin_s[a]) for a in anos_s}
    tra = {a: (tra_a[a] if a in tra_a else tra_s[a]) for a in anos_s}
    selic, ipca = sgs(4390), sgs(433)
    jr = {a: juro_real_dez(a, selic, ipca) for a in range(1996, 2026)}
    for ini in (1996, 2000):
        anos = list(range(ini, 2026))
        print(f"  Correlação finanças (série combinada) x juro real ex-post, {ini}-2025: "
              f"{corr([fin[a] for a in anos], [jr[a] for a in anos]):.3f}")
    print("  Médias por período (finanças, juro real):")
    for a0, a1 in ((1996, 1999), (2000, 2009), (2010, 2014), (2015, 2019), (2020, 2022), (2023, 2025)):
        r = range(a0, a1 + 1)
        print(f"    {a0}-{a1}: {sum(fin[a] for a in r) / len(r):.2f} / {sum(jr[a] for a in r) / len(r):.2f}")
    # volume e preço do VA das financeiras (tabelas 11.1 e 12.1)
    t11, t12 = sinotica("tab11_1"), sinotica("tab12_1")
    anos_v = [int(a) for a in t11[4] if isinstance(a, float)]
    def valores(linhas, rotulo):
        r = linha_rotulo(linhas, rotulo, col=1)
        return dict(zip(anos_v, [x for x in r[2:] if isinstance(x, float)]))
    vol_f = valores(t11, "Atividades financeiras")
    pre_f = valores(t12, "Atividades financeiras")
    pre_t = valores(t12, "Total")
    print("  VA das financeiras: volume (%), preço (%), preço do VA total (%), preço relativo (%)")
    rel = {}
    for a in anos_v:
        rel[a] = ((1 + pre_f[a] / 100) / (1 + pre_t[a] / 100) - 1) * 100
        print(f"    {a}: {vol_f[a]:6.1f} {pre_f[a]:6.1f} {pre_t[a]:6.1f} {rel[a]:6.1f}")
    selic_ano = {a: (math.prod(1 + selic[(a, m)] / 100 for m in range(1, 13)) - 1) * 100 for a in range(2000, 2024)}
    anos = list(range(2001, 2024))
    print(f"  Correlação preço relativo do VA financeiro x variação da Selic do ano (pontos), 2001-2023: "
          f"{corr([rel[a] for a in anos], [selic_ano[a] - selic_ano[a - 1] for a in anos]):.3f}")
    print(f"  Correlação volume do VA financeiro x variação da Selic, 2001-2023: "
          f"{corr([vol_f[a] for a in anos], [selic_ano[a] - selic_ano[a - 1] for a in anos]):.3f}")
    if gravar:
        caminho = os.path.join(ROOT, "dados", "5.4.2-financeiras-x-transformacao.json")
        with open(caminho, encoding="utf-8") as f:
            js = json.load(f)
        def rot(a):
            return f"{a}-06" if nq[a] == 2 else str(a)
        js["series"] = [
            {"nome": "Indústria de transformação",
             "pontos": [{"t": rot(a), "v": round(tra[a], 1)} for a in anos_s]},
            {"nome": "Atividades financeiras, seguros e relacionados",
             "pontos": [{"t": rot(a), "v": round(fin[a], 1)} for a in anos_s]},
        ]
        js["fonte"] = ("IBGE, Sistema de Contas Nacionais 2023, tabela sinótica 13.1 (participação no valor "
                       "adicionado bruto a preços básicos), para 2000–2023; IBGE, Contas Nacionais Trimestrais, "
                       "SIDRA 1846, valores correntes, soma dos trimestres, para 1996–1999 e 2024–2026; cálculo do "
                       "painel (tools/analises/5.4_scn2023.py), consulta em 02/11/2026")
        js["url"] = ("https://ftp.ibge.gov.br/Contas_Nacionais/Sistema_de_Contas_Nacionais/2023/tabelas_ods/"
                     "sinoticas/tab13_1.ods")
        js["consulta"] = CONSULTA
        difmax_txt = f"{difmax:.2f}".replace(".", ",")
        js["nota"] = ("Preços correntes. 2026-06 = 1º semestre de 2026. Em 2000–2023 os valores são os da tabela "
                      "13.1 do SCN anual; a participação calculada com o SIDRA 1846 coincide com ela na primeira "
                      f"casa decimal em todos esses anos (maior diferença: {difmax_txt} ponto). Antes de 2000 e "
                      "depois de 2023 só há as Contas Trimestrais.")
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(js, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("  gravado:", os.path.relpath(caminho, ROOT))
    print()


# ---------------------------------------------------------------- 4. Ipeadata
def secao_ipea():
    print("== 4. Ipeadata: taxa de investimento, FBCF trimestral, depreciação ==")
    with open(os.path.join(BRUTOS, "ipea-metadados-selecionados.json"), encoding="utf-8") as f:
        meta = {m["SERCODIGO"]: m for m in json.load(f)["dados"]}
    for cod in ("DIMAC_CFELCTOT", "DIMAC_CFELCMQEQ", "DIMAC_CFRCP", "DIMAC_CFDPRMQEQ", "DIMAC_CFINVLQMQEQ",
                "PAN_FBKFPIBV"):
        m = meta.get(cod)
        tem = os.path.exists(os.path.join(BRUTOS, f"ipea-{cod}.json"))
        print(f"  {cod:18s} valores coletados: {'sim' if tem else 'não'}; {m['SERNOME']} | "
              f"{m['UNINOME']} {m['MULNOME'] or ''} | atualizada em {m['SERATUALIZACAO'][:10]}")
    pan = ipea("PAN_FBKFPIBV")
    t7 = sinotica("tab07")
    tab7 = {int(r[0]): r[4] for r in t7 if r and isinstance(r[0], float)}
    s, nq = sidra_anual(1996)
    dif = []
    for a in range(1996, 2026):
        sid = s[(a, "Formação bruta de capital fixo")] / s[(a, "PIB a preços de mercado")] * 100
        p = pan[f"{a}-01"]
        t = tab7.get(a)
        dif.append(abs(round(p, 1) - round(sid, 1)))
        if a in (1996, 2013, 2017, 2022, 2023, 2024, 2025):
            print(f"  FBCF/PIB {a}: Ipeadata PAN_FBKFPIBV {p:.2f}; SCN tab. 7 {t if t is None else round(t, 2)}; "
                  f"SIDRA 1846 {sid:.2f}")
    print(f"  Maior diferença PAN_FBKFPIBV x SIDRA 1846 (uma casa) em 1996-2025: {max(dif):.1f}")
    tri = ipea("PAN4_FBKFPIBV4")
    vol = ipea("SCN104_FBKFG104")
    nom = ipea("SCN104_FBKFN104")
    sem = {a: [nom[f"{a}-01"], nom[f"{a}-04"]] for a in (2025, 2026)}
    print("  FBCF nominal, 1º semestre (SCN104_FBKFN104, R$ mi):", {a: round(sum(v), 1) for a, v in sem.items()})
    print("  Taxa de investimento trimestral (PAN4_FBKFPIBV4) 2025T1,T2 / 2026T1,T2:",
          tri["2025-01"], tri["2025-04"], "/", tri["2026-01"], tri["2026-04"])
    print("  FBCF, variação real sobre o mesmo trimestre (SCN104_FBKFG104) 2026T1, T2:",
          vol["2026-01"], vol["2026-04"])
    dep_m = ipea("DIMAC_CFDPRMQEQ")
    dep_c = ipea("DIMAC_CFDPRCTR")
    with open(os.path.join(ROOT, "insumos", "frente-L.json"), encoding="utf-8") as f:
        fl = json.load(f)
    est = [x for x in fl["series"] if "DIMAC_CFELCMQEQ" in x.get("fonte", "") and "trilh" in x.get("unidade", "")][0]
    km = {int(p["t"]): p["v"] * 1e6 for p in est["pontos"]}  # R$ milhões de 2025
    print("  Depreciação de máquinas (DIMAC_CFDPRMQEQ, R$ bi de 2025) e taxa implícita sobre o estoque do fim do "
          "ano anterior (DIMAC_CFELCMQEQ):")
    for a in (1995, 2005, 2014, 2019, 2021, 2022, 2023, 2024, 2025):
        print(f"    {a}: {dep_m[f'{a}-01'] / 1e3:7.1f}  {dep_m[f'{a}-01'] / km[a - 1] * 100:5.1f}%   "
              f"estoque {km[a] / 1e6:.2f} tri; variação {(km[a] - km[a - 1]) / 1e6:+.2f}")
    print(f"  Depreciação de construção (DIMAC_CFDPRCTR) 2025: R$ {dep_c['2025-01'] / 1e3:.1f} bi de 2025; "
          f"máquinas: R$ {dep_m['2025-01'] / 1e3:.1f} bi")
    print()


def main():
    gravar = "--gravar" in sys.argv
    secao_sinoticas()
    secao_tru()
    secao_va(gravar)
    secao_ipea()


if __name__ == "__main__":
    main()

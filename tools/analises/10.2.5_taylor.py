#!/usr/bin/env python3
"""Regra de Taylor aplicada ao Brasil, 2003-2026 (página 10.2.5 do painel).

Reproduz as contas da página "Regra de Taylor e os modelos do BC" e grava os JSON dos gráficos
em dados/10.2.5-*.json. Só usa a biblioteca padrão e numpy.

Uso: python3 tools/analises/10.2.5_taylor.py [--resumo]

Entradas (dados/brutos/, coleta de 02/11/2026):
  sgs-432.json            Selic meta definida pelo Copom (% a.a.), diária
  sgs-13522.json          IPCA acumulado em 12 meses (%), mensal
  sgs-24364.json          IBC-Br com ajuste sazonal (índice), mensal
  focus-inflacao_12m.json Focus, IPCA 12 meses à frente (mediana), diária

Método
  Regra de Taylor (1993):   i = r* + pi + 0,5 (pi - meta) + 0,5 h
  Versão "IPCA":   pi = IPCA dos 12 meses encerrados no mês (SGS 13522)
  Versão "Focus":  pi = mediana Focus do IPCA 12 meses à frente, série suavizada, base de 30 dias,
                   último dia do mês com registro
  Meta: centro fixado pelo CMN. Para o IPCA 12 meses encerrado no mês m do ano Y, média das metas
        de Y e Y-1 ponderada pelos meses de cada ano na janela (m/12 e (12-m)/12). Para a
        expectativa 12 meses à frente, média das metas de Y e Y+1 ponderada da mesma forma.
        2003 usa a meta oficial de 4,0% (o BC trabalhou com "meta ajustada" de 8,5%).
        Desde 2025, meta contínua de 3,0%.
  Hiato h: aproximação do painel, não o hiato do BC. Filtro HP (lambda = 129.600, padrão mensal)
        sobre 100 x ln(IBC-Br dessazonalizado), jan/2003 a ago/2026; o hiato mensal é a média
        móvel de 3 meses (mês e dois anteriores) da distância entre o índice e a tendência.
        Problemas conhecidos: viés de fim de amostra do filtro HP e distorção da tendência pelo
        tombo de 2020.
  r*: duas versões, 4,5% (hipótese do Copom até mai/2024) e 5,0% (desde dez/2024).
  Selic: meta vigente no último dia do mês (SGS 432).
  Juro neutro implícito: o r* que faz a regra igual à Selic, Selic - [pi + 0,5 (pi - meta) + 0,5 h].
  Variantes: "balanced approach" (peso 1,0 no hiato) e regra com suavização
        i_t = rho i_{t-1} + (1 - rho) i*_t, rho = 0,8 por trimestre (0,8^(1/3) por mês).
"""
import json
import os
import sys
from collections import OrderedDict, defaultdict

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
SAIDA = os.path.join(ROOT, "dados")
CONSULTA = "2026-11-02"

METAS = {2002: 3.5, 2003: 4.0, 2004: 5.5, 2005: 4.5}
METAS.update({a: 4.5 for a in range(2006, 2019)})
METAS.update({2019: 4.25, 2020: 4.0, 2021: 3.75, 2022: 3.5, 2023: 3.25})
METAS.update({a: 3.0 for a in range(2024, 2029)})

INICIO, FIM = (2003, 1), (2026, 8)
RSTAR = (4.5, 5.0)


def carregar(nome):
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        return json.load(f)["dados"]


def chave(data_br):
    d, m, a = data_br.split("/")
    return int(a), int(m)


def meses():
    a, m = INICIO
    while (a, m) <= FIM:
        yield a, m
        m += 1
        if m == 13:
            a, m = a + 1, 1


def selic_fim_mes():
    out = {}
    for x in carregar("sgs-432.json"):
        d, m, a = x["data"].split("/")
        out[(int(a), int(m))] = float(x["valor"])  # o último dia do mês sobrescreve
    return out


def mensal(nome):
    return {chave(x["data"]): float(x["valor"]) for x in carregar(nome)}


def focus_fim_mes():
    out = {}
    regs = [x for x in carregar("focus-inflacao_12m.json")
            if x["Suavizada"] == "S" and x.get("baseCalculo") == 0]
    regs.sort(key=lambda x: x["Data"])
    for x in regs:
        a, m, _ = x["Data"].split("-")
        out[(int(a), int(m))] = float(x["Mediana"])
    return out


def hp(y, lam):
    n = len(y)
    D = np.zeros((n - 2, n))
    for i in range(n - 2):
        D[i, i], D[i, i + 1], D[i, i + 2] = 1.0, -2.0, 1.0
    return np.linalg.solve(np.eye(n) + lam * D.T @ D, y)


def hiato_mensal():
    ibc = mensal("sgs-24364.json")
    ks = [k for k in meses() if k in ibc]
    y = 100 * np.log(np.array([ibc[k] for k in ks]))
    tend = hp(y, 129600.0)
    bruto = y - tend
    suave = [float(np.mean(bruto[max(0, i - 2):i + 1])) for i in range(len(bruto))]
    return dict(zip(ks, suave)), dict(zip(ks, bruto.tolist()))


def meta_passada(a, m):
    return (m / 12) * METAS[a] + ((12 - m) / 12) * METAS[a - 1]


def meta_futura(a, m):
    return ((12 - m) / 12) * METAS[a] + (m / 12) * METAS[a + 1]


def calcular():
    selic, ipca, focus = selic_fim_mes(), mensal("sgs-13522.json"), focus_fim_mes()
    hiato, hiato_bruto = hiato_mensal()
    linhas = []
    for a, m in meses():
        k = (a, m)
        if not all(k in s for s in (selic, ipca, focus, hiato)):
            continue
        h = hiato[k]
        p, pe = ipca[k], focus[k]
        mp, mf = meta_passada(a, m), meta_futura(a, m)
        base_ipca = p + 0.5 * (p - mp) + 0.5 * h
        base_focus = pe + 0.5 * (pe - mf) + 0.5 * h
        r = OrderedDict(t=f"{a}-{m:02d}", selic=selic[k], ipca=p, focus=pe, meta_ipca=mp,
                        meta_focus=mf, hiato=h, hiato_bruto=hiato_bruto[k])
        for rs in RSTAR:
            r[f"taylor_ipca_{rs}"] = rs + base_ipca
            r[f"taylor_focus_{rs}"] = rs + base_focus
        r["balanced_focus_5.0"] = 5.0 + pe + 0.5 * (pe - mf) + 1.0 * h
        r["neutro_impl_ipca"] = selic[k] - base_ipca
        r["neutro_impl_focus"] = selic[k] - base_focus
        linhas.append(r)
    # regra com suavização (versão Focus, r* = 5), partindo da Selic de jan/2003
    rho = 0.8 ** (1 / 3)
    ant = linhas[0]["selic"]
    for r in linhas:
        ant = rho * ant + (1 - rho) * r["taylor_focus_5.0"]
        r["suavizada_focus_5.0"] = ant
    return linhas


def media(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def por_ano(linhas, campo):
    g = defaultdict(list)
    for r in linhas:
        g[r["t"][:4]].append(campo(r))
    return OrderedDict((a, media(v)) for a, v in sorted(g.items()))


PERIODOS = [("2003–2005", 2003, 2005), ("2006–2010", 2006, 2010), ("2011–2012", 2011, 2012),
            ("2013–2016", 2013, 2016), ("2017–2019", 2017, 2019), ("2020–2021", 2020, 2021),
            ("2022–2024", 2022, 2024), ("2025–2026", 2025, 2026)]


def por_periodo(linhas, campo):
    out = OrderedDict()
    for nome, a0, a1 in PERIODOS:
        out[nome] = media([campo(r) for r in linhas if a0 <= int(r["t"][:4]) <= a1])
    return out


def r2(x):
    return None if x is None else round(x, 2)


def gravar(nome, obj):
    with open(os.path.join(SAIDA, nome), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


FONTE = ("BCB, SGS 432 (Selic meta), 13522 (IPCA 12 meses) e 24364 (IBC-Br dessazonalizado); "
         "BCB, Focus, API Olinda (IPCA 12 meses à frente); metas do CMN; cálculo do painel "
         "(tools/analises/10.2.5_taylor.py)")
URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json"


def escrever_json(linhas):
    ult = linhas[-1]["t"]
    nota_base = (
        "Regra de Taylor (1993): i = r* + π + 0,5(π − meta) + 0,5·hiato. "
        "Hiato: aproximação do painel (filtro HP, λ = 129.600, sobre o log do IBC-Br dessazonalizado, "
        "jan/2003 a ago/2026, média móvel de 3 meses); não é o hiato do BC, tem viés de fim de amostra "
        "e a tendência é distorcida pelo tombo de 2020. Meta: centro do CMN ponderado pelos meses da "
        "janela de 12 meses (2003 com a meta oficial de 4%, não a 'ajustada' de 8,5%). Selic: meta "
        f"vigente no fim do mês. Último mês: {ult}.")
    g1 = {
        "titulo": "Selic e regra de Taylor com o IPCA de 12 meses, dois valores de juro neutro (% a.a.)",
        "tipo": "linha", "unidade": "% a.a.", "fonte": FONTE, "url": URL, "consulta": CONSULTA,
        "nota": nota_base + " π = IPCA acumulado em 12 meses (SGS 13522), como no artigo de Taylor.",
        "governos": True,
        "series": [
            {"nome": "Selic meta", "pontos": [{"t": r["t"], "v": r2(r["selic"])} for r in linhas]},
            {"nome": "Regra, r* = 5,0%", "pontos": [{"t": r["t"], "v": r2(r["taylor_ipca_5.0"])} for r in linhas]},
            {"nome": "Regra, r* = 4,5%", "pontos": [{"t": r["t"], "v": r2(r["taylor_ipca_4.5"])} for r in linhas]},
        ],
    }
    gravar("10.2.5-selic-regra-taylor.json", g1)

    anos_ipca = por_ano(linhas, lambda r: r["selic"] - r["taylor_ipca_5.0"])
    anos_focus = por_ano(linhas, lambda r: r["selic"] - r["taylor_focus_5.0"])
    g2 = {
        "titulo": "Selic menos a regra de Taylor, média do ano, r* = 5% (p.p.)",
        "tipo": "barras", "unidade": "p.p.", "fonte": FONTE, "url": URL, "consulta": CONSULTA,
        "nota": nota_base + " Versão IPCA: inflação dos 12 meses passados. Versão Focus: mediana da "
                "inflação esperada para os 12 meses seguintes (série suavizada) e meta dos 12 meses "
                "seguintes. Com r* = 4,5% todas as barras sobem 0,5 p.p. Valor positivo: Selic acima "
                "da regra. 2026 vai de janeiro a agosto.",
        "ref": [{"v": 0, "rotulo": "Selic = regra"}],
        "series": [
            {"nome": "Versão IPCA 12m", "pontos": [{"t": a, "v": r2(v)} for a, v in anos_ipca.items()]},
            {"nome": "Versão Focus 12m", "pontos": [{"t": a, "v": r2(v)} for a, v in anos_focus.items()]},
        ],
    }
    gravar("10.2.5-selic-menos-regra.json", g2)

    n_ipca = por_ano(linhas, lambda r: r["neutro_impl_ipca"])
    n_focus = por_ano(linhas, lambda r: r["neutro_impl_focus"])
    g3 = {
        "titulo": "Juro neutro implícito: o r* que faria a regra de Taylor igual à Selic, média do ano (% a.a.)",
        "tipo": "linha", "unidade": "% a.a.", "fonte": FONTE, "url": URL, "consulta": CONSULTA,
        "nota": nota_base + " Juro neutro implícito = Selic − [π + 0,5(π − meta) + 0,5·hiato]. "
                "As linhas horizontais marcam as hipóteses do Copom (4,5% até mai/2024; 5,0% desde dez/2024). "
                "2026 vai de janeiro a agosto.",
        "governos": True,
        "ref": [{"v": 4.5, "rotulo": "4,5%"}, {"v": 5.0, "rotulo": "5,0%"}],
        "series": [
            {"nome": "Com IPCA 12m", "pontos": [{"t": a, "v": r2(v)} for a, v in n_ipca.items()]},
            {"nome": "Com Focus 12m", "pontos": [{"t": a, "v": r2(v)} for a, v in n_focus.items()]},
        ],
    }
    gravar("10.2.5-neutro-implicito.json", g3)
    return anos_ipca, anos_focus, n_ipca, n_focus


def resumo(linhas, anos_ipca, anos_focus, n_ipca, n_focus):
    print("mês      selic  ipca  focus metaI metaF hiato | T_ipca5 T_foc5 | gapI5 gapF5")
    for r in linhas:
        if r["t"].endswith(("-06", "-12")) or r["t"] >= "2026-01":
            print(f"{r['t']}  {r['selic']:5.2f} {r['ipca']:5.2f} {r['focus']:5.2f} {r['meta_ipca']:5.2f} "
                  f"{r['meta_focus']:5.2f} {r['hiato']:5.2f} | {r['taylor_ipca_5.0']:6.2f} "
                  f"{r['taylor_focus_5.0']:6.2f} | {r['selic']-r['taylor_ipca_5.0']:5.2f} "
                  f"{r['selic']-r['taylor_focus_5.0']:5.2f}")
    print("\nano   gapIPCA5 gapFocus5 neutroI neutroF hiato_medio")
    hm = por_ano(linhas, lambda r: r["hiato"])
    for a in anos_ipca:
        print(f"{a}  {anos_ipca[a]:7.2f} {anos_focus[a]:8.2f} {n_ipca[a]:7.2f} {n_focus[a]:7.2f} {hm[a]:6.2f}")
    print("\nperíodo     gapIPCA5 gapFocus5 neutroI neutroF  balanced-Focus5  suav-Focus5")
    pi_ = por_periodo(linhas, lambda r: r["selic"] - r["taylor_ipca_5.0"])
    pf = por_periodo(linhas, lambda r: r["selic"] - r["taylor_focus_5.0"])
    ni = por_periodo(linhas, lambda r: r["neutro_impl_ipca"])
    nf = por_periodo(linhas, lambda r: r["neutro_impl_focus"])
    pb = por_periodo(linhas, lambda r: r["selic"] - r["balanced_focus_5.0"])
    ps = por_periodo(linhas, lambda r: r["selic"] - r["suavizada_focus_5.0"])
    for k in pi_:
        print(f"{k:10}  {pi_[k]:7.2f} {pf[k]:8.2f} {ni[k]:7.2f} {nf[k]:7.2f} {pb[k]:10.2f} {ps[k]:12.2f}")
    tot_i = media([r["selic"] - r["taylor_ipca_5.0"] for r in linhas])
    tot_f = media([r["selic"] - r["taylor_focus_5.0"] for r in linhas])
    acima_i = sum(1 for r in linhas if r["selic"] > r["taylor_ipca_5.0"])
    acima_f = sum(1 for r in linhas if r["selic"] > r["taylor_focus_5.0"])
    acima_f45 = sum(1 for r in linhas if r["selic"] > r["taylor_focus_4.5"])
    acima_i45 = sum(1 for r in linhas if r["selic"] > r["taylor_ipca_4.5"])
    n = len(linhas)
    print(f"\nmeses: {n}; média Selic-regra r*5: IPCA {tot_i:.2f}, Focus {tot_f:.2f}")
    print(f"meses com Selic acima da regra: IPCA r*5 {acima_i} ({100*acima_i/n:.0f}%), r*4,5 {acima_i45} "
          f"({100*acima_i45/n:.0f}%); Focus r*5 {acima_f} ({100*acima_f/n:.0f}%), r*4,5 {acima_f45} ({100*acima_f45/n:.0f}%)")
    print(f"neutro implícito médio: IPCA {media([r['neutro_impl_ipca'] for r in linhas]):.2f}, "
          f"Focus {media([r['neutro_impl_focus'] for r in linhas]):.2f}")
    # correlação Selic x regra
    s = np.array([r["selic"] for r in linhas])
    for c in ("taylor_ipca_5.0", "taylor_focus_5.0"):
        print(f"correlação Selic × {c}: {np.corrcoef(s, np.array([r[c] for r in linhas]))[0,1]:.2f}")
    # regressão simples Selic = a + b*pi_e + c*h (sem suavização)
    X = np.column_stack([np.ones(n), [r["focus"] - r["meta_focus"] for r in linhas], [r["hiato"] for r in linhas]])
    b = np.linalg.lstsq(X, s - np.array([r["focus"] for r in linhas]), rcond=None)[0]
    print(f"MQO (Selic - πe) = a + b(πe - meta) + c h: a={b[0]:.2f} b={b[1]:.2f} c={b[2]:.2f}")
    # mesma regressão por subperíodo (conta ilustrativa: MQO sem suavização, hiato do painel)
    for a0, a1 in ((2003, 2010), (2011, 2016), (2017, 2026)):
        R = [r for r in linhas if a0 <= int(r["t"][:4]) <= a1]
        y = np.array([r["selic"] - r["focus"] for r in R])
        X = np.column_stack([np.ones(len(R)), [r["focus"] - r["meta_focus"] for r in R], [r["hiato"] for r in R]])
        b = np.linalg.lstsq(X, y, rcond=None)[0]
        r2 = 1 - ((y - X @ b) ** 2).sum() / ((y - y.mean()) ** 2).sum()
        print(f"  {a0}-{a1} ({len(R)} meses): a={b[0]:.2f} b={b[1]:.2f} c={b[2]:.2f} R2={r2:.2f}")
    mn = min(linhas, key=lambda r: r["hiato"])
    print(f"hiato mínimo: {mn['t']} {mn['hiato']:.2f} (bruto {mn['hiato_bruto']:.2f})")


def main():
    linhas = calcular()
    res = escrever_json(linhas)
    if "--resumo" in sys.argv:
        resumo(linhas, *res)


if __name__ == "__main__":
    main()

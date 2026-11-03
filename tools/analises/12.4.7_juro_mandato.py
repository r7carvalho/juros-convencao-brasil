#!/usr/bin/env python3
"""Juro real por mandato presidencial e Selic contra a regra de Taylor por presidente do BC
(página 12.4.7 do painel).

Calcula, para cada mandato presidencial de 1995 a 2026: o juro real ex-post anualizado (Selic
acumulada sobre IPCA acumulado no mandato), a distância média para cinco emergentes na régua do
BIS, o juro real dos EUA na mesma régua, o resultado primário médio e a dívida bruta no início e
no fim. Calcula também a distância média entre a Selic e a regra de Taylor da página 10.2.5 por
presidente do Banco Central (2003-2026). Grava dados/12.4.7-juro-real-mandato.json. Só usa a
biblioteca padrão e, por meio do script da 10.2.5, numpy.

Uso: python3 tools/analises/12.4.7_juro_mandato.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  sgs-4390.json   Selic acumulada no mês (% a.m.)
  sgs-433.json    IPCA, variação mensal (%)
  sgs-5793.json   NFSP primária do setor público consolidado, 12 meses, % do PIB (positivo =
                  déficit); começa em nov/2002
  sgs-13762.json  Dívida bruta do governo geral, % do PIB; começa em dez/2006
  bis-politica_monetaria.csv, bis-cpi.csv   BIS, WS_CBPOL (fim do mês) e WS_LONG_CPI (variação
                  em 12 meses)
  tools/analises/10.2.5_taylor.py           regra de Taylor mensal (r* = 5%), 2003-ago/2026

Método
  Mandatos: FHC 1 jan/1995-dez/1998; FHC 2 jan/1999-dez/2002; Lula 1 2003-2006; Lula 2
    2007-2010; Dilma 1 2011-2014; Dilma 2 jan/2015-abr/2016 (afastamento em 12/05/2016); Temer
    mai/2016-dez/2018; Bolsonaro 2019-2022; Lula 3 jan/2023-set/2026 (último IPCA do acervo).
  Juro real ex-post do mandato: [prod(1 + Selic_m) / prod(1 + IPCA_m)]^(12/n) - 1, n meses.
  Régua BIS: para cada mês, (1 + taxa de política) / (1 + inflação em 12 meses) - 1; média dos
    meses do mandato. Pares: México, Chile, Colômbia, Índia e África do Sul (média simples), a
    mesma cesta da 2.1. Começa em jan/2000 (FHC 2 fica com 2000-2002).
  Primário: média mensal de -SGS 5793 nos meses do mandato (positivo = superávit); só quando a
    série cobre ao menos 3/4 dos meses (FHC fica sem dado).
  Taylor: média mensal de Selic - regra (versões IPCA 12m e Focus 12m, r* = 5%) por presidente
    do BC: Meirelles jan/2003-dez/2010; Tombini jan/2011-mai/2016; Goldfajn jun/2016-fev/2019;
    Campos Neto mar/2019-dez/2022 (governo Bolsonaro) e jan/2023-dez/2024 (governo Lula);
    Galípolo jan/2025-ago/2026.
"""
import csv
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
SAIDA = os.path.join(ROOT, "dados", "12.4.7-juro-real-mandato.json")
CONSULTA = "2026-11-02"

MANDATOS = [
    ("FHC 1", (1995, 1), (1998, 12)),
    ("FHC 2", (1999, 1), (2002, 12)),
    ("Lula 1", (2003, 1), (2006, 12)),
    ("Lula 2", (2007, 1), (2010, 12)),
    ("Dilma 1", (2011, 1), (2014, 12)),
    ("Dilma 2", (2015, 1), (2016, 4)),
    ("Temer", (2016, 5), (2018, 12)),
    ("Bolsonaro", (2019, 1), (2022, 12)),
    ("Lula 3", (2023, 1), (2026, 9)),
]

PRESIDENTES_BC = [
    ("Meirelles (Lula 1 e 2)", (2003, 1), (2010, 12)),
    ("Tombini (Dilma)", (2011, 1), (2016, 5)),
    ("Goldfajn (Temer e início de Bolsonaro)", (2016, 6), (2019, 2)),
    ("Campos Neto (Bolsonaro)", (2019, 3), (2022, 12)),
    ("Campos Neto (Lula 3)", (2023, 1), (2024, 12)),
    ("Galípolo (Lula 3)", (2025, 1), (2026, 8)),
]

PARES = ["MX", "CL", "CO", "IN", "ZA"]


def sgs(cod):
    with open(os.path.join(BRUTOS, f"sgs-{cod}.json"), encoding="utf-8") as f:
        d = json.load(f)["dados"]
    out = {}
    for x in d:
        if x.get("valor") in ("", None):
            continue
        _, m, a = x["data"].split("/")
        out[(int(a), int(m))] = float(x["valor"])
    return out


def bis(nome):
    out = {}
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["FREQ"] != "M" or r["OBS_VALUE"] in ("", "NaN"):
                continue
            a, m = r["TIME_PERIOD"].split("-")
            out.setdefault(r["REF_AREA"], {})[(int(a), int(m))] = float(r["OBS_VALUE"])
    return out


def meses(ini, fim):
    a, m = ini
    while (a, m) <= fim:
        yield (a, m)
        m += 1
        if m == 13:
            a, m = a + 1, 1


def media(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def real_bis(pol, cpi, pais, k):
    if k in pol.get(pais, {}) and k in cpi.get(pais, {}):
        return ((1 + pol[pais][k] / 100) / (1 + cpi[pais][k] / 100) - 1) * 100
    return None


def taylor():
    caminho = os.path.join(ROOT, "tools", "analises", "10.2.5_taylor.py")
    spec = importlib.util.spec_from_file_location("taylor_1025", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.calcular()


def calcular():
    selic, ipca, prim, dbgg = sgs(4390), sgs(433), sgs(5793), sgs(13762)
    pol, cpi = bis("bis-politica_monetaria.csv"), bis("bis-cpi.csv")
    linhas = []
    for nome, ini, fim in MANDATOS:
        ks = list(meses(ini, fim))
        fs = fp = 1.0
        for k in ks:
            fs *= 1 + selic[k] / 100
            fp *= 1 + ipca[k] / 100
        n = len(ks)
        real = ((fs / fp) ** (12 / n) - 1) * 100
        selic_aa = (fs ** (12 / n) - 1) * 100
        ipca_aa = (fp ** (12 / n) - 1) * 100
        kb = [k for k in ks if k >= (2000, 1)]
        br = media([real_bis(pol, cpi, "BR", k) for k in kb])
        pares = media([media([real_bis(pol, cpi, p, k) for p in PARES]) for k in kb])
        eua = media([real_bis(pol, cpi, "US", k) for k in kb])
        vp = [-prim[k] for k in ks if k in prim]
        pr = media(vp) if len(vp) >= 0.75 * n else None
        d_ini = dbgg.get((ini[0] - 1, 12)) if ini[1] == 1 else dbgg.get((ini[0], ini[1] - 1))
        d_fim = dbgg.get(fim)
        linhas.append(dict(nome=nome, ini=ini, fim=fim, meses=n, selic=selic_aa, ipca=ipca_aa,
                           real=real, bis_br=br, bis_pares=pares,
                           dist=(br - pares) if br is not None else None, eua=eua,
                           primario=pr, dbgg_ini=d_ini, dbgg_fim=d_fim))
    return linhas


def calcular_bc():
    tl = taylor()
    out = []
    for nome, ini, fim in PRESIDENTES_BC:
        R = [r for r in tl if ini <= (int(r["t"][:4]), int(r["t"][5:])) <= fim]
        out.append(dict(nome=nome, ini=ini, fim=fim, meses=len(R),
                        ipca=media([r["selic"] - r["taylor_ipca_5.0"] for r in R]),
                        focus=media([r["selic"] - r["taylor_focus_5.0"] for r in R])))
    return out


def r2(x):
    return None if x is None else round(x, 2)


def gravar(linhas):
    obj = {
        "titulo": "Juro real ex-post por mandato presidencial (% a.a.)",
        "tipo": "barras",
        "unidade": "% a.a.",
        "fonte": "BCB, SGS 4390 (Selic acumulada no mês) e 433 (IPCA mensal); BIS, WS_CBPOL e "
                 "WS_LONG_CPI; cálculo do painel (tools/analises/12.4.7_juro_mandato.py)",
        "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json",
        "consulta": CONSULTA,
        "nota": "Brasil: Selic acumulada no mandato (SGS 4390) sobre o IPCA acumulado (SGS 433), "
                "anualizado. Dilma 2 vai de jan/2015 a abr/2016; Temer, de mai/2016 a dez/2018; "
                "Lula 3, de jan/2023 a set/2026. Emergentes: média simples de México, Chile, "
                "Colômbia, Índia e África do Sul na régua do BIS (taxa de política de fim de mês "
                "deflacionada pela inflação em 12 meses, média dos meses do mandato), a partir de "
                "jan/2000: FHC 2 cobre só 2000–2002 e FHC 1 fica sem dado. A régua do BIS dá ao "
                "Brasil valores próximos aos da série do BCB (10,0% em FHC 2; 8,2% em Lula 3).",
        "series": [
            {"nome": "Brasil", "pontos": [{"t": l["nome"], "v": r2(l["real"])} for l in linhas]},
            {"nome": "Média de cinco emergentes (BIS)",
             "pontos": [{"t": l["nome"], "v": r2(l["bis_pares"])} for l in linhas]},
        ],
    }
    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def resumo(linhas, bc):
    print("Mandato      meses  Selic  IPCA  real | BIS-BR pares dist  EUA | primário  DBGG ini->fim")
    for l in linhas:
        f = lambda x, w=6: (f"{x:{w}.2f}" if x is not None else " " * (w - 2) + "n/d")
        print(f"{l['nome']:<12} {l['meses']:>4} {f(l['selic'])} {f(l['ipca'])} {f(l['real'])} |"
              f" {f(l['bis_br'])} {f(l['bis_pares'])} {f(l['dist'])} {f(l['eua'])} |"
              f" {f(l['primario'])}  {f(l['dbgg_ini'])} -> {f(l['dbgg_fim'])}")
    print("\nSelic - regra de Taylor (r* = 5%), média mensal, p.p.")
    for b in bc:
        print(f"{b['nome']:<40} {b['meses']:>4}  IPCA {b['ipca']:6.2f}  Focus {b['focus']:6.2f}")


def main():
    linhas = calcular()
    bc = calcular_bc()
    if "--resumo" in sys.argv:
        resumo(linhas, bc)
    else:
        gravar(linhas)


if __name__ == "__main__":
    main()

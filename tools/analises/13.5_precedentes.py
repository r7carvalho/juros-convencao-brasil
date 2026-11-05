#!/usr/bin/env python3
"""Precedentes de juro fixado ou coordenado (página 13.5 do painel).

Gera dados/13.5-pos-guerra.json e dados/13.5-inflacao-episodios.json a partir do acervo bruto e
imprime, com --resumo, os números de cada episódio citados no texto. Só usa a biblioteca padrão.

Uso: python3 tools/analises/13.5_precedentes.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  bis-cpi.csv                 BIS, WS_LONG_CPI, inflação ao consumidor em 12 meses (%), mensal
  bis-politica_monetaria.csv  BIS, WS_CBPOL, taxa de política, fim do mês (%)
  sgs-432.json                Selic meta (% a.a.), último valor do mês
  sgs-13522.json              IPCA acumulado em 12 meses (%)
  sgs-3698.json               PTAX venda, média mensal (R$/US$)
  sgs-3546.json               Reservas internacionais, liquidez (US$ milhões)
  sgs-13762.json              DBGG, % do PIB (conceito BCB)
  sgs-5793.json               NFSP primária 12 meses, % do PIB (positivo = déficit)
  ipea-JPM366_EMBI366.json    EMBI+ Brasil (pontos-base), diário, via Ipeadata

Método do gráfico de episódios
  Para cada episódio: inflação em 12 meses no mês de início; a maior inflação em 12 meses entre
  o início e o fim; a maior nos 24 meses depois do fim. Datas de início e fim no dicionário
  EPISODIOS (fim = mês em que o juro fixado ou baixo deixou de valer). A Austrália não está no
  acervo do BIS: entram os números trimestrais do ABS (CPI, variação em 12 meses), citados na nota.
"""
import csv
import json
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
CONSULTA = "2026-11-05"


def bis(nome):
    serie = defaultdict(dict)
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        for x in csv.DictReader(f):
            if x["OBS_VALUE"]:
                serie[x["REF_AREA"]][x["TIME_PERIOD"]] = float(x["OBS_VALUE"])
    return serie


def sgs(codigo):
    with open(os.path.join(BRUTOS, f"sgs-{codigo}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    r = {}
    for x in dados:
        d, m, a = x["data"].split("/")
        if x["valor"] not in ("", None):
            r[f"{a}-{m}"] = float(x["valor"])  # o último do mês prevalece
    return r


def embi():
    with open(os.path.join(BRUTOS, "ipea-JPM366_EMBI366.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    r = {}
    for x in dados:
        if x["VALVALOR"] is not None:
            r[x["VALDATA"][:7]] = x["VALVALOR"]
    return r


def meses(ini, fim):
    a, m = map(int, ini.split("-"))
    a2, m2 = map(int, fim.split("-"))
    out = []
    while (a, m) <= (a2, m2):
        out.append(f"{a:04d}-{m:02d}")
        m += 1
        if m > 12:
            a, m = a + 1, 1
    return out


def somar(t, n):
    a, m = map(int, t.split("-"))
    m += n
    while m > 12:
        a, m = a + 1, m - 12
    return f"{a:04d}-{m:02d}"


CPI = bis("bis-cpi.csv")
POL = bis("bis-politica_monetaria.csv")
IPCA = sgs(13522)

# país (BIS) ou "BR" (IPCA, SGS 13522); início e fim do juro fixado ou baixo
EPISODIOS = [
    ("EUA 1942–1951", "US", "1942-04", "1951-03"),
    ("Reino Unido 1946–1951", "GB", "1946-01", "1951-10"),
    ("Japão 2016–2024", "JP", "2016-09", "2024-03"),
    ("Brasil 2011–2013", "BR", "2011-08", "2013-04"),
    ("Brasil 2017–2019", "BR", "2018-03", "2020-02"),
    ("Brasil 2020–2021", "BR", "2020-08", "2021-03"),
    ("Turquia 2021–2023", "TR", "2021-09", "2023-06"),
]
# ABS, CPI Austrália, variação em 12 meses: mar/2020 2,2; máximo durante (jun/2021) 3,8;
# máximo nos 24 meses seguintes (dez/2022) 7,8.
AUSTRALIA = ("Austrália 2020–2021", 2.2, 3.8, 7.8)


def inflacao(pais):
    return IPCA if pais == "BR" else CPI[pais]


def episodio(nome, pais, ini, fim):
    s = inflacao(pais)
    dur = [(t, s[t]) for t in meses(ini, fim) if t in s]
    dep = [(t, s[t]) for t in meses(somar(fim, 1), somar(fim, 24)) if t in s]
    mx_d = max(dur, key=lambda x: x[1])
    mx_p = max(dep, key=lambda x: x[1]) if dep else (None, None)
    return dict(nome=nome, inicio=(ini, s[ini]), max_durante=mx_d, max_depois=mx_p,
                ultimo_depois=dep[-1][0] if dep else None)


def grafico_pos_guerra():
    pts = lambda d, a, b: [{"t": t, "v": round(d[t], 2)} for t in meses(a, b) if t in d]
    return {
        "titulo": "Juro fixado no pós-guerra: inflação nos EUA e no Reino Unido e Bank Rate britânica, 1940–1955 (%)",
        "tipo": "linha",
        "unidade": "%",
        "fonte": "BIS, inflação ao consumidor em 12 meses (WS_LONG_CPI) e taxa de política (WS_CBPOL; Bank Rate do Banco da Inglaterra, série a partir de jan/1946); cálculo do painel em tools/analises/13.5_precedentes.py",
        "url": "https://data.bis.org/",
        "consulta": CONSULTA,
        "nota": "Mensal. O teto americano (3/8% nas letras do Tesouro de abr/1942 a jul/1947 e 2,5% nos títulos longos até o acordo de 04/03/1951) não está no acervo do BIS e aparece só como linha de referência de 2,5%. A Bank Rate ficou em 2% de 1932 a out/1951 (o BIS começa em 1946).",
        "governos": False,
        "ref": [{"v": 2.5, "rotulo": "teto dos títulos longos dos EUA"}],
        "series": [
            {"nome": "EUA, inflação em 12 meses", "pontos": pts(CPI["US"], "1940-01", "1955-12")},
            {"nome": "Reino Unido, inflação em 12 meses", "pontos": pts(CPI["GB"], "1945-01", "1955-12")},
            {"nome": "Reino Unido, Bank Rate", "pontos": pts(POL["GB"], "1946-01", "1955-12")},
        ],
    }


def grafico_episodios(eps):
    cats = [e["nome"] for e in eps] + [AUSTRALIA[0]]
    ini = [round(e["inicio"][1], 1) for e in eps] + [AUSTRALIA[1]]
    dur = [round(e["max_durante"][1], 1) for e in eps] + [AUSTRALIA[2]]
    # Brasil 2017–2019: os 24 meses seguintes são o episódio de 2020–2021; fica sem valor
    dep = [None if e["nome"] == "Brasil 2017–2019" else round(e["max_depois"][1], 1) for e in eps] + [AUSTRALIA[3]]
    ordem = [0, 1, 2, 7, 3, 5, 4]  # EUA, RU, Japão, Austrália, Br 2011, Br 2020, Br 2017 (Turquia fora da escala)
    serie = lambda vals: [{"t": cats[i], "v": vals[i]} for i in ordem]
    return {
        "titulo": "Inflação em 12 meses no início, no máximo durante e no máximo nos 24 meses depois de cada episódio, sem a Turquia (%)",
        "tipo": "barras",
        "unidade": "%",
        "fonte": "BIS, WS_LONG_CPI (EUA, Reino Unido, Japão, Turquia); IBGE, IPCA 12 meses via BCB, SGS 13522 (Brasil); ABS, Consumer Price Index (Austrália); cálculo do painel em tools/analises/13.5_precedentes.py",
        "url": "https://data.bis.org/",
        "consulta": CONSULTA,
        "nota": "Início e fim: EUA abr/1942 a mar/1951; Reino Unido jan/1946 a out/1951; Japão set/2016 a mar/2024 (depois, até set/2026); Austrália mar/2020 a nov/2021 (trimestral); Brasil ago/2011 a abr/2013, mar/2018 a fev/2020 (sem a barra dos 24 meses seguintes, que coincidem com o episódio de 2020–2021) e ago/2020 a mar/2021; A Turquia (set/2021 a jun/2023: 19,6% no início, 85,5% no máximo durante e 75,4% nos 24 meses seguintes, BIS) fica fora para não achatar a escala; ver o gráfico da página 6.4.3.",
        "series": [
            {"nome": "No início", "pontos": serie(ini)},
            {"nome": "Máximo durante", "pontos": serie(dur)},
            {"nome": "Máximo nos 24 meses seguintes", "pontos": serie(dep)},
        ],
    }


def resumo(eps):
    for e in eps:
        print(f"{e['nome']:24} início {e['inicio']}  máx durante {e['max_durante']}  máx depois {e['max_depois']} (até {e['ultimo_depois']})")
    selic, ptax, res, dbgg, prim, em = sgs(432), sgs(3698), sgs(3546), sgs(13762), sgs(5793), embi()
    print("\nBrasil, posições de mês (Selic meta fim do mês; IPCA 12m; PTAX média; reservas US$ bi; DBGG % PIB; NFSP primária 12m; EMBI)")
    for t in ["2011-08", "2012-10", "2012-12", "2013-04", "2013-12", "2017-12", "2018-03", "2018-12",
              "2019-12", "2020-02", "2020-08", "2020-12", "2021-03", "2021-12", "2022-04", "2022-12", "2026-09"]:
        print(t, selic.get(t), IPCA.get(t), ptax.get(t), round(res[t] / 1000, 1) if t in res else None,
              dbgg.get(t), prim.get(t), em.get(t))
    for a, b in [("2011-07", "2013-12"), ("2020-02", "2021-03"), ("2017-12", "2019-12")]:
        print(f"PTAX {a}→{b}: {100 * (ptax[b] / ptax[a] - 1):+.1f}%")
    print("\nJuro real da taxa de política, BIS (taxa − inflação, Fisher), média anual")
    for p, anos in [("TR", [2022, 2023]), ("JP", [2017, 2023]), ("US", [])]:
        for a in anos:
            ms = [f"{a}-{m:02d}" for m in range(1, 13)]
            v = [(1 + POL[p][t] / 100) / (1 + CPI[p][t] / 100) - 1 for t in ms if t in POL[p] and t in CPI[p]]
            print(p, a, round(100 * sum(v) / len(v), 1))
    print("\nReino Unido, Bank Rate:", {t: POL["GB"][t] for t in meses("1951-09", "1952-04")})
    print("EUA, inflação 1947 e 1951:", {t: CPI["US"][t] for t in meses("1947-01", "1947-06") + meses("1951-01", "1951-04")})
    # Focus, IPCA 12 meses à frente, mediana não suavizada de 23/10/2026: 4,53%
    print("Proposta: Selic 7,5% sobre Focus 12m de 4,53%:", round(100 * (1.075 / 1.0453 - 1), 2))
    for i in (3.0, 5.5):
        for pi in (3.0, 4.53):
            print(f"  faixa {i}% com inflação {pi}%: juro real {100 * ((1 + i / 100) / (1 + pi / 100) - 1):.2f}%")


def main():
    eps = [episodio(*e) for e in EPISODIOS]
    for nome, obj in [("13.5-pos-guerra.json", grafico_pos_guerra()), ("13.5-inflacao-episodios.json", grafico_episodios(eps))]:
        with open(os.path.join(ROOT, "dados", nome), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
            f.write("\n")
    if "--resumo" in sys.argv:
        resumo(eps)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Juro real contra medidas de risco, países do acervo do BIS (página 13.10 do painel).

Refaz os arquivos dados/13.10-*.json. Só usa a biblioteca padrão.

Uso: python3 tools/analises/13.10_risco.py [--resumo]

Entradas
  dados/brutos/bis-politica_monetaria.csv  BIS, WS_CBPOL, taxa de política, mensal, fim de período
  dados/brutos/bis-cpi.csv                 BIS, WS_LONG_CPI, inflação ao consumidor em 12 meses, mensal
  (coleta automática de 02/11/2026; 18 áreas, das quais 13 entram na comparação com risco)
  Medidas de risco digitadas abaixo (RISCO), cada uma com fonte e data.

Método
  Juro real ex-post do ano = (1 + média anual da taxa de política) / (1 + média anual da inflação
  em 12 meses) - 1, a régua da página 2.1 (reproduz Brasil 2025 = 9,09 e 2010-2019 = 3,93).
  Meses sem valor (EUA, CPI de out/2025, "NaN" no BIS) ficam fora da média.
  Ex-ante: ranking MoneYou e Lev de 16/09/2026 (juro de 1 ano sobre a inflação projetada),
  já usado em dados/2.1-ranking-ex-ante-2026.json; não cobre Peru e Coreia.
  Rating: S&P, moeda estrangeira, longo prazo, convertido em degraus abaixo de AAA
  (AAA = 0, AA+ = 1, ..., BBB- = 9, BB+ = 10, BB = 11, BB- = 12).
  Inflação passada recente: média simples das médias anuais da inflação em 12 meses, 2015-2024.
  Histórico de inflação: média de ln(1 + inflação anual) em 1985-2004, devolvida como taxa anual
  equivalente (média geométrica), e usada na regressão em logaritmo.
  Regressão: mínimos quadrados ordinários, erros-padrão clássicos (sem correção, n pequeno).
  Resíduo do Brasil "fora da amostra": o modelo é estimado sem o Brasil e o resíduo é o juro
  observado menos o previsto. O mesmo exercício é feito para cada país (validação deixando um
  de fora), para ver se o erro do Brasil é grande perto do erro típico.
  Testes extras (res["testes_extras"]): intervalo da previsão do juro brasileiro no M1; M3 sem o Brasil
  e sem o Peru, com erro-padrão do histórico e intervalo do resíduo; ratings vigentes em 2025; Suíça,
  Suécia e Dinamarca no M1 como AAA; posição do Brasil na validação do M1 e do M2.
"""
import csv
import json
import math
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
DADOS = os.path.join(ROOT, "dados")
CONSULTA = "2026-11-05"

NOMES = {
    "BR": "Brasil", "MX": "México", "CO": "Colômbia", "CL": "Chile", "PE": "Peru",
    "ZA": "África do Sul", "TR": "Turquia", "ID": "Indonésia", "IN": "Índia", "KR": "Coreia do Sul",
    "US": "Estados Unidos", "GB": "Reino Unido", "JP": "Japão",
}
EMERGENTES = ["BR", "MX", "CO", "CL", "PE", "ZA", "TR", "ID", "IN", "KR"]

DEGRAU = {"AAA": 0, "AA+": 1, "AA": 2, "AA-": 3, "A+": 4, "A": 5, "A-": 6, "BBB+": 7, "BBB": 8,
          "BBB-": 9, "BB+": 10, "BB": 11, "BB-": 12, "B+": 13, "B": 14}

# Medidas de risco. rating = S&P, moeda estrangeira, longo prazo, com a data da última ação conhecida
# pelo painel; divida = dívida bruta do governo geral, % do PIB, 2025.
RISCO = {
    "BR": {"rating": "BB", "rating_fonte": "S&P, elevação de BB- para BB em 19/12/2023, reafirmada em 05/06/2025 (Movimento Econômico; IstoÉ Dinheiro)",
           "divida": 93.3, "divida_fonte": "FMI, DataMapper GGXWDG_NGDP, consulta 28/10/2026 (dados/3.4)"},
    "MX": {"rating": "BBB", "rating_fonte": "S&P, BBB com perspectiva negativa desde mai/2026 (Mexico Daily Post, 14/05/2026)",
           "divida": 61.7, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "CO": {"rating": "BB-", "rating_fonte": "S&P, rebaixamento de BB para BB- em 08/04/2026 (La República; Scotiabank Colpatria)",
           "divida": 59.9, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "CL": {"rating": "A", "rating_fonte": "S&P, A estável (FX Empire e Trading Economics, listas de ratings, consulta 05/11/2026)",
           "divida": 41.5, "divida_fonte": "Ministério da Fazenda do Chile, 2025, via Trading Economics (conceito nacional; o FMI projeta 43,7% para 2026, FRED CHLGGXWDGGDP)"},
    "PE": {"rating": "BBB-", "rating_fonte": "S&P, BBB- estável (listas de ratings, consulta 05/11/2026)",
           "divida": 33.7, "divida_fonte": "FMI, estimativa de 2025 compilada na Wikipédia, List of countries by government debt, versão de mar/2026"},
    "ZA": {"rating": "BB", "rating_fonte": "S&P, BB com perspectiva positiva desde 14/11/2025 (Wikipédia, List of countries by credit rating, versão de mar/2026)",
           "divida": 78.4, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "TR": {"rating": "BB-", "rating_fonte": "S&P, elevação de B+ para BB- em 2024, mantida em abr/2026 (Property Turkey, 2026; conferir na S&P)",
           "divida": 23.7, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "ID": {"rating": "BBB", "rating_fonte": "S&P, BBB (listas de ratings, consulta 05/11/2026)",
           "divida": 41.0, "divida_fonte": "FMI, estimativa de 2025 compilada na Wikipédia, versão de mar/2026"},
    "IN": {"rating": "BBB", "rating_fonte": "S&P, elevação para BBB em 14/08/2025 (Wikipédia, versão de mar/2026)",
           "divida": 84.3, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "KR": {"rating": "AA", "rating_fonte": "S&P, AA (FX Empire, consulta 05/11/2026)",
           "divida": 54.5, "divida_fonte": "FMI, estimativa de 2025 compilada na Wikipédia, versão de mar/2026"},
    "US": {"rating": "AA+", "rating_fonte": "S&P, AA+ desde 2011 (listas de ratings, consulta 05/11/2026)",
           "divida": 124.4, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "GB": {"rating": "AA", "rating_fonte": "S&P, AA (listas de ratings, consulta 05/11/2026)",
           "divida": 102.1, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
    "JP": {"rating": "A+", "rating_fonte": "S&P, A+ (listas de ratings, consulta 05/11/2026)",
           "divida": 204.8, "divida_fonte": "FMI, DataMapper, consulta 28/10/2026 (dados/3.4)"},
}

# Juro real ex-ante do ranking MoneYou e Lev de 16/09/2026 (dados/2.1-ranking-ex-ante-2026.json).
EX_ANTE = {"BR": 8.45, "CO": 6.33, "TR": 6.25, "MX": 3.08, "ZA": 2.93, "ID": 2.14, "CL": 2.09,
           "IN": 1.63, "GB": 0.80, "US": 0.74, "JP": -0.44}

# CDS de 5 anos, América Latina, duas datas de 2026 (pontos-base).
CDS = {
    "ago/2026": {"fonte": "Revista Mercado (República Dominicana), ranking latino-americano de CDS de 5 anos, ago/2026; "
                         "página não aberta pelo painel (bloqueada para leitura), números do resumo de busca, dia exato não conferido",
                 "url": "https://revistamercado.do/money-invest/daily-news/republica-dominicana-supera-a-brasil-y-colombia-en-riesgo-pais-asi-queda-el-ranking-latinoamericano/",
                 "v": {"BR": 122.21, "CO": 136.18, "MX": 79.44, "PE": 59.02, "CL": 41.24}},
    "mai/2026": {"fonte": "La República (Colômbia), com dados da Bloomberg, semana anterior ao 1º turno colombiano, mai/2026",
                 "url": "https://www.larepublica.co/economia/el-riesgo-pais-se-disparo-a-menos-de-una-semana-de-las-elecciones-presidenciales-4400255",
                 "v": {"BR": 128.28, "CO": 220.9, "MX": 96.06, "PE": 74.20, "CL": 50.90}},
}


# ------------------------------------------------------------------ dados do BIS
def carregar(nome):
    d = defaultdict(dict)
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            v = r["OBS_VALUE"]
            if not v or v.lower() == "nan":
                continue
            d[r["REF_AREA"]][r["TIME_PERIOD"]] = float(v)
    return d


POL = carregar("bis-politica_monetaria.csv")
CPI = carregar("bis-cpi.csv")


def media_ano(serie, pais, ano, meses=12):
    vals = [serie[pais].get(f"{ano}-{m:02d}") for m in range(1, meses + 1)]
    vals = [v for v in vals if v is not None]
    return sum(vals) / len(vals) if vals else None


def juro_real(pais, ano, meses=12):
    i, p = media_ano(POL, pais, ano, meses), media_ano(CPI, pais, ano, meses)
    if i is None or p is None:
        return None
    return ((1 + i / 100) / (1 + p / 100) - 1) * 100


def inflacao_media(pais, a0, a1):
    vals = [media_ano(CPI, pais, a) for a in range(a0, a1 + 1)]
    vals = [v for v in vals if v is not None]
    return sum(vals) / len(vals)


def inflacao_geom(pais, a0, a1):
    vals = [media_ano(CPI, pais, a) for a in range(a0, a1 + 1)]
    vals = [math.log(1 + v / 100) for v in vals if v is not None]
    return (math.exp(sum(vals) / len(vals)) - 1) * 100, len(vals)


# ------------------------------------------------------------------ álgebra
def inversa(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[piv] = a[piv], a[c]
        if abs(a[c][c]) < 1e-12:
            raise ValueError("matriz singular")
        f = a[c][c]
        a[c] = [x / f for x in a[c]]
        for r in range(n):
            if r != c:
                g = a[r][c]
                a[r] = [x - g * y for x, y in zip(a[r], a[c])]
    return [row[n:] for row in a]


def mqo(y, xs):
    """y: lista; xs: lista de colunas (sem constante). Devolve coeficientes, erros-padrão, R²."""
    n = len(y)
    X = [[1.0] + [col[i] for col in xs] for i in range(n)]
    k = len(X[0])
    XtX = [[sum(X[r][i] * X[r][j] for r in range(n)) for j in range(k)] for i in range(k)]
    Xty = [sum(X[r][i] * y[r] for r in range(n)) for i in range(k)]
    inv = inversa(XtX)
    b = [sum(inv[i][j] * Xty[j] for j in range(k)) for i in range(k)]
    yhat = [sum(b[j] * X[r][j] for j in range(k)) for r in range(n)]
    res = [y[r] - yhat[r] for r in range(n)]
    sqr = sum(e * e for e in res)
    my = sum(y) / n
    sqt = sum((v - my) ** 2 for v in y)
    gl = n - k
    s2 = sqr / gl if gl > 0 else float("nan")
    ep = [math.sqrt(s2 * inv[i][i]) if gl > 0 else float("nan") for i in range(k)]
    return {"b": b, "ep": ep, "r2": 1 - sqr / sqt if sqt else float("nan"), "n": n, "gl": gl,
            "s2": s2, "inv": inv}


def ep_previsao(m, x):
    """Erro-padrão da previsão de uma observação nova com regressores x (sem a constante)."""
    v = [1.0] + list(x)
    k = len(v)
    q = sum(v[i] * m["inv"][i][j] * v[j] for i in range(k) for j in range(k))
    return math.sqrt(m["s2"] * (1 + q))


# valor crítico t bicaudal de 95% para poucos graus de liberdade
T95 = {4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160}


def prever(b, x):
    return b[0] + sum(bi * xi for bi, xi in zip(b[1:], x))


def correl(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    sab = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    saa = sum((x - ma) ** 2 for x in a)
    sbb = sum((y - mb) ** 2 for y in b)
    return sab / math.sqrt(saa * sbb)


def vif(cols):
    out = []
    for j in range(len(cols)):
        outros = [c for i, c in enumerate(cols) if i != j]
        r2 = mqo(cols[j], outros)["r2"]
        out.append(1 / (1 - r2))
    return out


# ------------------------------------------------------------------ brinquedo de colinearidade
def brinquedo():
    """Seis cidades; x1 e x2 quase iguais; y = x1 + x2 + ruído. Duas amostras de ruído pequeno."""
    x1 = [1, 2, 3, 4, 5, 6]
    x2 = [1.1, 1.9, 3.0, 4.1, 4.9, 6.0]
    ruido_a = [0.2, -0.2, 0.0, 0.1, -0.1, 0.0]
    ruido_b = [-0.2, 0.2, 0.0, -0.1, 0.1, 0.0]
    saida = {"x1": x1, "x2": x2, "amostras": {}}
    for nome, e in (("A", ruido_a), ("B", ruido_b)):
        y = [a + b + u for a, b, u in zip(x1, x2, e)]
        m = mqo(y, [x1, x2])
        so = mqo(y, [[a + b for a, b in zip(x1, x2)]])
        saida["amostras"][nome] = {"y": [round(v, 2) for v in y], "b1": m["b"][1], "b2": m["b"][2],
                                   "ep1": m["ep"][1], "ep2": m["ep"][2], "soma": m["b"][1] + m["b"][2],
                                   "b_soma": so["b"][1], "ep_soma": so["ep"][1], "r2": m["r2"]}
    saida["correlacao_x1_x2"] = correl(x1, x2)
    saida["vif"] = vif([x1, x2])[0]
    return saida


# ------------------------------------------------------------------ série brasileira (colinearidade no tempo)
def serie_brasil():
    """Brasil, anual, 2007-2023: juro real (régua BIS), EMBI+ (média do ano), DBGG (média dos meses,
    conceito BCB) e IPCA de 12 meses de dezembro do ano anterior (inflação passada)."""
    with open(os.path.join(BRUTOS, "ipea-JPM366_EMBI366.json"), encoding="utf-8") as f:
        embi_d = json.load(f)["dados"]
    embi = defaultdict(list)
    for r_ in embi_d:
        if r_["VALVALOR"] is not None:
            embi[int(r_["VALDATA"][:4])].append(r_["VALVALOR"])

    def sgs(nome):
        with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
            d = json.load(f)["dados"]
        out = {}
        for r_ in d:
            dd, mm, aa = r_["data"].split("/")
            out[(int(aa), int(mm))] = float(r_["valor"])
        return out
    dbgg, ipca = sgs("sgs-13762.json"), sgs("sgs-13522.json")
    anos = list(range(2007, 2024))
    tab = []
    for a in anos:
        dv = [dbgg[(a, m)] for m in range(1, 13) if (a, m) in dbgg]
        tab.append({"ano": a, "r": juro_real("BR", a), "embi": sum(embi[a]) / len(embi[a]),
                    "dbgg": sum(dv) / len(dv), "ipca_ant": ipca[(a - 1, 12)]})
    cols = {k: [t[k] for t in tab] for k in ("r", "embi", "dbgg", "ipca_ant")}
    out = {"anos": [anos[0], anos[-1]], "tabela": tab,
           "correlacoes": {a: {b: correl(cols[a], cols[b]) for b in cols} for a in cols},
           "vif": dict(zip(("embi", "dbgg", "ipca_ant"), vif([cols["embi"], cols["dbgg"], cols["ipca_ant"]])))}
    for nome, (a0, a1) in (("2007-2023", (2007, 2023)), ("2007-2015", (2007, 2015)), ("2016-2023", (2016, 2023))):
        sub = [t for t in tab if a0 <= t["ano"] <= a1]
        m = mqo([t["r"] for t in sub], [[t["embi"] / 100 for t in sub], [t["dbgg"] for t in sub], [t["ipca_ant"] for t in sub]])
        out["mqo_" + nome] = {"n": m["n"], "r2": m["r2"], "coef": m["b"], "ep": m["ep"],
                              "nota": "coeficientes: constante, EMBI+ (por 100 pontos-base), DBGG (por ponto do PIB), IPCA do ano anterior"}
    return out


# ------------------------------------------------------------------ principal
def montar():
    paises = list(RISCO)
    linhas = {}
    for p in paises:
        hist, nh = inflacao_geom(p, 1985, 2004)
        linhas[p] = {
            "nome": NOMES[p],
            "r2024": juro_real(p, 2024), "r2025": juro_real(p, 2025), "r2026": juro_real(p, 2026, 9),
            "r2019": juro_real(p, 2019),
            "ex_ante": EX_ANTE.get(p),
            "rating": RISCO[p]["rating"], "degrau": DEGRAU[RISCO[p]["rating"]],
            "divida": RISCO[p]["divida"],
            "infl_15_24": inflacao_media(p, 2015, 2024),
            "hist_85_04": hist, "hist_anos": nh,
            "ln_hist": math.log(1 + hist / 100),
        }
        l = linhas[p]
        l["r2023_25"] = sum(juro_real(p, a) for a in (2023, 2024, 2025)) / 3
    return linhas


def regressao(linhas, paises, dep, regs):
    ps = [p for p in paises if linhas[p][dep] is not None]
    y = [linhas[p][dep] for p in ps]
    xs = [[linhas[p][r] for p in ps] for r in regs]
    return ps, mqo(y, xs)


def residuo_fora(linhas, paises, dep, regs, alvo="BR"):
    outros = [p for p in paises if p != alvo]
    ps, m = regressao(linhas, outros, dep, regs)
    prev = prever(m["b"], [linhas[alvo][r] for r in regs])
    return linhas[alvo][dep] - prev, prev, m


def loo(linhas, paises, dep, regs):
    out = {}
    for p in paises:
        if linhas[p][dep] is None:
            continue
        r, prev, _ = residuo_fora(linhas, [q for q in paises if linhas[q][dep] is not None], dep, regs, p)
        out[p] = r
    return out


MODELOS = {
    "M1 rating": ["degrau"],
    "M2 rating, inflação 2015-24, dívida": ["degrau", "infl_15_24", "divida"],
    "M3 M2 + histórico 1985-2004": ["degrau", "infl_15_24", "divida", "ln_hist"],
    "M4 inflação 2015-24 e dívida": ["infl_15_24", "divida"],
}
DEPS = {"r2025": "ex-post 2025", "r2026": "ex-post 2026 (jan-set)", "r2024": "ex-post 2024",
        "r2023_25": "ex-post 2023-2025", "ex_ante": "ex-ante 16/09/2026"}
AMOSTRAS = {"13 países": list(RISCO), "10 emergentes": EMERGENTES,
            "12 sem Turquia": [p for p in RISCO if p != "TR"],
            "12 sem Peru": [p for p in RISCO if p != "PE"]}


def r(v, c=2):
    return None if v is None else round(v, c)


def main():
    linhas = montar()
    todos = list(RISCO)
    res = {"consulta": CONSULTA, "paises": {}, "regressoes": {}, "sensibilidade": [], "correlacoes": {},
           "vif": {}, "loo": {}, "cds": {}, "brinquedo": brinquedo()}
    for p, l in linhas.items():
        res["paises"][p] = {k: (r(v, 3) if isinstance(v, float) else v) for k, v in l.items()}
        res["paises"][p]["rating_fonte"] = RISCO[p]["rating_fonte"]
        res["paises"][p]["divida_fonte"] = RISCO[p]["divida_fonte"]

    # regressões principais (ex-post 2025, 13 países) e com o Brasil fora
    for nome, regs in MODELOS.items():
        ps, m = regressao(linhas, todos, "r2025", regs)
        resid, prev, m_sem = residuo_fora(linhas, todos, "r2025", regs)
        res["regressoes"][nome] = {
            "regressores": regs, "n": m["n"], "r2": r(m["r2"], 3),
            "coef": [r(b, 3) for b in m["b"]], "ep": [r(e, 3) for e in m["ep"]],
            "t": [r(b / e, 2) if e else None for b, e in zip(m["b"], m["ep"])],
            "sem_brasil": {"coef": [r(b, 3) for b in m_sem["b"]], "ep": [r(e, 3) for e in m_sem["ep"]],
                           "r2": r(m_sem["r2"], 3), "n": m_sem["n"],
                           "previsto_brasil": r(prev), "residuo_brasil": r(resid),
                           "ep_previsao": r(ep_previsao(m_sem, [linhas["BR"][x] for x in regs])),
                           "ic95_residuo": [r(resid - T95[m_sem["gl"]] * ep_previsao(m_sem, [linhas["BR"][x] for x in regs])),
                                            r(resid + T95[m_sem["gl"]] * ep_previsao(m_sem, [linhas["BR"][x] for x in regs]))]},
        }

    # sensibilidade: resíduo do Brasil fora da amostra
    for dn, dl in DEPS.items():
        for an, am in AMOSTRAS.items():
            am2 = [p for p in am if linhas[p][dn] is not None]
            for mn, regs in MODELOS.items():
                if len(am2) - 1 <= len(regs) + 1:
                    continue
                resid, prev, m = residuo_fora(linhas, am2, dn, regs)
                res["sensibilidade"].append({"dep": dl, "amostra": an, "modelo": mn, "n_sem_brasil": m["n"],
                                             "observado": r(linhas["BR"][dn]), "previsto": r(prev),
                                             "residuo": r(resid), "r2_sem_brasil": r(m["r2"], 3)})

    # correlações e VIF
    vars_ = ["r2025", "degrau", "infl_15_24", "divida", "ln_hist"]
    for a in vars_:
        res["correlacoes"][a] = {b: r(correl([linhas[p][a] for p in todos], [linhas[p][b] for p in todos]), 2) for b in vars_}
    for nome in ("M2 rating, inflação 2015-24, dívida", "M3 M2 + histórico 1985-2004"):
        regs = MODELOS[nome]
        res["vif"][nome] = dict(zip(regs, [r(v, 2) for v in vif([[linhas[p][x] for p in todos] for x in regs])]))
    # só emergentes (onde a colinearidade aparece mais)
    regs = MODELOS["M3 M2 + histórico 1985-2004"]
    res["vif"]["M3, 10 emergentes"] = dict(zip(regs, [r(v, 2) for v in vif([[linhas[p][x] for p in EMERGENTES] for x in regs])]))
    res["correlacoes_emergentes"] = {a: {b: r(correl([linhas[p][a] for p in EMERGENTES], [linhas[p][b] for p in EMERGENTES]), 2)
                                         for b in vars_} for a in vars_}

    # validação deixando um de fora (M2, ex-post 2025)
    lo = loo(linhas, todos, "r2025", MODELOS["M2 rating, inflação 2015-24, dívida"])
    res["loo"]["M2, ex-post 2025"] = {p: r(v) for p, v in sorted(lo.items(), key=lambda kv: -abs(kv[1]))}
    lo1 = loo(linhas, todos, "r2025", MODELOS["M1 rating"])
    res["loo"]["M1, ex-post 2025"] = {p: r(v) for p, v in sorted(lo1.items(), key=lambda kv: -abs(kv[1]))}

    # CDS na América Latina
    for data, c in CDS.items():
        ps = list(c["v"])
        res["cds"][data] = {
            "fonte": c["fonte"], "url": c["url"], "valores": c["v"],
            "corr_cds_degrau": r(correl([c["v"][p] for p in ps], [linhas[p]["degrau"] for p in ps]), 2),
            "corr_cds_r2025": r(correl([c["v"][p] for p in ps], [linhas[p]["r2025"] for p in ps]), 2),
            "corr_cds_r2026": r(correl([c["v"][p] for p in ps], [linhas[p]["r2026"] for p in ps]), 2),
        }
        outros = [p for p in ps if p != "BR"]
        m = mqo([linhas[p]["r2026"] for p in outros], [[c["v"][p] for p in outros]])
        res["cds"][data]["sem_brasil_r2026"] = {"coef": [r(b, 4) for b in m["b"]], "r2": r(m["r2"], 3),
                                                "previsto_brasil": r(prever(m["b"], [c["v"]["BR"]])),
                                                "residuo_brasil": r(linhas["BR"]["r2026"] - prever(m["b"], [c["v"]["BR"]]))}

    # dívida x juro entre emergentes, com e sem o Brasil
    em_sem = [p for p in EMERGENTES if p != "BR"]
    res["corr_divida_juro_emergentes"] = {
        "com_brasil": r(correl([linhas[p]["divida"] for p in EMERGENTES], [linhas[p]["r2025"] for p in EMERGENTES]), 2),
        "sem_brasil": r(correl([linhas[p]["divida"] for p in em_sem], [linhas[p]["r2025"] for p in em_sem]), 2)}

    # robustez: rating de cada país (exceto o Brasil) um degrau acima ou abaixo
    rob = []
    for q in todos:
        if q == "BR":
            continue
        for delta in (-1, 1):
            orig = linhas[q]["degrau"]
            linhas[q]["degrau"] = orig + delta
            for mn in ("M1 rating", "M2 rating, inflação 2015-24, dívida"):
                resid, prev, m = residuo_fora(linhas, todos, "r2025", MODELOS[mn])
                rob.append({"pais": q, "delta": delta, "modelo": mn, "residuo": r(resid), "coef_rating": r(m["b"][1], 3)})
            linhas[q]["degrau"] = orig
    res["robustez_rating"] = {"casos": rob,
                              "residuo_min": min(x["residuo"] for x in rob), "residuo_max": max(x["residuo"] for x in rob),
                              "coef_min": min(x["coef_rating"] for x in rob), "coef_max": max(x["coef_rating"] for x in rob)}

    # pares com rating igual ou pior que o do Brasil
    piores = [p for p in todos if p != "BR" and linhas[p]["degrau"] >= linhas["BR"]["degrau"]]
    res["risco_igual_ou_maior"] = {"paises": piores}
    for dep in ("r2025", "r2026", "ex_ante", "r2019"):
        vals = [linhas[p][dep] for p in piores if linhas[p][dep] is not None]
        media = sum(vals) / len(vals)
        res["risco_igual_ou_maior"][dep] = {"media_pares": r(media), "brasil": r(linhas["BR"][dep]),
                                            "distancia": r(linhas["BR"][dep] - media)}
    # faixas do resíduo do Brasil
    faixas = {}
    for s_ in res["sensibilidade"]:
        chave = "com histórico (M3)" if s_["modelo"].startswith("M3") else "sem histórico (M1, M2, M4)"
        f = faixas.setdefault(s_["dep"], {}).setdefault(chave, [None, None])
        v = s_["residuo"]
        f[0] = v if f[0] is None else min(f[0], v)
        f[1] = v if f[1] is None else max(f[1], v)
    res["faixas_residuo"] = faixas

    res["testes_extras"] = testes_extras(linhas, res)

    sb = serie_brasil()
    res["serie_brasil"] = json.loads(json.dumps(sb), parse_float=lambda x: round(float(x), 3))

    with open(os.path.join(DADOS, "13.10-resultados.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")

    graficos(linhas, res)
    if "--resumo" in sys.argv:
        imprimir(linhas, res)


# Ratings S&P vigentes em 2025, quando diferem dos de 2026 usados na tabela (datas do próprio RISCO):
# África do Sul BB- até 14/11/2025; Índia BBB- até 14/08/2025; Colômbia BB até 08/04/2026, e BB+ no começo
# de 2025 (rebaixada para BB em jun/2025, a conferir na S&P). Duas variantes para a Colômbia.
RATING_2025 = {"BB+ (Colômbia)": {"CO": 10, "ZA": 12, "IN": 9}, "BB (Colômbia)": {"CO": 11, "ZA": 12, "IN": 9}}

# Países do acervo do BIS que a tabela principal deixa fora por falta de dívida comparável; entram só no M1
# (o M1 não usa dívida), como AAA na S&P.
AAA_EXTRAS = {"CH": "Suíça", "SE": "Suécia", "DK": "Dinamarca"}


def testes_extras(linhas, res):
    out = {}
    todos = list(RISCO)
    # 1. intervalo da previsão (e não do resíduo) do juro brasileiro no M1
    regs = MODELOS["M1 rating"]
    resid, prev, m = residuo_fora(linhas, todos, "r2025", regs)
    e = ep_previsao(m, [linhas["BR"][x] for x in regs])
    out["M1_ic95_previsao_brasil"] = [r(prev - T95[m["gl"]] * e), r(prev + T95[m["gl"]] * e)]

    # 2. M3 sem o Brasil e sem o Peru: o histórico não se estima
    regs = MODELOS["M3 M2 + histórico 1985-2004"]
    am = [p for p in todos if p != "PE"]
    resid, prev, m = residuo_fora(linhas, am, "r2025", regs)
    e = ep_previsao(m, [linhas["BR"][x] for x in regs])
    k = regs.index("ln_hist") + 1
    outros = [p for p in am if p != "BR"]
    maior = max(outros, key=lambda p: linhas[p]["ln_hist"])
    out["M3_sem_peru_2025"] = {
        "coef_hist": r(m["b"][k]), "ep_hist": r(m["ep"][k]), "t_hist": r(m["b"][k] / m["ep"][k]), "gl": m["gl"],
        "previsto_brasil": r(prev), "residuo_brasil": r(resid),
        "ic95_residuo": [r(resid - T95[m["gl"]] * e), r(resid + T95[m["gl"]] * e)],
        "ln_hist_brasil": r(linhas["BR"]["ln_hist"]), "maior_ln_hist_fora_brasil": [NOMES[maior], r(linhas[maior]["ln_hist"])]}

    # 3. ratings datados de 2025
    rt = {}
    for nome, troca in RATING_2025.items():
        orig = {q: linhas[q]["degrau"] for q in troca}
        for q, v in troca.items():
            linhas[q]["degrau"] = v
        rt[nome] = {}
        for mn in ("M1 rating", "M2 rating, inflação 2015-24, dívida"):
            resid, prev, m = residuo_fora(linhas, todos, "r2025", MODELOS[mn])
            rt[nome][mn] = r(resid)
        piores = [p for p in todos if p != "BR" and linhas[p]["degrau"] >= linhas["BR"]["degrau"]]
        media = sum(linhas[p]["r2025"] for p in piores) / len(piores)
        rt[nome]["igual_ou_pior"] = {"paises": [NOMES[p] for p in piores], "distancia_2025": r(linhas["BR"]["r2025"] - media)}
        for q, v in orig.items():
            linhas[q]["degrau"] = v
    out["ratings_2025"] = rt

    # 4. Suíça, Suécia e Dinamarca no M1, como AAA
    ext = {p: juro_real(p, 2025) for p in AAA_EXTRAS}
    ys = [linhas[p]["r2025"] for p in todos if p != "BR"] + [ext[p] for p in AAA_EXTRAS]
    xs = [linhas[p]["degrau"] for p in todos if p != "BR"] + [0 for _ in AAA_EXTRAS]
    m = mqo(ys, [xs])
    prev = prever(m["b"], [linhas["BR"]["degrau"]])
    resid = linhas["BR"]["r2025"] - prev
    e = ep_previsao(m, [linhas["BR"]["degrau"]])
    out["M1_com_suica_suecia_dinamarca"] = {
        "juro_real_2025": {AAA_EXTRAS[p]: r(v) for p, v in ext.items()}, "n_sem_brasil": m["n"],
        "coef": [r(b, 3) for b in m["b"]], "previsto_brasil": r(prev), "residuo_brasil": r(resid),
        "ic95_residuo": [r(resid - T95[m["gl"]] * e), r(resid + T95[m["gl"]] * e)]}

    # 5. lugar do Brasil na validação deixando um de fora
    for chave in ("M1, ex-post 2025", "M2, ex-post 2025"):
        ordem = list(res["loo"][chave])
        out["posicao_brasil_loo_" + chave.split(",")[0]] = ordem.index("BR") + 1
    out["paises_erro_acima_de_4_M1"] = [NOMES[p] for p, v in res["loo"]["M1, ex-post 2025"].items() if abs(v) > 4]
    return out


def graficos(linhas, res):
    todos = list(RISCO)
    base = {"consulta": CONSULTA, "url": "https://data.bis.org"}
    fonte_r = "BIS (WS_CBPOL e WS_LONG_CPI, coleta de 02/11/2026); S&P via imprensa e listas de ratings (datas por país em dados/13.10-resultados.json); FMI; cálculo do painel (tools/analises/13.10_risco.py)"
    m_sem = res["regressoes"]["M1 rating"]["sem_brasil"]["coef"]
    g1 = dict(base, titulo="Juro real ex-post de 2025 e rating soberano, 13 países",
              tipo="dispersao", unidade="% a.a.", eixo_x="degraus abaixo de AAA",
              eixo_y="juro real ex-post de 2025 (% a.a.)", fonte=fonte_r, destaque=["Brasil"],
              reta={"a": round(m_sem[0], 3), "b": round(m_sem[1], 3), "rotulo": "reta estimada sem o Brasil"},
              nota="Eixo horizontal: rating de longo prazo em moeda estrangeira da S&P, em degraus abaixo de AAA (0 = AAA, 2 = AA, 5 = A, 8 = BBB, 11 = BB, 12 = BB-); notas de 2026, com datas e fontes por país no arquivo de resultados. Juro real: média anual da taxa de política deflacionada pela média anual da inflação em 12 meses (régua da 2.1). Rússia (sem rating desde 2022) e área do euro ficam fora; Suíça, Suécia e Dinamarca ficam fora da tabela por falta de dívida no acervo e entram num teste à parte do modelo só com rating (resíduo do Brasil de 5,0).",
              series=[{"nome": "Países", "pontos": [{"t": linhas[p]["nome"], "x": linhas[p]["degrau"], "v": r(linhas[p]["r2025"])} for p in todos]}])
    g2 = dict(base, titulo="Juro real ex-post de 2025 e dívida bruta do governo geral, 13 países",
              tipo="dispersao", unidade="% a.a.", eixo_x="dívida bruta do governo geral, 2025 (% do PIB)",
              eixo_y="juro real ex-post de 2025 (% a.a.)", fonte="BIS (coleta de 02/11/2026); FMI, DataMapper (consulta 28/10/2026) e compilações das estimativas do FMI para Peru, Indonésia e Coreia; Ministério da Fazenda do Chile; cálculo do painel (tools/analises/13.10_risco.py)",
              destaque=["Brasil"],
              nota="Chile no conceito nacional (41,5%); demais países no conceito do FMI, com o Brasil a 93,3% (78,6% no conceito do BCB).",
              series=[{"nome": "Países", "pontos": [{"t": linhas[p]["nome"], "x": linhas[p]["divida"], "v": r(linhas[p]["r2025"])} for p in todos]}])
    c = CDS["ago/2026"]
    g3 = dict(base, titulo="América Latina: juro real ex-post de 2026 (jan-set) e CDS de 5 anos de ago/2026",
              tipo="dispersao", unidade="% a.a.", eixo_x="CDS de 5 anos, ago/2026 (pontos-base)",
              eixo_y="juro real ex-post, jan-set 2026 (% a.a.)",
              fonte="BIS (coleta de 02/11/2026); Revista Mercado, ranking latino-americano de CDS, ago/2026, página não aberta pelo painel (números do resumo de busca); cálculo do painel",
              url=c["url"], destaque=["Brasil"],
              nota="Cinco países, uma data de CDS. Em mai/2026, às vésperas da eleição colombiana, o CDS da Colômbia estava em 220,9 e o do Brasil em 128,3 (La República, com dados da Bloomberg).",
              series=[{"nome": "Países", "pontos": [{"t": linhas[p]["nome"], "x": c["v"][p], "v": r(linhas[p]["r2026"])} for p in c["v"]]}])
    b = res["brinquedo"]["amostras"]
    g4 = dict(consulta=CONSULTA, titulo="Exemplo de brinquedo: o mesmo dado, duas amostras de ruído, coeficientes trocados",
              tipo="barras", unidade="coeficiente", fonte="Exemplo de brinquedo do painel (tools/analises/13.10_risco.py)",
              nota="Verdade do exemplo: y = 1·x1 + 1·x2. x1 e x2 têm correlação de 0,999. A soma dos dois coeficientes sai perto de 2 nas duas amostras; a divisão entre eles muda de lado.",
              ref=[{"v": 1, "rotulo": "valor verdadeiro de cada um"}],
              series=[{"nome": "Amostra A", "pontos": [{"t": "peso de x1", "v": r(b["A"]["b1"])}, {"t": "peso de x2", "v": r(b["A"]["b2"])}, {"t": "soma", "v": r(b["A"]["soma"])}]},
                      {"nome": "Amostra B", "pontos": [{"t": "peso de x1", "v": r(b["B"]["b1"])}, {"t": "peso de x2", "v": r(b["B"]["b2"])}, {"t": "soma", "v": r(b["B"]["soma"])}]}])
    # sensibilidade do resíduo do Brasil: 13 países, M1 a M3, cada variável dependente; mais o caso sem o Peru
    curto = {"ex-post 2025": "2025", "ex-post 2026 (jan-set)": "2026 (jan-set)", "ex-post 2024": "2024",
             "ex-post 2023-2025": "média 2023-25", "ex-ante 16/09/2026": "ex-ante set/2026"}
    pts = []
    for s_ in res["sensibilidade"]:
        cod = s_["modelo"].split(" ")[0]
        if s_["amostra"] == "13 países" and cod in ("M1", "M2", "M3"):
            pts.append({"t": f'{curto[s_["dep"]]}, {cod}', "v": s_["residuo"]})
    g5 = dict(base, titulo="Quanto o juro real do Brasil fica acima do previsto pelos outros países (p.p.)",
              tipo="barrash", unidade="p.p.", fonte=fonte_r,
              nota="Cada barra estima o modelo sem o Brasil e mede o juro brasileiro observado menos o previsto. M1: só rating; M2: rating, inflação média de 2015 a 2024 e dívida bruta; M3: M2 mais o histórico de inflação de 1985 a 2004 (em log). Amostra de 13 países (12 sem o Brasil; 10 no ex-ante, que não cobre Peru e Coreia). Com 9 a 12 países, cada resíduo tem margem de erro grande. O M3 sem o Peru fica fora do gráfico: nessa amostra o coeficiente do histórico não se estima (t de 0,4) e o resíduo é extrapolação, com intervalo de 95% de −23 a +27 pontos.",
              series=[{"nome": "Resíduo do Brasil", "pontos": pts}])
    for nome, g in (("dispersao-rating", g1), ("dispersao-divida", g2), ("cds-latam", g3),
                    ("brinquedo-colinearidade", g4), ("residuo-brasil", g5)):
        with open(os.path.join(DADOS, f"13.10-{nome}.json"), "w", encoding="utf-8") as f:
            json.dump(g, f, ensure_ascii=False, indent=1)
            f.write("\n")


def imprimir(linhas, res):
    print("País  r2019 r2024 r2025 r2026 r23-25 exante rating dívida infl15-24 hist85-04")
    for p, l in linhas.items():
        f = lambda v: "  -  " if v is None else f"{v:5.2f}"
        print(f'{p:4} {f(l["r2019"])} {f(l["r2024"])} {f(l["r2025"])} {f(l["r2026"])} {f(l["r2023_25"])} {f(l["ex_ante"])} {l["rating"]:5}({l["degrau"]:2}) {l["divida"]:6.1f} {l["infl_15_24"]:6.2f} {l["hist_85_04"]:8.1f} ({l["hist_anos"]})')
    print(json.dumps({k: res[k] for k in ("regressoes", "correlacoes", "correlacoes_emergentes", "vif", "loo", "cds", "brinquedo")}, ensure_ascii=False))
    sb = res["serie_brasil"]
    print("\nSérie Brasil", sb["anos"], "VIF", sb["vif"])
    for k in sb["correlacoes"]:
        print("  corr", k, sb["correlacoes"][k])
    for k in ("mqo_2007-2023", "mqo_2007-2015", "mqo_2016-2023"):
        print("  ", k, sb[k]["n"], sb[k]["r2"], sb[k]["coef"], sb[k]["ep"])
    for t in sb["tabela"]:
        print("   ", t)
    print("Corr dívida x juro emergentes:", res["corr_divida_juro_emergentes"])
    rb = res["robustez_rating"]
    print("Robustez rating ±1:", rb["residuo_min"], rb["residuo_max"], rb["coef_min"], rb["coef_max"])
    print("\nTestes extras:", json.dumps(res["testes_extras"], ensure_ascii=False, indent=1))
    print("\nRisco igual ou maior:", json.dumps(res["risco_igual_ou_maior"], ensure_ascii=False))
    print("Faixas:", json.dumps(res["faixas_residuo"], ensure_ascii=False, indent=1))
    print("\nSensibilidade (resíduo do Brasil fora da amostra):")
    for s in res["sensibilidade"]:
        print(f'  {s["dep"]:24} {s["amostra"]:15} {s["modelo"]:38} n={s["n_sem_brasil"]:2} obs={s["observado"]:5} prev={s["previsto"]:5} res={s["residuo"]:5} R2={s["r2_sem_brasil"]}')


if __name__ == "__main__":
    main()

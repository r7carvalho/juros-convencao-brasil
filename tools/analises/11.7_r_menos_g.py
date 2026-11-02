#!/usr/bin/env python3
"""Sustentabilidade da dívida: r − g nominal e real do Brasil e um teste de Bohn simples (página 11.7).

Refaz dados/11.7-r-menos-g.json e dados/11.7-brinquedo-trajetorias.json; com --resumo, imprime a tabela
do texto e as regressões do teste de Bohn (que entram na página como tabela, sem gráfico).
Usa numpy só para a regressão.

Uso: python3 tools/analises/11.7_r_menos_g.py [--resumo]

Entradas
  insumos/frente-J.json   registro das tabelas "Dívida bruta do Governo Geral: fatores condicionantes"
                          das Estatísticas Fiscais do BCB (edições de setembro de 2008 a 2026, lidas em
                          28/10/2026): juros nominais apropriados sobre a DBGG em p.p. do PIB, por ano,
                          e o acumulado de jan-ago/2026. É a mesma base de dados/3.1 e dados/3.2.
  dados/brutos/sgs-13762.json  DBGG, conceito BCB, % do PIB (fim de mês)
  dados/brutos/sgs-4382.json   PIB acumulado em 12 meses, R$ milhões correntes
  dados/brutos/sgs-13522.json  IPCA acumulado em 12 meses (%)
  dados/brutos/sgs-7326.json   PIB real, variação anual (%)
  dados/brutos/sgs-5793.json   NFSP primária do setor público consolidado, 12 meses, % do PIB (+ = déficit)
  dados/brutos/sgs-4513.json   DLSP, % do PIB (fim de mês)

Método
  Taxa implícita (i) do ano t = juros apropriados no ano ÷ estoque da DBGG no fim do ano t−1.
    Como o BCB divide os fluxos pelo PIB do ano (Y_t) e o estoque está sobre Y_{t−1}:
    i_t = juros_pp_t × (Y_t / Y_{t−1}) / d_{t−1}. Reproduz a série publicada em dados/3.1 (12,55% em 2025).
  Crescimento nominal (g) = PIB de 12 meses em dezembro sobre o de dezembro anterior (SGS 4382).
  Diferencial nominal: i − g. Fator da fórmula da 3.1: (i − g)/(1 + g).
  Versão real com o IPCA (dez/dez, SGS 13522): r = (1+i)/(1+π) − 1, g_IPCA = (1+g)/(1+π) − 1,
    r − g_IPCA = (i − g)/(1 + π). O sinal é o mesmo da versão nominal; o tamanho cai um pouco.
  Para referência, crescimento real das contas nacionais (SGS 7326) e deflator implícito.
  2026 é preliminar: i de jan-ago/2026 (juros do período ÷ DBGG de dez/2025 em reais) anualizado
    por (1 + i_8m)^(12/8) − 1; g = PIB de 12 meses até set/2026 sobre o de set/2025; π = IPCA de
    12 meses até set/2026.

  Teste de Bohn (versão mínima do painel): s_t = a + ρ·d_{t−1} + b·γ_t (+ dummy de 2020) + e_t,
    com s = superávit primário do setor público consolidado em dezembro (−SGS 5793), d = DLSP ou DBGG
    em dezembro do ano anterior, γ = crescimento real (SGS 7326) como controle do ciclo.
    MQO com erros-padrão de Newey-West (2 defasagens). Sem controle de gasto temporário (o GVAR de
    Bohn), sem teste de raiz unitária: serve para mostrar o sinal, não para substituir a literatura.
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
CONSULTA = "2026-11-02"
URL_BCB = "https://www.bcb.gov.br/content/estatisticas/hist_estatisticasfiscais/202609_Tabelas_de_estatisticas_fiscais.xlsx"


def sgs(codigo):
    with open(os.path.join(BRUTOS, f"sgs-{codigo}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = {}
    for r in dados:
        if r["valor"] in ("", None):
            continue
        _, m, a = r["data"].split("/")
        out[(int(a), int(m))] = float(r["valor"])
    return out


def juros_bcb():
    with open(os.path.join(ROOT, "insumos", "frente-J.json"), encoding="utf-8") as f:
        d = json.load(f)
    for s in d["series"]:
        if s["nome"].startswith("Fator 1"):
            return {p["t"]: p["v"] for p in s["pontos"]}
    raise SystemExit("série de juros apropriados não encontrada")


def calcular():
    dbgg, pib, ipca, real = sgs(13762), sgs(4382), sgs(13522), sgs(7326)
    jur = juros_bcb()
    linhas = []
    for ano in range(2007, 2026):
        jp = jur[f"{ano}-12"]
        y1, y0 = pib[(ano, 12)], pib[(ano - 1, 12)]
        d0 = dbgg[(ano - 1, 12)]
        i = jp * (y1 / y0) / d0 * 100
        g = (y1 / y0 - 1) * 100
        pi = ipca[(ano, 12)]
        gam = real.get((ano, 1))
        linhas.append(dict(ano=str(ano), i=i, g=g, pi=pi, gam=gam, d0=d0))
    # 2006: estoque de dez/2005 não está no SGS 13762 (começa em dez/2006); usa a taxa publicada.
    y1, y0 = pib[(2006, 12)], pib[(2005, 12)]
    linhas.insert(0, dict(ano="2006", i=14.18, g=(y1 / y0 - 1) * 100, pi=ipca[(2006, 12)],
                          gam=real.get((2006, 1)), d0=None))
    # 2026 preliminar
    i8 = jur["2026-08"] * pib[(2026, 8)] / (dbgg[(2025, 12)] * pib[(2025, 12)]) * 100
    i26 = ((1 + i8 / 100) ** 1.5 - 1) * 100
    g26 = (pib[(2026, 9)] / pib[(2025, 9)] - 1) * 100
    linhas.append(dict(ano="2026*", i=i26, g=g26, pi=ipca[(2026, 9)], gam=None,
                       d0=dbgg[(2025, 12)], i8=i8))
    for l in linhas:
        l["dif"] = l["i"] - l["g"]
        l["r"] = ((1 + l["i"] / 100) / (1 + l["pi"] / 100) - 1) * 100
        l["g_ipca"] = ((1 + l["g"] / 100) / (1 + l["pi"] / 100) - 1) * 100
        l["dif_real"] = l["r"] - l["g_ipca"]
        l["defl"] = (((1 + l["g"] / 100) / (1 + l["gam"] / 100) - 1) * 100) if l["gam"] is not None else None
    return linhas


def bohn():
    prim, dlsp, dbgg, real = sgs(5793), sgs(4513), sgs(13762), sgs(7326)
    out = {}
    for nome, div, ini in (("DLSP", dlsp, 2002), ("DBGG", dbgg, 2007)):
        for rot, a0, a1 in (("completo", ini, 2025), ("até 2013", ini, 2013), ("desde 2014", 2014, 2025)):
            ys, xs, anos = [], [], []
            for ano in range(a0, a1 + 1):
                if (ano, 12) not in prim or (ano - 1, 12) not in div or (ano, 1) not in real:
                    continue
                s = -prim[(ano, 12)]
                ys.append(s)
                xs.append([1.0, div[(ano - 1, 12)], real[(ano, 1)], 1.0 if ano == 2020 else 0.0])
                anos.append(ano)
            X, y = np.array(xs), np.array(ys)
            if X[:, 3].sum() == 0:
                X = X[:, :3]
            b, *_ = np.linalg.lstsq(X, y, rcond=None)
            e = y - X @ b
            n, k = X.shape
            XtXi = np.linalg.inv(X.T @ X)
            S = (X * e[:, None]).T @ (X * e[:, None])
            for lag in (1, 2):
                w = 1 - lag / 3
                G = (X[lag:] * e[lag:, None]).T @ (X[:-lag] * e[:-lag, None])
                S += w * (G + G.T)
            V = XtXi @ S @ XtXi * n / (n - k)
            se = np.sqrt(np.diag(V))
            out[(nome, rot)] = dict(n=n, anos=(anos[0], anos[-1]), rho=b[1], se=se[1], t=b[1] / se[1],
                                    b_gam=b[2], r2=1 - (e @ e) / ((y - y.mean()) @ (y - y.mean())))
    pares = []
    for ano in range(2002, 2026):
        if (ano, 12) in prim and (ano - 1, 12) in dlsp:
            pares.append((ano, dlsp[(ano - 1, 12)], -prim[(ano, 12)]))
    return out, pares


def r2(v):
    return None if v is None else round(v, 2)


def grafico_rg(linhas):
    return {
        "titulo": "Diferencial entre juro e crescimento da dívida bruta, nominal e real (p.p.)",
        "tipo": "linha",
        "unidade": "p.p.",
        "fonte": "BCB, Estatísticas Fiscais, tabela \"Dívida bruta do Governo Geral: fatores condicionantes\" (edições de setembro de 2008 a 2026, consulta em 28/10/2026), juros apropriados sobre a DBGG; BCB, SGS 13762 (DBGG), 4382 (PIB de 12 meses) e 13522 (IPCA), coleta de 02/11/2026; cálculo do painel (tools/analises/11.7_r_menos_g.py)",
        "url": URL_BCB,
        "consulta": CONSULTA,
        "nota": "i = juros apropriados no ano ÷ DBGG do fim do ano anterior; g = crescimento do PIB nominal no ano. A versão real deflaciona os dois pelo IPCA de dezembro a dezembro: r − g = (i − g)/(1 + IPCA), com o mesmo sinal da nominal. Acima de zero, a dívida cresce em proporção do PIB se o primário for zero. 2026 é preliminar: juro de jan-ago anualizado, PIB e IPCA de 12 meses até setembro.",
        "governos": True,
        "ref": [{"v": 0, "rotulo": "juro = crescimento"}],
        "series": [
            {"nome": "Nominal (i − g)", "pontos": [{"t": l["ano"].rstrip("*"), "v": r2(l["dif"])} for l in linhas]},
            {"nome": "Real, deflator IPCA (r − g)", "pontos": [{"t": l["ano"].rstrip("*"), "v": r2(l["dif_real"])} for l in linhas]},
        ],
    }


def brinquedo():
    """Duas dívidas de 80% do PIB, primário zero, r − g = −2 e +4 p.p. (g real de 2%)."""
    series = []
    for rotulo, r, g in (("r − g = −2 (r = 0%, g = 2%)", 0.00, 0.02), ("r − g = +4 (r = 6%, g = 2%)", 0.06, 0.02)):
        d, pts = 80.0, [{"t": "Ano 0", "v": 80.0}]
        for t in range(1, 11):
            d = d * (1 + r) / (1 + g)
            pts.append({"t": f"Ano {t}", "v": round(d, 1)})
        series.append({"nome": rotulo, "pontos": pts})
    return {
        "titulo": "Duas dívidas de 80% do PIB com primário zero: r − g de −2 e de +4 pontos (% do PIB)",
        "tipo": "barras",
        "unidade": "% do PIB",
        "fonte": "Exemplo de brinquedo do painel: d_t = d_{t−1}(1 + r)/(1 + g), com primário zero (tools/analises/11.7_r_menos_g.py)",
        "url": "https://www.imf.org/external/pubs/ft/tnm/2010/tnm1002.pdf",
        "consulta": CONSULTA,
        "nota": "Números inventados. Juro real e crescimento real constantes por dez anos; nenhum superávit.",
        "series": series,
    }


def gravar(nome, obj):
    caminho = os.path.join(ROOT, "dados", nome)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("gravado", os.path.relpath(caminho, ROOT))


def main():
    linhas = calcular()
    est, _ = bohn()
    if "--resumo" in sys.argv:
        print(f"{'ano':6} {'i':>6} {'g':>6} {'i-g':>6} {'IPCA':>6} {'r':>6} {'gIPCA':>6} {'r-g':>6} {'gam':>6} {'defl':>6}")
        for l in linhas:
            f = lambda v: f"{v:6.2f}" if v is not None else "     -"
            print(f"{l['ano']:6} {f(l['i'])} {f(l['g'])} {f(l['dif'])} {f(l['pi'])} {f(l['r'])} {f(l['g_ipca'])} {f(l['dif_real'])} {f(l['gam'])} {f(l['defl'])}")
        print("2026: i jan-ago", round(linhas[-1]["i8"], 2))
        for per in (("2006", "2013"), ("2014", "2016"), ("2017", "2019"), ("2020", "2022"), ("2023", "2025")):
            sel = [l for l in linhas if per[0] <= l["ano"] <= per[1]]
            m = lambda c: sum(l[c] for l in sel) / len(sel)
            print("média", per, "i-g", round(m("dif"), 2), "r-g real", round(m("dif_real"), 2), "r", round(m("r"), 2), "i", round(m("i"), 2), "g", round(m("g"), 2))
        for k, v in est.items():
            print("Bohn", k, {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()})
        return
    gravar("11.7-r-menos-g.json", grafico_rg(linhas))
    gravar("11.7-brinquedo-trajetorias.json", brinquedo())


if __name__ == "__main__":
    main()

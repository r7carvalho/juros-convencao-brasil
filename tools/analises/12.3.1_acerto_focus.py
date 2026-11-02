#!/usr/bin/env python3
"""Acerto das projeções do Focus para o fim de ano, 2002-2025 (página 12.3.1 do painel).

Mede, para Selic, PIB e IPCA, o erro da mediana do Focus em três horizontes e compara com uma
referência ingênua (passeio aleatório). Grava os gráficos dados/12.3.1-*.json. Só usa a biblioteca
padrão.

Uso: python3 tools/analises/12.3.1_acerto_focus.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  focus-anuais_selic.json  Focus, Selic de fim de ano (mediana), API Olinda, desde 03/01/2000
  focus-anuais_pib.json    Focus, PIB Total, variação real no ano (mediana), desde 01/07/1999
  focus-anuais_ipca.json   Focus, IPCA do ano (mediana); o arquivo bruto foi cortado no limite de
                           40.000 linhas da consulta e só começa em 05/10/2007
  sgs-432.json             Selic meta (% a.a.), diária
  sgs-7326.json            PIB, variação real anual (%), vintage de 02/11/2026 (já revisada)
  sgs-13522.json           IPCA acumulado em 12 meses (%)

Método
  Projeção: mediana com baseCalculo = 0, registrada no último dia com dado do mês de referência
    (mesma regra da página 2.4.1). Horizontes para o ano Y:
      jan  = último registro de janeiro de Y (cerca de 11 meses antes do fim do ano)
      jun  = último registro de junho de Y (cerca de 6 meses antes)
      ant  = último registro de janeiro de Y-1 (cerca de 23 meses antes)
  Realizado: Selic meta no último dia de Y (SGS 432); PIB do ano Y (SGS 7326); IPCA do ano Y
    (SGS 13522 em dezembro). Variante "pib1": o PIB realizado é aproximado pela última
    mediana do Focus para o ano, registrada dias antes da primeira divulgação do IBGE, para separar
    o erro de projeção do efeito das revisões posteriores (SGS 7326 traz a série já revisada).
  Erro = realizado - projetado. Positivo: o mercado projetou abaixo do que veio.
  Referência ingênua (passeio aleatório): o último valor conhecido na data da projeção.
      Selic: Selic meta no dia da projeção.
      IPCA: IPCA de 12 meses do mês anterior ao da projeção (último divulgado).
      PIB: crescimento do ano anterior (Y-1 para jan e jun; Y-2 para ant). Em janeiro o PIB de
           Y-1 ainda não saiu, de modo que a referência ingênua leva vantagem de informação.
  Anos de eleição presidencial: 2002, 2006, 2010, 2014, 2018, 2022.
  Anos de choque (escolha do painel, declarada na página): 2002 (crise de confiança),
      2008 e 2009 (crise financeira), 2015 e 2016 (recessão), 2020 (pandemia), 2021 e 2022
      (inflação pós-pandemia e guerra).
"""
import json
import math
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
DADOS = os.path.join(ROOT, "dados")
CONSULTA = "2026-11-02"
ANOS = list(range(2002, 2026))
ELEICAO = {2002, 2006, 2010, 2014, 2018, 2022}
CHOQUE = {2002, 2008, 2009, 2015, 2016, 2020, 2021, 2022}
HORIZ = ["jan", "jun", "ant"]
NOME_H = {"jan": "janeiro do ano", "jun": "junho do ano", "ant": "janeiro do ano anterior"}


def carregar(nome):
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        return json.load(f)["dados"]


def sgs(nome):
    out = {}
    for r in carregar(nome):
        d, m, a = r["data"].split("/")
        out[date(int(a), int(m), int(d))] = float(r["valor"])
    return out


def focus_anual(nome):
    """{ano_ref: {date: mediana}} com baseCalculo 0."""
    out = {}
    for r in carregar(nome):
        if r["baseCalculo"] != 0 or r["Mediana"] is None:
            continue
        out.setdefault(int(r["DataReferencia"]), {})[date.fromisoformat(r["Data"])] = float(r["Mediana"])
    return out


def ultimo_no_mes(serie, ano, mes):
    ds = [d for d in serie if d.year == ano and d.month == mes]
    if not ds:
        return None, None
    d = max(ds)
    return d, serie[d]


def valor_em(serie, dia):
    ds = [d for d in serie if d <= dia]
    return serie[max(ds)] if ds else None


def data_proj(ano, h):
    return {"jan": (ano, 1), "jun": (ano, 6), "ant": (ano - 1, 1)}[h]


# ---------------------------------------------------------------- realizados
FOC = {
    "selic": focus_anual("focus-anuais_selic.json"),
    "pib": focus_anual("focus-anuais_pib.json"),
    "ipca": focus_anual("focus-anuais_ipca.json"),
}

selic_d = sgs("sgs-432.json")
pib_a = {d.year: v for d, v in sgs("sgs-7326.json").items()}
ipca12 = sgs("sgs-13522.json")


def selic_fim(ano):
    return valor_em(selic_d, date(ano, 12, 31))


def ipca_ano(ano):
    """IPCA do ano: acumulado em 12 meses de dezembro (SGS 13522), igual ao produto dos 12 meses do
    SGS 433 com o arredondamento oficial."""
    return ipca12[date(ano, 12, 1)]


def pib_primeira(ano):
    """Última mediana do Focus para o ano, registrada pouco antes da divulgação do IBGE (fim de
    fevereiro ou início de março de ano+1): aproximação da primeira divulgação do PIB, antes das
    revisões e das mudanças de base das Contas Nacionais."""
    s = FOC["pib"][ano]
    return s[max(s)]


REAL = {
    "selic": {a: selic_fim(a) for a in ANOS},
    "pib": {a: pib_a[a] for a in ANOS},
    "ipca": {a: ipca_ano(a) for a in ANOS},
}
REAL["pib1"] = {a: pib_primeira(a) for a in ANOS}
FOC["pib1"] = FOC["pib"]


def ingenuo(var, ano, h):
    a, m = data_proj(ano, h)
    if var == "selic":
        d, _ = ultimo_no_mes(FOC["selic"].get(ano, {}), a, m)
        dia = d if d else date(a, m, 28)
        return valor_em(selic_d, dia)
    if var == "ipca":
        # último IPCA 12 meses divulgado: o do mês anterior
        mm, aa = (m - 1, a) if m > 1 else (12, a - 1)
        return ipca12[date(aa, mm, 1)]
    if var == "pib":
        return pib_a[ano - 2] if h == "ant" else pib_a[ano - 1]
    if var == "pib1":
        return pib_primeira(ano - 2) if h == "ant" else pib_primeira(ano - 1)




def tabela(var):
    linhas = []
    for ano in ANOS:
        lin = {"ano": ano, "real": REAL[var][ano]}
        for h in HORIZ:
            a, m = data_proj(ano, h)
            d, v = ultimo_no_mes(FOC[var].get(ano, {}), a, m)
            lin[h] = v
            lin[h + "_data"] = d.isoformat() if d else None
            lin[h + "_ing"] = ingenuo(var, ano, h) if v is not None else None
        linhas.append(lin)
    return linhas


def stats(linhas, h, filtro=lambda a: True):
    e, ei = [], []
    for l in linhas:
        if l[h] is None or not filtro(l["ano"]):
            continue
        e.append(l["real"] - l[h])
        ei.append(l["real"] - l[h + "_ing"])
    n = len(e)
    if n == 0:
        return None
    me = sum(e) / n
    mae = sum(abs(x) for x in e) / n
    rmse = math.sqrt(sum(x * x for x in e) / n)
    mae_i = sum(abs(x) for x in ei) / n
    rmse_i = math.sqrt(sum(x * x for x in ei) / n)
    pos = sum(1 for x in e if x > 0.005)
    neg = sum(1 for x in e if x < -0.005)
    venceu = sum(1 for x, y in zip(e, ei) if abs(x) < abs(y))
    sd = math.sqrt(sum((x - me) ** 2 for x in e) / (n - 1)) if n > 1 else float("nan")
    t = me / (sd / math.sqrt(n)) if n > 1 and sd > 0 else float("nan")
    med = sorted(e)[n // 2] if n % 2 else (sorted(e)[n // 2 - 1] + sorted(e)[n // 2]) / 2
    return dict(n=n, me=me, med=med, mae=mae, rmse=rmse, pos=pos, neg=neg, t=t,
                mae_i=mae_i, rmse_i=rmse_i, me_i=sum(ei) / n, venceu=venceu,
                u_mae=mae / mae_i if mae_i else float("nan"),
                u_rmse=rmse / rmse_i if rmse_i else float("nan"))


def fmt(x, nd=2):
    return "  —  " if x is None else f"{x:6.{nd}f}"


def imprimir(var, linhas):
    print(f"\n=== {var.upper()} ===")
    print(" ano   real |  jan(data)          ing  err |  jun          ing  err |  ant(data)          ing  err")
    for l in linhas:
        s = f"{l['ano']} {fmt(l['real'])} |"
        for h in HORIZ:
            if l[h] is None:
                s += "      sem dado                  |"
            else:
                s += f" {fmt(l[h])} ({l[h+'_data']}) {fmt(l[h+'_ing'])} {l['real']-l[h]:+6.2f} |"
        print(s)
    for h in HORIZ:
        for rot, f in [("todos", lambda a: True), ("eleição", lambda a: a in ELEICAO),
                       ("não eleição", lambda a: a not in ELEICAO), ("choque", lambda a: a in CHOQUE),
                       ("sem choque", lambda a: a not in CHOQUE),
                       ("2002-2013", lambda a: a <= 2013), ("2014-2025", lambda a: a >= 2014),
                       ("2017-2025", lambda a: a >= 2017), ("2023-2025", lambda a: a >= 2023)]:
            st = stats(linhas, h, f)
            if st:
                print(f"  {h:3s} {rot:12s} n={st['n']:2d} viés={st['me']:+.2f} mediana={st['med']:+.2f} "
                      f"t={st['t']:+.2f} EAM={st['mae']:.2f} REQM={st['rmse']:.2f} acima={st['pos']} abaixo={st['neg']} "
                      f"| ingênuo viés={st['me_i']:+.2f} EAM={st['mae_i']:.2f} REQM={st['rmse_i']:.2f} "
                      f"U(EAM)={st['u_mae']:.2f} U(REQM)={st['u_rmse']:.2f} Focus melhor em {st['venceu']}")


def grafico(nome, titulo, unidade, nota, series, tipo="barras", ref=None):
    g = {"titulo": titulo, "tipo": tipo, "unidade": unidade,
         "fonte": "BCB, Sistema de Expectativas de Mercado (Focus), API Olinda; BCB, SGS 432, 13522 e 7326; cálculo do painel",
         "url": "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/aplicacao",
         "consulta": CONSULTA, "nota": nota}
    if ref:
        g["ref"] = ref
    g["series"] = series
    with open(os.path.join(DADOS, nome), "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=1)
        f.write("\n")


def serie_erro(linhas, h, nome):
    return {"nome": nome, "pontos": [{"t": str(l["ano"]),
                                      "v": None if l[h] is None else round(l["real"] - l[h], 2)}
                                     for l in linhas]}


def main():
    T = {v: tabela(v) for v in ["selic", "pib", "pib1", "ipca"]}
    if "--resumo" in sys.argv:
        for v in T:
            imprimir(v, T[v])

    nota = ("Erro = realizado menos mediana do Focus (baseCalculo 0) no último dia com dado do mês. "
            "Positivo: o mercado projetou abaixo do que veio. Realizado: Selic meta em 31/12 (SGS 432), "
            "PIB do ano na série de 02/11/2026, já revisada (SGS 7326), IPCA do ano (SGS 13522, dezembro).")
    grafico("12.3.1-erro-selic.json",
            "Erro do Focus para a Selic de fim de ano, 2002-2025 (p.p.)", "p.p.",
            nota + " Negativo: a Selic terminou o ano abaixo do projetado.",
            [serie_erro(T["selic"], "jan", "Projeção de janeiro do ano"),
             serie_erro(T["selic"], "ant", "Projeção de janeiro do ano anterior")],
            ref=[{"v": 0, "rotulo": "acerto"}])
    grafico("12.3.1-erro-pib.json",
            "Erro do Focus de janeiro para o crescimento do PIB, 2002-2025 (p.p.)", "p.p.",
            "Erro = PIB realizado menos mediana do Focus no último dia com dado de janeiro do próprio ano. "
            "Positivo: o PIB cresceu mais do que o projetado. Primeira divulgação aproximada pela última mediana "
            "do Focus antes da divulgação do IBGE (fim de fevereiro ou início de março do ano seguinte); "
            "série revisada: SGS 7326 em 02/11/2026, que incorpora as mudanças de base das Contas Nacionais.",
            [serie_erro(T["pib1"], "jan", "Contra a primeira divulgação (aprox.)"),
             serie_erro(T["pib"], "jan", "Contra a série revisada")],
            ref=[{"v": 0, "rotulo": "acerto"}])
    # Selic projetada em janeiro x realizada (linha)
    grafico("12.3.1-selic-projetada-realizada.json",
            "Selic de fim de ano: projetada em janeiro e realizada, 2002-2025 (% a.a.)", "% a.a.",
            "Mediana do Focus no último dia com dado de janeiro do próprio ano e de janeiro do ano anterior; "
            "Selic meta em 31/12 (SGS 432).",
            [{"nome": "Realizada em 31/12", "pontos": [{"t": str(l["ano"]), "v": round(l["real"], 2)} for l in T["selic"]]},
             {"nome": "Focus, janeiro do ano", "pontos": [{"t": str(l["ano"]), "v": l["jan"]} for l in T["selic"]]},
             {"nome": "Focus, janeiro do ano anterior", "pontos": [{"t": str(l["ano"]), "v": l["ant"]} for l in T["selic"]]}],
            tipo="linha")
    # quadro-resumo do viés por variável e horizonte (barras)
    cats = []
    for v, rot in [("selic", "Selic"), ("pib1", "PIB"), ("ipca", "IPCA")]:
        for h, hr in [("jan", "jan."), ("jun", "jun."), ("ant", "ano ant.")]:
            st = stats(T[v], h)
            cats.append((f"{rot} {hr}", st))
    grafico("12.3.1-vies-resumo.json",
            "Viés e erro absoluto médio do Focus por variável e horizonte (p.p.)", "p.p.",
            "Selic e PIB: anos de 2002 a 2025; PIB contra a primeira divulgação aproximada. IPCA: 2008 a 2025 (janeiro e junho) e 2009 a 2025 (ano anterior), "
            "porque o arquivo bruto do IPCA anual começa em outubro de 2007. Viés = média de realizado menos projetado.",
            [{"nome": "Viés (erro médio)", "pontos": [{"t": c, "v": round(s["me"], 2)} for c, s in cats]},
             {"nome": "Erro absoluto médio", "pontos": [{"t": c, "v": round(s["mae"], 2)} for c, s in cats]}])
    if "--resumo" not in sys.argv:
        print("gráficos gravados em dados/12.3.1-*.json")


if __name__ == "__main__":
    main()

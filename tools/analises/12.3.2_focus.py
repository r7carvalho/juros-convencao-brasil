#!/usr/bin/env python3
"""O Focus como instituição: respondentes, dispersão e erro comum (página 12.3.2 do painel).

Mede, com as estatísticas agregadas que a API Olinda publica (mediana, desvio-padrão, mínimo,
máximo e número de respondentes), três coisas:
  1. quantos respondentes entram em cada estatística, mês a mês, desde que o campo existe (2014);
  2. quanto as projeções se dispersam entre instituições ao longo do tempo;
  3. se a dispersão mede a incerteza: quantas vezes o valor realizado caiu fora de toda a faixa
     de projeções (do mínimo ao máximo) e quantos desvios-padrão entre respondentes separam o
     realizado da mediana.
Grava dados/12.3.2-*.json. Só usa a biblioteca padrão.

Uso: python3 tools/analises/12.3.2_focus.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  focus-anuais_selic.json  Focus, Selic de fim de ano; desvio, mínimo e máximo desde 06/11/2001
  focus-anuais_pib.json    Focus, PIB Total
  focus-anuais_ipca.json   Focus, IPCA do ano; o arquivo começa em 05/10/2007 (corte da consulta)
  focus-inflacao_12m.json  Focus, IPCA dos 12 meses seguintes, desde 07/11/2001
  sgs-432.json, sgs-13522.json

Método
  Estatística do dia: baseCalculo = 0 (a série longa). O campo numeroRespondentes só existe a
    partir de 02/01/2014. A partir de 2014 a API traz também baseCalculo = 1, outra janela de
    validade das projeções, com menos respondentes; não é usada aqui, salvo na comparação das
    medianas das duas bases (--resumo).
  Projeção de janeiro: último registro de janeiro do ano Y para o fim do ano Y (cerca de 11
    meses); "ano anterior": último registro de janeiro de Y-1 para o fim de Y (cerca de 23 meses).
  Realizado: Selic meta em 31/12 (SGS 432); IPCA do ano (SGS 13522, dezembro); PIB aproximado pela
    última mediana do Focus para o ano, registrada dias antes da primeira divulgação do IBGE (a
    mesma aproximação da página 12.3.1, que separa erro de projeção de revisão posterior).
  Fora da faixa: realizado acima do máximo ou abaixo do mínimo de todas as projeções válidas.
  z = (realizado - mediana) / desvio-padrão entre respondentes, no mesmo dia da mediana.
  Se as projeções fossem tiros independentes em torno do valor verdadeiro, e a dispersão entre
    elas medisse a incerteza, |z| ficaria em geral abaixo de 1 (mediana de |z| perto de 0,67 numa
    normal) e o realizado quase nunca cairia fora da faixa de cem ou mais projeções.
"""
import json
import math
import os
import statistics as st
import sys
from collections import defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
DADOS = os.path.join(ROOT, "dados")
CONSULTA = "2026-11-02"
URL = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/aplicacao"
FONTE = "BCB, Sistema de Expectativas de Mercado (Focus), API Olinda"


def carregar(nome):
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        return json.load(f)["dados"]


def sgs(nome):
    out = {}
    for r in carregar(nome):
        d, m, a = r["data"].split("/")
        out[date(int(a), int(m), int(d))] = float(r["valor"])
    return out


def anual(nome, base=0):
    """{ano_ref: {data: registro}} para a base de cálculo pedida."""
    out = defaultdict(dict)
    for r in carregar(nome):
        if r["baseCalculo"] != base or r["Mediana"] is None:
            continue
        out[int(r["DataReferencia"])][date.fromisoformat(r["Data"])] = r
    return out


def ultimo_no_mes(serie, ano, mes):
    ds = [d for d in serie if d.year == ano and d.month == mes]
    return serie[max(ds)] if ds else None


FOC = {
    "selic": anual("focus-anuais_selic.json"),
    "pib": anual("focus-anuais_pib.json"),
    "ipca": anual("focus-anuais_ipca.json"),
}
SELIC_D = sgs("sgs-432.json")
IPCA12 = sgs("sgs-13522.json")


def selic_fim(a):
    return SELIC_D[max(d for d in SELIC_D if d <= date(a, 12, 31))]


def pib_primeira(a):
    s = FOC["pib"][a]
    return s[max(s)]["Mediana"]


REAL = {
    "selic": selic_fim,
    "pib": pib_primeira,
    "ipca": lambda a: IPCA12[date(a, 12, 1)],
}
ANOS = {"selic": range(2002, 2026), "pib": range(2002, 2026), "ipca": range(2008, 2026)}
NOME = {"selic": "Selic de fim de ano", "pib": "PIB do ano", "ipca": "IPCA do ano"}


def linhas_faixa(var, h):
    out = []
    for a in ANOS[var]:
        if h == "jan":
            r = ultimo_no_mes(FOC[var].get(a, {}), a, 1)
        else:
            r = ultimo_no_mes(FOC[var].get(a, {}), a - 1, 1)
        if not r or r["Minimo"] is None or not r["DesvioPadrao"]:
            continue
        x = REAL[var](a)
        e = x - r["Mediana"]
        out.append(dict(ano=a, data=r["Data"], med=r["Mediana"], dp=r["DesvioPadrao"],
                        mn=r["Minimo"], mx=r["Maximo"], n=r["numeroRespondentes"], real=x,
                        erro=e, z=e / r["DesvioPadrao"],
                        fora=(x > r["Maximo"] + 1e-9) or (x < r["Minimo"] - 1e-9)))
    return out


def spearman(x, y):
    def ranks(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    rx, ry = ranks(x), ranks(y)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den


def resumo_faixa():
    tab = []
    for var in ["selic", "ipca", "pib"]:
        for h in ["jan", "ant"]:
            ls = linhas_faixa(var, h)
            zs = [abs(l["z"]) for l in ls]
            dps = [l["dp"] for l in ls]
            eas = [abs(l["erro"]) for l in ls]
            tab.append(dict(var=var, h=h, n=len(ls), fora=sum(l["fora"] for l in ls),
                            z_med=st.median(zs), dp_med=st.median(dps), ea_med=st.median(eas),
                            rho=spearman(dps, eas), anos=(ls[0]["ano"], ls[-1]["ano"]), linhas=ls))
    return tab


# ------------------------------------------------------------- séries mensais
def mensal_12m():
    """Último registro de cada mês do IPCA 12 meses à frente (não suavizado, base 0)."""
    bym = defaultdict(list)
    for r in carregar("focus-inflacao_12m.json"):
        if r["Suavizada"] == "N" and r["baseCalculo"] == 0 and r["DesvioPadrao"] is not None:
            bym[r["Data"][:7]].append(r)
    return {m: max(rs, key=lambda x: x["Data"]) for m, rs in sorted(bym.items())}


def respondentes_mensal():
    """Maior número de respondentes registrado em cada mês, para a pergunta do ano corrente
    (IPCA, Selic, PIB) e para o IPCA 12 meses à frente, base 0, de 2014 em diante."""
    out = {}
    for var, nome in [("ipca", "IPCA do ano corrente"), ("selic", "Selic do fim do ano corrente"),
                      ("pib", "PIB do ano corrente")]:
        bym = defaultdict(int)
        for a, s in FOC[var].items():
            for d, r in s.items():
                if d.year == a and r["numeroRespondentes"] is not None:
                    k = f"{d.year}-{d.month:02d}"
                    bym[k] = max(bym[k], r["numeroRespondentes"])
        out[nome] = dict(sorted(bym.items()))
    bym = defaultdict(int)
    for r in carregar("focus-inflacao_12m.json"):
        if r["Suavizada"] == "N" and r["baseCalculo"] == 0 and r["numeroRespondentes"] is not None:
            k = r["Data"][:7]
            bym[k] = max(bym[k], r["numeroRespondentes"])
    out["IPCA dos 12 meses seguintes"] = dict(sorted(bym.items()))
    return out


def comparar_bases():
    out = {}
    for var in ["ipca", "selic"]:
        b1 = anual(f"focus-anuais_{var}.json", base=1)
        dif, n0, n1 = [], [], []
        for a, s in b1.items():
            for d, r1 in s.items():
                r0 = FOC[var].get(a, {}).get(d)
                if r0 and d.year == a:
                    dif.append(abs(r0["Mediana"] - r1["Mediana"]))
                    if r0["numeroRespondentes"] and r1["numeroRespondentes"]:
                        n0.append(r0["numeroRespondentes"])
                        n1.append(r1["numeroRespondentes"])
        out[var] = dict(dias=len(dif), dif_media=st.mean(dif), dif_max=max(dif),
                        n0=st.mean(n0), n1=st.mean(n1))
    return out


# ------------------------------------------------------------------ gráficos
def gravar(nome, spec):
    spec = {"titulo": spec.pop("titulo"), "tipo": spec.pop("tipo"), "unidade": spec.pop("unidade"),
            "fonte": spec.pop("fonte", FONTE + "; cálculo do painel"), "url": URL,
            "consulta": CONSULTA, **spec}
    with open(os.path.join(DADOS, nome), "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=1)
        f.write("\n")


def r2(x):
    return None if x is None else round(x, 2)


def main():
    tab = resumo_faixa()
    m12 = mensal_12m()
    resp = respondentes_mensal()

    # 1. Dispersão do IPCA 12 meses à frente
    gravar("12.3.2-dispersao-ipca12m.json", dict(
        titulo="Desvio-padrão entre as projeções do IPCA dos 12 meses seguintes, 2001-2026 (p.p.)",
        tipo="linha", unidade="p.p.",
        nota=("Desvio-padrão entre as projeções das instituições, no último dia com dado de cada mês; "
              "série não suavizada, base de cálculo 0 (projeções dos últimos 30 dias)."),
        governos=True,
        series=[{"nome": "Desvio-padrão entre respondentes",
                 "pontos": [{"t": m, "v": r2(r["DesvioPadrao"])} for m, r in m12.items()]}]))

    # 2. Faixa das projeções de janeiro para a Selic de fim de ano e o realizado
    ls = linhas_faixa("selic", "jan")
    gravar("12.3.2-selic-faixa.json", dict(
        titulo="Selic de fim de ano: faixa das projeções de janeiro e Selic realizada, 2002-2025 (% a.a.)",
        tipo="linha", unidade="% a.a.",
        fonte=FONTE + "; BCB, SGS 432; cálculo do painel",
        nota=("Mínimo, mediana e máximo das projeções válidas no último dia com dado de janeiro de cada "
              "ano, para a Selic de 31/12 do mesmo ano; Selic meta em 31/12 (SGS 432). Em 16 dos 24 anos "
              "a Selic realizada ficou fora da faixa."),
        series=[
            {"nome": "Realizada em 31/12", "pontos": [{"t": str(l["ano"]), "v": l["real"]} for l in ls]},
            {"nome": "Maior projeção", "pontos": [{"t": str(l["ano"]), "v": r2(l["mx"])} for l in ls]},
            {"nome": "Mediana", "pontos": [{"t": str(l["ano"]), "v": r2(l["med"])} for l in ls]},
            {"nome": "Menor projeção", "pontos": [{"t": str(l["ano"]), "v": r2(l["mn"])} for l in ls]},
        ]))

    # 3. Respondentes por mês
    gravar("12.3.2-respondentes.json", dict(
        titulo="Instituições que entram na estatística do Focus, maior número em cada mês, 2014-2026",
        tipo="linha", unidade="instituições",
        nota=("Campo numeroRespondentes da API Olinda, que só existe desde 02/01/2014; maior valor "
              "registrado no mês, base de cálculo 0. O número de participantes cadastrados é maior "
              "(165 em julho de 2026, segundo o presidente do BC)."),
        series=[{"nome": k, "pontos": [{"t": m, "v": v} for m, v in s.items()]} for k, s in resp.items()]))

    if "--resumo" in sys.argv:
        print("Faixa e z (realizado - mediana)/dp")
        for t in tab:
            print(f"{t['var']:6} {t['h']:4} {t['anos']} n={t['n']:2} fora={t['fora']:2} "
                  f"({100*t['fora']/t['n']:.0f}%) mediana|z|={t['z_med']:.2f} "
                  f"dp_med={t['dp_med']:.2f} |erro|_med={t['ea_med']:.2f} "
                  f"spearman(dp,|erro|)={t['rho']:.2f}")
        print("\nAno a ano (jan)")
        for t in tab:
            if t["h"] != "jan":
                continue
            print(t["var"])
            for l in t["linhas"]:
                print(f"  {l['ano']} {l['data']} med {l['med']:6.2f} dp {l['dp']:.2f} "
                      f"[{l['mn']:.2f}; {l['mx']:.2f}] real {l['real']:6.2f} z {l['z']:6.1f} "
                      f"n {l['n']} {'FORA' if l['fora'] else ''}")
        print("\nIPCA 12m: desvio-padrão médio por período")
        for a, b in [(2002, 2003), (2004, 2014), (2015, 2016), (2017, 2019), (2020, 2022),
                     (2023, 2026), (2004, 2026)]:
            v = [r["DesvioPadrao"] for m, r in m12.items() if a <= int(m[:4]) <= b]
            cv = [r["DesvioPadrao"] / r["Mediana"] for m, r in m12.items() if a <= int(m[:4]) <= b]
            print(f"  {a}-{b}: dp {st.mean(v):.2f}  cv {st.mean(cv):.3f}")
        mx = max(m12.items(), key=lambda kv: kv[1]["DesvioPadrao"])
        mn = min(m12.items(), key=lambda kv: kv[1]["DesvioPadrao"])
        print(f"  máximo {mx[0]} {mx[1]['DesvioPadrao']}; mínimo {mn[0]} {mn[1]['DesvioPadrao']}")
        print(f"  último {list(m12)[-1]}: {list(m12.values())[-1]}")
        print("\nRespondentes (média anual do máximo mensal)")
        for k, s in resp.items():
            por = defaultdict(list)
            for m, v in s.items():
                por[m[:4]].append(v)
            print(" ", k, {a: round(st.mean(v)) for a, v in por.items()})
        print("\nBase 0 x base 1 (ano corrente)", comparar_bases())


if __name__ == "__main__":
    main()

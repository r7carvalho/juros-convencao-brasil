#!/usr/bin/env python3
"""Reservas internacionais e custo de carregamento (página 10.3.6).

Refaz dados/10.3.6-reservas.json e dados/10.3.6-custo-carregamento.json a partir do acervo bruto.
Só usa a biblioteca padrão.

Uso: python3 tools/analises/10.3.6_reservas.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  sgs-3546.json   reservas internacionais, conceito liquidez, fim de mês (US$ milhões)
  sgs-1.json      dólar PTAX venda, diário (R$/US$); o painel usa o último dia útil de cada mês
  sgs-4390.json   Selic acumulada no mês (% a.m.)
  sgs-4382.json   PIB acumulado em 12 meses, R$ milhões correntes
  bis-politica_monetaria.csv  taxa de política dos EUA (ponto médio do intervalo dos fed funds,
                  fim de mês), BIS

Método (declarado na página 10.3.6; mesmo desenho da IFI, Nota Técnica 39, 2019, que mostra o
custo com e sem a variação cambial):
  Para cada mês m, com R = reservas em US$ no fim do mês anterior e E = PTAX do fim do mês:
    custo de juros (diferencial)  = R(m-1) × E(m-1) × [ s(m) − u(m) ]
        s(m) = Selic do mês (SGS 4390 / 100)
        u(m) = (1 + taxa dos EUA / 100)^(1/12) − 1, com a taxa média dos fins de m−1 e m
        A taxa dos EUA entra como aproximação do rendimento das reservas. O rendimento
        efetivo publicado pelo BCB (Relatório de Gestão das Reservas) difere ano a ano porque
        a carteira tem prazo, outras moedas e ouro; em 2025 foi de 9,18% em dólares, contra
        cerca de 4,2% da taxa americana média.
    efeito cambial = R(m-1) × [ E(m) − E(m-1) ]   (ganho em reais quando o dólar sobe)
    custo líquido  = custo de juros − efeito cambial
  O ano soma os doze meses e divide pelo PIB do ano (SGS 4382 de dezembro). O último ponto
  é a soma dos 12 meses até set/2026 sobre o PIB de 12 meses até set/2026.
  Não entram: o resultado dos swaps cambiais (passivo à parte), a mudança do estoque por
  compras e vendas dentro do mês, o imposto implícito de a base monetária não render juros.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
CONSULTA = "2026-11-02"
URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.3546/dados?formato=json"


def sgs_mensal(codigo):
    with open(os.path.join(BRUTOS, f"sgs-{codigo}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = {}
    for r in dados:
        if r["valor"] in ("", None):
            continue
        _, m, a = r["data"].split("/")
        out[(int(a), int(m))] = float(r["valor"])
    return out


def ptax_fim_de_mes():
    with open(os.path.join(BRUTOS, "sgs-1.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = {}
    for r in dados:  # a série vem em ordem cronológica; o último valor do mês fica
        if r["valor"] in ("", None):
            continue
        d, m, a = r["data"].split("/")
        out[(int(a), int(m))] = float(r["valor"])
    return out


def eua():
    out = {}
    with open(os.path.join(BRUTOS, "bis-politica_monetaria.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["REF_AREA"] != "US" or not r["OBS_VALUE"]:
                continue
            a, m = r["TIME_PERIOD"].split("-")
            out[(int(a), int(m))] = float(r["OBS_VALUE"])
    return out


def anterior(k):
    a, m = k
    return (a - 1, 12) if m == 1 else (a, m - 1)


def mensal():
    res, ptax, selic, us = sgs_mensal(3546), ptax_fim_de_mes(), sgs_mensal(4390), eua()
    linhas = []
    for k in sorted(selic):
        k0 = anterior(k)
        if k[0] < 2000 or not all(x in d for x, d in ((k0, res), (k0, ptax), (k, ptax), (k, us), (k0, us))):
            continue
        r0 = res[k0]  # US$ milhões
        e0, e1 = ptax[k0], ptax[k]
        s = selic[k] / 100
        u = (1 + (us[k0] + us[k]) / 200) ** (1 / 12) - 1
        juros = r0 * e0 * (s - u)  # R$ milhões
        cambio = r0 * (e1 - e0)
        linhas.append(dict(k=k, juros=juros, cambio=cambio, liquido=juros - cambio,
                           estoque_rs=r0 * e0, selic=s, us=u))
    return linhas


def agregar(linhas, pib):
    """Anos-calendário completos e os 12 meses até o último mês disponível."""
    anos = {}
    for l in linhas:
        anos.setdefault(l["k"][0], []).append(l)
    out = []
    for a in sorted(anos):
        ls = anos[a]
        if len(ls) == 12 and (a, 12) in pib:
            out.append((str(a), ls, pib[(a, 12)]))
    ult = linhas[-1]["k"]
    if ult[1] != 12:
        ls = linhas[-12:]
        out.append((f"{ult[0]}*", ls, pib[ult]))
    res = []
    for rot, ls, p in out:
        j = sum(l["juros"] for l in ls)
        c = sum(l["cambio"] for l in ls)
        sel = 1.0
        usa = 1.0
        for l in ls:
            sel *= 1 + l["selic"]
            usa *= 1 + l["us"]
        res.append(dict(rot=rot, juros=j, cambio=c, liquido=j - c, pib=p,
                        juros_pib=100 * j / p, cambio_pib=100 * c / p, liquido_pib=100 * (j - c) / p,
                        estoque_medio=sum(l["estoque_rs"] for l in ls) / len(ls),
                        selic_ano=100 * (sel - 1), us_ano=100 * (usa - 1)))
    return res


def r2(v):
    return round(v, 2)


def grafico_reservas():
    res = sgs_mensal(3546)
    pts = [{"t": f"{a}-{m:02d}", "v": round(v / 1000, 1)} for (a, m), v in sorted(res.items()) if a >= 1995]
    return {
        "titulo": "Reservas internacionais do Brasil, conceito liquidez (US$ bilhões, fim de mês)",
        "tipo": "linha",
        "unidade": "US$ bi",
        "fonte": "BCB, SGS 3546 (reservas internacionais, conceito liquidez), coleta de 02/11/2026",
        "url": URL,
        "consulta": CONSULTA,
        "nota": "Mensal, jan/1995 a set/2026. Em dez/2024 a queda de US$ 33,3 bi corresponde praticamente à soma das vendas à vista e de linha do mês. O estoque de swaps cambiais não entra: é um passivo em reais referenciado no dólar, fora das reservas.",
        "governos": True,
        "series": [{"nome": "Reservas", "pontos": pts}],
    }


def grafico_custo(agg):
    sel = [x for x in agg if x["rot"] >= "2003"]
    return {
        "titulo": "Custo de carregar as reservas: diferencial de juros e efeito do câmbio (% do PIB, por ano)",
        "tipo": "empilhadas",
        "unidade": "% do PIB",
        "fonte": "BCB, SGS 3546 (reservas), 1 (PTAX), 4390 (Selic) e 4382 (PIB de 12 meses), coleta de 02/11/2026; BIS, taxa de política dos EUA (consulta em 02/11/2026); cálculo do painel (tools/analises/10.3.6_reservas.py)",
        "url": URL,
        "consulta": CONSULTA,
        "nota": "Positivo é custo para o setor público, negativo é ganho. Diferencial de juros = estoque de reservas do mês anterior, em reais, vezes (Selic do mês − taxa de política dos EUA no mês), somado no ano. Efeito do câmbio = estoque em dólares vezes a variação da PTAX no mês, com sinal trocado (a alta do dólar é ganho). A soma das duas barras é o custo líquido com câmbio. A taxa dos EUA aproxima o rendimento das reservas; o rendimento efetivo publicado pelo BCB difere (9,18% em dólares em 2025). 2026* = 12 meses até set/2026.",
        "ref": [{"v": 0, "rotulo": ""}],
        "series": [
            {"nome": "Diferencial de juros (Selic − juro americano)",
             "pontos": [{"t": x["rot"], "v": r2(x["juros_pib"])} for x in sel]},
            {"nome": "Efeito do câmbio sobre as reservas (sinal trocado)",
             "pontos": [{"t": x["rot"], "v": r2(-x["cambio_pib"])} for x in sel]},
        ],
    }


def gravar(nome, obj):
    caminho = os.path.join(ROOT, "dados", nome)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("gravado", os.path.relpath(caminho, ROOT))


def main():
    pib = sgs_mensal(4382)
    linhas = mensal()
    agg = agregar(linhas, pib)
    if "--resumo" in sys.argv:
        print(f"{'ano':>6} {'estq R$bi':>9} {'Selic':>6} {'EUA':>5} {'juros R$bi':>10} {'%PIB':>5} {'câmbio R$bi':>11} {'%PIB':>6} {'líq R$bi':>9} {'%PIB':>6}")
        for x in agg:
            print(f"{x['rot']:>6} {x['estoque_medio']/1000:9.0f} {x['selic_ano']:6.2f} {x['us_ano']:5.2f} "
                  f"{x['juros']/1000:10.1f} {x['juros_pib']:5.2f} {x['cambio']/1000:11.1f} {x['cambio_pib']:6.2f} "
                  f"{x['liquido']/1000:9.1f} {x['liquido_pib']:6.2f}")
        for a0, a1 in ((2003, 2025), (2006, 2025), (2012, 2025), (2016, 2025)):
            ss = [x for x in agg if x["rot"].isdigit() and a0 <= int(x["rot"]) <= a1]
            print(f"{a0}-{a1}: juros R$ {sum(x['juros'] for x in ss)/1e3:.0f} bi, média {sum(x['juros_pib'] for x in ss)/len(ss):.2f}% PIB; "
                  f"câmbio R$ {sum(x['cambio'] for x in ss)/1e3:.0f} bi; líquido R$ {sum(x['liquido'] for x in ss)/1e3:.0f} bi, "
                  f"média {sum(x['liquido_pib'] for x in ss)/len(ss):.2f}% PIB")
        return
    gravar("10.3.6-reservas.json", grafico_reservas())
    gravar("10.3.6-custo-carregamento.json", grafico_custo(agg))


if __name__ == "__main__":
    main()

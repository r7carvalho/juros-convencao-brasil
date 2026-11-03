#!/usr/bin/env python3
"""Desancoragem: distância entre o Focus e a meta por horizonte (página 12.4.5 do painel).

Mede, mês a mês, quanto a mediana do Focus para a inflação de um a quatro anos-calendário à frente
ficou acima da meta de inflação, de out/2007 a out/2026, e, com a série de 12 meses à frente, de
nov/2001 a out/2026. Lista os episódios de desancoragem e quando fecharam, e compara a expectativa
com a inflação que veio (o sentido em que o Focus errou). Grava dados/12.4.5-*.json. Só usa a
biblioteca padrão.

Uso: python3 tools/analises/12.4.5_desancoragem.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  focus-anuais_ipca.json   Focus, IPCA de cada ano-calendário; o arquivo começa em 05/10/2007
                           (corte de 40.000 linhas da consulta)
  focus-inflacao_12m.json  Focus, IPCA dos 12 meses seguintes, desde 07/11/2001
  sgs-13522.json           IPCA em 12 meses (para o erro da expectativa)

Método
  Estatística do dia: baseCalculo = 0 (série longa), mediana; série de 12 meses não suavizada
    (a convenção do painel em conteudo/_divergencias.md).
  Mês: último registro do mês. Horizonte h: no mês do ano Y, a projeção para o ano Y + h.
  Meta: a meta de cada ano conhecida na data da projeção. Ano cuja meta ainda não tinha sido
    fixada recebe a última meta fixada (hipótese usual do próprio BC nas projeções). Datas das
    resoluções do CMN: fim de junho de cada ano (as exatas que o painel conhece estão abaixo).
    Na série de 12 meses, a meta é a média das metas dos 12 meses cobertos, ponderada por mês.
  Distância = mediana - meta, em pontos percentuais. Desancorada, para o painel: distância de
    0,5 ponto ou mais (um terço do intervalo de tolerância de 1,5 ponto); o BC não fixa limiar.
  Episódio: sequência de meses com distância de 0,5 ou mais no horizonte de dois anos; fecha no
    primeiro mês em que a distância cai abaixo de 0,25.
"""
import json
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
FONTE = "BCB, Sistema de Expectativas de Mercado (Focus), API Olinda; CMN, metas para a inflação"

# (data em que o CMN fixou, ano de referência, meta)
METAS_FIXADAS = [
    (date(2001, 6, 28), 2003, 3.25),
    (date(2002, 6, 27), 2003, 4.0),   # revisão da meta de 2003
    (date(2002, 6, 27), 2004, 3.75),
    (date(2003, 6, 25), 2004, 5.5),   # revisão da meta de 2004
    (date(2003, 6, 25), 2005, 4.5),
    (date(2004, 6, 30), 2006, 4.5),
    (date(2005, 6, 30), 2007, 4.5),
    (date(2006, 6, 30), 2008, 4.5),
    (date(2007, 6, 30), 2009, 4.5),
    (date(2008, 6, 30), 2010, 4.5),
    (date(2009, 6, 30), 2011, 4.5),
    (date(2010, 6, 30), 2012, 4.5),
    (date(2011, 6, 30), 2013, 4.5),
    (date(2012, 6, 30), 2014, 4.5),
    (date(2013, 6, 30), 2015, 4.5),
    (date(2014, 6, 30), 2016, 4.5),
    (date(2015, 6, 30), 2017, 4.5),
    (date(2016, 6, 30), 2018, 4.5),
    (date(2017, 6, 29), 2019, 4.25),
    (date(2017, 6, 29), 2020, 4.0),
    (date(2018, 6, 26), 2021, 3.75),
    (date(2019, 6, 27), 2022, 3.5),
    (date(2020, 6, 25), 2023, 3.25),
    (date(2021, 6, 24), 2024, 3.0),
    (date(2022, 6, 23), 2025, 3.0),
    (date(2023, 6, 29), 2026, 3.0),
    (date(2024, 6, 26), 2027, 3.0),   # meta contínua (Decreto 12.079)
]
META_FINAL = {a: v for _, a, v in sorted(METAS_FIXADAS)}
META_FINAL.update({2001: 4.0, 2002: 3.5})


def meta_na_data(ano, d):
    """Meta do ano conhecida em d; se ainda não fixada, a última fixada até d."""
    conhecidas = [(dd, a, v) for dd, a, v in METAS_FIXADAS if dd <= d]
    if d >= date(2024, 6, 26):
        return 3.0
    for dd, a, v in sorted(conhecidas, reverse=True):
        if a == ano:
            return v
    if not conhecidas:
        return META_FINAL.get(ano, 4.0)
    ult = max(conhecidas, key=lambda x: (x[1], x[0]))
    if ano <= ult[1]:
        return META_FINAL.get(ano, ult[2])
    return ult[2]


def carregar(nome):
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        return json.load(f)["dados"]


def sgs(nome):
    out = {}
    for r in carregar(nome):
        dd, m, a = r["data"].split("/")
        out[date(int(a), int(m), int(dd))] = float(r["valor"])
    return out


def mensal_anuais():
    """{(ano, mes): {ano_ref: (data, mediana)}} com o último registro do mês."""
    tmp = defaultdict(dict)
    for r in carregar("focus-anuais_ipca.json"):
        if r["baseCalculo"] != 0 or r["Mediana"] is None:
            continue
        d = date.fromisoformat(r["Data"])
        ref = int(r["DataReferencia"])
        k = (d.year, d.month)
        if ref not in tmp[k] or tmp[k][ref][0] < d:
            tmp[k][ref] = (d, r["Mediana"])
    return tmp


def mensal_12m():
    tmp = {}
    for r in carregar("focus-inflacao_12m.json"):
        if r["baseCalculo"] != 0 or r["Suavizada"] != "N" or r["Mediana"] is None:
            continue
        d = date.fromisoformat(r["Data"])
        k = (d.year, d.month)
        if k not in tmp or tmp[k][0] < d:
            tmp[k] = (d, r["Mediana"])
    return tmp


def meta_12m(d):
    """Meta média dos 12 meses seguintes ao mês de d, conhecida em d."""
    vals = []
    a, m = d.year, d.month
    for _ in range(12):
        m += 1
        if m > 12:
            a, m = a + 1, 1
        vals.append(meta_na_data(a, d))
    return sum(vals) / 12


AN = mensal_anuais()
M12 = mensal_12m()
IPCA12 = sgs("sgs-13522.json")


def distancias():
    """{h: [(ano, mes, mediana, meta, dist)]} para h = 0..4."""
    out = defaultdict(list)
    for (a, m) in sorted(AN):
        for h in range(0, 5):
            v = AN[(a, m)].get(a + h)
            if not v:
                continue
            d, med = v
            mt = meta_na_data(a + h, d)
            out[h].append((a, m, med, mt, round(med - mt, 4), META_FINAL.get(a + h, 3.0)))
    return out


def episodios(serie, entra=0.5, sai=0.25):
    eps, cur = [], None
    for a, m, med, mt, dist, _ in serie:
        if cur is None and dist >= entra:
            cur = dict(ini=(a, m), pico=(dist, a, m, med, mt), fim=None)
        elif cur is not None:
            if dist > cur["pico"][0]:
                cur["pico"] = (dist, a, m, med, mt)
            if dist < sai:
                cur["fim"] = (a, m)
                eps.append(cur)
                cur = None
    if cur is not None:
        eps.append(cur)
    return eps


def media_anual(serie):
    acc = defaultdict(list)
    for a, m, med, mt, dist, _ in serie:
        acc[a].append(dist)
    return {a: (round(st.mean(v), 2), max(v), min(v), len(v)) for a, v in acc.items()}


def serie_12m():
    out = []
    for (a, m) in sorted(M12):
        d, med = M12[(a, m)]
        mt = meta_12m(d)
        # IPCA realizado nos 12 meses seguintes: 12 meses terminados 12 meses depois
        a2, m2 = (a + 1, m)
        real = IPCA12.get(date(a2, m2, 1))
        out.append((a, m, med, round(mt, 3), round(med - mt, 3), real))
    return out


def gravar(nome, obj):
    with open(os.path.join(DADOS, nome), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    resumo = "--resumo" in sys.argv
    D = distancias()
    nomes = {1: "Ano seguinte", 2: "Dois anos à frente", 3: "Três anos à frente", 4: "Quatro anos à frente"}

    print("== Média anual da distância (mediana - meta), por horizonte, p.p. ==")
    print("ano   " + "  ".join(f"h={h}(méd/máx)" for h in range(1, 5)))
    MA = {h: media_anual(D[h]) for h in range(0, 5)}
    for a in range(2008, 2027):
        cols = []
        for h in range(1, 5):
            x = MA[h].get(a)
            cols.append(f"{x[0]:+.2f}/{x[1]:+.2f}" if x else "   -   ")
        print(a, "  ".join(cols))

    print("\n== Meses com distância >= 0,5 por horizonte, por ano ==")
    for a in range(2008, 2027):
        cont = []
        for h in range(1, 5):
            n = sum(1 for r in D[h] if r[0] == a and r[4] >= 0.5)
            t = sum(1 for r in D[h] if r[0] == a)
            cont.append(f"{n}/{t}")
        print(a, cont)

    print("\n== Episódios (h=2, entra >= 0,5, fecha < 0,25) ==")
    for h in (1, 2, 3, 4):
        print(f"-- h={h}")
        for e in episodios(D[h]):
            p = e["pico"]
            print(f"  início {e['ini'][1]:02d}/{e['ini'][0]}  pico {p[0]:+.2f} em {p[2]:02d}/{p[1]} "
                  f"(mediana {p[3]:.2f}, meta {p[4]:.2f})  fim {e['fim'][1]:02d}/{e['fim'][0] if e['fim'] else ''}"
                  if e["fim"] else
                  f"  início {e['ini'][1]:02d}/{e['ini'][0]}  pico {p[0]:+.2f} em {p[2]:02d}/{p[1]} "
                  f"(mediana {p[3]:.2f}, meta {p[4]:.2f})  em aberto")

    print("\n== Mínimo e máximo por horizonte ==")
    for h in range(1, 5):
        mx = max(D[h], key=lambda r: r[4])
        mn = min(D[h], key=lambda r: r[4])
        print(f"h={h}: máx {mx[4]:+.2f} em {mx[1]:02d}/{mx[0]} (mediana {mx[2]}, meta {mx[3]}); "
              f"mín {mn[4]:+.2f} em {mn[1]:02d}/{mn[0]} (mediana {mn[2]}, meta {mn[3]})")

    print("\n== Fração de meses com distância > 0 e >= 0,5, por horizonte (out/2007 a out/2026) ==")
    for h in range(1, 5):
        n = len(D[h])
        print(f"h={h}: n={n}, >0: {sum(r[4] > 0.001 for r in D[h])}, =0: {sum(abs(r[4]) <= 0.001 for r in D[h])}, "
              f"<0: {sum(r[4] < -0.001 for r in D[h])}, >=0,5: {sum(r[4] >= 0.5 for r in D[h])}")

    print("\n== Sensibilidade: meta final do ano em vez da meta conhecida na data (h=3,4, 2015-2021) ==")
    for h in (3, 4):
        for a in range(2015, 2022):
            rs = [r for r in D[h] if r[0] == a]
            if rs:
                print(h, a, round(st.mean(r[4] for r in rs), 2), round(st.mean(r[2] - r[5] for r in rs), 2))

    print("\n== Série de 12 meses à frente (não suavizada): média anual da distância ==")
    S12 = serie_12m()
    acc = defaultdict(list)
    for a, m, med, mt, dist, real in S12:
        acc[a].append((dist, med, mt, real))
    for a in sorted(acc):
        v = acc[a]
        reais = [x[3] - x[1] for x in v if x[3] is not None]
        print(a, f"dist {st.mean(x[0] for x in v):+.2f}  máx {max(x[0] for x in v):+.2f}  "
              f"meta {st.mean(x[2] for x in v):.2f}  erro(real-med) {st.mean(reais) if reais else float('nan'):+.2f} ({len(reais)})")

    print("\n== Valores pontuais ==")
    for (a, m) in [(2010, 12), (2013, 12), (2014, 12), (2015, 9), (2015, 12), (2016, 12), (2017, 12),
                   (2019, 12), (2020, 12), (2021, 10), (2021, 12), (2022, 6), (2022, 12), (2023, 6),
                   (2023, 12), (2024, 6), (2024, 12), (2025, 1), (2025, 6), (2025, 12), (2026, 3),
                   (2026, 6), (2026, 9), (2026, 10)]:
        row = AN.get((a, m), {})
        print(f"{m:02d}/{a}", {r: v[1] for r, v in sorted(row.items()) if r >= a},
              {r: meta_na_data(r, v[0]) for r, v in sorted(row.items()) if r >= a})

    print("\n== Projeção média feita h anos antes contra o IPCA do ano (realizado - projeção) ==")
    for h in (1, 2, 3, 4):
        erros = []
        for Y in range(2010, 2026):
            v = [r[2] for r in D[h] if r[0] == Y - h]
            if not v:
                continue
            real = IPCA12[date(Y, 12, 1)]
            erros.append((Y, round(st.mean(v), 2), real, round(real - st.mean(v), 2)))
        pos = sum(1 for e in erros if e[3] > 0)
        print(f"h={h}: {pos} de {len(erros)} anos com realizado acima; erro médio "
              f"{st.mean(e[3] for e in erros):+.2f}")
        print("   ", erros)

    # Gráfico: distância mensal, h = 1, 2 e 4
    series = []
    for h in (1, 2, 4):
        pts = [{"t": f"{a}-{m:02d}", "v": round(dist, 2)} for a, m, med, mt, dist, _ in D[h]]
        series.append({"nome": nomes[h], "pontos": pts})
    gravar("12.4.5-distancia-meta.json", {
        "titulo": "Mediana do Focus para o IPCA menos a meta, por horizonte (pontos percentuais)",
        "tipo": "linha",
        "unidade": "p.p.",
        "fonte": FONTE + "; cálculo do painel",
        "url": URL,
        "consulta": CONSULTA,
        "nota": ("Último registro de cada mês, base de cálculo 0. Horizonte: no mês do ano Y, a projeção "
                 "para o ano-calendário Y+1, Y+2 ou Y+4. Meta: a de cada ano conhecida na data; ano sem "
                 "meta fixada recebe a última meta fixada. O arquivo de projeções anuais começa em "
                 "out/2007. Linha em 0,5: limiar do painel para chamar a expectativa de desancorada. "
                 "Script: tools/analises/12.4.5_desancoragem.py."),
        "governos": True,
        "ref": [{"v": 0, "rotulo": "na meta"}, {"v": 0.5, "rotulo": "0,5 acima"}],
        "series": series,
    })
    if resumo:
        return


if __name__ == "__main__":
    main()

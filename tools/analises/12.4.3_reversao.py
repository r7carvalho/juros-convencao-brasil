#!/usr/bin/env python3
"""O mercado está nervoso: o que acontece depois dos maiores saltos (página 12.4.3 do painel).

Mede três coisas com os brutos de dados/brutos/ (coleta de 02/11/2026):
  1. Os 12 maiores saltos de 20 dias úteis do risco-país (EMBI+ Brasil, JP Morgan, via Ipeadata,
     série diária até 30/07/2024) e da PTAX (SGS 1), desde 01/03/1999, e quanto de cada salto foi
     desfeito 20, 60 e 250 dias úteis depois.
  2. O EMBI+ e a PTAX em datas de evento (2002, 2015, 2020, abr/2024, jun-jul/2024) e a PTAX em
     nov/2024 e out/2026.
  3. O CDI efetivo de 29/11/2024 a 31/12/2026 (SGS 12), para comparar com a taxa do DI de janeiro
     de 2027 no dia seguinte ao pacote fiscal (cerca de 13,9%, Giro S.A., 28/11/2024). Os dias úteis
     de 03/11 a 31/12/2026 usam o CDI de 30/10/2026 (Selic de 13,75% mantida), hipótese do painel.
Grava dados/12.4.3-saltos-embi.json. Só usa a biblioteca padrão.

Uso: python3 tools/analises/12.4.3_reversao.py

Método dos saltos
  Salto: variação em 20 dias úteis (EMBI+ em pontos-base; PTAX em log). Os 12 maiores, com fins de
    janela separados por pelo menos 60 dias úteis, para não contar o mesmo episódio duas vezes.
  Reversão em h dias: -(variação de h dias depois do fim do salto) / salto. 100% quer dizer que o
    indicador voltou ao nível de antes do salto; acima de 100%, ficou abaixo dele; negativo, subiu mais.
  Viés de seleção: o fim de cada janela é escolhido onde o salto é máximo, perto de um pico local,
    de modo que parte da reversão seguinte é mecânica. O número serve para descrever, e não para
    testar se o mercado exagera.
"""
import json
import math
import os
import statistics as st
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
DADOS = os.path.join(ROOT, "dados")
CONSULTA = "2026-11-02"
INICIO = date(1999, 3, 1)


def sgs(codigo):
    with open(os.path.join(BRUTOS, f"sgs-{codigo}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = []
    for r in dados:
        d, m, a = r["data"].split("/")
        out.append((date(int(a), int(m), int(d)), float(r["valor"])))
    return out


def embi():
    with open(os.path.join(BRUTOS, "ipea-JPM366_EMBI366.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    return [(date.fromisoformat(r["VALDATA"][:10]), float(r["VALVALOR"]))
            for r in dados if r["VALVALOR"] is not None]


def ate(serie, dia):
    v = None
    for x in serie:
        if x[0] <= dia:
            v = x
        else:
            break
    return v


def saltos(serie, log, janela=20, n=12, sep=60):
    s = [x for x in serie if x[0] >= INICIO]
    v = [x[1] for x in s]
    var = []
    for i in range(janela, len(s)):
        c = math.log(v[i] / v[i - janela]) if log else v[i] - v[i - janela]
        var.append((c, i))
    var.sort(reverse=True)
    escolhidos = []
    for c, i in var:
        if any(abs(i - j) < sep for _, j in escolhidos):
            continue
        escolhidos.append((c, i))
        if len(escolhidos) == n:
            break
    linhas = []
    for c, i in sorted(escolhidos, key=lambda e: e[1]):
        lin = {"inicio": s[i - janela][0], "fim": s[i][0], "antes": v[i - janela], "pico": v[i], "salto": c}
        for h in (20, 60, 250):
            if i + h < len(s):
                depois = math.log(v[i + h] / v[i]) if log else v[i + h] - v[i]
                lin[h] = depois
                lin[f"rev{h}"] = -depois / c
                lin[f"nivel{h}"] = v[i + h]
        linhas.append(lin)
    return linhas


def resumo(nome, linhas, log):
    print(f"\n{nome}: 12 maiores saltos de 20 dias úteis desde 01/03/1999")
    for x in linhas:
        salto = f"{100 * (math.exp(x['salto']) - 1):+.1f}%" if log else f"{x['salto']:+.0f} pb"
        revs = "  ".join(f"rev{h} {100 * x[f'rev{h}']:5.0f}%" if f"rev{h}" in x else f"rev{h}   n/d" for h in (20, 60, 250))
        print(f"  {x['inicio']} a {x['fim']}: {x['antes']} -> {x['pico']} ({salto})  {revs}  nível em 250 d: {x.get('nivel250')}")
    for h in (20, 60, 250):
        r = [x[f"rev{h}"] for x in linhas if f"rev{h}" in x]
        print(f"  h={h}: n={len(r)}, mediana {100 * st.median(r):.0f}%, desfeito por inteiro (>=100%) {sum(1 for y in r if y >= 1)}, "
              f"mais da metade {sum(1 for y in r if y > 0.5)}, subiu mais {sum(1 for y in r if y < 0)}")


def cdi_realizado():
    cdi = sgs(12)
    ini, fim = date(2024, 11, 29), date(2027, 1, 1)
    fator, n = 1.0, 0
    for d, v in cdi:
        if ini <= d < fim:
            fator *= 1 + v / 100
            n += 1
    ultimo_dia, ultima_taxa = cdi[-1]
    feriados = {date(2026, 11, 2), date(2026, 11, 20), date(2026, 12, 25)}
    d, extra = ultimo_dia + timedelta(days=1), 0
    while d < fim:
        if d.weekday() < 5 and d not in feriados:
            extra += 1
        d += timedelta(days=1)
    fator_total = fator * (1 + ultima_taxa / 100) ** extra
    print(f"\nCDI de 29/11/2024 a {ultimo_dia}: {n} dias, {100 * (fator ** (252 / n) - 1):.2f}% a.a.")
    print(f"Com {extra} dias úteis a {100 * ((1 + ultima_taxa / 100) ** 252 - 1):.2f}% até 31/12/2026: "
          f"{100 * (fator_total ** (252 / (n + extra)) - 1):.2f}% a.a.")


def main():
    em, pt = embi(), sgs(1)
    print("EMBI+ vai de", em[0][0], "a", em[-1][0])
    for d in ["2002-09-27", "2003-12-31", "2015-01-02", "2015-09-24", "2015-12-31", "2016-12-30",
              "2020-02-28", "2020-03-23", "2020-12-31", "2022-12-30", "2023-12-29",
              "2024-04-01", "2024-04-16", "2024-04-30", "2024-06-14", "2024-07-02", "2024-07-30"]:
        dia = date.fromisoformat(d)
        print(d, "EMBI+", ate(em, dia)[1], "PTAX", ate(pt, dia)[1])
    for d in ["2024-11-26", "2024-11-29", "2024-12-18", "2024-12-31", "2025-12-31",
              "2026-10-23", "2026-10-26", "2026-10-28", "2026-10-30"]:
        print(d, "PTAX", ate(pt, date.fromisoformat(d))[1])

    le = saltos(em, log=False)
    lp = saltos(pt, log=True)
    resumo("EMBI+ Brasil (pontos-base)", le, False)
    resumo("PTAX (R$/US$)", lp, True)
    cdi_realizado()

    pontos_salto, pontos_ano = [], []
    for x in le:
        rot = f"{x['fim'].strftime('%m/%Y')}"
        pontos_salto.append({"t": rot, "v": round(x["salto"])})
        pontos_ano.append({"t": rot, "v": round(x[250])})
    grafico = {
        "titulo": "Os 12 maiores saltos do risco-país em 20 dias úteis e a variação no ano seguinte (pontos-base)",
        "tipo": "barras",
        "unidade": "pontos-base",
        "fonte": "JP Morgan, EMBI+ Brasil, série diária via Ipeadata (JPM366_EMBI366); cálculo do painel",
        "url": "http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=40940&module=M",
        "consulta": CONSULTA,
        "nota": ("Saltos de 20 dias úteis desde 01/03/1999, separados por pelo menos 60 dias úteis; o rótulo é o mês "
                 "em que o salto terminou. A segunda barra é a variação nos 250 dias úteis seguintes: abaixo de menos "
                 "o salto, o risco-país ficou abaixo do nível de antes do salto. A série do Ipeadata termina em "
                 "30/07/2024. Script: tools/analises/12.4.3_reversao.py."),
        "series": [
            {"nome": "Salto em 20 dias úteis", "pontos": pontos_salto},
            {"nome": "Variação nos 250 dias úteis seguintes", "pontos": pontos_ano},
        ],
    }
    with open(os.path.join(DADOS, "12.4.3-saltos-embi.json"), "w", encoding="utf-8") as f:
        json.dump(grafico, f, ensure_ascii=False, indent=1)
    print("\ngravado dados/12.4.3-saltos-embi.json")


if __name__ == "__main__":
    main()

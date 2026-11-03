#!/usr/bin/env python3
"""Dominância fiscal como explicação de tudo (página 12.4.4 do painel).

Mede, com os brutos de dados/brutos/ (coleta de 02/11/2026):
  1. Todos os ciclos de alta da meta da Selic desde março de 1999 (SGS 432): para cada um, a PTAX
     (SGS 1) e o EMBI+ Brasil (JP Morgan, via Ipeadata, diário até 30/07/2024) da véspera da primeira
     alta ao dia da última e até 250 dias úteis depois, e o IPCA em 12 meses (SGS 13522) no mês da
     primeira alta, no da última e 12 meses depois. É o teste de sinal de Blanchard (2004) em forma
     descritiva: no lado perverso, a moeda se deprecia e o risco sobe enquanto o juro sobe.
  2. Os episódios em que a expressão "dominância fiscal" circulou com força (fim de 2015, fim de
     2024 e janeiro de 2025): Selic, PTAX, EMBI+, IPCA e dívida bruta (SGS 13762) antes e depois.
Imprime as tabelas. Só usa a biblioteca padrão.

Uso: python3 tools/analises/12.4.4_dominancia.py

Limite declarado: o Banco Central sobe o juro justamente quando o câmbio e a inflação pressionam, de
modo que a comparação inclina o resultado para o sinal perverso. Ela não identifica causa; serve para
dizer se o padrão de 2002 se repetiu nos outros ciclos.
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")


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


def depois(serie, dia, n):
    """Valor n observações depois da última observação até `dia` (None se a série acaba antes)."""
    idx = None
    for i, x in enumerate(serie):
        if x[0] <= dia:
            idx = i
        else:
            break
    if idx is None or idx + n >= len(serie):
        return None
    return serie[idx + n]


def mes(serie, a, m):
    for x in serie:
        if x[0].year == a and x[0].month == m:
            return x[1]
    return None


def mais_meses(a, m, k):
    t = a * 12 + (m - 1) + k
    return t // 12, t % 12 + 1


SELIC = sgs(432)
PTAX = sgs(1)
IPCA = sgs(13522)
DBGG = sgs(13762)
EMBI = embi()
PAUSA = 120  # dias corridos sem alta que encerram um ciclo, mesmo sem corte (2010-11, 2013-15)


def ciclos_de_alta():
    """Mudanças da meta (valor diferente do anterior) e agrupamento em ciclos de alta."""
    mudancas = []
    ant = None
    for d, v in SELIC:
        if d < date(1999, 3, 5):
            continue
        if ant is not None and v != ant:
            mudancas.append((d, ant, v))
        ant = v
    ciclos = []
    atual = None
    for d, a, b in mudancas:
        if b > a:
            if atual is not None and (d - atual["fim"]).days > PAUSA:
                ciclos.append(atual)
                atual = None
            if atual is None:
                atual = {"ini": d, "de": a, "fim": d, "para": b}
            else:
                atual["fim"], atual["para"] = d, b
        else:
            if atual is not None:
                ciclos.append(atual)
                atual = None
    if atual is not None:
        ciclos.append(atual)
    return ciclos


def fmt(x, nd=2):
    return "-" if x is None else f"{x:.{nd}f}"


def tabela_ciclos():
    print("Ciclos de alta da Selic meta desde mar/1999 (SGS 432)")
    print("ini | fim | Selic | PTAX véspera -> fim (var%) | PTAX +250du (var% desde véspera) |"
          " EMBI véspera -> fim | EMBI +250du | IPCA12m ini / fim / fim+12m")
    print(f"(ciclo: altas seguidas, sem corte e sem pausa de mais de {PAUSA} dias entre elas)")
    from datetime import timedelta
    for c in ciclos_de_alta():
        vesp = c["ini"] - timedelta(days=1)
        p0 = ate(PTAX, vesp)
        p1 = ate(PTAX, c["fim"])
        p2 = depois(PTAX, c["fim"], 250)
        e0 = ate(EMBI, vesp)
        e1 = ate(EMBI, c["fim"]) if c["fim"] <= EMBI[-1][0] else None
        e2 = depois(EMBI, c["fim"], 250)
        i0 = mes(IPCA, c["ini"].year, c["ini"].month)
        i1 = mes(IPCA, c["fim"].year, c["fim"].month)
        a12, m12 = mais_meses(c["fim"].year, c["fim"].month, 12)
        i2 = mes(IPCA, a12, m12)
        vp1 = (p1[1] / p0[1] - 1) * 100
        pm = max((x for x in PTAX if c["ini"] <= x[0] <= c["fim"]), key=lambda x: x[1])
        vpm = (pm[1] / p0[1] - 1) * 100
        vp2 = None if p2 is None else (p2[1] / p0[1] - 1) * 100
        print(f"{c['ini']} | {c['fim']} | {c['de']:.2f}->{c['para']:.2f} | "
              f"{p0[1]:.4f} -> {p1[1]:.4f} ({vp1:+.1f}; máx {pm[1]:.4f} em {pm[0]}, {vpm:+.1f}) | "
              f"{fmt(None if p2 is None else p2[1], 4)} ({fmt(vp2, 1)}) | "
              f"{fmt(None if e0 is None else e0[1], 0)} -> {fmt(None if e1 is None else e1[1], 0)} | "
              f"{fmt(None if e2 is None else e2[1], 0)} | {fmt(i0)} / {fmt(i1)} / {fmt(i2)}")


def pontos():
    print("\nEpisódio 2015-2017")
    for d in [date(2015, 7, 29), date(2015, 9, 24), date(2015, 12, 31), date(2016, 1, 21),
              date(2016, 12, 30), date(2017, 12, 29)]:
        print(d, "PTAX", ate(PTAX, d), "EMBI", ate(EMBI, d), "Selic", ate(SELIC, d))
    pmax = max((x for x in PTAX if date(2015, 1, 1) <= x[0] <= date(2016, 12, 31)), key=lambda x: x[1])
    emax = max((x for x in EMBI if date(2015, 1, 1) <= x[0] <= date(2016, 12, 31)), key=lambda x: x[1])
    print("PTAX máx 2015-16", pmax, "EMBI máx 2015-16", emax)
    for a, m in [(2015, 7), (2015, 12), (2016, 1), (2016, 10), (2016, 12), (2017, 12)]:
        print(f"IPCA12m {m:02d}/{a}", mes(IPCA, a, m))
    for a in [2014, 2015, 2016, 2017]:
        print(f"DBGG dez/{a}", mes(DBGG, a, 12))

    print("\nEpisódio 2024-2026")
    for d in [date(2024, 9, 18), date(2024, 11, 13), date(2024, 12, 18), date(2024, 12, 31),
              date(2025, 1, 20), date(2025, 6, 18), date(2025, 12, 31), date(2026, 3, 18),
              date(2026, 9, 30), date(2026, 10, 23)]:
        print(d, "PTAX", ate(PTAX, d), "Selic", ate(SELIC, d))
    for a, m in [(2024, 9), (2024, 12), (2025, 1), (2025, 4), (2025, 10), (2025, 12), (2026, 9)]:
        print(f"IPCA12m {m:02d}/{a}", mes(IPCA, a, m))
    for a, m in [(2024, 12), (2025, 12), (2026, 9)]:
        print(f"DBGG {m:02d}/{a}", mes(DBGG, a, m))


if __name__ == "__main__":
    tabela_ciclos()
    pontos()

#!/usr/bin/env python3
"""Contas da página 13.4 (coerência interna e base legal da proposta de Lara Resende).

Uso: python3 -I tools/analises/13.4_coerencia.py [--json]
Lê dados/brutos (SGS 432, 13522, 3546, 1) e imprime os números que a página usa.
Com --json, grava dados/13.4-selic-ipca-faixa.json (gráfico da página).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PISO, TETO, TETO_META, META = 3.0, 5.5, 4.5, 3.0


def sgs(cod):
    d = json.load(open(os.path.join(ROOT, "dados", "brutos", f"sgs-{cod}.json"), encoding="utf-8"))
    return d["dados"]


def mensal_ultimo(cod):
    """Último valor de cada mês (AAAA-MM -> valor)."""
    out = {}
    for x in sgs(cod):
        dd, mm, aa = x["data"].split("/")
        out[f"{aa}-{mm}"] = float(x["valor"])
    return out


selic = mensal_ultimo("432")
ipca = mensal_ultimo("13522")

# 1. Regra de Taylor com o neutro da própria proposta (2,5%) e coeficiente 0,5 no desvio da inflação
#    i = r* + pi + 0,5 (pi - meta). Inflação a partir da qual o juro de Taylor passa do teto da faixa:
for rstar in (2.5, 5.0):
    pi_teto = (TETO - rstar + 0.5 * META) / 1.5
    pi_piso = (PISO - rstar + 0.5 * META) / 1.5
    print(f"r* = {rstar}: Taylor passa do teto (5,5%) com inflação acima de {pi_teto:.2f}%; "
          f"fica abaixo do piso (3%) com inflação abaixo de {pi_piso:.2f}%")
for pi in (3.0, 4.0, 4.5, 4.58, 6.0):
    print(f"  inflação {pi:.2f}%: Taylor com r*=2,5 -> {2.5 + pi + 0.5 * (pi - META):.2f}%; "
          f"com r*=5 -> {5 + pi + 0.5 * (pi - META):.2f}%; juro real no teto = {(1 + TETO / 100) / (1 + pi / 100) * 100 - 100:.2f}%")

# 2. Quantas vezes, desde a meta contínua de 3% (2025) e no período 2005-2026, o IPCA de 12 meses
#    ficou acima de 3% e acima de 4,5%; e quantos meses a Selic meta ficou dentro da faixa
def conta(ini, fim):
    meses = sorted(m for m in ipca if ini <= m <= fim)
    acima_meta = sum(1 for m in meses if ipca[m] > META)
    acima_teto = sum(1 for m in meses if ipca[m] > TETO_META)
    dentro = sum(1 for m in meses if m in selic and PISO <= selic[m] <= TETO)
    print(f"{ini} a {fim}: {len(meses)} meses; IPCA 12m > 3%: {acima_meta} ({acima_meta / len(meses):.0%}); "
          f"> 4,5%: {acima_teto} ({acima_teto / len(meses):.0%}); Selic meta na faixa 3%-5,5%: {dentro}")
    return meses


conta("2005-01", "2026-09")
conta("2017-01", "2026-09")
conta("2025-01", "2026-09")
faixa = [m for m in sorted(selic) if "1999-07" <= m <= "2026-10" and PISO <= selic[m] <= TETO]
print("Meses com Selic meta (fim do mês) dentro da faixa desde jul/1999:", len(faixa), faixa[0], "...", faixa[-1])
print("  ", ", ".join(faixa))

# 3. Reservas e detentores não residentes da DPMFi (RMD de ago/2026: R$ 8,9 tri; 9,91%), em dólares
reservas = float(sgs("3546")[-1]["valor"]) / 1000
ptax = float([x for x in sgs("1") if x["data"] == "30/10/2026"][0]["valor"])
nres = 8900 * 0.0991 / ptax
print(f"Reservas {reservas:.1f} bi (SGS 3546, {sgs('3546')[-1]['data']}); PTAX 30/10/2026 {ptax:.4f}; "
      f"não residentes na DPMFi ~ US$ {nres:.0f} bi = {nres / reservas:.0%} das reservas")

# 4. Diferencial de juros contra os EUA (fed funds, ponto médio de 3,875% em set/2026, BIS, como na 13.3)
ff = 3.875
for s in (13.75, 7.5, 5.5):
    print(f"Selic {s}%: diferencial {s - ff:.2f} p.p.; depreciação que zera o carry em um ano "
          f"{((1 + s / 100) / (1 + ff / 100) - 1) * 100:.2f}%")

# 5. Repasse ilustrativo de 10% (2.4) aplicado ao dólar +20% do caso (c) da 13.3
print("Dólar +20% com repasse de 10%: +2,0 p.p. de IPCA em um ano; com 5%: +1,0; com 15%: +3,0")

if "--json" in sys.argv:
    meses = [m for m in sorted(set(selic) | set(ipca)) if "2010-01" <= m <= "2026-10"]
    dados = {
        "titulo": "Selic meta e IPCA de 12 meses contra a faixa proposta (% a.a.)",
        "tipo": "linha",
        "unidade": "% a.a.",
        "fonte": "BCB, SGS 432 (Selic meta, último valor do mês) e SGS 13522 (IPCA 12 meses); faixa de Lara Resende, \"Eu acuso\", 25/09/2026",
        "url": "https://www3.bcb.gov.br/sgspub/",
        "consulta": "2026-11-02",
        "nota": "Linhas de referência: piso da faixa (3%, igual à meta contínua), teto da meta (4,5%) e teto da faixa (5,5%). Selic até out/2026; IPCA até set/2026. Cálculo do painel em tools/analises/13.4_coerencia.py.",
        "governos": True,
        "ref": [
            {"v": 3.0, "rotulo": "piso da faixa e meta"},
            {"v": 4.5, "rotulo": "teto da meta"},
            {"v": 5.5, "rotulo": "teto da faixa"},
        ],
        "series": [
            {"nome": "Selic meta", "pontos": [{"t": m, "v": selic.get(m)} for m in meses]},
            {"nome": "IPCA 12 meses", "pontos": [{"t": m, "v": ipca.get(m)} for m in meses]},
        ],
    }
    caminho = os.path.join(ROOT, "dados", "13.4-selic-ipca-faixa.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=1)
    print("gravado", caminho)

# 6. Prêmio aproximado do DI jan/29 (perto de 15% em 26/10/2026, 12.4.3) sobre a Selic média esperada pelo
#    Focus de 23/10/2026 (13,25% no fim de 2026, 11,75% no fim de 2027, 10% no fim de 2028), com trajetória
#    linear entre os fins de ano, de nov/2026 a dez/2028, capitalizada mês a mês.
pontos = {0: 13.75, 2: 13.25, 14: 11.75, 26: 10.0}  # meses a partir de out/2026
def selic_mes(k):
    ks = sorted(pontos)
    for a, b in zip(ks, ks[1:]):
        if a <= k <= b:
            return pontos[a] + (pontos[b] - pontos[a]) * (k - a) / (b - a)
    return pontos[ks[-1]]
fator = 1.0
for k in range(1, 27):
    fator *= (1 + selic_mes(k) / 100) ** (1 / 12)
media = (fator ** (12 / 26) - 1) * 100
print(f"Selic média esperada nov/2026-dez/2028 ~ {media:.2f}% a.a.; prêmio do DI jan/29 a 15% ~ {15 - media:.1f} p.p.")

#!/usr/bin/env python3
"""Contas da página 13.6 (as críticas e as respostas à proposta de Lara Resende).

Uso: python3 -I tools/analises/13.6_contas.py
Lê dados/brutos (SGS 3546, SGS 1, Focus 12 meses) e imprime os números que a página usa.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def sgs(cod):
    d = json.load(open(os.path.join(ROOT, "dados", "brutos", f"sgs-{cod}.json"), encoding="utf-8"))
    return d["dados"]


def focus_12m(data):
    d = json.load(open(os.path.join(ROOT, "dados", "brutos", "focus-inflacao_12m.json"), encoding="utf-8"))
    for r in d["dados"]:
        if r["Data"] == data and r["Suavizada"] == "N" and r.get("baseCalculo") == 0:
            return r["Mediana"]
    raise SystemExit(f"Focus de {data} não encontrado")


# 1. Brinquedo do carry trade: depreciação que zera o ganho de ficar em reais
juro_externo = 0.04
for selic in (0.1375, 0.075):
    print(f"Selic {selic:.2%}: depreciação de equilíbrio = {(1 + selic) / (1 + juro_externo) - 1:.2%}")

# 2. Reservas (SGS 3546, set/2026) contra a DPF (R$ 9,29 tri, RMD de ago/2026) em dólares (PTAX de 30/10/2026)
reservas = float(sgs("3546")[-1]["valor"]) / 1000  # US$ bilhões
ptax = float([x for x in sgs("1") if x["data"] == "30/10/2026"][0]["valor"])
dpf_usd = 9290 / ptax  # US$ bilhões
print(f"Reservas {reservas:.1f} bi; DPF {dpf_usd:.0f} bi de dólares; razão {reservas / dpf_usd:.1%}")

# 3. Juro real ex-ante com Selic de 7,5% sobre a mediana do Focus de 12 meses de 23/10/2026
pi_e = focus_12m("2026-10-23") / 100
print(f"Focus 12m 23/10/2026 = {pi_e:.2%}; juro real com Selic 7,5% = {1.075 / (1 + pi_e) - 1:.2%}")

# 4. Brinquedo do dilema real × nominal (dívida de 80% do PIB)
d = 0.80
real_antes = 1.13 / 1.05 - 1
real_depois = 1.075 / 1.03 - 1
print(f"Real antes {real_antes:.2%}, depois {real_depois:.2%}; economia nominal {d * (0.13 - 0.075):.2%} do PIB;"
      f" parte real {d * (real_antes - real_depois):.2%} do PIB")

# 5. Conferência da conta de Gabrielli: primário que estabiliza com d = 82,9%, i = 11,4%, g nominal = 7%
print(f"Primário estabilizador (Gabrielli) = {0.829 * (0.114 - 0.07) / 1.07:.2%} do PIB")

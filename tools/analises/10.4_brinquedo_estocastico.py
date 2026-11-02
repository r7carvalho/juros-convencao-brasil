#!/usr/bin/env python3
"""Brinquedo da página 10.4: a mesma dívida de 100 com r − g incerto.

Hipóteses (números inventados): dívida inicial de 100% do PIB; o diferencial x = r − g
dos próximos 20 anos é sorteado uma vez de uma normal com média mu e desvio sigma e fica
fixo; a dívida evolui por d_t = d_{t-1} * (1 + x) - s (aproximação de (1+r)/(1+g)).
A dívida está em trajetória explosiva quando x * d > s, isto é, x > s/d.
Probabilidade = 1 - Phi((s/d - mu)/sigma). Grava dois JSON em dados/.
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D0, SIGMA, ANOS = 100.0, 2.0, 20
CASOS = [("r − g médio de −1 ponto", -1.0), ("r − g médio de +3 pontos", 3.0)]


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def zq(p):  # quantil da normal padrão por bisseção
    lo, hi = -10.0, 10.0
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if phi(m) < p else (lo, m)
    return (lo + hi) / 2


def prob_explosao(mu, s):
    return 100 * (1 - phi((s / D0 * 100 - mu) / SIGMA))


def divida_final(x, s=0.0):
    d = D0
    for _ in range(ANOS):
        d = d * (1 + x / 100) - s
    return d


base = {"unidade": "", "url": "https://www.piie.com/sites/default/files/2023-01/blanchard2023-01-20ppt.pdf",
        "consulta": "2026-11-02"}

prob = dict(base)
prob.update({
    "titulo": "Dívida de 100% do PIB: probabilidade de trajetória explosiva conforme o superávit primário (%)",
    "tipo": "barras", "unidade": "%",
    "fonte": "Exemplo de brinquedo do painel, no espírito da análise estocástica de Blanchard (2023); "
             "cálculo em tools/analises/10.4_brinquedo_estocastico.py",
    "nota": "Números inventados. r − g sorteado uma vez de uma normal com desvio de 2 pontos e mantido; "
            "a dívida explode quando (r − g) × dívida supera o primário.",
    "series": []})
for nome, mu in CASOS:
    prob["series"].append({"nome": nome, "pontos": [
        {"t": f"primário {s}%", "v": round(prob_explosao(mu, s), 1)} for s in range(0, 7)]})

fan = dict(base)
fan.update({
    "titulo": "Dívida depois de 20 anos com primário zero, partindo de 100 (% do PIB)",
    "tipo": "barras", "unidade": "% do PIB",
    "fonte": "Exemplo de brinquedo do painel; cálculo em tools/analises/10.4_brinquedo_estocastico.py",
    "nota": "Números inventados. Percentis do r − g sorteado (desvio de 2 pontos), aplicado por 20 anos.",
    "ref": [{"v": 100, "rotulo": "dívida inicial"}],
    "series": []})
for nome, mu in CASOS:
    pts = []
    for rot, p in (("1 em 10 (melhor)", 0.10), ("mediana", 0.5), ("1 em 10 (pior)", 0.90)):
        x = mu + SIGMA * zq(p)
        pts.append({"t": rot, "v": round(divida_final(x), 1)})
    fan["series"].append({"nome": nome, "pontos": pts})

for nome_arq, obj in (("10.4-probabilidade-explosao.json", prob), ("10.4-divida-20-anos.json", fan)):
    with open(os.path.join(ROOT, "dados", nome_arq), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(nome_arq, json.dumps(obj["series"], ensure_ascii=False))

for nome, mu in CASOS:
    print(nome, "primário p/ prob 5%:", round(D0 * (mu + 1.6449 * SIGMA) / 100, 2))

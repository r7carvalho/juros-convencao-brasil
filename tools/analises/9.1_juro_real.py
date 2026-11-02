#!/usr/bin/env python3
"""Juro real ex-post e ex-ante no Brasil, 2000-2026 (página 9.1 do painel).

Refaz dados/9.1-juro-real-ex-ante-ex-post.json a partir do acervo bruto. Só usa a biblioteca padrão.

Uso: python3 tools/analises/9.1_juro_real.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  sgs-4390.json            Selic acumulada no mês (% a.m.), mensal
  sgs-13522.json           IPCA acumulado em 12 meses (%), mensal
  sgs-1178.json            Selic over diária, anualizada (% a.a.), diária
  focus-inflacao_12m.json  Focus, IPCA 12 meses à frente (mediana), diária, API Olinda

Método (convenção única do painel, conteudo/_divergencias.md, 02/11/2026)
  Equação de Fisher: r = (1 + i) / (1 + pi) - 1.
  Ex-post, posição de dezembro: i = Selic acumulada nos 12 meses até dezembro (produto de
      1 + SGS 4390 / 100 nos 12 meses); pi = IPCA de 12 meses até dezembro (SGS 13522).
      Último ponto: 12 meses até setembro de 2026.
  Ex-ante, posição de dezembro: i = Selic over anualizada (SGS 1178) do último dia útil do mês;
      pi = mediana Focus do IPCA 12 meses à frente, série não suavizada (Suavizada = "N"),
      baseCalculo = 0, último registro do mês até aquele dia. Últimos pontos: 30/09/2026 e
      23/10/2026 (último Focus do acervo).
  Comparações (só impressas com --resumo): mediana suavizada e Selic meta (SGS 432) no lugar
      da over.
"""
import json
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
SAIDA = os.path.join(ROOT, "dados", "9.1-juro-real-ex-ante-ex-post.json")
CONSULTA = "2026-11-02"


def carregar(nome):
    with open(os.path.join(BRUTOS, nome), encoding="utf-8") as f:
        return json.load(f)["dados"]


def sgs(nome):
    out = {}
    for r in carregar(nome):
        d, m, a = r["data"].split("/")
        out[date(int(a), int(m), int(d))] = float(r["valor"])
    return out


def focus(suavizada="N", base=0):
    out = {}
    for r in carregar("focus-inflacao_12m.json"):
        if r["Indicador"] == "IPCA" and r["Suavizada"] == suavizada and r["baseCalculo"] == base:
            out[date.fromisoformat(r["Data"])] = float(r["Mediana"])
    return out


def fisher(i, pi):
    return ((1 + i / 100) / (1 + pi / 100) - 1) * 100


def ultimo_ate(serie, dia):
    """Último registro da série no mesmo mês de `dia`, com data <= dia."""
    cands = [d for d in serie if d <= dia and (d.year, d.month) == (dia.year, dia.month)]
    return max(cands) if cands else None


def ex_post(selic_mes, ipca12, ano, mes):
    fator = 1.0
    for k in range(12):
        a, m = ano, mes - k
        while m <= 0:
            m += 12
            a -= 1
        fator *= 1 + selic_mes[date(a, m, 1)] / 100
    return fisher((fator - 1) * 100, ipca12[date(ano, mes, 1)])


def ex_ante(over, foc, ano, mes, dia=None):
    if dia is None:
        dias = [d for d in over if (d.year, d.month) == (ano, mes)]
        dia = max(dias)
    df = ultimo_ate(foc, dia)
    return fisher(over[dia], foc[df]), dia, df, over[dia], foc[df]


def main():
    selic_mes = sgs("sgs-4390.json")
    ipca12 = sgs("sgs-13522.json")
    over = sgs("sgs-1178.json")
    foc_n = focus("N", 0)

    pontos_post = [{"t": str(a), "v": round(ex_post(selic_mes, ipca12, a, 12), 2)} for a in range(2000, 2026)]
    pontos_post.append({"t": "2026-09", "v": round(ex_post(selic_mes, ipca12, 2026, 9), 2)})

    pontos_ante = []
    for a in range(2001, 2026):
        pontos_ante.append({"t": str(a), "v": round(ex_ante(over, foc_n, a, 12)[0], 2)})
    pontos_ante.append({"t": "2026-09", "v": round(ex_ante(over, foc_n, 2026, 9)[0], 2)})
    pontos_ante.append({"t": "2026-10", "v": round(ex_ante(over, foc_n, 2026, 10, date(2026, 10, 23))[0], 2)})

    saida = {
        "titulo": "Juro real ex-post e ex-ante no Brasil (% a.a.)",
        "tipo": "linha",
        "unidade": "% a.a.",
        "fonte": "BCB, SGS 4390 (Selic mensal), 13522 (IPCA 12 meses) e 1178 (Selic over diária anualizada); BCB, Focus, IPCA 12 meses à frente, mediana não suavizada (API Olinda); cálculo do painel (tools/analises/9.1_juro_real.py)",
        "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json",
        "consulta": CONSULTA,
        "nota": "r = (1 + i) / (1 + π) − 1. Ex-post: Selic acumulada em 12 meses (SGS 4390) sobre o IPCA de 12 meses (SGS 13522), posição de dezembro; 2026-09 = 12 meses até setembro de 2026. Ex-ante: Selic over do último dia útil do mês (SGS 1178) sobre a mediana Focus do IPCA 12 meses à frente, série não suavizada, base de cálculo 0, mesmo dia; 2026-09 = 30/09/2026; 2026-10 = 23/10/2026. Com a mediana suavizada o ex-ante muda até 0,3 ponto (30/09/2026: 8,65 em vez de 8,39). Coleta automática de 02/11/2026; dados de 2025–2026 sujeitos a revisão.",
        "governos": True,
        "ref": [{"v": 5.0, "rotulo": "juro neutro estimado pelo BCB (5,0%)"}],
        "series": [
            {"nome": "Ex-post (realizado)", "pontos": pontos_post},
            {"nome": "Ex-ante (esperado)", "pontos": pontos_ante},
        ],
    }
    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)
        f.write("\n")

    if "--resumo" in sys.argv:
        foc_s = focus("S", 0)
        meta = sgs("sgs-432.json")
        print("ano  ex-post  ex-ante  (suavizada)")
        post = {p["t"]: p["v"] for p in pontos_post}
        for p in pontos_ante:
            t = p["t"]
            if t == "2026-10":
                a, m, d = 2026, 10, date(2026, 10, 23)
            elif t == "2026-09":
                a, m, d = 2026, 9, None
            else:
                a, m, d = int(t), 12, None
            s = ex_ante(over, foc_s, a, m, d)[0]
            print(f"{t:8} {post.get(t, float('nan')):7.2f} {p['v']:7.2f} {s:9.2f}")
        for dia in (date(2026, 9, 30), date(2026, 10, 23)):
            r, _, df, i, pi = ex_ante(over, foc_n, dia.year, dia.month, dia)
            mt = meta[max(d for d in meta if d <= dia)]
            print(f"{dia}: over {i}, Focus {pi} ({df}) -> {r:.2f}; com a meta {mt}: {fisher(mt, pi):.2f}")
        for ini, fim in ((2000, 2009), (2010, 2019)):
            v = [post[str(a)] for a in range(ini, fim + 1)]
            print(f"média ex-post {ini}-{fim}: {sum(v) / len(v):.2f}")


if __name__ == "__main__":
    main()

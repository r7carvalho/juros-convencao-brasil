#!/usr/bin/env python3
"""Base monetária, M1 e IPCA no Brasil desde o Real (página 12.4.6 do painel).

Calcula, ano a ano, a variação de dezembro a dezembro da base monetária restrita e do M1 e a
compara com o IPCA do ano e do ano seguinte; calcula a base e o M1 em proporção do PIB de 12
meses e as taxas médias de crescimento. Grava dados/12.4.6-base-m1-ipca.json. Só usa a
biblioteca padrão.

Uso: python3 tools/analises/12.4.6_moeda_ipca.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  sgs-1788.json   Base monetária restrita, saldo em fim de período. Unidade: R$ mil (o arquivo
                  diz "R$ milhões (conferir)"; o valor de jul/2020, 423.674.702, bate com os
                  R$ 423,7 bilhões da nota de estatísticas monetárias do BCB de ago/2020, e o de
                  ago/2026 com os R$ 432,7 bi já usados na página 10).
  sgs-1824.json   M1, saldo em fim de período, R$ mil; a série antiga termina em jun/2018, quando
                  o BCB reformulou os meios de pagamento (nova série M1 no SGS 27791, não coletada).
  sgs-13522.json  IPCA, variação em 12 meses (%).
  sgs-4382.json   PIB de 12 meses a preços correntes, R$ milhões.

Método
  Variação dez/dez: saldo de dezembro do ano sobre o de dezembro do ano anterior. Para 2026, set/set.
  Começa em 1995 (primeiro ano inteiro do Real; antes disso as séries mudam de unidade monetária).
  Correlações de Pearson entre a variação anual da base (ou do M1) e o IPCA do mesmo ano e do ano
  seguinte.
"""
import json
import math
import os
import statistics as st
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
DADOS = os.path.join(ROOT, "dados")


def serie(cod):
    with open(os.path.join(BRUTOS, f"sgs-{cod}.json"), encoding="utf-8") as f:
        d = json.load(f)["dados"]
    out = {}
    for x in d:
        if x.get("valor") in ("", None):
            continue
        dia, mes, ano = x["data"].split("/")
        out[f"{ano}-{mes}"] = float(x["valor"])
    return out


def var(s, ano, mes="12"):
    a, b = f"{ano}-{mes}", f"{ano - 1}-{mes}"
    if a in s and b in s:
        return (s[a] / s[b] - 1) * 100
    return None


def main():
    resumo = "--resumo" in sys.argv
    base, m1, ipca, pib = serie(1788), serie(1824), serie(13522), serie(4382)
    anos = list(range(1995, 2026))
    linhas = []
    for a in anos:
        linhas.append((a, var(base, a), var(m1, a), ipca[f"{a}-12"]))

    # correlações
    ys = [a for a in range(1995, 2026)]
    gb = [var(base, a) for a in ys]
    pi = [ipca[f"{a}-12"] for a in ys]
    c_mesmo = st.correlation(gb, pi)
    c_seg = st.correlation(gb[:-1], [ipca[f"{a + 1}-12"] for a in ys[:-1]])
    ys1 = list(range(1995, 2018))
    gm = [var(m1, a) for a in ys1]
    c_m1 = st.correlation(gm, [ipca[f"{a}-12"] for a in ys1])
    c_m1s = st.correlation(gm, [ipca[f"{a + 1}-12"] for a in ys1])

    # médias geométricas
    def cagr(s, a0, a1):
        return ((s[f"{a1}-12"] / s[f"{a0}-12"]) ** (1 / (a1 - a0)) - 1) * 100

    ipca_med = (math.prod(1 + ipca[f"{a}-12"] / 100 for a in range(1996, 2026)) ** (1 / 30) - 1) * 100
    ipca_med_m1 = (math.prod(1 + ipca[f"{a}-12"] / 100 for a in range(1996, 2018)) ** (1 / 22) - 1) * 100

    if resumo:
        print("ano  base%  M1%   IPCA")
        for a, b, m, p in linhas:
            fb = f"{b:6.1f}" if b is not None else "     -"
            fm = f"{m:6.1f}" if m is not None else "     -"
            print(a, fb, fm, f"{p:6.2f}")
        print(f"2026 (set/set) base {var(base, 2026, '09'):.1f}%  IPCA 12m set/2026 {ipca['2026-09']:.2f}")
        print(f"correlação base × IPCA mesmo ano (1995–2025): {c_mesmo:.2f}; ano seguinte: {c_seg:.2f}")
        print(f"correlação M1 × IPCA mesmo ano (1995–2017): {c_m1:.2f}; ano seguinte: {c_m1s:.2f}")
        print(f"base: {cagr(base, 1995, 2025):.1f}% a.a. 1995–2025; PIB nominal {cagr(pib, 1995, 2025):.1f}%; IPCA {ipca_med:.1f}%")
        print(f"M1: {cagr(m1, 1995, 2017):.1f}% a.a. 1995–2017; IPCA {ipca_med_m1:.1f}%")
        for a in (1995, 2000, 2005, 2010, 2015, 2019, 2020, 2021, 2025):
            k = f"{a}-12"
            print(f"{a}: base/PIB {base[k] / 1e3 / pib[k] * 100:.2f}%", end="")
            print(f"; M1/PIB {m1[k] / 1e3 / pib[k] * 100:.2f}%" if k in m1 else "")
        print(f"set/2026: base/PIB {base['2026-09'] / 1e3 / pib['2026-09'] * 100:.2f}%; base R$ {base['2026-09'] / 1e6:.1f} bi")
        for k in ("2019-12", "2020-02", "2020-07", "2020-12", "2021-12"):
            print(f"base {k}: R$ {base[k] / 1e6:.1f} bi")

    out = {
        "titulo": "Base monetária, M1 e IPCA no Brasil, variação no ano (%)",
        "tipo": "linha",
        "unidade": "% no ano",
        "fonte": "BCB, SGS 1788 (base monetária restrita), 1824 (M1, série encerrada em jun/2018) e 13522 (IPCA); cálculo do painel",
        "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1788/dados?formato=json",
        "consulta": "2026-11-02",
        "nota": (
            "Variação de dezembro a dezembro dos saldos de fim de período; IPCA acumulado no ano. "
            "O M1 antigo termina em jun/2018, quando o BCB reformulou os meios de pagamento. "
            f"Correlação entre a variação da base e o IPCA do mesmo ano, 1995–2025: {c_mesmo:.2f}; "
            f"com o IPCA do ano seguinte: {c_seg:.2f}. Script: tools/analises/12.4.6_moeda_ipca.py."
        ),
        "governos": True,
        "series": [
            {"nome": "Base monetária", "pontos": [{"t": str(a), "v": round(b, 1)} for a, b, m, p in linhas]},
            {"nome": "M1", "pontos": [{"t": str(a), "v": round(m, 1) if m is not None else None}
                                       for a, b, m, p in linhas]},
            {"nome": "IPCA", "pontos": [{"t": str(a), "v": round(p, 2)} for a, b, m, p in linhas]},
        ],
    }
    with open(os.path.join(DADOS, "12.4.6-base-m1-ipca.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()

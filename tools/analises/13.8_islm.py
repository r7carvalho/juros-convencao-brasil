#!/usr/bin/env python3
"""Contas e gráficos da página 13.8 (o IS-LM, a moeda fiduciária e as curvas horizontais).

Uso: python3 -I tools/analises/13.8_islm.py [--json]
Imprime todos os números da economia de brinquedo e do episódio da base monetária.
Com --json, grava os dados/13.8-*.json da página.

Economia de brinquedo (números ilustrativos, sem dado real):
  consumo      C = 100 + 0,5 Y - 2 i
  investimento I = 300 - 3 i          (investimento autônomo 300)
  gasto        G = 150
  IS: Y = C + I + G  =>  Y = 2 (550 - 5 i) = 1100 - 10 i
  demanda por moeda L = 0,2 Y + (100 - 10 i)  (transações + preferência pela liquidez)
  oferta de moeda M = 260 (fixada pelo BC no IS-LM de manual)
  LM: 0,2 Y + 100 - 10 i = M  =>  i = 0,02 Y - (M - 100) / 10
  curva de Phillips de brinquedo: pi - meta = kappa * hiato + u
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONSULTA = "2026-11-05"
FONTE_BRINQ = "Economia de brinquedo do painel (curvas ilustrativas, sem dado real)"

C0, MPC, CI = 100.0, 0.5, 2.0       # consumo
I0, II = 300.0, 3.0                 # investimento
G0 = 150.0
K, L0, H = 0.2, 100.0, 10.0         # demanda por moeda
M0 = 260.0


def is_y(i, g=G0, i0=I0):
    """Renda que equilibra o mercado de bens dado o juro (curva IS)."""
    return (C0 + i0 + g - (CI + II) * i) / (1 - MPC)


def is_i(y, g=G0, i0=I0):
    return (C0 + i0 + g - (1 - MPC) * y) / (CI + II)


def lm_i(y, m=M0, l0=L0):
    """Juro que equilibra o mercado de moeda dada a renda (curva LM)."""
    return (K * y + l0 - m) / H


def demanda_moeda(y, i, l0=L0):
    return K * y + l0 - H * i


def equilibrio(g=G0, m=M0, i0=I0, l0=L0):
    # IS: y = a - b i ; LM: i = c y - d
    a = (C0 + i0 + g) / (1 - MPC)
    b = (CI + II) / (1 - MPC)
    c = K / H
    d = (m - l0) / H
    i = (c * a - d) / (1 + c * b)
    return a - b * i, i


def r(v):
    return round(v, 2)


def mensal_ultimo(cod):
    d = json.load(open(os.path.join(ROOT, "dados", "brutos", f"sgs-{cod}.json"), encoding="utf-8"))
    out = {}
    for x in d["dados"]:
        dd, mm, aa = x["data"].split("/")
        out[f"{aa}-{mm}"] = float(x["valor"])
    return out


def main():
    gravar = "--json" in sys.argv
    out = {}

    print("== IS passo a passo")
    for i in (4, 5, 6):
        y = is_y(i)
        c = C0 + MPC * y - CI * i
        inv = I0 - II * i
        print(f"juro {i}%: renda {y:.0f} = consumo {c:.1f} + investimento {inv:.0f} + gasto {G0:.0f}")
    print("multiplicador:", 1 / (1 - MPC), "; cada ponto de juro tira", CI + II, "de demanda direta e",
          (CI + II) / (1 - MPC), "de renda")
    print("IS com gasto +15: renda a 5% =", is_y(5, g=G0 + 15), "; IS com investimento autônomo -15:",
          is_y(5, i0=I0 - 15))

    print("== Mercado de moeda (excesso de demanda = demanda - oferta 260)")
    for y in (1000, 1050):
        print(f"renda {y}:", [(i, demanda_moeda(y, i), demanda_moeda(y, i) - M0) for i in range(2, 9)])
    print("LM: juro com renda 1000, 1050, 1100 =", [lm_i(y) for y in (1000, 1050, 1100)])

    print("== Encontro e políticas")
    y0, i0 = equilibrio()
    print(f"base: renda {y0:.1f}, juro {i0:.2f}")
    y1, i1 = equilibrio(g=G0 + 15)
    print(f"gasto +15: renda {y1:.1f}, juro {i1:.2f}; com juro parado em {i0:.0f}: renda {is_y(i0, g=G0 + 15):.0f}")
    y2, i2 = equilibrio(m=M0 + 12)
    print(f"moeda +12 (272): renda {y2:.1f}, juro {i2:.2f}")

    print("== LM horizontal (BC fixa o juro e fornece a moeda pedida)")
    for g, i in ((G0, 5), (G0 + 15, 5), (G0, 4)):
        y = is_y(i, g=g)
        print(f"gasto {g:.0f}, juro {i}%: renda {y:.0f}, moeda que o sistema pede {demanda_moeda(y, i):.0f}")
    ys, is_ = equilibrio(l0=L0 + 12)
    print(f"choque de liquidez +12 com moeda fixa em 260: renda {ys:.1f}, juro {is_:.2f}")
    print(f"choque de liquidez +12 com juro fixo em 5%: renda {is_y(5):.0f}, moeda pedida {demanda_moeda(is_y(5), 5, l0=L0 + 12):.0f}")

    print("== Phillips de brinquedo e identificação")
    kap = 0.5
    d = [2, -1, 1, -2]                     # choques de demanda (BC passivo: hiato = d)
    u = [1, -0.5, 0.5, -1]                 # choques de custo
    passivo = [(x, kap * x) for x in d]
    ativo = [(-u_ / kap, kap * (-u_ / kap) + u_) for u_ in u]   # BC usa o hiato para zerar a inflação
    metade = [(-u_ / (2 * kap), kap * (-u_ / (2 * kap)) + u_) for u_ in u]
    print("passivo (hiato, inflação - meta):", passivo)
    print("ativo:", ativo)
    print("metade:", metade, "; inclinação aparente:", [r(p / x) for x, p in metade])
    print("custo de desinflação: para tirar 1 ponto pelo hiato, com kappa 0,5 e 0,1:", 1 / 0.5, 1 / 0.1)

    print("== Base monetária em dezembro e janeiro com a Selic parada (SGS 1788 e 432)")
    bm = mensal_ultimo("1788")
    sm = mensal_ultimo("432")
    pares = [("2018", "2019"), ("2022", "2023"), ("2025", "2026")]
    pts = []
    for a, b in pares:
        nov, dez, jan = bm[f"{a}-11"], bm[f"{a}-12"], bm[f"{b}-01"]
        vd, vj = 100 * (dez / nov - 1), 100 * (jan / dez - 1)
        sel = (sm[f"{a}-11"], sm[f"{a}-12"], sm[f"{b}-01"])
        print(f"{a}/{b}: dez {vd:+.1f}%, jan {vj:+.1f}%, Selic meta fim de nov/dez/jan {sel}; "
              f"base em dez R$ {dez / 1e6:.1f} bi")
        pts.append({"t": f"dez/{a}", "v": r(vd)})
        pts.append({"t": f"jan/{b}", "v": r(vj)})

    if not gravar:
        return

    def grava(nome, spec):
        p = os.path.join(ROOT, "dados", nome)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(spec, f, ensure_ascii=False, indent=1)
        print("gravado", p)

    def curva(fn, ys):
        return [{"t": f"{y:04d}", "v": r(fn(y))} for y in ys]

    nota_eixo = ("Eixo horizontal: renda da economia de brinquedo (de 1.000 a 1.130); eixo vertical: juro, em % ao ano. "
                 "Curvas ilustrativas, calculadas em tools/analises/13.8_islm.py.")

    grava("13.8-is-brinquedo.json", {
        "titulo": "Brinquedo: a curva IS e o que a desloca (renda no eixo horizontal, juro no vertical)",
        "tipo": "linha", "unidade": "% ao ano", "fonte": FONTE_BRINQ, "consulta": CONSULTA,
        "nota": nota_eixo + " IS: renda = 1.100 − 10 × juro. Gasto público +15 desloca a curva 30 para a direita; "
                "queda de 15 no investimento autônomo (confiança) desloca 30 para a esquerda.",
        "governos": False,
        "series": [
            {"nome": "IS (gasto 150)", "pontos": curva(is_i, range(1000, 1101, 10))},
            {"nome": "IS com gasto público +15", "pontos": curva(lambda y: is_i(y, g=G0 + 15), range(1030, 1131, 10))},
            {"nome": "IS com confiança menor", "pontos": curva(lambda y: is_i(y, i0=I0 - 15), range(1000, 1071, 10))},
        ]})

    grava("13.8-mercado-de-moeda.json", {
        "titulo": "Brinquedo: quanto o público quer de moeda além dos 260 que o BC oferece, para cada juro",
        "tipo": "barras", "unidade": "unidades de moeda", "fonte": FONTE_BRINQ, "consulta": CONSULTA,
        "nota": "Demanda por moeda = 0,2 × renda (transações) + 100 − 10 × juro (preferência pela liquidez); oferta fixa "
                "de 260. A barra mostra demanda menos oferta: acima de zero falta moeda e o juro sobe; abaixo, sobra e o juro "
                "cai. O juro de equilíbrio é onde a barra zera: 4% com renda de 1.000 e 5% com renda de 1.050.",
        "series": [
            {"nome": "Renda de 1.000", "pontos": [{"t": f"juro {i}%", "v": r(demanda_moeda(1000, i) - M0)} for i in range(2, 9)]},
            {"nome": "Renda de 1.050", "pontos": [{"t": f"juro {i}%", "v": r(demanda_moeda(1050, i) - M0)} for i in range(2, 9)]},
        ]})

    grava("13.8-is-lm-encontro.json", {
        "titulo": "Brinquedo: o encontro da IS com a LM e o que as políticas fiscal e monetária fazem",
        "tipo": "linha", "unidade": "% ao ano", "fonte": FONTE_BRINQ, "consulta": CONSULTA,
        "nota": nota_eixo + " Equilíbrio inicial: renda 1.050 e juro 5%. Gasto +15: renda 1.075 e juro 5,5%. "
                "Moeda de 260 para 272: renda 1.060 e juro 4%.",
        "governos": False,
        "series": [
            {"nome": "IS (gasto 150)", "pontos": curva(is_i, range(1000, 1101, 10))},
            {"nome": "IS com gasto +15", "pontos": curva(lambda y: is_i(y, g=G0 + 15), range(1030, 1131, 10))},
            {"nome": "LM (moeda 260)", "pontos": curva(lm_i, range(1000, 1131, 10))},
            {"nome": "LM (moeda 272)", "pontos": curva(lambda y: lm_i(y, m=M0 + 12), range(1000, 1131, 10))},
        ]})

    grava("13.8-lm-horizontal.json", {
        "titulo": "Brinquedo: quando o BC fixa o juro, a LM vira uma reta horizontal",
        "tipo": "linha", "unidade": "% ao ano", "fonte": FONTE_BRINQ, "consulta": CONSULTA,
        "nota": nota_eixo + " Com o juro fixado em 5%, o gasto +15 leva a renda a 1.080 (o efeito inteiro) e o sistema "
                "pede 266 de moeda, que o BC fornece; o corte para 4% leva a renda a 1.060 e a moeda a 272.",
        "governos": False,
        "series": [
            {"nome": "IS (gasto 150)", "pontos": curva(is_i, range(1000, 1101, 10))},
            {"nome": "IS com gasto +15", "pontos": curva(lambda y: is_i(y, g=G0 + 15), range(1030, 1131, 10))},
            {"nome": "LM de manual (moeda 260)", "pontos": curva(lm_i, range(1000, 1131, 10))},
            {"nome": "Regra de juro: 5%", "pontos": curva(lambda y: 5.0, range(1000, 1131, 10))},
            {"nome": "Regra de juro: 4%", "pontos": curva(lambda y: 4.0, range(1000, 1131, 10))},
        ]})

    grava("13.8-phillips-brinquedo.json", {
        "titulo": "Brinquedo: inflação acima da meta para cada hiato, com curva de Phillips inclinada e achatada",
        "tipo": "barras", "unidade": "pontos acima da meta", "fonte": FONTE_BRINQ, "consulta": CONSULTA,
        "nota": "Inflação − meta = inclinação × hiato, sem choques e com expectativa na meta. Inclinada: 0,5; achatada: 0,1. "
                "Hiato: quanto a renda está acima (+) ou abaixo (−) da renda que não acelera a inflação, em %.",
        "series": [
            {"nome": "Inclinada (0,5)", "pontos": [{"t": f"hiato {h:+d}%".replace("+0", "0"), "v": r(0.5 * h)} for h in range(-2, 3)]},
            {"nome": "Achatada (0,1)", "pontos": [{"t": f"hiato {h:+d}%".replace("+0", "0"), "v": r(0.1 * h)} for h in range(-2, 3)]},
        ]})

    grava("13.8-identificacao-brinquedo.json", {
        "titulo": "Brinquedo: a mesma curva de Phillips (inclinação 0,5) vista com um BC passivo e com um BC que reage bem",
        "tipo": "barras", "unidade": "pontos", "fonte": FONTE_BRINQ + "; mecanismo de McLeay e Tenreyro (2020)",
        "url": "https://www.nber.org/papers/w25892", "consulta": CONSULTA,
        "nota": "Curva verdadeira: inflação − meta = 0,5 × hiato + choque de custo. BC passivo: só choques de demanda "
                "(+2, −1, +1, −2), e a inflação acompanha o hiato com inclinação 0,5. BC ativo: choques de custo (+1, −0,5, "
                "+0,5, −1), e o BC move o hiato (−2, +1, −1, +2) até a inflação ficar na meta; nos dados, o hiato varia e a "
                "inflação não, como se a curva fosse horizontal.",
        "series": [
            {"nome": "Hiato, BC passivo", "pontos": [{"t": f"Ano {k + 1}", "v": r(x)} for k, (x, p) in enumerate(passivo)]},
            {"nome": "Inflação − meta, BC passivo", "pontos": [{"t": f"Ano {k + 1}", "v": r(p)} for k, (x, p) in enumerate(passivo)]},
            {"nome": "Hiato, BC ativo", "pontos": [{"t": f"Ano {k + 1}", "v": r(x)} for k, (x, p) in enumerate(ativo)]},
            {"nome": "Inflação − meta, BC ativo", "pontos": [{"t": f"Ano {k + 1}", "v": r(p) + 0.0} for k, (x, p) in enumerate(ativo)]},
        ]})

    grava("13.8-base-monetaria-dezembro.json", {
        "titulo": "Base monetária: variação no mês em dezembro e janeiro, em três viradas de ano com a Selic parada (%)",
        "tipo": "barras", "unidade": "% no mês", "fonte": "BCB, SGS 1788 (base monetária restrita, saldo de fim de mês) e SGS 432 (Selic meta); cálculo do painel",
        "url": "https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarGraficoPorId&hdOidSeriesSelecionadas=1788",
        "consulta": "2026-11-02",
        "nota": "Selic meta parada nos três pares de meses: 6,5% (nov/2018 a jan/2019), 13,75% (nov/2022 a jan/2023) e "
                "15% (nov/2025 a jan/2026). A base restrita soma o papel-moeda emitido e as reservas bancárias; o acervo "
                "do painel não separa as duas partes.",
        "series": [{"nome": "Variação da base monetária no mês", "pontos": pts}]})

    grava("13.8-hazell-inclinacao.json", {
        "titulo": "Inclinação da curva de Phillips nos estados americanos, antes e depois de 1990, com e sem efeitos fixos de tempo",
        "tipo": "barras", "unidade": "κ (coeficiente)",
        "fonte": "Hazell, Herreño, Nakamura e Steinsson, NBER Working Paper 28005 (rev. maio de 2021), Tabela 2, colunas 1 a 4",
        "url": "https://www.nber.org/papers/w28005", "consulta": CONSULTA,
        "nota": "κ é a resposta da inflação de bens não comercializáveis do estado ao desemprego do estado, em pontos por ponto, "
                "na equação (17) do artigo. Sem efeitos fixos de tempo, a curva parece cem vezes mais plana depois de 1990; "
                "com eles, que absorvem a mudança das expectativas de longo prazo, a queda é de cerca de metade.",
        "series": [
            {"nome": "Sem efeitos fixos de tempo", "pontos": [{"t": "1978–1990", "v": 0.0278}, {"t": "1991–2018", "v": 0.0002}]},
            {"nome": "Com efeitos fixos de tempo", "pontos": [{"t": "1978–1990", "v": 0.0107}, {"t": "1991–2018", "v": 0.0050}]},
        ]})


if __name__ == "__main__":
    main()

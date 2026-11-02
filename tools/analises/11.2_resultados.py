#!/usr/bin/env python3
"""Resultados fiscais: primário, juros nominais, juros reais e resultado operacional (página 11.2).

Refaz dados/11.2-tres-resultados.json e dados/11.2-juros-correcao-real.json a partir do acervo bruto.
Só usa a biblioteca padrão.

Uso: python3 tools/analises/11.2_resultados.py [--resumo]

Entradas (dados/brutos/, coleta automática de 02/11/2026):
  sgs-5793.json   NFSP primária do setor público consolidado, 12 meses, % do PIB (positivo = déficit)
  sgs-5727.json   NFSP nominal do setor público consolidado, 12 meses, % do PIB (positivo = déficit)
  sgs-4513.json   DLSP, % do PIB, fim de mês
  sgs-4382.json   PIB acumulado em 12 meses, R$ milhões correntes
  sgs-13522.json  IPCA acumulado em 12 meses (%)
  sgs-5839.json   série encerrada em dez/2009, rotulada no coletor como "juros nominais (conferir)";
                  só entra na comparação impressa com --resumo, nunca nos gráficos

Método (declarado na página 11.2)
  Juros nominais (% do PIB, 12 meses) = SGS 5727 − SGS 5793. É a mesma conta das páginas 3.3, 9.1 e 11.
  Atualização monetária estimada (% do PIB, 12 meses até o mês m):
      IPCA de 12 meses até m × DLSP de m−12 em reais / PIB de 12 meses até m,
      com DLSP em reais = razão (SGS 4513) × PIB de 12 meses (SGS 4382) do mês m−12.
  Juros reais = juros nominais − atualização monetária estimada.
  Resultado operacional (NFSP operacional) = NFSP primária + juros reais.
  É a mesma aproximação usada em 3.3 e 3.5 para 2025 (IPCA de 4,26% sobre a DLSP de dez/2024),
  estendida a todos os meses. Diferenças em relação à série oficial do BCB (encerrada em 2009):
  o BCB deduzia a atualização monetária efetiva dos saldos; o painel aplica o IPCA à DLSP inteira,
  inclusive à parte externa líquida, e não separa o resultado dos swaps cambiais nem o custo de
  carregamento das reservas, que ficam dentro do "juro real" residual.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
CONSULTA = "2026-11-02"
URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.5727/dados?formato=json"


def sgs(codigo):
    with open(os.path.join(BRUTOS, f"sgs-{codigo}.json"), encoding="utf-8") as f:
        dados = json.load(f)["dados"]
    out = {}
    for r in dados:
        if r["valor"] in ("", None):
            continue
        _, m, a = r["data"].split("/")
        out[(int(a), int(m))] = float(r["valor"])
    return out


def menos12(chave):
    a, m = chave
    return (a - 1, m)


def calcular():
    prim, nom, dlsp, pib, ipca = (sgs(c) for c in (5793, 5727, 4513, 4382, 13522))
    linhas = []
    for k in sorted(nom):
        k0 = menos12(k)
        if k not in prim or k0 not in dlsp or k0 not in pib or k not in ipca:
            continue
        jn = nom[k] - prim[k]
        corr = ipca[k] / 100 * dlsp[k0] * pib[k0] / pib[k]
        jr = jn - corr
        linhas.append(dict(
            ano=k[0], mes=k[1], prim=prim[k], nom=nom[k], jn=jn, corr=corr, jr=jr,
            op=prim[k] + jr, pib=pib[k], ipca=ipca[k], dlsp0=dlsp[k0],
        ))
    return linhas


def r2(v):
    return round(v, 2)


def anuais(linhas):
    """Dezembro de cada ano e o último mês disponível."""
    sel = [l for l in linhas if l["mes"] == 12]
    ult = linhas[-1]
    if ult["mes"] != 12:
        sel.append(ult)
    return sel


def rotulo_ano(l):
    return str(l["ano"]) if l["mes"] == 12 else f"{l['ano']}*"


def grafico_linha(linhas):
    def pts(campo):
        return [{"t": f"{l['ano']}-{l['mes']:02d}", "v": r2(l[campo])} for l in linhas]
    return {
        "titulo": "Três resultados do setor público consolidado: primário, operacional e nominal (NFSP, % do PIB, 12 meses)",
        "tipo": "linha",
        "unidade": "% do PIB",
        "fonte": "BCB, SGS 5793 (NFSP primária), 5727 (NFSP nominal), 4513 (DLSP), 4382 (PIB de 12 meses) e 13522 (IPCA de 12 meses), coleta de 02/11/2026; resultado operacional calculado pelo painel (tools/analises/11.2_resultados.py)",
        "url": URL,
        "consulta": CONSULTA,
        "nota": "Sinal da NFSP: positivo é déficit, negativo é superávit. Operacional = primário + juros reais; juros reais = juros nominais (5727 − 5793) menos a atualização monetária estimada pelo painel (IPCA de 12 meses vezes a DLSP de 12 meses antes, em reais, sobre o PIB de 12 meses). O BCB publicou a série oficial do operacional só até dez/2009, com outro método; a do painel não a reproduz. Mensal, de dez/2002 a set/2026.",
        "governos": True,
        "ref": [{"v": 0, "rotulo": "equilíbrio"}],
        "series": [
            {"nome": "Nominal", "pontos": pts("nom")},
            {"nome": "Operacional (cálculo do painel)", "pontos": pts("op")},
            {"nome": "Primário", "pontos": pts("prim")},
        ],
    }


def grafico_empilhado(linhas):
    sel = anuais(linhas)
    return {
        "titulo": "Juros nominais do setor público: quanto repõe a inflação e quanto é juro real (% do PIB, 12 meses)",
        "tipo": "empilhadas",
        "unidade": "% do PIB",
        "fonte": "BCB, SGS 5727 − 5793 (juros nominais apropriados), 4513 (DLSP), 4382 (PIB de 12 meses) e 13522 (IPCA), coleta de 02/11/2026; divisão calculada pelo painel (tools/analises/11.2_resultados.py)",
        "url": URL,
        "consulta": CONSULTA,
        "nota": "A soma das duas partes é o juro nominal apropriado por competência. Atualização monetária = IPCA do ano vezes a DLSP do fim do ano anterior, em reais, sobre o PIB do ano; juro real = o resto, que inclui o resultado dos swaps cambiais e o custo de carregamento das reservas. Em 2021 a inflação superou o juro, e o juro real ficou negativo. 2026* = 12 meses até setembro.",
        "series": [
            {"nome": "Atualização monetária (IPCA sobre a dívida líquida)",
             "pontos": [{"t": rotulo_ano(l), "v": r2(l["corr"])} for l in sel]},
            {"nome": "Juro real",
             "pontos": [{"t": rotulo_ano(l), "v": r2(l["jr"])} for l in sel]},
        ],
    }


def gravar(nome, obj):
    caminho = os.path.join(ROOT, "dados", nome)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("gravado", os.path.relpath(caminho, ROOT))


def resumo(linhas):
    sel = anuais(linhas)
    print(f"{'ano':6} {'prim':>6} {'jn':>6} {'corr':>6} {'jr':>6} {'op':>6} {'nom':>6} {'jn R$bi':>8} {'jr R$bi':>8}")
    for l in sel:
        bi = l["pib"] / 1e5  # R$ milhões × % / 100 → R$ bilhões: pib/1e3 * v/100
        print(f"{rotulo_ano(l):6} {l['prim']:6.2f} {l['jn']:6.2f} {l['corr']:6.2f} {l['jr']:6.2f} {l['op']:6.2f} "
              f"{l['nom']:6.2f} {l['jn']*bi:8.1f} {l['jr']*bi:8.1f}")

    def media(ini, fim, campo):
        xs = [l[campo] for l in sel if l["mes"] == 12 and ini <= l["ano"] <= fim]
        return sum(xs) / len(xs)

    print("\nMédias anuais (% do PIB)")
    for ini, fim in ((2002, 2013), (2014, 2019), (2020, 2022), (2023, 2025), (2002, 2025)):
        print(f"  {ini}-{fim}: primário {media(ini, fim, 'prim'):5.2f}  juros nominais {media(ini, fim, 'jn'):5.2f}  "
              f"atualização {media(ini, fim, 'corr'):5.2f}  juros reais {media(ini, fim, 'jr'):5.2f}  "
              f"operacional {media(ini, fim, 'op'):5.2f}  nominal {media(ini, fim, 'nom'):5.2f}")

    soma_jn = sum(l["jn"] * l["pib"] / 1e5 for l in sel if l["mes"] == 12)
    soma_jr = sum(l["jr"] * l["pib"] / 1e5 for l in sel if l["mes"] == 12)
    print(f"\nSoma 2002-2025, R$ bi correntes: juros nominais {soma_jn:.0f}, juros reais {soma_jr:.0f} "
          f"({soma_jr / soma_jn * 100:.0f}%)")
    pos = [rotulo_ano(l) for l in sel if l["nom"] <= 0]
    print("Anos com superávit nominal:", pos or "nenhum")
    print("Menor déficit nominal:", min((l["nom"], rotulo_ano(l)) for l in sel))
    sup = [rotulo_ano(l) for l in sel if l["prim"] < 0]
    print("Anos com superávit primário:", sup)
    print("Maior superávit primário:", min((l["prim"], rotulo_ano(l)) for l in sel))
    print("Faixa de juros 2002-2013:", min((l["jn"], rotulo_ano(l)) for l in sel if l["ano"] <= 2013),
          max((l["jn"], rotulo_ano(l)) for l in sel if l["ano"] <= 2013))

    # Comparação com a série 5839 (rótulo não confirmado; fica fora dos gráficos)
    s5839 = sgs(5839)
    print("\nSGS 5839 × juros nominais (5727 − 5793) × juros reais do painel, dezembro:")
    for l in sel:
        if l["mes"] == 12 and (l["ano"], 12) in s5839:
            print(f"  {l['ano']}: 5839 {s5839[(l['ano'], 12)]:6.2f}   jn {l['jn']:6.2f}   jr painel {l['jr']:6.2f}   IPCA {l['ipca']:5.2f}")

    # Ponte de 2024 e 2025 com o resultado dos swaps (BNDES/FGV IBRE: +1,0% do PIB em 2024, −0,8% em 2025)
    swaps = {2024: 1.0, 2025: -0.8}
    print("\nJuro real do painel sem o resultado dos swaps (BNDES/FGV IBRE):")
    for l in sel:
        if l["mes"] == 12 and l["ano"] in swaps:
            print(f"  {l['ano']}: com swaps {l['jr']:.2f}; sem swaps {l['jr'] - swaps[l['ano']]:.2f}")


def main():
    linhas = calcular()
    gravar("11.2-tres-resultados.json", grafico_linha(linhas))
    gravar("11.2-juros-correcao-real.json", grafico_empilhado(linhas))
    if "--resumo" in sys.argv:
        resumo(linhas)


if __name__ == "__main__":
    main()

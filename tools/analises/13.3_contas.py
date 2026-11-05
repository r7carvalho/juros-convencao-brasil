#!/usr/bin/env python3
"""As contas da proposta de Lara Resende: juros, déficit e dívida (página 13.3).

Refaz dados/13.3-alivio-juros.json, dados/13.3-juros-nominais.json, dados/13.3-dbgg.json e
dados/13.3-dlsp.json; com --resumo, imprime as tabelas do texto (exemplo de brinquedo, alívio ano a
ano, déficit nominal e operacional, r − g, primário estabilizador, reservas e detentores).
Só usa a biblioteca padrão.

Uso: python3 tools/analises/13.3_contas.py [--resumo]

Entradas (dados/brutos/, coleta de 02/11/2026, e números decididos em conteudo/_divergencias.md)
  sgs-13762.json  DBGG, % do PIB (set/2026: 82,93)
  sgs-4513.json   DLSP, % do PIB (set/2026: 69,98)
  sgs-4382.json   PIB de 12 meses, R$ milhões (set/2026: 13.402.023,7)
  sgs-5727.json   NFSP nominal, 12 meses, % do PIB (set/2026: 9,51)
  sgs-5793.json   NFSP primária, 12 meses, % do PIB (set/2026: 0,52)
  sgs-4390.json   Selic acumulada no mês (Selic média de 12 meses até set/2026: 14,47%)
  sgs-13522.json  IPCA de 12 meses (set/2026: 4,58)
  focus-anuais_selic/ipca/pib.json  medianas do Focus de 23/10/2026 para 2027 a 2030
  Números do painel (conteudo/_divergencias.md): DPF de R$ 9,29 tri em ago/2026 (RMD), LFT 52,74%,
  índices de preços 23,22%, prefixados 20,31%, câmbio 3,74%; compromissadas de 10,28% do PIB
  (ago/2026, fatores condicionantes da DBGG); R$ 61,7 bi por ponto de Selic (DLSP, BCB, dez/2025);
  R$ 49 bi por ponto (DPF); custo médio da DPF em 12 meses de 12,59% (RMD ago/2026, página 3.4);
  juro implícito da DBGG de 2026 (jan-ago anualizado) de 13,16% (página 11.7); custo de carregamento
  das reservas de R$ 189,5 bi e R$ 19 bi por ponto (página 10.3.6); sensibilidade da DLSP ao dólar de
  −0,8 p.p. do PIB por 10% de alta, com swaps (página 10.3.6); detentores da DPMFi em ago/2026
  (página 3.3).

Modelo (todas as hipóteses estão declaradas na página 13.3)
  A DBGG de set/2026 é dividida em cinco blocos, com participação constante ao longo do tempo:
    flutuante  F = LFT (52,74% da DPF) + compromissadas (10,28% do PIB): custa a Selic média do ano
    prefixado  P = 20,31% da DPF: custo médio c_P; a cada ano uma fração 1/N_P vence e é refinanciada
               à taxa nova = Selic média esperada dos três anos seguintes + prêmio τ_P
    inflação   X = 23,22% da DPF: juro real médio ρ_X; a cada ano 1/N_X vence e é refinanciada ao juro
               real novo = (Selic − IPCA) médio dos três anos seguintes + prêmio τ_X; custo nominal
               = (1 + ρ_X)(1 + IPCA) − 1
    câmbio     C = 3,74% da DPF: 6% ao ano em dólar (hipótese); a variação do dólar entra como ajuste
    outros     O = resto da DBGG (dívida bancária de estados e municípios e outros): custa a Selic
  Calibração: c_P inicial = 12,59% (custo médio da DPF); ρ_X inicial é a taxa que faz o custo da DBGG
  de set/2026 igual a 13,16% (juro implícito de 2026, página 11.7).
  Juros brutos do ano t:  J_G(t) = Σ_k B_k(t−1) × custo_k(t)
  Juros líquidos (NFSP):  J_L(t) = J_G(t) − K(t), K = renda dos ativos que a DLSP desconta, calibrada
    para que, nos 12 meses até set/2026, juros brutos (13,16% sobre a DBGG de set/2025) menos K deem os
    R$ 1.204,8 bi observados (8,99% do PIB); a parte das reservas (US$ 362,8 bi a 3,875% ao ano) cresce
    com o dólar e o resto com o PIB nominal.
  Dívidas:  D_G(t) = D_G(t−1) + J_G(t) + déficit primário(t) + ajuste cambial da dívida em dólar
            D_L(t) = D_L(t−1) + J_L(t) + déficit primário(t) − ganho cambial líquido (0,8 p.p. do PIB
            por 10% de alta do dólar)
            d(t) = D(t) / PIB(t), PIB(t) = PIB(t−1)(1 + γ)(1 + π), deflator do PIB = IPCA (hipótese)
  Primário: déficit de 0,52% do PIB em todos os casos, para isolar o efeito do juro.
  Atualização monetária (método da 11.2): π(t) × D_L(t−1) / PIB(t); juro real = J_L − atualização;
  resultado operacional = primário + juro real.
  r − g: i(t) = J_G(t)/D_G(t−1); primário estabilizador s* = d (i − g)/(1 + g), com g nominal.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
CONSULTA = "2026-11-02"
URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.13762/dados?formato=json"
ANOS = [2027, 2028, 2029, 2030, 2031]


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


def focus(nome, data="2026-10-23"):
    with open(os.path.join(BRUTOS, f"focus-anuais_{nome}.json"), encoding="utf-8") as f:
        dd = json.load(f)["dados"]
    return {int(x["DataReferencia"]): x["Mediana"] for x in dd
            if x["Data"] == data and x["baseCalculo"] == 0}


# ---------------------------------------------------------------- ponto de partida (set/2026)
dbgg, dlsp, pib, nom, prim, selm, ipca = (sgs(c) for c in (13762, 4513, 4382, 5727, 5793, 4390, 13522))
K0 = (2026, 9)
PIB0 = pib[K0] / 1e3                      # R$ bi, 12 meses até set/2026
DG0 = dbgg[K0] / 100 * PIB0               # R$ bi
DL0 = dlsp[K0] / 100 * PIB0
JL0_PP = nom[K0] - prim[K0]               # 8,99% do PIB
JL0 = JL0_PP / 100 * PIB0                 # R$ 1.204,8 bi
PRIM0 = prim[K0]                          # déficit, % do PIB
SEL0 = 1.0
for k in [k for k in sorted(selm) if (2025, 10) <= k <= (2026, 9)]:
    SEL0 *= 1 + selm[k] / 100
SEL0 = (SEL0 - 1) * 100                   # Selic efetiva de 12 meses até set/2026
PI0 = ipca[K0]

DPF = 9290.0                              # R$ bi, ago/2026 (RMD)
SH = dict(lft=0.5274, ipca=0.2322, pre=0.2031, cam=0.0374)
COMP = 0.1028 * PIB0                      # compromissadas, 10,28% do PIB (ago/2026)
B0 = dict(F=SH["lft"] * DPF + COMP, P=SH["pre"] * DPF, X=SH["ipca"] * DPF, C=SH["cam"] * DPF)
B0["O"] = DG0 - sum(B0.values())
W = {k: v / DG0 for k, v in B0.items()}   # participações constantes na DBGG

I_IMPL0 = 13.16                           # juro implícito da DBGG, 2026 (página 11.7)
CP0 = 12.59                               # custo médio da DPF em 12 meses (RMD ago/2026)
CUSTO_CAM = 6.0                           # % ao ano em dólar (hipótese)
RES_USD = 362.821                         # US$ bi, set/2026 (SGS 3546)
PTAX0 = 5.40                              # R$/US$ de referência (hipótese; PTAX de fim de out/2026: 5,42)
US_RATE = 3.875                           # fed funds, ponto médio, set/2026 (BIS)
SENS_DLSP_FX = 0.8                        # p.p. do PIB de queda da DLSP por 10% de alta do dólar

# juro real inicial do bloco de inflação: calibra o custo total em 13,16%
_resto = W["F"] * SEL0 + W["P"] * CP0 + W["C"] * CUSTO_CAM + W["O"] * SEL0
_nom_x = (I_IMPL0 - _resto) / W["X"]
RX0 = ((1 + _nom_x / 100) / (1 + PI0 / 100) - 1) * 100
DG_ANT = dbgg[(2025, 9)] / 100 * pib[(2025, 9)] / 1e3   # estoque de um ano antes (set/2025)
JG0 = I_IMPL0 / 100 * DG_ANT              # juros brutos de 12 meses compatíveis com o fluxo da NFSP
K_RES0 = RES_USD * PTAX0 * US_RATE / 100
K_OUT0 = JG0 - JL0 - K_RES0


# ---------------------------------------------------------------- os casos
FS, FI, FP = focus("selic"), focus("ipca"), focus("pib")


def media_ano(fim_ant, fim):
    return (fim_ant + fim) / 2


SELIC_A = {2027: media_ano(FS[2026], FS[2027]), 2028: media_ano(FS[2027], FS[2028]),
           2029: FS[2029], 2030: FS[2030], 2031: FS[2030]}
IPCA_A = {2027: FI[2027], 2028: FI[2028], 2029: FI[2029], 2030: FI[2030], 2031: FI[2030]}
PIB_A = {2027: FP[2027], 2028: FP[2028], 2029: FP[2029], 2030: FP[2030], 2031: FP[2030]}

CASOS = {
    "a": dict(nome="(a) Selic do Focus",
              selic=SELIC_A, ipca=IPCA_A, pib=PIB_A, dolar={}, tau_p=1.5, tau_x=0.5),
    "b": dict(nome="(b) Proposta, inflação na meta",
              selic={2027: media_ano(13.75, 7.5), 2028: 7.5, 2029: 6.5, 2030: 5.5, 2031: 5.5},
              ipca={2027: FI[2027], 2028: 3.0, 2029: 3.0, 2030: 3.0, 2031: 3.0},
              pib=PIB_A, dolar={}, tau_p=1.0, tau_x=0.5),
    "c": dict(nome="(c) Proposta com desancoragem",
              selic={2027: media_ano(13.75, 7.5), 2028: 7.5, 2029: 7.5, 2030: 7.5, 2031: 7.5},
              ipca={2027: 6.0, 2028: 7.5, 2029: 7.5, 2030: 7.0, 2031: 7.0},
              pib=PIB_A, dolar={2027: 20.0, 2028: 10.0}, tau_p=4.0, tau_x=2.5),
}
# variantes impressas no --resumo (não vão aos gráficos)
VARIANTES = {
    "c2": dict(CASOS["c"], nome="(c') desancoragem com reversão (Selic a 11%, 13% e 12% em 2029-2031)",
               selic={2027: media_ano(13.75, 7.5), 2028: 7.5, 2029: 11.0, 2030: 13.0, 2031: 12.0}),
    "b_pib": dict(CASOS["b"], nome="(b+) proposta na meta com PIB 0,5 p.p. maior",
                  pib={a: v + 0.5 for a, v in PIB_A.items()}),
    "k1375": dict(CASOS["a"], nome="Selic parada em 13,75%",
                  selic={a: 13.75 for a in ANOS}),
    # O caso (b) usa prêmio de 1 ponto nos prefixados novos, contra 1,5 no (a): hipótese de anúncio
    # crível. A variante dá ao (b) o mesmo 1,5 do (a), para separar o efeito do corte do efeito do
    # prêmio. Referência do prêmio observado (13.4_coerencia.py): DI jan/29 cerca de 0,6 a 0,9 ponto
    # acima da Selic média esperada em 19-20/10/2026, antes do choque eleitoral; cerca de 3,3 em 26/10.
    "b_tau15": dict(CASOS["b"], nome="(b, prêmio 1,5) proposta na meta com o prêmio dos prefixados do caso (a)",
                    tau_p=1.5),
}
N_P, N_X = 3.0, 6.0                       # anos para o estoque prefixado e o de inflação vencerem


def ext(serie, ano):
    return serie.get(ano, serie[max(serie)])


def simular(c, n_p=N_P, n_x=N_X):
    cp, rx = CP0, RX0
    b = dict(B0)
    dg, dl, y = DG0, DL0, PIB0
    fx_nivel = 1.0
    k_out, k_res = K_OUT0, K_RES0
    linhas = []
    for t in ANOS:
        s, pi, gam = c["selic"][t], c["ipca"][t], c["pib"][t]
        dep = c["dolar"].get(t, 0.0)
        fut = [t, t + 1, t + 2]
        nova_p = sum(ext(c["selic"], a) for a in fut) / 3 + c["tau_p"]
        nova_x = sum(ext(c["selic"], a) - ext(c["ipca"], a) for a in fut) / 3 + c["tau_x"]
        cp = (1 - 1 / n_p) * cp + (1 / n_p) * nova_p
        rx = (1 - 1 / n_x) * rx + (1 / n_x) * nova_x
        cx = ((1 + rx / 100) * (1 + pi / 100) - 1) * 100
        custo = dict(F=s, P=cp, X=cx, C=CUSTO_CAM, O=s)
        partes = {k: b[k] * custo[k] / 100 for k in b}
        jg = sum(partes.values())
        y_ant = y
        y = y * (1 + gam / 100) * (1 + pi / 100)
        g = (y / y_ant - 1) * 100
        fx_nivel *= 1 + dep / 100
        k_out *= y / y_ant
        k_res = RES_USD * PTAX0 * fx_nivel * US_RATE / 100
        jl = jg - k_out - k_res
        deficit_prim = PRIM0 / 100 * y
        aj_g = b["C"] * dep / 100
        aj_l = -SENS_DLSP_FX * (dep / 10) / 100 * y
        dg_ant, dl_ant = dg, dl
        dg = dg + jg + deficit_prim + aj_g
        dl = dl + jl + deficit_prim + aj_l
        b = {k: W[k] * dg for k in W}
        b["C"] = W["C"] * dg  # participação constante
        atual = pi / 100 * dl_ant
        jr = jl - atual
        i_impl = jg / dg_ant * 100
        linhas.append(dict(
            ano=t, selic=s, ipca=pi, g=g, dep=dep, cp=cp, rx=rx, nova_p=nova_p, nova_x=nova_x,
            partes=partes, jg=jg, jl=jl, y=y, dg=dg / y * 100, dl=dl / y * 100,
            jl_pp=jl / y * 100, jg_pp=jg / y * 100, atual_pp=atual / y * 100, jr_pp=jr / y * 100,
            nominal_pp=jl / y * 100 + PRIM0, oper_pp=jr / y * 100 + PRIM0,
            i=i_impl, i_g=i_impl - g,
            r_g=((1 + i_impl / 100) / (1 + g / 100) - 1) * 100,
            sstar=(dg / y) * (i_impl - g) / (100 + g) * 100,
        ))
    return linhas


def r1(v):
    return round(v, 1)


def r2(v):
    return round(v, 2)


# ---------------------------------------------------------------- gráficos
FONTE_BASE = ("BCB, SGS 13762 (DBGG), 4513 (DLSP), 4382 (PIB), 5727 e 5793 (NFSP), 4390 (Selic) e "
              "13522 (IPCA), coleta de 02/11/2026; Focus de 23/10/2026 (API Olinda); Tesouro, RMD de "
              "ago/2026 (composição da DPF); simulação do painel (tools/analises/13.3_contas.py)")
NOTA_CASOS = ("Simulação, não previsão. Ponto de partida: set/2026. (a) Selic, IPCA e PIB das medianas "
              "do Focus de 23/10/2026. (b) Selic de 13,75% a 7,5% em 2027 (média de 10,6%), 7,5% em 2028, "
              "6,5% em 2029 e 5,5% (teto da faixa, sem o spread de segurança) de 2030 em diante; IPCA do Focus em 2027 e 3% depois. (c) Selic da "
              "proposta até 7,5%, mantida em 7,5%; IPCA de 6% a 7,5%; dólar 20% mais caro em 2027 e 10% "
              "em 2028; prêmio maior nos títulos novos. Crescimento real do Focus e déficit primário de "
              "0,52% do PIB nos três casos. Prefixados vencem em três anos e títulos de inflação em seis "
              "(hipótese do painel).")


def grafico_alivio(a, b):
    nomes = {"F": "LFT e compromissadas (Selic do dia)", "P": "Prefixados, ao vencer",
             "X": "Títulos de inflação, ao vencer"}
    series = []
    for k in ("F", "P", "X"):
        series.append({"nome": nomes[k], "pontos": [
            {"t": str(la["ano"]), "v": r1(la["partes"][k] - lb["partes"][k])} for la, lb in zip(a, b)]})
    return {
        "titulo": "Quanto a proposta reduz os juros brutos da dívida em relação à Selic do Focus, por tipo de título (R$ bilhões por ano)",
        "tipo": "empilhadas",
        "unidade": "R$ bi",
        "fonte": FONTE_BASE,
        "url": URL,
        "consulta": CONSULTA,
        "nota": "Diferença entre os juros da DBGG no caso (a), Selic do Focus, e no caso (b), proposta com inflação na meta, em reais correntes de cada caso. A parte flutuante reage no mês do corte; prefixados e títulos de inflação só quando vencem (hipótese: um terço dos prefixados e um sexto dos títulos de inflação por ano). Na parte de inflação entra também a inflação mais baixa do caso (b). " + NOTA_CASOS,
        "series": series,
    }


def grafico_linha(sims, campo, titulo, unidade, base, nota_extra):
    series = []
    for k in ("a", "b", "c"):
        pts = [{"t": "2026", "v": r2(base)}] + [{"t": str(l["ano"]), "v": r2(l[campo])} for l in sims[k]]
        series.append({"nome": CASOS[k]["nome"], "pontos": pts})
    return {
        "titulo": titulo,
        "tipo": "linha",
        "unidade": unidade,
        "fonte": FONTE_BASE,
        "url": URL,
        "consulta": CONSULTA,
        "nota": nota_extra + " O ponto de 2026 é o dado de set/2026 (12 meses ou fim de mês); os demais são fins de ano simulados. " + NOTA_CASOS,
        "series": series,
    }


def gravar(nome, obj):
    caminho = os.path.join(ROOT, "dados", nome)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("gravado", os.path.relpath(caminho, ROOT))


# ---------------------------------------------------------------- resumo impresso
def brinquedo():
    print("\nExemplo de brinquedo: dívida 100 = 60 flutuante + 40 prefixado a 12% (10 vencem por ano, refeitos a 9%)")
    sel = [14, 11, 8, 8, 8]
    pre_velho = 40
    for ano, s in enumerate(sel):
        if ano > 0:
            pre_velho -= 10
        custo = 60 * s / 100 + pre_velho * 0.12 + (40 - pre_velho) * 0.09
        print(f"  ano {ano}: Selic média {s:>2}; juros {custo:5.2f}; alívio {13.2 - custo:4.2f}")
    print("  ano 4 com inflação de 3%: juro real", 8.4 - 3.0, "; com inflação de 8%:", round(8.4 - 8.0, 1))


def resumo(sims):
    print(f"Partida set/2026: PIB R$ {PIB0:,.1f} bi; DBGG {DG0:,.0f} bi ({dbgg[K0]}%); DLSP {DL0:,.0f} bi ({dlsp[K0]}%)")
    print(f"  juros líquidos {JL0:,.1f} bi ({JL0_PP:.2f}% do PIB); NFSP nominal {nom[K0]}; primário {PRIM0}")
    print(f"  Selic efetiva 12m {SEL0:.2f}; IPCA 12m {PI0}")
    print("  blocos R$ bi:", {k: round(v) for k, v in B0.items()}, "participações:", {k: round(v * 100, 1) for k, v in W.items()})
    print(f"  custo da DBGG de set/2026 no ritmo atual: {I_IMPL0 / 100 * DG0:,.0f} bi ({I_IMPL0 * dbgg[K0] / 100:.2f}% do PIB)")
    print(f"  juros brutos de 12 meses {JG0:,.0f} bi ({JG0 / PIB0 * 100:.2f}% do PIB); juro real calibrado dos títulos de inflação {RX0:.2f}%")
    print(f"  K (ativos) {JG0 - JL0:,.0f} bi = reservas {K_RES0:,.0f} + outros {K_OUT0:,.0f}")
    print(f"  sensibilidade bruta da parte flutuante: R$ {B0['F'] / 100:.1f} bi por ponto (BCB, DLSP: 61,7; só LFT: {SH['lft'] * DPF / 100:.1f})")
    print(f"  conta direta: 6,25 × 61,7 = {6.25 * 61.7:.0f} bi = {6.25 * 61.7 / PIB0 * 100:.2f}% do PIB; "
          f"ano 1 (Selic média 10,625): {(13.75 - 10.625) * 61.7:.0f} bi")
    print(f"  conta do autor (resumos): 82,5 × 12,68% = {82.5 * 0.1268:.2f}; a 7,5%: {82.5 * 0.075:.2f}; diferença {82.5 * (0.1268 - 0.075):.2f}")
    print(f"  NFSP com Selic a 7,5% um ano inteiro, parte fixa intacta: juros {JL0_PP - 6.25 * 61.7 / PIB0 * 100:.2f}; "
          f"nominal {JL0_PP - 6.25 * 61.7 / PIB0 * 100 + PRIM0:.2f}")
    print(f"  reservas: R$ 19 bi por ponto × 6,25 = {19 * 6.25:.0f} bi; sobre 189,5: {(189.5 - 19 * 6.25):.0f} bi restam")
    det = dict(IF=31.22, previdencia=22.63, fundos=22.52, nao_res=9.91, outros=100 - 31.22 - 22.63 - 22.52 - 9.91)
    lft_al = SH["lft"] * DPF / 100 * 6.25
    comp_al = COMP / 100 * 6.25
    print(f"  alívio pleno: LFT {lft_al:.0f} bi + compromissadas {comp_al:.0f} bi")
    print("  LFT repartida pelas participações da DPMFi (ordem de grandeza):",
          {k: round(lft_al * v / 100) for k, v in det.items()})

    for k, lin in sims.items():
        nome = (CASOS.get(k) or VARIANTES[k])["nome"]
        print(f"\n{nome}")
        print(f"{'ano':5} {'Selic':>6} {'IPCA':>5} {'g':>5} {'i':>6} {'i-g':>6} {'r-g':>6} {'novaP':>6} {'novaX':>6} "
              f"{'JG%':>6} {'JL%':>6} {'atual':>6} {'jreal':>6} {'nomin':>6} {'oper':>6} {'DBGG':>6} {'DLSP':>6} {'s*':>5}")
        for l in lin:
            print(f"{l['ano']:5} {l['selic']:6.2f} {l['ipca']:5.2f} {l['g']:5.2f} {l['i']:6.2f} {l['i_g']:6.2f} {l['r_g']:6.2f} "
                  f"{l['nova_p']:6.2f} {l['nova_x']:6.2f} {l['jg_pp']:6.2f} {l['jl_pp']:6.2f} {l['atual_pp']:6.2f} "
                  f"{l['jr_pp']:6.2f} {l['nominal_pp']:6.2f} {l['oper_pp']:6.2f} {l['dg']:6.2f} {l['dl']:6.2f} {l['sstar']:5.2f}")

    a, b = sims["a"], sims["b"]
    print("\nAlívio de juros brutos, (a) − (b), R$ bi correntes e % do PIB de (b):")
    for la, lb in zip(a, b):
        d = {kk: la["partes"][kk] - lb["partes"][kk] for kk in la["partes"]}
        tot = la["jg"] - lb["jg"]
        print(f"  {la['ano']}: flutuante {d['F']:6.0f}  prefixados {d['P']:5.0f}  inflação {d['X']:5.0f}  outros {d['O'] + d['C']:4.0f}"
              f"  total {tot:6.0f} ({tot / lb['y'] * 100:.2f}% do PIB)   líquido {la['jl'] - lb['jl']:6.0f}")
    k = sims["k1375"]
    print("Alívio contra Selic parada em 13,75%:")
    for lk, lb in zip(k, b):
        print(f"  {lk['ano']}: total {lk['jg'] - lb['jg']:6.0f} bi; flutuante {lk['partes']['F'] - lb['partes']['F']:6.0f}; "
              f"% do PIB {(lk['jl_pp'] - lb['jl_pp']):.2f} (líquido)")

    bt = sims["b_tau15"]
    print("Alívio contra (a) com o caso (b) no mesmo prêmio de 1,5 ponto nos prefixados novos:")
    for la, lb, lt in zip(a, b, bt):
        print(f"  {la['ano']}: total {la['jg'] - lt['jg']:6.0f} bi ({(la['jg'] - lt['jg']) / lt['y'] * 100:.2f}% do PIB); "
              f"com prêmio de 1 ponto: {(la['jg'] - lb['jg']) / lb['y'] * 100:.2f}%; DBGG {lt['dg']:.1f} (b: {lb['dg']:.1f}); "
              f"nominal {lt['nominal_pp']:.2f} (b: {lb['nominal_pp']:.2f})")

    print("\nDecomposição do alívio de juros líquidos (p.p. do PIB) entre inflação (atualização) e juro real, contra a partida (8,99 = 2,76 + 6,23):")
    from_atual = 8.99 - 6.23
    for kk in ("a", "b", "c"):
        for l in sims[kk]:
            if l["ano"] in (2028, 2031):
                print(f"  {kk} {l['ano']}: juros {l['jl_pp']:.2f} (queda {JL0_PP - l['jl_pp']:.2f}); "
                      f"atualização {l['atual_pp']:.2f} (queda {from_atual - l['atual_pp']:.2f}); juro real {l['jr_pp']:.2f} "
                      f"(queda {6.23 - l['jr_pp']:.2f})")

    print("\nSensibilidade ao prazo (caso b, DBGG e juros líquidos em 2031):")
    for npp, nxx in ((3, 6), (4, 4), (2, 8), (5, 10)):
        l = simular(CASOS["b"], npp, nxx)[-1]
        la = simular(CASOS["a"], npp, nxx)[-1]
        print(f"  N_P={npp}, N_X={nxx}: DBGG b {l['dg']:.1f} (a {la['dg']:.1f}); juros líquidos b {l['jl_pp']:.2f}")


def main():
    sims = {k: simular(c) for k, c in CASOS.items()}
    sims.update({k: simular(c) for k, c in VARIANTES.items()})
    gravar("13.3-alivio-juros.json", grafico_alivio(sims["a"], sims["b"]))
    gravar("13.3-juros-nominais.json", grafico_linha(
        sims, "nominal_pp", "Déficit nominal do setor público nos três casos (NFSP, % do PIB)", "% do PIB",
        nom[K0], "Déficit nominal = juros líquidos simulados + déficit primário de 0,52% do PIB."))
    gravar("13.3-dbgg.json", grafico_linha(
        sims, "dg", "Dívida bruta do governo geral nos três casos (DBGG, conceito BCB, % do PIB)", "% do PIB",
        dbgg[K0], "Dívida bruta, conceito do BCB."))
    gravar("13.3-dlsp.json", grafico_linha(
        sims, "dl", "Dívida líquida do setor público nos três casos (DLSP, % do PIB)", "% do PIB",
        dlsp[K0], "Dívida líquida; no caso (c) a alta do dólar reduz a DLSP em 0,8 ponto do PIB por 10% (reservas maiores que a dívida em dólar, com swaps)."))
    if "--resumo" in sys.argv:
        brinquedo()
        resumo(sims)


if __name__ == "__main__":
    main()

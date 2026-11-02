#!/usr/bin/env python3
"""Fontes e bibliografia do painel (página 9.2), gerada a partir das próprias páginas.

Lê as seções "## Para ler" de todas as páginas (conteudo/*/*.md, ignorando pastas e arquivos que
começam com _ e a própria 9.2) e os campos "fonte" e "url" dos gráficos (dados/*.json). Classifica
cada referência em fonte primária (por instituição), literatura ou imprensa e outras fontes
secundárias, junta as citações da mesma obra feitas de formas diferentes, anota as páginas que
usam cada uma e grava conteudo/9-metodo/9.2-fontes-e-bibliografia.md. Só biblioteca padrão.

Uso:
    python3 tools/analises/9.2_bibliografia.py              # grava a página
    python3 tools/analises/9.2_bibliografia.py --relatorio  # grava e imprime contagens,
                                                            # divergências e referências incompletas
    python3 tools/analises/9.2_bibliografia.py --seco       # só imprime o relatório, não grava

Regras (cartão do item 9.3 do PLANO, parte "bibliografia"):
  - Mesma obra citada de formas diferentes vira uma entrada. Chave: sobrenome do primeiro autor +
    três primeiras palavras significativas do título (ALIAS cobre os casos que a chave não pega).
  - Se as citações divergem em ano, volume(número) ou páginas, vale a de página com
    "estado: revisada" (a mais completa entre elas); a divergência sai no relatório.
  - Nada é completado de fora: referência incompleta em todas as páginas fica incompleta e sai no
    relatório. A única fusão de campos é acrescentar o link de outra citação quando a escolhida
    não tem nenhum.
  - Fontes primárias: CATALOGO descreve os itens de cada instituição (descrição escrita à mão,
    páginas calculadas por expressão regular). O que não casa com nenhum item entra em "Outros
    documentos" da instituição e sai no relatório, para que a próxima rodada o cataloge.
  - Códigos do SGS e tabelas do SIDRA são extraídos do texto e das URLs; só entram os que têm
    descrição em SGS ou SIDRA (os demais saem no relatório).

Depois dos blocos 10 a 12, basta rodar de novo: as páginas novas entram sozinhas; obras novas que
a chave automática não juntar vão para ALIAS; fontes primárias novas, para CATALOGO.
"""
import glob
import json
import os
import re
import sys
import unicodedata
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTEUDO = os.path.join(ROOT, "conteudo")
DADOS = os.path.join(ROOT, "dados")
BRUTOS = os.path.join(DADOS, "brutos")
SAIDA = os.path.join(CONTEUDO, "9-metodo", "9.2-fontes-e-bibliografia.md")
PROPRIA = "9.2"
REPO = "https://github.com/r7carvalho/juros-convencao-brasil"

# --------------------------------------------------------------------------- utilidades


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    s = sem_acento(s).lower().replace("-", " ")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def id_key(pid):
    return [int(p) if p.isdigit() else 999 for p in str(pid).split(".")]


def links_paginas(pids):
    pids = sorted(set(pids), key=id_key)
    ls = [f"[{p}](pagina:{p})" for p in pids]
    if len(ls) <= 1:
        return "".join(ls)
    return ", ".join(ls[:-1]) + " e " + ls[-1]


RE_URL_MD = re.compile(r"\]\((https?://[^)\s]+)\)")
RE_URL_NU = re.compile(r"(?<![(\[])(https?://[^\s)\]]+)")


def urls(t):
    return RE_URL_MD.findall(t) + [u.rstrip(".,;") for u in RE_URL_NU.findall(t)]


def dominio(u):
    d = re.sub(r"^https?://", "", u).split("/")[0]
    return re.sub(r"^www\d?\.", "", d)


def limpar(t):
    """Normaliza uma referência para exibição: links nus viram Markdown, sem resíduo interno."""
    t = t.strip()
    t = re.sub(r"\s*\((?:via )?(?:insumo )?Frente [A-Z]\)", "", t)
    t = re.sub(r",? via insumo Frente [A-Z]", "", t)
    t = RE_URL_NU.sub(lambda m: f"[{dominio(m.group(1).rstrip('.,;'))}]({m.group(1).rstrip('.,;')})"
                      + m.group(1)[len(m.group(1).rstrip('.,;')):], t)
    t = re.sub(r"\[(https?://[^\]]+)\]\(", lambda m: "[" + dominio(m.group(1)) + "](", t)
    t = re.sub(r"\s+", " ", t).strip()
    if not t.endswith((".", ")")):
        t += "."
    if t.endswith(")") and not t.endswith(").") and re.search(r"\]\([^)]*\)$", t):
        t += "."
    return t


# --------------------------------------------------------------------------- leitura

class Ref:
    def __init__(self, pid, estado, texto):
        self.pid, self.estado, self.texto = pid, estado, texto.strip()
        self.revisada = estado == "revisada"


def ler_paginas():
    refs, existentes = [], set()
    for p in sorted(glob.glob(os.path.join(CONTEUDO, "*", "*.md"))):
        rel = os.path.relpath(p, CONTEUDO).split(os.sep)
        if any(x.startswith("_") for x in rel):
            continue
        txt = open(p, encoding="utf-8").read()
        m = re.search(r"^id:\s*(\S+)", txt, re.M)
        if not m:
            continue
        pid = m.group(1)
        if pid == PROPRIA:
            continue
        existentes.add(pid)
        est = re.search(r"^estado:\s*(.+?)\s*$", txt, re.M)
        sec = re.search(r"^## Para ler\s*\n(.*?)(?=^## |\Z)", txt, re.M | re.S)
        if not sec:
            continue
        for linha in sec.group(1).split("\n"):
            if linha.startswith("- "):
                refs.append(Ref(pid, est.group(1) if est else "", linha[2:]))
    return refs, existentes


def ler_graficos():
    out = []
    for p in sorted(glob.glob(os.path.join(DADOS, "*.json"))):
        nome = os.path.basename(p)
        pid = nome.split("-")[0]
        d = json.load(open(p, encoding="utf-8"))
        out.append((pid, nome, (d.get("fonte") or "") + " " + (d.get("url") or "")))
    return out


def ler_coleta():
    try:
        d = json.load(open(os.path.join(BRUTOS, "_coleta.json"), encoding="utf-8"))
    except OSError:
        return {}, 0, ""
    sgs = {}
    for x in d.get("ok", []):
        if x.get("grupo") == "sgs":
            cod, desc = x["nome"].split(" ", 1)
            sgs[cod] = desc
    n = len([f for f in os.listdir(BRUTOS) if not f.startswith("_")])
    return sgs, n, d.get("inicio", "")[:10]


# --------------------------------------------------------------------------- classificação

IGNORAR = [r"^Para o (contraponto|lado)", r"^Painel Alarmismo"]

LEGISLACAO = (r"^(Brasil\.|Lei\b|Lei Complementar|Decreto|Constituição|Emenda Constitucional|"
              r"Medida Provisória|Conselho Monetário Nacional|Conselho Nacional de Previdência|Previc\.|"
              r"Banco Central do Brasil\. (Resolução CMN|Circular 3\.086))")

INSTITUICOES = OrderedDict([
    ("bcb", ("Banco Central do Brasil", r"^(Banco Central do Brasil|BCB\b)")),
    ("ibge", ("IBGE", r"^IBGE\b")),
    ("tesouro", ("Tesouro Nacional", r"^(Tesouro Nacional|Secretaria do Tesouro Nacional)")),
    ("ifi", ("Instituição Fiscal Independente (IFI)", r"^(Instituição Fiscal Independente|IFI\b)")),
    ("ipea", ("Ipea", r"^(Ipea\b|Ipeadata)")),
    ("fgv", ("FGV IBRE", r"^(FGV IBRE|Observatório de Política Fiscal|CODACE|Blog do IBRE \(FGV\))")),
    ("bis", ("Banco de Compensações Internacionais (BIS)", r"^(Bank for International Settlements|BIS\.)")),
    ("fmi", ("Fundo Monetário Internacional (FMI)", r"^(FMI\b|Fundo Monetário Internacional|International Monetary Fund)")),
    ("bm", ("Banco Mundial", r"^(Banco Mundial\.|Organização Internacional do Trabalho)")),
    ("pwt", ("Penn World Table", r"^Penn World Table")),
    ("ext", ("Bancos centrais, tesouros e institutos de estatística de outros países",
             r"^(Federal Reserve|Board of Governors|Bureau of Labor|Bank of England|BCE\b|European Central Bank|"
             r"Banco Central da República da Turquia|Banco Central de la República|INDEC|TurkStat|US Treasury|"
             r"National Treasury|Ministerio de Finanzas|National Bureau of Economic Research\.)")),
    ("orgaos", ("Congresso, Receita Federal, BNDES e outros órgãos",
                r"^(Câmara dos Deputados|Senado Federal|Receita Federal|BNDES\.|Nações Unidas|TSE\b|Tribunal Superior Eleitoral)")),
    ("leg", ("Legislação e normas", LEGISLACAO)),
])

IMPRENSA = (r"^(Agência Brasil|Agência Senado|ADVFN|Aos Fatos|Associação Comercial|B3\b|BPMoney|"
            r"Buenos Aires Herald|Cadaminuto|CNN Brasil|Correio Braziliense|Estado de Minas|Exame|"
            r"Forbes Brasil|Gazeta do Povo|Giro S\.A\.|IHU|Il Sole 24 Ore|Imprensa usada|InfoMoney|"
            r"Jornal do Brasil|Jovem Pan|Metrópoles|NPR|OAB|Poder360|SBT News|Times Brasil|Vero Notícias|"
            r"\"Open letter|Idec|Instituto Mercado Popular|Instituto de Economia da Unicamp|"
            r"Holland, M\. \(20(18|26)\)|Kobori|Peter G\. Peterson|MoneYou)")

# veículos que aparecem só nas fontes dos gráficos
IMPRENSA_GRAFICOS = ["Estado de Minas", "InfoMoney", "Poder360", "Revista Oeste", "O Cafezinho",
                     "Cadaminuto", "Taxas do Tesouro", "Legismap", "Reuters", "Estadão", "Terra",
                     "Buenos Aires Herald", "Voz", "Statistics of the World", "Agência Brasil"]


def classificar(r):
    t = r.texto
    if any(re.search(p, t) for p in IGNORAR):
        return "ignorar"
    if re.search(LEGISLACAO, t):
        return "leg"
    for k, (_, rx) in INSTITUICOES.items():
        if k != "leg" and re.search(rx, t):
            return k
    if re.search(IMPRENSA, t):
        return "imprensa"
    return "lit"


# --------------------------------------------------------------------------- SGS e SIDRA

SGS = {
    "1": "Dólar comercial PTAX, venda, diário (R$/US$)",
    "7": "Ibovespa",
    "11": "Selic over diária (% a.d.)",
    "12": "CDI diário (% a.d.)",
    "432": "Selic meta definida pelo Copom (% a.a.)",
    "433": "IPCA, variação mensal (%)",
    "1178": "Selic over diária anualizada, base 252 (% a.a.)",
    "1635": "IPCA, alimentação e bebidas, variação mensal (%)",
    "3546": "Reservas internacionais, conceito liquidez (US$ milhões)",
    "3698": "Dólar PTAX, venda, média mensal (R$/US$)",
    "4189": "Selic acumulada no mês, anualizada, base 252 (% a.a.)",
    "4382": "PIB acumulado em 12 meses, valores correntes (R$ milhões)",
    "4390": "Selic acumulada no mês (% a.m.)",
    "4447": "IPCA, bens comercializáveis, variação mensal (%)",
    "4448": "IPCA, bens não comercializáveis, variação mensal (%)",
    "4449": "IPCA, preços monitorados, variação mensal (%)",
    "4513": "Dívida líquida do setor público (DLSP), % do PIB",
    "5727": "NFSP nominal do setor público consolidado, 12 meses, % do PIB",
    "5793": "NFSP primária do setor público consolidado, 12 meses, % do PIB",
    "7326": "PIB, variação real anual (%)",
    "10844": "IPCA, serviços, variação mensal (%)",
    "11428": "IPCA, itens livres, variação mensal (%)",
    "11752": "Taxa de câmbio real efetiva, deflator IPCA (jun/1994 = 100)",
    "13522": "IPCA acumulado em 12 meses (%)",
    "13761": "Dívida bruta do governo geral (DBGG), citada junto com a 13762",
    "13762": "Dívida bruta do governo geral (DBGG), % do PIB, conceito BCB",
    "20539": "Saldo da carteira de crédito, total (R$ milhões)",
    "20593": "Saldo da carteira de crédito com recursos direcionados (R$ milhões)",
    "20783": "Spread médio das operações de crédito, total (p.p.)",
    "24364": "IBC-Br com ajuste sazonal (índice)",
    "28964": "Depósitos voluntários remunerados no BCB, saldo (R$ mil)",
}

SIDRA = {
    "1419": "IPCA por grupos, subgrupos, itens e subitens, jan/2012 a dez/2019 (pesos e variações)",
    "1620": "Contas Nacionais Trimestrais, índice de volume sem ajuste sazonal",
    "1621": "Contas Nacionais Trimestrais, índice de volume com ajuste sazonal",
    "1737": "IPCA, série histórica (número-índice e variações mensal, anual e em 12 meses)",
    "1846": "Contas Nacionais Trimestrais, valores a preços correntes (óticas da produção e da despesa)",
    "4099": "PNAD Contínua, taxa de desocupação trimestral",
    "5436": "PNAD Contínua, rendimento médio real",
    "5932": "Contas Nacionais Trimestrais, taxas de variação",
    "7060": "IPCA por grupos, subgrupos, itens e subitens, desde jan/2020 (pesos e variações)",
    "8888": "Pesquisa Industrial Mensal, Produção Física",
}


def codigos_sgs(t):
    achados = set()
    for m in re.finditer(r"SGS", t):
        seg = t[m.end():m.end() + 400]
        seg = re.split(r"[Cc]onsulta|https?:|\]\(|; Focus|; Estat|; tabela|Focus|\. ", seg)[0]
        for n in re.finditer(r"(?<![\d/.,])(\d{1,5})(?!\d)(?![/.,]\d)(?!\s*(?:mes|ano|dia|ponto|p\.p))", seg):
            achados.add(n.group(1))
    achados.update(re.findall(r"bcdata\.sgs\.(\d+)", t))
    return achados


def tabelas_sidra(t):
    achados = set(re.findall(r"/t/(\d{3,4})/", t))
    achados.update(re.findall(r"sidra\.ibge\.gov\.br/tabela/(\d{3,4})", t))
    for m in re.finditer(r"(SIDRA|[Tt]abelas?)", t):
        seg = t[m.end():m.end() + 90]
        seg = re.split(r"[Cc]onsulta|https?:|\]\(|;|\. ", seg)[0]
        achados.update(re.findall(r"(?<![\d/.,])(\d{4})(?!\d)(?![/.,]\d)", seg))
    return achados


# --------------------------------------------------------------------------- catálogo primário
# (instituição, descrição em Markdown, regex sobre a referência ou a fonte do gráfico, modo)
# modo "item": uma linha com as páginas; "lista": uma linha e, abaixo, cada documento distinto.

BCB_SGSPUB = "https://www3.bcb.gov.br/sgspub"
CATALOGO = [
    ("bcb", "Sistema de Expectativas de Mercado (boletim Focus): medianas das projeções de instituições "
            "financeiras para IPCA, Selic e PIB, anuais e para 12 meses à frente. Séries completas pela API "
            "Olinda, que o coletor grava em `dados/brutos/focus-*.json`. "
            "[Focus](https://www.bcb.gov.br/publicacoes/focus); "
            "[API Olinda](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/aplicacao#!/recursos).",
     r"Focus|Olinda|Expectativas de Mercado", "item"),
    ("bcb", "Questionário Pré-Copom, inclusive o da 275ª reunião. "
            "[bcb.gov.br](https://www.bcb.gov.br/publicacoes/questionariopre-copom).",
     r"Pré-Copom", "item"),
    ("bcb", "Firmus, pesquisa de expectativas das empresas. [bcb.gov.br](https://www.bcb.gov.br/publicacoes/firmus).",
     r"Firmus", "item"),
    ("bcb", "Estatísticas fiscais: DBGG e DLSP, necessidades de financiamento do setor público (NFSP), "
            "tabela \"Dívida bruta do Governo Geral: fatores condicionantes\" (edições de setembro de 2008 a "
            "2026, consulta em 28/10/2026), tabela especial Divggnp.xlsx (DBGG nos conceitos BCB e FMI, "
            "operações compromissadas) e estimativa de sensibilidade da dívida líquida à Selic. "
            "[Estatísticas fiscais](https://www.bcb.gov.br/estatisticas/estatisticasfiscais); "
            "[Divggnp.xlsx](https://www.bcb.gov.br/content/estatisticas/Documents/Tabelas_especiais/Divggnp.xlsx); "
            "[tabelas de setembro de 2026](https://www.bcb.gov.br/content/estatisticas/hist_estatisticasfiscais/202609_Tabelas_de_estatisticas_fiscais.xlsx).",
     r"Estat[íi]sticas [Ff]iscais|Divggnp|fatores condicionantes|NFSP|sensibilidade|hist_estatisticasfiscais",
     "item", r"^\*?(Estat[íi]sticas [Ff]iscais|Tabela especial|NFSP)"),
    ("bcb", "Histórico das taxas de juros fixadas pelo Copom e atas das reuniões. "
            "[Histórico](https://www.bcb.gov.br/controleinflacao/historicotaxasjuros); "
            "[atas](https://www.bcb.gov.br/publicacoes/atascopom).",
     r"taxas de juros fixadas|[Hh]istórico das taxas|[Aa]tas? (da|das) reuni|historicotaxasjuros|atascopom", "item"),
    ("bcb", "Histórico das metas para a inflação (metas, intervalos e inflação observada). "
            "[bcb.gov.br](https://www.bcb.gov.br/controleinflacao/historicometas).",
     r"[Hh]istórico (de|das) metas|historicometas", "item"),
    ("bcb", "Relatório de Inflação (até 2024) e Relatório de Política Monetária (desde 2025), com os boxes "
            "anuais de decomposição da inflação. [bcb.gov.br](https://www.bcb.gov.br/publicacoes/rpm).",
     r"^(?!.*Estudo Especial)(?=.*(Relatórios? de (Inflação|Política Monetária)|\bRPM\b|\bRI\b|relatorioinflacao/20|relinf))",
     "lista", r"^\*?(Relatório de (Inflação|Política Monetária)|Boxes|Determinantes do prêmio|Repasse cambial)"),
    ("bcb", "Cartas abertas do presidente do BCB ao ministro da Fazenda sobre o descumprimento da meta. "
            "[bcb.gov.br](https://www.bcb.gov.br/controleinflacao/cartasabertas).",
     r"[Cc]artas? abertas?|carta_aberta|cartasabertas", "lista", r"^Cartas? aberta"),

    ("ibge", "Índice Nacional de Preços ao Consumidor Amplo (IPCA): notas metodológicas e série histórica. "
             "[ibge.gov.br](https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html); "
             "[série histórica](https://ftp.ibge.gov.br/Precos_Indices_de_Precos_ao_Consumidor/IPCA/Serie_Historica/).",
     r"Índices de Preços|Índice Nacional de Preços|Serie_Historica|9256", "item"),
    ("ibge", "Contas Nacionais Trimestrais (as tabelas usadas estão no quadro do SIDRA acima). "
             "[ibge.gov.br](https://www.ibge.gov.br/estatisticas/economicas/industria/9300-contas-nacionais-trimestrais.html).",
     r"Contas Nacionais Trimestrais", "item"),
    ("ibge", "Sistema de Contas Nacionais (anual): Tabela de Recursos e Usos, Contas Econômicas Integradas, "
             "notas metodológicas e divulgações. O coletor grava a listagem das tabelas de 2023 e a série do "
             "PIB real de 1947 a 2023 em `dados/brutos/scn/`.",
     r"Sistema de Contas Nacionais|Contas Econômicas Integradas|Contas Nacionais n\.|financeirização", "lista",
     r"^(Sistema de Contas Nacionais|Contas Nacionais n\.|Indicadores macroeconômicos de financeirização)"),

    ("tesouro", "Relatório Mensal da Dívida Pública Federal (RMD), sobretudo a edição de agosto de 2026, "
                "publicada em 28/09/2026, e a apresentação de março de 2026 com a série de detentores desde 2011. "
                "[Tesouro Transparente](https://www.tesourotransparente.gov.br/publicacoes/relatorio-mensal-da-divida-rmd/2026/8); "
                "cópias em [Texto_RMD_Ago_26.pdf](https://static.poder360.com.br/uploads/2026/09/Texto_RMD_Ago_26.pdf) e "
                "[Apresentacao-RMD-Marco.pdf](https://static.poder360.com.br/2026/04/Apresentacao-RMD-Marco.pdf).",
     r"Relatório Mensal da Dívida|\bRMD\b|relatorio-mensal|Texto_RMD", "item"),
    ("tesouro", "Plano Anual de Financiamento (PAF) 2026, de 28/01/2026, e revisão de 26/08/2026. "
                "[Tesouro Transparente](https://www.tesourotransparente.gov.br/publicacoes/plano-anual-de-financiamento-paf); "
                "cópia em [projecao-divida-paf-tesouro-28jan2026.pdf](https://static.poder360.com.br/2026/01/projecao-divida-paf-tesouro-28jan2026.pdf).",
     r"Plano Anual de Financiamento|\bPAF\b", "item"),
    ("tesouro", "Resultado do Tesouro Nacional (RTN), dezembro de 2025, apresentação. Cópia em "
                "[Tesouro-apresentacao-resultado-dez-25.pdf](https://static.poder360.com.br/2026/01/Tesouro-apresentacao-resultado-dez-25.pdf).",
     r"Resultado do Tesouro", "item"),

    ("ifi", "Relatório de Acompanhamento Fiscal (RAF), sobretudo o nº 117, de 29/10/2026, e o nº 113, de "
            "junho de 2026. [senado.leg.br/ifi](https://www12.senado.leg.br/ifi); "
            "[RAF 113](https://www12.senado.leg.br/ifi/pdf/raf113_jun2026.pdf).",
     r"Relatório de Acompanhamento Fiscal|\bRAF\b|senado\.leg\.br/ifi", "item"),

    ("ipea", "Ipeadata: EMBI+ Brasil (série JPM366_EMBI366, do JP Morgan) e estoque líquido de capital fixo "
             "e relação capital-produto (DIMAC_CFELCTOT, DIMAC_CFELCMQEQ, DIMAC_CFRCP). "
             "[ipeadata.gov.br](http://www.ipeadata.gov.br).",
     r"Ipeadata|ipeadata", "item"),

    ("fgv", "Boletim Macro, edição de setembro de 2026. [portalibre.fgv.br](https://portalibre.fgv.br/boletim-macro).",
     r"Boletim Macro", "item"),
    ("fgv", "Observatório de Política Fiscal: investimento público, série histórica 1947–2025. "
            "[observatorio-politica-fiscal.ibre.fgv.br](https://observatorio-politica-fiscal.ibre.fgv.br/series-historicas/investimentos-publicos/investimentos-publicos-serie-historica-1947-2025).",
     r"Observatório de Política Fiscal", "item"),
    ("fgv", "Comitê de Datação de Ciclos Econômicos (CODACE): pico no 1º trimestre de 2014, vale no 4º "
            "trimestre de 2016. [portalibre.fgv.br/codace](https://portalibre.fgv.br/codace).",
     r"CODACE", "item"),

    ("bis", "Taxas de política monetária (WS_CBPOL) e preços ao consumidor (WS_LONG_CPI), base do juro real "
            "comparado entre países. O coletor grava `dados/brutos/bis-politica_monetaria.csv` e "
            "`dados/brutos/bis-cpi.csv`. [data.bis.org](https://data.bis.org).",
     r"WS_CBPOL|WS_LONG_CPI|policy rates|data\.bis\.org|stats\.bis\.org", "item"),

    ("fmi", "DataMapper (World Economic Outlook de outubro de 2026 e Fiscal Monitor): dívida bruta "
            "(GGXWDG_NGDP), resultado primário (GGXONLB_G01_GDP_PT) e resultado nominal "
            "(GGXCNL_G01_GDP_PT) do governo geral, consulta em 28/10/2026. "
            "[imf.org/external/datamapper](https://www.imf.org/external/datamapper).",
     r"DataMapper|datamapper|GGX", "item"),

    ("bm", "World Development Indicators: formação bruta de capital fixo (NE.GDI.FTOT.ZS), poupança bruta "
           "(NY.GNS.ICTR.ZS), população de 15 a 64 anos e razão de dependência (SP.POP.1564.TO.ZS, "
           "SP.POP.DPND, a partir do World Population Prospects da ONU), saldo em transações correntes "
           "(BN.CAB.XOKA.GD.ZS) e PIB por ocupado (SL.GDP.PCAP.EM.KD, estimativa modelada da OIT). "
           "[data.worldbank.org](https://data.worldbank.org).",
     r"World Development Indicators|worldbank|NE\.GDI|NY\.GNS|SP\.POP|SL\.GDP|BN\.CAB|Organização Internacional", "item"),

    ("pwt", "Penn World Table, versões 10.0 (taxa interna de retorno real do capital, irr) e 11.0 (estoque "
            "de capital e PIB, rnna e rgdpna), Groningen Growth and Development Centre. "
            "[rug.nl/ggdc](https://www.rug.nl/ggdc/productivity/pwt/). A referência acadêmica é Feenstra, "
            "Inklaar e Timmer (2015), na Literatura.",
     r"Penn World Table|rug\.nl/ggdc", "item"),

    ("ext", "FRED, Federal Reserve Bank of St. Louis: base monetária (BOGMBASE) e M2 (M2SL) do Fed, "
            "velocidade de M2 (M2V), CPI-U do BLS (CPIAUCSL), núcleo do deflator do consumo do BEA "
            "(PCEPILFE) e rendimento real do TIPS de 10 anos (DFII10). [fred.stlouisfed.org](https://fred.stlouisfed.org).",
     r"FRED|fred\.stlouisfed", "item"),
    ("ext", "Metas de inflação de emergentes (gráfico de 10.1.2): Banco Central de Chile (IPoM), Banco de la "
            "República, Banxico, BCRP, governo da Índia (notificação de 25/03/2026), Tesouro da África do "
            "Sul e SARB (12/11/2025), Ministério das Finanças da Indonésia (PMK 31/2024), Banco da Rússia, "
            "Banco Central da Turquia, Fed (2012, 2025) e BCE (2021), consultados por busca.",
     r"Banxico|Banco Central de Chile", "item"),
    ("ext", "INDEC (Argentina), índice de preços ao consumidor. [indec.gob.ar](https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31).",
     r"INDEC", "item"),

    ("orgaos", "Balanço Geral da União de 2025: juros e encargos pagos pela União, em caixa (gráficos de 3.5).",
     r"\bBGU\b", "item"),
    ("orgaos", "BNDES, *Estudos especiais do BNDES 2025*: desembolsos em % do PIB, consulta em 28/10/2026. "
               "[PDF](https://web.bndes.gov.br/bib/jspui/bitstream/1408/28928/1/PRLiiv_216874_Estudos%20especiais%20do%20BNDES%202025_.pdf).",
     r"Estudos especiais do BNDES", "item"),
]

DESC_INST = {
    "bcb": "O BCB produz a maior parte dos dados do painel. As séries do Sistema Gerenciador de Séries "
           "Temporais (SGS) e do Focus vêm das APIs públicas (`api.bcb.gov.br` e `olinda.bcb.gov.br`) e "
           "estão em `dados/brutos/sgs-<código>.json` e `dados/brutos/focus-*.json`. Os códigos usados nas "
           "páginas e nos gráficos são estes ([portal do SGS]({sgspub})):",
    "ibge": "Os dados do IBGE vêm da API do SIDRA (`apisidra.ibge.gov.br`), gravados em "
            "`dados/brutos/sidra-*.json`, e do servidor de arquivos das Contas Nacionais. Parte das séries de "
            "preços chega pelo SGS do BCB, que reproduz o IPCA do IBGE (códigos 433, 13522 e agregados). "
            "Tabelas do SIDRA usadas ([sidra.ibge.gov.br](https://sidra.ibge.gov.br)):",
    "tesouro": "O coletor consulta o catálogo do Tesouro Transparente (`dados/brutos/tesouro-busca-*.json`) "
               "para localizar os arquivos do RMD, dos detentores e do resultado do Tesouro; os números do "
               "texto vêm dos relatórios abaixo.",
}

# --------------------------------------------------------------------------- literatura

STOP = set("the a an of and on in to for o os as um uma de do da dos das e em no na por para com "
           "le la les l du des et".split())

# Fusões que a chave automática não faz: prefixo do texto -> chave canônica
ALIAS = {
    "Keynes, J. M. (1936)": "keynes|1936",
    "Keynes, J. M. (1937)": "keynes|1937",
}

# Texto canônico escrito à mão quando as citações divergem só no capítulo citado
CANONICO = {
    "keynes|1936": "Keynes, J. M. (1936). *The General Theory of Employment, Interest and Money*. Londres: "
                   "Macmillan. Capítulos usados no painel: 7, 11, 12, 14, 15 e 17. Texto integral dos caps. 12 e "
                   "15 em [hetwebsite.net](https://www.hetwebsite.net/het/texts/keynes/gt/chap12.htm) e "
                   "[hetwebsite.net](https://www.hetwebsite.net/het/texts/keynes/gt/chap15.htm). Edição brasileira: "
                   "*A teoria geral do emprego, do juro e da moeda*, várias edições (Abril Cultural, Os Economistas; Saraiva).",
}

# Referências que o parser não marca como incompletas mas que o são em todas as citações
INCOMPLETAS_MANUAIS = {
    "pessoa|conjuntura economica": "sem título do artigo, só o veículo e o mês",
    "revista de economia politica|formacao distorcida precos": "sem autor e sem ano; só título e link",
    "sistema financeiro contas|ufrj repositorio pantheon": "sem autor e sem ano; só título e link",
    "yale program financial|fichas sobre linhas": "sem ano e sem títulos das fichas",
    "leite junior|dissertacao mestrado universidade": "sem título da dissertação",
    "tucker|artigo sobre solvencia": "sem título do artigo",
    "de mello|artigo para valor": "sem título do artigo",
    "lara resende|eu acuso proposta": "texto reproduzido; veículo original não registrado",
    "cemec fipe|notas sobre retorno": "sem ano e sem número das notas",
}


def separar_autor(t):
    m = re.search(r"\((\d{4}[a-z]?|s\.d\.)\)", t)
    if m and m.start() < 170:
        return t[:m.start()].strip().rstrip(".,"), m.group(1), t[m.end():].lstrip(".,: ").strip()
    if " et al. " in t[:60]:
        a, r = t.split(" et al. ", 1)
        return a + " et al.", None, r
    for m in re.finditer(r"\. ", t):
        prox = t[m.end():m.end() + 1]
        token = re.search(r"(\S+)$", t[:m.start()]).group(1)
        if prox in "\"*“" or len(token.strip("()")) > 2:
            return t[:m.start()].strip(), None, t[m.end():].strip()
    return t, None, ""


def extrair_titulo(resto):
    if not resto:
        return ""
    if resto[0] in "\"“":
        f = re.search(r"[\"”]", resto[1:])
        return resto[1:f.start() + 1] if f else resto[1:]
    if resto[0] == "*":
        f = resto.find("*", 1)
        return resto[1:f] if f > 0 else resto[1:]
    m = re.search(r"[.?](\s|$)", resto)
    return resto[:m.start()] if m else resto


def chave_lit(t):
    for pre, k in ALIAS.items():
        if t.startswith(pre):
            return k
    aut, ano, resto = separar_autor(t)
    sobrenome = norm(aut.split(",")[0].split(";")[0])
    tit = [w for w in norm(extrair_titulo(resto)).split() if w not in STOP]
    return sobrenome + "|" + " ".join(tit[:6])


RE_VOLNUM = re.compile(r"(?<![\d/])(\d{1,4})\s?\(([\w. ]{1,8})\)")
RE_PAGS = re.compile(r"^\s*[:,]?\s*(?:pp?\.\s*)?(\d+\s?[–-]\s?\d+|\d{5,})\b")


def campos(t):
    aut, ano, resto = separar_autor(t)
    vol = vn = pg = None
    fim_venue = resto.rfind("*")
    depois = resto[fim_venue + 1:] if fim_venue >= 0 else resto
    m = RE_VOLNUM.search(depois)
    if m and not re.fullmatch(r"\d{4}", m.group(2)):
        vol, vn = m.group(1), f"{m.group(1)}({m.group(2)})"
        p = RE_PAGS.match(depois[m.end():])
    else:
        mv = re.match(r"\s*[,.]?\s*(?:v\.\s*|vol\.\s*)?(\d{1,4})(?=[\s,:.;]|$)", depois) if fim_venue >= 0 else None
        p = None
        if mv and not re.fullmatch(r"(1[89]|20)\d\d", mv.group(1)):
            vol = mv.group(1)
            p = RE_PAGS.match(depois[mv.end():])
    if p:
        pg = re.sub(r"\s", "", p.group(1)).replace("-", "–")
    else:
        q = re.search(r"(?:\bpp?\.\s*|:\s*)(\d+[–-]\d+)", depois)
        if q:
            pg = q.group(1).replace("-", "–")
    return {"autor": aut, "ano": ano, "vol": vol, "volnum": vn, "pags": pg, "link": bool(urls(t))}


def formatar_lit(t):
    t = re.sub(r"(\*[^*]+\*)\s+(\d{1,4}\s?\()", r"\1, \2", t)
    t = re.sub(r"(\*[^*]+\*)\s+(\d{1,4})(?=[:,.]\s)", r"\1, \2", t)
    t = re.sub(r"(\d{1,4}\([^)]{1,8}\))\s*:\s*", r"\1, ", t)
    t = re.sub(r"(\*, \d{1,4}):\s*(\d+[–-]\d+)", r"\1, \2", t)
    t = re.sub(r"(Q[1-4]):\s*", r"\1, ", t)
    t = re.sub(r",\s*pp?\.\s*(\d+\s?[–-]\s?\d+)", r", \1", t)
    return limpar(t)


def tipo_artigo(t):
    """Artigo de periódico: título fora de itálico seguido de veículo em itálico, sem 'In:'."""
    aut, ano, resto = separar_autor(t)
    if not resto or resto.startswith("*"):
        return False
    if re.search(r"\bIn\b|\bEm \w|Terra é Redonda|Extra Classe|Agroanalysis|Central Banking|Boletim de Conjuntura|"
                 r"Economia em Perspectiva|Regional Economist|Encyclopaedia|Jackson Hole|Working Paper|\bWP\b|Texto para Discussão|\bTD\b|Discussion|Papers? \d|"
                 r"Nota|Mimeo|Blog|Folha|Valor|Substack|vídeo|Estudo|Working Document|Bulletin \d|BIS Bulletin|"
                 r"Staff|Technical|Brookings Papers|Macroeconomics Annual|Quarterly Bulletin|Economic Papers|"
                 r"Conferência|apresentad|publicado em", resto):
        return False
    return "*" in resto


def montar_literatura(refs):
    grupos = OrderedDict()
    for r in refs:
        grupos.setdefault(chave_lit(r.texto), []).append(r)
    # mesma obra com título abreviado numa página e completo noutra: o título curto é prefixo do longo
    for k in sorted(grupos, key=lambda x: len(x.split("|")[1].split())):
        if k not in grupos or k in CANONICO or k in ALIAS.values():
            continue
        sob, tit = k.split("|")
        ws = tit.split()
        if len(ws) < 2:
            continue
        for k2 in list(grupos):
            s2, t2 = k2.split("|")
            if k2 != k and s2 == sob and t2.split()[:len(ws)] == ws:
                grupos[k2] = grupos.pop(k) + grupos[k2]
                break
    obras, divergencias, incompletas = [], [], []
    for k, rs in grupos.items():
        cs = [(r, campos(r.texto)) for r in rs]
        cand = [x for x in cs if x[0].revisada] or cs
        cand.sort(key=lambda x: (x[1]["volnum"] is not None, x[1]["pags"] is not None, x[1]["link"],
                                 x[1]["ano"] is not None, len(x[0].texto)), reverse=True)
        esc, cf = cand[0]
        texto = CANONICO.get(k, esc.texto)
        if not cf["link"] and k not in CANONICO:
            for r, c in cs:
                if c["link"]:
                    us = RE_URL_MD.search(r.texto)
                    if us:
                        lab = re.search(r"\[([^\]]*)\]\(" + re.escape(us.group(1)), r.texto).group(1)
                        texto = texto.rstrip(". ") + f". [{lab}]({us.group(1)})"
                    else:
                        u = urls(r.texto)[0]
                        texto = texto.rstrip(". ") + f". {u}"
                    break
        pids = sorted({r.pid for r in rs}, key=id_key)
        # divergências
        div = []
        for campo, nome in (("ano", "ano"), ("volnum", "volume(número)"), ("pags", "páginas")):
            if k in CANONICO:
                break
            vals = defaultdict(set)
            for r, c in cs:
                if c[campo]:
                    vals[c[campo]].add(r.pid + ("*" if r.revisada else ""))
            if len(vals) > 1:
                div.append(f"{nome}: " + "; ".join(f"{v} ({', '.join(sorted(p, key=lambda x: id_key(x.rstrip('*'))))})"
                                                   for v, p in vals.items()) + f"; adotado {cf[campo] or 'nenhum'}")
        if div:
            divergencias.append((esc.texto[:90], div))
        # incompletude
        falta = []
        if all(c["ano"] is None for _, c in cs):
            falta.append("sem ano")
        if tipo_artigo(esc.texto):
            if all(c["vol"] is None for _, c in cs):
                falta.append("sem volume")
            if all(c["pags"] is None for _, c in cs):
                falta.append("sem páginas")
        for kk, motivo in INCOMPLETAS_MANUAIS.items():
            if k.startswith(kk.split("|")[0]) and kk.split("|")[1].split()[0] in k:
                falta.append(motivo)
        if falta:
            incompletas.append((esc.texto[:90], ", ".join(dict.fromkeys(falta)), pids))
        aut, ano, _ = separar_autor(texto)
        ordem = norm(aut) + " " + (ano or "9999")
        obras.append((ordem, formatar_lit(texto), pids, len(rs)))
    obras.sort(key=lambda x: x[0])
    return obras, divergencias, incompletas


# --------------------------------------------------------------------------- imprensa

def montar_imprensa(refs):
    grupos = OrderedDict()
    for r in refs:
        us = urls(r.texto)
        k = us[0] if us else norm(r.texto)[:80]
        grupos.setdefault(k, []).append(r)
    itens = []
    for k, rs in grupos.items():
        rs.sort(key=lambda r: (r.revisada, len(r.texto)), reverse=True)
        itens.append((norm(rs[0].texto.lstrip('"')), limpar(rs[0].texto), sorted({r.pid for r in rs}, key=id_key)))
    itens.sort(key=lambda x: x[0])
    return itens


# --------------------------------------------------------------------------- primárias

def sem_instituicao(inst, t):
    """Tira da referência o nome da instituição (e o ano) que abre o texto."""
    if inst not in ("bcb", "ibge", "tesouro", "ifi", "ipea", "bis", "fmi"):
        return t
    rx = INSTITUICOES[inst][1]
    m = re.match(rx + r"(?:\s*\(\d{4}\))?(?:[;,][^.]*)?\.\s+", t)
    return t[m.end():] if m else t


def montar_primarias(por_inst, graficos, todas, existentes):
    sec = OrderedDict((k, {"itens": [], "outros": []}) for k in INSTITUICOES)
    casadas = set()
    for item in CATALOGO:
        inst, desc, rx, modo = item[:4]
        principal = item[4] if len(item) > 4 else None
        pids, docs = set(), OrderedDict()
        for r in por_inst.get(inst, []):
            if re.search(rx, r.texto):
                pids.add(r.pid)
                if principal and not re.search(principal, sem_instituicao(inst, r.texto)):
                    continue          # citação composta: conta a página, mas o texto vai para "outros"
                casadas.add(id(r))
                if modo == "lista":
                    us = urls(r.texto)
                    k = us[0] if us else norm(r.texto)
                    docs.setdefault(k, []).append(r)
        for pid, nome, fonte in graficos:
            if re.search(rx, fonte) and pid in existentes:
                pids.add(pid)
        if pids:
            sub = []
            for k, rs in docs.items():
                rs.sort(key=lambda r: (r.revisada, len(r.texto)), reverse=True)
                sub.append((limpar(sem_instituicao(inst, rs[0].texto)), sorted({r.pid for r in rs}, key=id_key)))
            sec[inst]["itens"].append((desc, sorted(pids, key=id_key), sub))
    # SGS e SIDRA (todas as referências e gráficos)
    sgs_p, sidra_p, sgs_desconh, sidra_desconh = defaultdict(set), defaultdict(set), set(), set()
    for r in todas:
        cs = codigos_sgs(r.texto)
        for c in cs:
            (sgs_p[c].add(r.pid) if c in SGS else sgs_desconh.add(c))
        if cs & set(SGS) and r.texto.startswith(("Banco Central", "BCB")) and \
                re.match(r"(SGS|Séries temporais)", sem_instituicao("bcb", r.texto)) or \
                r.texto.startswith("IBGE. IPCA mensal, série SGS"):
            casadas.add(id(r))
        if r.texto.startswith("IBGE") or "SIDRA" in r.texto:
            ts = tabelas_sidra(r.texto)
            for c in ts:
                (sidra_p[c].add(r.pid) if c in SIDRA else sidra_desconh.add(c))
            if ts & set(SIDRA) and r.texto.startswith("IBGE"):
                casadas.add(id(r))
    for pid, nome, fonte in graficos:
        if pid not in existentes:
            continue
        for c in codigos_sgs(fonte):
            (sgs_p[c].add(pid) if c in SGS else sgs_desconh.add(c))
        if "SIDRA" in fonte or "apisidra" in fonte:
            for c in tabelas_sidra(fonte):
                (sidra_p[c].add(pid) if c in SIDRA else sidra_desconh.add(c))
    # outros documentos
    for inst, rs in por_inst.items():
        docs = OrderedDict()
        for r in rs:
            if id(r) in casadas:
                continue
            us = urls(r.texto)
            k = us[0] if us else norm(r.texto)
            docs.setdefault(k, []).append(r)
        for k, grp in docs.items():
            grp.sort(key=lambda r: (r.revisada, len(r.texto)), reverse=True)
            t = grp[0].texto if inst == "leg" else sem_instituicao(inst, grp[0].texto)
            sec[inst]["outros"].append((limpar(t), sorted({r.pid for r in grp}, key=id_key)))
        sec[inst]["outros"].sort(key=lambda x: norm(x[0]))
    return sec, sgs_p, sidra_p, sgs_desconh, sidra_desconh


# --------------------------------------------------------------------------- página

def gerar():
    refs, existentes = ler_paginas()
    graficos = ler_graficos()
    coleta_sgs, n_brutos, data_coleta = ler_coleta()
    por_tipo = defaultdict(list)
    for r in refs:
        por_tipo[classificar(r)].append(r)
    por_inst = {k: por_tipo[k] for k in INSTITUICOES}
    sec, sgs_p, sidra_p, sgs_desc, sidra_desc = montar_primarias(por_inst, graficos, refs, existentes)
    obras, divergencias, incompletas = montar_literatura(por_tipo["lit"])
    imprensa = montar_imprensa(por_tipo["imprensa"])

    # trabalhos para discussão e working papers de instituições, listados na literatura
    tds = defaultdict(list)
    for _, t, pids, _n in obras:
        aut, ano, _ = separar_autor(t)
        nomes = [x.split(",")[0].strip() for x in aut.split(";")]
        rot = (nomes[0] if len(nomes) == 1 else f"{nomes[0]} e {nomes[1]}" if len(nomes) == 2
               else f"{nomes[0]} et al.") + f" ({ano or 's.d.'})"
        if re.search(r"(BCB|Banco Central do Brasil)[^.]*(Working Paper|Trabalhos? para Discussão)|wps\d", t):
            tds["bcb"].append(rot)
        if re.search(r"Ipea[^.]*(TD|Texto para Discussão)|Ipea, TD", t):
            tds["ipea"].append(rot)
        if re.search(r"IFI, Estudo Especial", t):
            tds["ifi"].append(rot)
        if re.search(r"Tesouro Nacional, Texto para Discussão", t):
            tds["tesouro"].append(rot)
        if re.search(r"BIS (Working Papers|Economic Papers|Papers|Bulletin|Quarterly Review|Policy Papers)", t):
            tds["bis"].append(rot)
        if re.search(r"IMF (Working Paper|WP|SPN|Staff)|FMI, Technical", t):
            tds["fmi"].append(rot)
        if re.search(r"Blog do IBRE|Conjuntura Econômica|FGV IBRE", t):
            tds["fgv"].append(rot)

    def lista_nomes(xs):
        xs = list(dict.fromkeys(xs))
        return ", ".join(xs[:-1]) + " e " + xs[-1] if len(xs) > 1 else "".join(xs)

    n_itens_prim = 0
    corpo_prim = []
    for inst, (rot, _) in INSTITUICOES.items():
        s = sec[inst]
        tem = s["itens"] or s["outros"] or (inst == "bcb" and sgs_p) or (inst == "ibge" and sidra_p)
        if not tem:
            continue
        corpo_prim.append(f"### {rot}\n")
        if inst in DESC_INST:
            corpo_prim.append(DESC_INST[inst].format(sgspub=BCB_SGSPUB) + "\n")
        if inst == "bcb":
            corpo_prim.append("| Código | Série | Páginas |\n|---|---|---|")
            for c in sorted(sgs_p, key=int):
                corpo_prim.append(f"| {c} | {SGS[c]} | {links_paginas(sgs_p[c])} |")
            corpo_prim.append("")
            nao_cit = [c for c in sorted(coleta_sgs, key=int) if c not in sgs_p]
            if nao_cit:
                com = [f"{c} ({coleta_sgs[c]})" for c in nao_cit if "conferir" not in coleta_sgs[c]]
                sem = [c for c in nao_cit if "conferir" in coleta_sgs[c]]
                frase = "O acervo bruto tem ainda séries que nenhuma página cita por enquanto"
                if com:
                    frase += ": " + lista_nomes(com)
                if sem:
                    frase += ("; e os códigos " if com else ": os códigos ") + lista_nomes(sem) + \
                             ", cuja descrição o índice da coleta ainda marca para conferência pelo comportamento dos dados"
                corpo_prim.append(frase + ".\n")
            n_itens_prim += len(sgs_p)
        if inst == "ibge":
            corpo_prim.append("| Tabela | Conteúdo | Páginas |\n|---|---|---|")
            for c in sorted(sidra_p, key=int):
                corpo_prim.append(f"| {c} | {SIDRA[c]} | {links_paginas(sidra_p[c])} |")
            corpo_prim.append("")
            n_itens_prim += len(sidra_p)
        linhas = []
        for desc, pids, sub in s["itens"]:
            linhas.append(f"- {desc} Usado em {links_paginas(pids)}." + (" Citados:" if sub else ""))
            n_itens_prim += 1 if not sub else 0
            for t, ps in sub:
                linhas.append(f"  - {t} Em {links_paginas(ps)}.")
                n_itens_prim += 1
        if inst in tds:
            linhas.append(f"- Textos para discussão e estudos da instituição com autor identificado estão na "
                          f"Literatura, pelo nome do autor: {lista_nomes(tds[inst])}.")
        if linhas:
            corpo_prim.append("\n".join(linhas) + "\n")
        if s["outros"]:
            if linhas:
                corpo_prim.append("Outros documentos citados:\n")
            corpo_prim.append("\n".join(f"- {t} Usado em {links_paginas(ps)}." for t, ps in s["outros"]) + "\n")
            n_itens_prim += len(s["outros"])

    n_obras = len(obras)
    n_imp = len(imprensa)
    n_pag = len({r.pid for r in refs})
    n_graf = len([g for g in graficos if g[0] in existentes])

    # imprensa citada só nos gráficos
    imp_graf = defaultdict(set)
    for pid, nome, fonte in graficos:
        if pid not in existentes:
            continue
        for v in IMPRENSA_GRAFICOS:
            if re.search(r"\b" + re.escape(v) + r"\b", fonte):
                imp_graf[v].add(pid)

    resumo = (f"Reúne sem repetição as fontes que o painel cita: {n_itens_prim} fontes primárias de dados "
              f"agrupadas por instituição, com os códigos do SGS e as tabelas do SIDRA e as páginas que usam "
              f"cada um; {n_obras} obras de literatura em ordem alfabética, cada uma com as páginas que a "
              f"usam; e {n_imp} matérias de imprensa e outras fontes secundárias, separadas porque o painel só "
              f"recorre a elas quando não achou a fonte primária. Diz também onde ficam os dados brutos e como "
              f"são atualizados.")

    intro = f"""O painel cita {n_itens_prim} fontes primárias de dados, {n_obras} obras de literatura e {n_imp} matérias de imprensa ou outras fontes secundárias. Elas vêm das seções "Para ler" de {n_pag} páginas e das fontes declaradas em {n_graf} arquivos de dados de gráficos, e estão reunidas aqui sem repetição, cada uma com links para as páginas que a usam. Quando a mesma obra aparece citada de formas diferentes em páginas distintas, ficou uma entrada só, com a versão conferida na revisão daquelas páginas.

A ordem dos três blocos segue a hierarquia de fontes de [Método e regras de evidência](pagina:9.1). Primeiro vêm as fontes primárias: séries e documentos de órgãos oficiais e de organismos internacionais, além da legislação, agrupados pela instituição que os produz. O Banco Central e o IBGE ganham um quadro com os códigos do Sistema Gerenciador de Séries Temporais (SGS) e as tabelas do SIDRA, porque é por esses números que o leitor encontra a série na fonte e refaz a conta. Depois vem a literatura: livros, artigos, capítulos e textos para discussão com autor identificado, e estudos assinados por organizações (centrais sindicais, institutos de pesquisa privados, a Auditoria Cidadã da Dívida). Por último vêm a imprensa e as demais fontes secundárias.

Boa parte das séries primárias não foi transcrita à mão. Um coletor automático (`tools/coletar.py`), executado no GitHub Actions toda segunda-feira de manhã e também sob demanda, baixa das APIs oficiais do BCB (SGS e Olinda), do IBGE (SIDRA e servidor de arquivos das Contas Nacionais), do Tesouro Transparente e do BIS os dados brutos e os grava em [`dados/brutos/`]({REPO}/tree/main/dados/brutos), um arquivo por série, com a URL da API e a hora da coleta; o arquivo `_coleta.json` lista o que veio. A coleta usada nesta versão é a de {data_coleta[8:10]}/{data_coleta[5:7]}/{data_coleta[0:4]}, com {n_brutos} arquivos. Quando o coletor roda de novo, os gráficos calculados a partir do acervo podem ser refeitos pelos scripts de `tools/analises/`, e a data de consulta muda junto. Planilhas que a rede da produção não alcançava pela API (fatores condicionantes da dívida, tabela Divggnp do BCB, DataMapper do FMI, Ipeadata, Banco Mundial, relatórios do Tesouro) foram baixadas à mão, a maior parte em 28/10/2026, e cada gráfico informa a própria data.

A literatura está em ordem alfabética do sobrenome do primeiro autor, ou do nome da organização autora, no formato sobrenome, iniciais (ano), título, veículo, volume(número), páginas e link quando há. Os nomes seguem a forma abreviada usada nas páginas. Uma referência que chegou incompleta em todas as páginas que a citam ficou incompleta aqui: o painel não completa ano, volume ou página de memória.

A lista é gerada pelo script `tools/analises/9.2_bibliografia.py`, que lê as páginas e os arquivos de dados. Quando entram páginas novas, ele é rodado de novo e a contagem se atualiza."""

    corpo = [f"---\nid: 9.2\ntitulo: Fontes e bibliografia\npai: 9\nordem: 2\nresumo: {resumo}\nestado: 1ª versão\n---\n",
             intro + "\n",
             "## Fontes primárias de dados\n",
             "As fontes estão agrupadas pela instituição que produz o dado. Ao lado de cada uma vêm as páginas que a "
             "usam, no texto ou nos gráficos. Documentos de uma instituição que o painel cita sem que se encaixem nos "
             "itens principais aparecem logo abaixo deles.\n"]
    corpo += corpo_prim
    corpo.append("## Literatura\n")
    corpo.append("Livros, artigos, capítulos, textos para discussão e notas técnicas, com as páginas do painel "
                 "que usam cada obra.\n")
    corpo.append("\n".join(f"- {t} Citada em {links_paginas(p)}." for _, t, p, _n in obras) + "\n")
    corpo.append("## Imprensa e outras fontes secundárias\n")
    corpo.append("Matérias de jornal, revistas, portais, agências de notícias, blogs, vídeos e compilações de "
                 "terceiros. O painel só as usa quando não achou a fonte primária do número, ou quando a própria "
                 "declaração noticiada é o fato discutido; nesses casos a página diz de onde a matéria tira o dado.\n")
    corpo.append("\n".join(f"- {t} Citada em {links_paginas(p)}." for _, t, p in imprensa) + "\n")
    if imp_graf:
        partes = [f"{v} ({links_paginas(ps)})" for v, ps in sorted(imp_graf.items(), key=lambda x: norm(x[0]))]
        corpo.append("Alguns gráficos também tomam números de imprensa, indicados na fonte do próprio gráfico: "
                     + lista_nomes(partes) + ".\n")
    corpo.append("## Para ler\n")
    corpo.append(f"- Método e regras de evidência do painel: [9.1](pagina:9.1).\n"
                 f"- Acervo de dados brutos e índice da coleta: [{REPO.split('//')[1]}/dados/brutos]({REPO}/tree/main/dados/brutos).\n"
                 f"- Coletor: [tools/coletar.py]({REPO}/blob/main/tools/coletar.py); script desta lista: "
                 f"[tools/analises/9.2_bibliografia.py]({REPO}/blob/main/tools/analises/9.2_bibliografia.py).\n")
    texto = "\n".join(corpo)

    nao_cat = {inst: s["outros"] for inst, s in sec.items() if s["outros"]}
    rel = {
        "paginas": n_pag, "graficos": n_graf, "referencias": len(refs),
        "primarias": n_itens_prim, "sgs": len(sgs_p), "sidra": len(sidra_p),
        "obras": n_obras, "imprensa": n_imp, "ignoradas": [r.pid + ": " + r.texto[:70] for r in por_tipo["ignorar"]],
        "divergencias": divergencias, "incompletas": incompletas,
        "sgs_desconhecidos": sorted(c for c in sgs_desc if len(c) >= 3 and not re.fullmatch(r"(19|20)\d\d", c)),
        "sidra_desconhecidas": sorted(c for c in sidra_desc if not re.fullmatch(r"(19|20)\d\d", c)),
        "nao_catalogadas": {k: len(v) for k, v in nao_cat.items()},
        "fusoes": sum(1 for o in obras if o[3] > 1),
    }
    return texto, rel


def main():
    texto, rel = gerar()
    if "--seco" not in sys.argv:
        with open(SAIDA, "w", encoding="utf-8") as f:
            f.write(texto)
        print("gravado:", os.path.relpath(SAIDA, ROOT))
    if "--relatorio" in sys.argv or "--seco" in sys.argv:
        for k in ("paginas", "graficos", "referencias", "primarias", "sgs", "sidra", "obras", "fusoes", "imprensa"):
            print(f"{k}: {rel[k]}")
        print("ignoradas:", rel["ignoradas"])
        print("SGS sem descrição:", rel["sgs_desconhecidos"], "| SIDRA sem descrição:", rel["sidra_desconhecidas"])
        print("primárias fora do catálogo (em 'outros'):", rel["nao_catalogadas"])
        print(f"\nDIVERGÊNCIAS ({len(rel['divergencias'])})")
        for t, d in rel["divergencias"]:
            print(" -", t, "|", " / ".join(d))
        print(f"\nINCOMPLETAS ({len(rel['incompletas'])})")
        for t, f, p in rel["incompletas"]:
            print(" -", t, "|", f, "|", ",".join(p))


if __name__ == "__main__":
    main()

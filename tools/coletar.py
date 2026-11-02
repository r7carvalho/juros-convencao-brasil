#!/usr/bin/env python3
"""Coletor de dados primários do painel (só biblioteca padrão).

Baixa séries das APIs públicas e grava o bruto em dados/brutos/, com a URL e a data da coleta,
para que as páginas citem a fonte primária. Roda localmente ou no GitHub Actions
(.github/workflows/coletar-dados.yml).

    python3 tools/coletar.py                 # tudo
    python3 tools/coletar.py sgs sidra       # só alguns grupos
    python3 tools/coletar.py --listar        # mostra o catálogo

Grupos: sgs (BCB/SGS), focus (BCB/Olinda), sidra (IBGE/SIDRA), scn (IBGE/FTP, Sistema de Contas
Nacionais), tesouro (Tesouro Transparente/CKAN), bis (BIS/SDMX), ipea (Ipeadata).
Falhas não interrompem: o relatório final (dados/brutos/_coleta.json) diz o que veio e o que não.
"""
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRUTOS = os.path.join(ROOT, "dados", "brutos")
UA = "Mozilla/5.0 (painel juros-convencao-brasil; coleta de dados publicos)"
HOJE = date.today()

# ------------------------------------------------------------------ catálogo

# BCB SGS: código -> descrição. Os códigos marcados com (conferir) devem ter o nome checado na
# página da série (https://www3.bcb.gov.br/sgspub) na primeira coleta.
SGS = {
    432: "Selic meta definida pelo Copom (% a.a.)",
    11: "Selic over diária (% a.d.)",
    4189: "Selic acumulada no mês anualizada base 252 (% a.a.)",
    4390: "Selic acumulada no mês (% a.m.)",
    12: "CDI diário (% a.d.)",
    4391: "CDI acumulado no mês (% a.m.)",
    433: "IPCA, variação mensal (%)",
    13522: "IPCA, variação acumulada em 12 meses (%)",
    11428: "IPCA, itens livres, variação mensal (%)",
    4449: "IPCA, preços monitorados, variação mensal (%)",
    1635: "IPCA, alimentação e bebidas, variação mensal (%) (conferir)",
    10844: "IPCA, serviços, variação mensal (%) (conferir)",
    4447: "IPCA, comercializáveis, variação mensal (%) (conferir)",
    4448: "IPCA, não comercializáveis, variação mensal (%) (conferir)",
    11426: "IPCA, núcleo por exclusão EX0, variação mensal (%) (conferir)",
    4466: "IPCA, núcleo médias aparadas com suavização, variação mensal (%) (conferir)",
    189: "IGP-M, variação mensal (%)",
    1: "Dólar comercial PTAX venda, diário (R$/US$)",
    3698: "Dólar PTAX venda, média mensal (R$/US$)",
    11752: "Taxa de câmbio real efetiva, IPCA, índice jun/1994=100",
    3546: "Reservas internacionais, conceito liquidez, mensal (US$ milhões)",
    13762: "Dívida bruta do governo geral, % do PIB (conceito BCB)",
    4513: "Dívida líquida do setor público consolidado, % do PIB",
    5793: "NFSP primária do setor público consolidado, 12 meses, % do PIB",
    5727: "NFSP nominal do setor público consolidado, 12 meses, % do PIB",
    5839: "NFSP juros nominais do setor público consolidado, 12 meses, % do PIB (conferir)",
    4382: "PIB acumulado dos últimos 12 meses, valores correntes (R$ milhões)",
    4380: "PIB mensal, valores correntes (R$ milhões)",
    24364: "IBC-Br com ajuste sazonal, índice",
    20539: "Saldo da carteira de crédito, total (R$ milhões)",
    20593: "Saldo da carteira de crédito com recursos direcionados, total (R$ milhões)",
    20542: "Saldo da carteira de crédito com recursos livres, total (R$ milhões) (conferir)",
    20783: "Spread médio das operações de crédito, total (p.p.)",
    20714: "Taxa média de juros das operações de crédito, total (% a.a.) (conferir)",
    27815: "Base monetária ampliada?, saldo em fim de período (R$ mil) (conferir)",
    1788: "Base monetária restrita, saldo em fim de período (R$ milhões) (conferir)",
    1824: "Meios de pagamento M1, saldo em fim de período (R$ milhões) (conferir)",
    28964: "Base monetária ampliada, depósitos voluntários remunerados, saldo (conferir)",
    1178: "Taxa de juros de longo prazo, TJLP (% a.a.) (conferir)",
    24369: "Taxa de desocupação, PNAD Contínua (%) (conferir)",
    7326: "PIB, variação real anual (%) (conferir)",
}

FOCUS = {
    "anuais_ipca": "ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'IPCA'&$orderby=Data%20desc&$top=40000&$format=json",
    "anuais_selic": "ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'Selic'&$orderby=Data%20desc&$top=40000&$format=json",
    "anuais_pib": "ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'PIB%20Total'&$orderby=Data%20desc&$top=40000&$format=json",
    "inflacao_12m": "ExpectativasMercadoInflacao12Meses?$filter=Indicador%20eq%20'IPCA'&$orderby=Data%20desc&$top=40000&$format=json",
}
FOCUS_BASE = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/"

# IBGE SIDRA: nome -> caminho da API (https://apisidra.ibge.gov.br/values/...)
GRUPOS_IPCA = "7169,7170,7445,7486,7558,7625,7660,7712,7766,7786"  # geral e nove grupos
SIDRA = {
    "pib_trimestral_correntes": "/t/1846/n1/all/v/all/p/all/c11255/all",
    "pib_trimestral_volume": "/t/1620/n1/all/v/all/p/all/c11255/all",
    "pib_trimestral_taxas": "/t/5932/n1/all/v/all/p/all/c11255/all",
    "ipca_grupos_2020_hoje": f"/t/7060/n1/all/v/63,66,2265/p/all/c315/{GRUPOS_IPCA}",
    "ipca_grupos_2012_2019": f"/t/1419/n1/all/v/63,66,2265/p/all/c315/{GRUPOS_IPCA}",
    "ipca_grupos_2006_2011": f"/t/2938/n1/all/v/all/p/all/c315/{GRUPOS_IPCA}",
    "pnad_desocupacao": "/t/4099/n1/all/v/4099/p/all",
    "pnad_rendimento_real": "/t/5436/n1/all/v/5932/p/all",
}

# IBGE FTP: diretórios do Sistema de Contas Nacionais (TRU, CEI, tabelas sinóticas)
SCN_DIRS = [
    "https://ftp.ibge.gov.br/Contas_Nacionais/Sistema_de_Contas_Nacionais/2023/",
    "https://ftp.ibge.gov.br/Contas_Nacionais/Contas_Trimestrais/Tabelas_Completas/",
]
SCN_PROFUNDIDADE = 3
SCN_MAX_MB = 60

TESOURO_CKAN = "https://www.tesourotransparente.gov.br/ckan/api/3/action/package_search?rows=50&q="
TESOURO_BUSCAS = ["detentores", "divida publica federal estoque", "relatorio mensal da divida", "resultado do tesouro nacional"]

# BIS SDMX (stats.bis.org): taxas de política e CPI de vários países, mensal
BIS_PAISES = "BR+MX+CL+CO+IN+ZA+TR+US+XM+JP+GB+RU+ID"
BIS = {
    "politica_monetaria": f"https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/M.{BIS_PAISES}?format=csv",
    "cpi": f"https://stats.bis.org/api/v2/data/dataflow/BIS/WS_LONG_CPI/1.0/M.{BIS_PAISES}.771?format=csv",
}

# Ipeadata OData: códigos de série (estoque de capital etc.). Preencha com SERCODIGO conferido em
# http://www.ipeadata.gov.br. A coleta grava também a busca por palavra-chave para achar os códigos.
IPEA_BUSCAS = ["capital fixo", "estoque de capital", "taxa de investimento", "formação bruta de capital"]
IPEA_SERIES = []

# ------------------------------------------------------------------ rede

CTX = ssl.create_default_context()
for cand in (os.environ.get("SSL_CERT_FILE"), "/root/.ccr/ca-bundle.crt"):
    if cand and os.path.exists(cand):
        try:
            CTX.load_verify_locations(cand)
        except Exception:  # noqa
            pass


FALHAS_HOST = {}
LIMITE_HOST = 3  # depois de 3 falhas seguidas num host, desiste dele nesta execução


def baixar(url, tentativas=2, timeout=40, binario=False):
    host = urllib.parse.urlsplit(url).hostname
    if FALHAS_HOST.get(host, 0) >= LIMITE_HOST:
        raise RuntimeError(f"host {host} desativado nesta execução após {LIMITE_HOST} falhas seguidas")
    ultimo = None
    for k in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                dados = r.read()
                FALHAS_HOST[host] = 0
                return dados if binario else dados.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:  # resposta válida do servidor: não conta como host fora do ar
                raise RuntimeError(f"HTTPError: {e}")
            ultimo = e
            time.sleep(2 * (k + 1))
        except Exception as e:  # noqa
            ultimo = e
            time.sleep(2 * (k + 1))
    FALHAS_HOST[host] = FALHAS_HOST.get(host, 0) + 1
    raise RuntimeError(f"{type(ultimo).__name__}: {ultimo}")


def gravar(nome, obj):
    os.makedirs(BRUTOS, exist_ok=True)
    path = os.path.join(BRUTOS, nome)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    return os.path.relpath(path, ROOT)


def agora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


RELATORIO = {"inicio": agora(), "ok": [], "falhas": []}


def ok(grupo, nome, arquivo, n=None):
    RELATORIO["ok"].append({"grupo": grupo, "nome": nome, "arquivo": arquivo, "registros": n})
    print(f"  ok   {grupo:8} {nome}  ({n if n is not None else '-'})")


def falha(grupo, nome, url, e):
    RELATORIO["falhas"].append({"grupo": grupo, "nome": nome, "url": url, "erro": str(e)[:300]})
    print(f"  FALHA {grupo:8} {nome}: {str(e)[:160]}")


# ------------------------------------------------------------------ coletores

def coletar_sgs():
    # A API do SGS limita consultas de séries diárias a janelas de 10 anos; fatiamos tudo.
    for cod, desc in SGS.items():
        pontos, urls = [], []
        try:
            for ini in range(1980, HOJE.year + 1, 5):
                fim = min(ini + 4, HOJE.year)
                url = (f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{cod}/dados?formato=json"
                       f"&dataInicial=01/01/{ini}&dataFinal=31/12/{fim}")
                urls.append(url)
                try:
                    txt = baixar(url)
                except RuntimeError as e:
                    if "404" in str(e):  # série sem dados nessa janela
                        continue
                    raise
                if txt.strip().startswith("["):
                    pontos.extend(json.loads(txt))
                elif txt.strip():
                    RELATORIO.setdefault("avisos", []).append({"serie": cod, "url": url, "resposta": txt[:200]})
                time.sleep(0.3)
            if not pontos:
                raise RuntimeError("nenhum dado retornado")
            arq = gravar(f"sgs-{cod}.json", {
                "fonte": "Banco Central do Brasil, Sistema Gerenciador de Séries Temporais (SGS)",
                "serie": cod, "descricao": desc,
                "pagina": f"https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarGraficoPorId&hdOidSeriesSelecionadas={cod}",
                "url_api": urls[0].split("&dataInicial")[0], "coleta": agora(), "dados": pontos})
            ok("sgs", f"{cod} {desc}", arq, len(pontos))
        except Exception as e:  # noqa
            falha("sgs", f"{cod} {desc}", urls[-1] if urls else "", e)


def coletar_focus():
    for nome, q in FOCUS.items():
        url = FOCUS_BASE + q
        try:
            d = json.loads(baixar(url, timeout=120))
            arq = gravar(f"focus-{nome}.json", {"fonte": "Banco Central do Brasil, Sistema de Expectativas de Mercado (Focus), API Olinda",
                                                "url_api": url, "coleta": agora(), "dados": d.get("value", d)})
            ok("focus", nome, arq, len(d.get("value", [])))
        except Exception as e:  # noqa
            falha("focus", nome, url, e)


def coletar_sidra():
    for nome, caminho in SIDRA.items():
        url = "https://apisidra.ibge.gov.br/values" + caminho
        try:
            d = json.loads(baixar(url, timeout=180))
            arq = gravar(f"sidra-{nome}.json", {"fonte": "IBGE, SIDRA", "url_api": url, "coleta": agora(), "dados": d})
            ok("sidra", nome, arq, len(d) - 1 if isinstance(d, list) else None)
        except Exception as e:  # noqa
            falha("sidra", nome, url, e)


def coletar_scn():
    """Percorre os diretórios do FTP do IBGE (até SCN_PROFUNDIDADE níveis) e baixa planilhas e zips."""
    import re
    destino = os.path.join(BRUTOS, "scn")
    os.makedirs(destino, exist_ok=True)
    vistos, fila, listagem_total = set(), [(d, 0) for d in SCN_DIRS], []
    while fila:
        d, nivel = fila.pop(0)
        if d in vistos:
            continue
        vistos.add(d)
        try:
            listagem = baixar(d)
        except Exception as e:  # noqa
            falha("scn", d, d, e)
            continue
        hrefs = re.findall(r'href="([^"?#]+)"', listagem, re.I)
        for h in hrefs:
            url = urllib.parse.urljoin(d, h)
            if not url.startswith(d) or url == d:
                continue
            if url.endswith("/"):
                if nivel + 1 <= SCN_PROFUNDIDADE:
                    fila.append((url, nivel + 1))
                continue
            if not re.search(r"\.(zip|xls|xlsx|ods)$", url, re.I):
                continue
            listagem_total.append(url)
            rel = urllib.parse.unquote(url[len("https://ftp.ibge.gov.br/Contas_Nacionais/"):]).replace("/", "__")
            alvo = os.path.join(destino, rel)
            if os.path.exists(alvo):
                continue
            try:
                b = baixar(url, binario=True, timeout=300)
                if len(b) > SCN_MAX_MB * 1e6:
                    raise RuntimeError(f"arquivo grande demais ({len(b) / 1e6:.0f} MB)")
                with open(alvo, "wb") as f:
                    f.write(b)
                ok("scn", rel, os.path.relpath(alvo, ROOT), len(b))
            except Exception as e:  # noqa
                falha("scn", rel, url, e)
    gravar("scn-listagem.json", {"raizes": SCN_DIRS, "coleta": agora(), "arquivos": listagem_total})


def coletar_tesouro():
    for q in TESOURO_BUSCAS:
        url = TESOURO_CKAN + urllib.parse.quote(q)
        try:
            d = json.loads(baixar(url))
            pacotes = [{"nome": p.get("name"), "titulo": p.get("title"),
                        "recursos": [{"nome": r.get("name"), "url": r.get("url"), "formato": r.get("format")} for r in p.get("resources", [])]}
                       for p in d.get("result", {}).get("results", [])]
            arq = gravar(f"tesouro-busca-{q.replace(' ', '-')}.json", {"fonte": "Tesouro Transparente (CKAN)", "url_api": url, "coleta": agora(), "pacotes": pacotes})
            ok("tesouro", q, arq, len(pacotes))
        except Exception as e:  # noqa
            falha("tesouro", q, url, e)


def coletar_bis():
    for nome, url in BIS.items():
        try:
            txt = baixar(url, timeout=180)
            os.makedirs(BRUTOS, exist_ok=True)
            path = os.path.join(BRUTOS, f"bis-{nome}.csv")
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            ok("bis", nome, os.path.relpath(path, ROOT), txt.count("\n"))
        except Exception as e:  # noqa
            falha("bis", nome, url, e)


def coletar_ipea():
    # Baixa o catálogo inteiro de metadados e filtra localmente (o filtro OData dava 400).
    url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
    try:
        d = json.loads(baixar(url, timeout=180))
        todos = d.get("value", [])
        sel = [m for m in todos if any(q in (m.get("SERNOME") or "").lower() for q in IPEA_BUSCAS)]
        arq = gravar("ipea-metadados-selecionados.json", {"fonte": "Ipeadata", "url_api": url, "coleta": agora(),
                                                          "filtro": IPEA_BUSCAS, "dados": sel})
        ok("ipea", "metadados", arq, len(sel))
        for m in sel[:40]:
            IPEA_SERIES.append(m.get("SERCODIGO"))
    except Exception as e:  # noqa
        falha("ipea", "metadados", url, e)
    for cod in dict.fromkeys(c for c in IPEA_SERIES if c):
        url = f"http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{cod}')"
        try:
            d = json.loads(baixar(url, timeout=120))
            arq = gravar(f"ipea-{cod}.json", {"fonte": "Ipeadata", "url_api": url, "coleta": agora(), "dados": d.get("value", d)})
            ok("ipea", cod, arq, len(d.get("value", [])))
        except Exception as e:  # noqa
            falha("ipea", cod, url, e)


GRUPOS = {"sgs": coletar_sgs, "focus": coletar_focus, "sidra": coletar_sidra, "scn": coletar_scn,
          "tesouro": coletar_tesouro, "bis": coletar_bis, "ipea": coletar_ipea}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--listar" in sys.argv:
        for c, d in SGS.items():
            print(f"sgs {c}: {d}")
        for k, v in {**SIDRA}.items():
            print(f"sidra {k}: {v}")
        return
    escolhidos = args or list(GRUPOS)
    print("Diagnóstico de conectividade:")
    for h in ["https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json",
              "https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/63/p/last%201",
              "https://ftp.ibge.gov.br/", "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/",
              "https://stats.bis.org/api/v2/", "https://www.tesourotransparente.gov.br/ckan/api/3/action/site_read"]:
        try:
            txt = baixar(h, tentativas=1, timeout=20)
            print(f"  ok    {h}  -> {txt[:80]!r}")
        except Exception as e:  # noqa
            print(f"  falha {h}  -> {str(e)[:120]}")
    RELATORIO["diagnostico"] = {k: v for k, v in FALHAS_HOST.items()}
    FALHAS_HOST.clear()
    for g in escolhidos:
        print(f"[{g}]")
        GRUPOS[g]()
    RELATORIO["fim"] = agora()
    gravar("_coleta.json", RELATORIO)
    print(f"\n{len(RELATORIO['ok'])} itens coletados, {len(RELATORIO['falhas'])} falhas. Relatório em dados/brutos/_coleta.json")


if __name__ == "__main__":
    main()

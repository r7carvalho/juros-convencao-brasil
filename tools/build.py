#!/usr/bin/env python3
"""Build do painel "Juros, convenção e dívida no Brasil".

Lê conteudo/**/*.md (frontmatter + Markdown) e dados/*.json, gera HTML estático em docs/.
Só biblioteca padrão. Uso:
    python3 tools/build.py           # gera docs/
    python3 tools/build.py --check   # só valida e relata (não grava)
"""
import glob
import html
import json
import os
import re
import shutil
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTEUDO = os.environ.get("BUILD_CONTEUDO") or os.path.join(ROOT, "conteudo")
DADOS = os.path.join(ROOT, "dados")
DOCS = os.environ.get("BUILD_DOCS") or os.path.join(ROOT, "docs")
ASSETS_SRC = os.path.join(ROOT, "tools", "assets")
SITE_TITULO = "Juros, convenção e dívida no Brasil"
SITE_URL = "https://r7carvalho.github.io/juros-convencao-brasil/"
REPO_URL = "https://github.com/r7carvalho/juros-convencao-brasil"

AVISOS = []
ERROS = []


def aviso(msg):
    AVISOS.append(msg)


def erro(msg):
    ERROS.append(msg)


# ---------------------------------------------------------------- páginas

def id_key(pid):
    out = []
    for p in str(pid).split("."):
        out.append(int(p) if p.isdigit() else 999)
    return out


def parse_front(texto, path):
    if not texto.startswith("---"):
        erro(f"{path}: sem frontmatter")
        return {}, texto
    fim = texto.find("\n---", 3)
    if fim < 0:
        erro(f"{path}: frontmatter não fechado")
        return {}, texto
    bloco = texto[3:fim]
    corpo = texto[fim + 4:]
    corpo = corpo[corpo.find("\n") + 1:] if "\n" in corpo else ""
    meta, chave = {}, None
    for linha in bloco.splitlines():
        if not linha.strip():
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", linha)
        if m and not linha[:1].isspace():
            chave = m.group(1).strip().lower()
            v = m.group(2).strip()
            if v in (">", "|", ">-", "|-"):
                v = ""
            meta[chave] = v
        elif chave:
            meta[chave] = (meta[chave] + " " + linha.strip()).strip()
    for k, v in list(meta.items()):
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            meta[k] = v[1:-1]
    return meta, corpo


class Pagina:
    def __init__(self, path):
        self.src = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as f:
            texto = f.read().replace("\r\n", "\n")
        meta, corpo = parse_front(texto, self.src)
        self.id = str(meta.get("id", "")).strip()
        self.titulo = meta.get("titulo", "").strip()
        self.pai = str(meta.get("pai", "")).strip()
        try:
            self.ordem = float(meta.get("ordem", "0") or 0)
        except ValueError:
            self.ordem = 0
        self.resumo = meta.get("resumo", "").strip()
        self.estado = meta.get("estado", "").strip()
        self.corpo = corpo
        stem = os.path.splitext(os.path.basename(path))[0]
        self.arquivo = "index.html" if self.id == "0" else stem + ".html"
        self.filhos = []
        self.palavras = len(re.findall(r"\w+", corpo))
        if not self.id:
            erro(f"{self.src}: sem id")
        if not self.titulo:
            erro(f"{self.src}: sem titulo")
        if not self.resumo:
            aviso(f"{self.src}: sem resumo")


def carregar_paginas():
    paginas = {}
    for path in sorted(glob.glob(os.path.join(CONTEUDO, "**", "*.md"), recursive=True)):
        if os.path.basename(path).startswith("_"):
            continue
        p = Pagina(path)
        if not p.id:
            continue
        if p.id in paginas:
            erro(f"id {p.id} duplicado: {paginas[p.id].src} e {p.src}")
            continue
        paginas[p.id] = p
    if "0" not in paginas:
        aviso("página 0 (início) ausente: gerando uma provisória")
        p = Pagina.__new__(Pagina)
        p.src, p.id, p.titulo, p.pai, p.ordem = "(gerada)", "0", SITE_TITULO, "", 0
        p.resumo = "Mapa do painel."
        p.estado = ""
        p.corpo = "{{mapa}}\n"
        p.arquivo, p.filhos, p.palavras = "index.html", [], 0
        paginas["0"] = p
    for p in paginas.values():
        if p.id == "0":
            continue
        pai = paginas.get(p.pai)
        if pai is None:
            # sobe na árvore pelo id (1.4.1 -> 1.4 -> 1 -> 0)
            partes = p.id.split(".")
            cand = None
            while len(partes) > 1:
                partes = partes[:-1]
                if ".".join(partes) in paginas:
                    cand = ".".join(partes)
                    break
            cand = cand or "0"
            aviso(f"{p.src}: pai '{p.pai}' não existe; pendurado em {cand}")
            p.pai = cand
            pai = paginas[cand]
        pai.filhos.append(p)
    for p in paginas.values():
        p.filhos.sort(key=lambda c: (c.ordem, id_key(c.id)))
    return paginas


def preordem(raiz):
    out = [raiz]
    for f in raiz.filhos:
        out.extend(preordem(f))
    return out


def ancestrais(paginas, p):
    cadeia = []
    while p.id != "0":
        p = paginas[p.pai]
        cadeia.append(p)
    return list(reversed(cadeia))


# ---------------------------------------------------------------- gráficos

TIPOS = {"linha", "barras", "empilhadas", "barrash"}


def carregar_grafico(rel, pagina):
    rel = rel.strip()
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        erro(f"{pagina.src}: gráfico {rel} não existe")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            spec = json.load(f)
    except Exception as e:  # noqa
        erro(f"{rel}: JSON inválido ({e})")
        return None
    for k in ("titulo", "fonte", "consulta", "series"):
        if not spec.get(k):
            erro(f"{rel}: falta '{k}'")
            return None
    if spec.get("tipo", "linha") not in TIPOS:
        erro(f"{rel}: tipo '{spec.get('tipo')}' inválido")
        return None
    for s in spec["series"]:
        for pt in s.get("pontos", []):
            v = pt.get("v")
            if v is not None and not isinstance(v, (int, float)):
                erro(f"{rel}: valor não numérico em '{s.get('nome')}' {pt}")
                return None
            if spec.get("tipo", "linha") == "linha" and not re.match(r"^\d{4}(-(\d{1,2}|T[1-4]|Q[1-4]))?(-\d{1,2})?", str(pt.get("t", ""))):
                aviso(f"{rel}: data '{pt.get('t')}' não reconhecida em gráfico de linha")
    return spec


def fmt_num(v):
    if v is None:
        return "–"
    a = abs(v)
    casas = 0 if a >= 1000 else 1 if a >= 100 else 2
    s = f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if casas and "," in s:
        s = s.rstrip("0").rstrip(",")
    return s


def tabela_grafico(spec):
    series = spec["series"]
    ts = []
    for s in series:
        for pt in s.get("pontos", []):
            if pt.get("t") not in ts:
                ts.append(pt.get("t"))
    linhas = ["<table><thead><tr><th></th>" + "".join(
        f"<th>{html.escape(str(s.get('nome', '')))}</th>" for s in series) + "</tr></thead><tbody>"]
    idx = [{str(pt.get("t")): pt.get("v") for pt in s.get("pontos", [])} for s in series]
    for t in ts:
        linhas.append("<tr><th>" + html.escape(str(t)) + "</th>" + "".join(
            f"<td>{fmt_num(m.get(str(t)))}</td>" for m in idx) + "</tr>")
    linhas.append("</tbody></table>")
    return "".join(linhas)


GRAF_N = [0]


def render_grafico(rel, pagina):
    spec = carregar_grafico(rel, pagina)
    if spec is None:
        return f'<div class="box box-nota"><p>Gráfico indisponível: {html.escape(rel)}</p></div>'
    GRAF_N[0] += 1
    gid = f"g{GRAF_N[0]}"
    fonte = html.escape(spec["fonte"])
    url = spec.get("url")
    if url and re.match(r"^https?://", url):
        fonte = f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{fonte}</a>'
    nota = f' {inline(spec["nota"])}' if spec.get("nota") else ""
    dados_json = json.dumps(spec, ensure_ascii=False).replace("</", "<\\/")
    return (
        f'<figure class="grafico" id="{gid}">'
        f'<figcaption class="g-titulo">{html.escape(spec["titulo"])}</figcaption>'
        f'<div class="g-area" data-grafico="{gid}" role="img" aria-label="{html.escape(spec["titulo"])}"></div>'
        f'<script type="application/json" id="{gid}-dados">{dados_json}</script>'
        f'<p class="g-fonte">Fonte: {fonte}. Consulta em {html.escape(str(spec["consulta"]))}.{nota}</p>'
        f'<details class="g-tabela"><summary>Ver os dados em tabela</summary>'
        f'<div class="tabela-wrap">{tabela_grafico(spec)}</div></details>'
        f"</figure>"
    )


# ---------------------------------------------------------------- Markdown

PAGINAS = {}
PAGINA_ATUAL = [None]


def slug(t):
    t = re.sub(r"<[^>]+>", "", t).lower()
    trans = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçñ", "aaaaaeeeeiiiiooooouuuucn")
    t = t.translate(trans)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60] or "secao"


def resolver_pagina(pid):
    p = PAGINAS.get(pid.strip())
    if p is None:
        cur = PAGINA_ATUAL[0]
        erro(f"{cur.src if cur else '?'}: link para página inexistente '{pid}'")
        return "#"
    return p.arquivo


RE_CODE = re.compile(r"`([^`]+)`")
RE_MATH_D = re.compile(r"\$\$(.+?)\$\$")
RE_MATH_I = re.compile(r"(?<![\w$\\])\$(?=[^\s$])([^$\n]+?)(?<=[^\s\\])\$(?![\w$])")
RE_LINK = re.compile(r"\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")
RE_BOLD = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")
RE_ITAL = re.compile(r"(?<![\*\w])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\*\w])")
RE_AUTO = re.compile(r"&lt;(https?://[^\s&]+)&gt;")


def inline(texto):
    guard = []

    def guarda(s):
        guard.append(s)
        return f"\x00{len(guard) - 1}\x00"

    texto = RE_CODE.sub(lambda m: guarda(f"<code>{html.escape(m.group(1))}</code>"), texto)
    texto = RE_MATH_D.sub(lambda m: guarda(
        f'<span class="math" data-display="1">{html.escape(m.group(1))}</span>'), texto)
    texto = RE_MATH_I.sub(lambda m: guarda(
        f'<span class="math">{html.escape(m.group(1))}</span>'), texto)

    def link(m):
        rotulo, href = m.group(1), m.group(2)
        if href.startswith("pagina:"):
            alvo = href[7:]
            ancora = ""
            if "#" in alvo:
                alvo, ancora = alvo.split("#", 1)
                ancora = "#" + ancora
            return guarda(f'<a href="{resolver_pagina(alvo)}{html.escape(ancora)}">') + rotulo + guarda("</a>")
        if href.startswith("#"):
            return guarda(f'<a href="{html.escape(href)}">') + rotulo + guarda("</a>")
        return guarda(f'<a href="{html.escape(href)}" target="_blank" rel="noopener">') + rotulo + guarda("</a>")

    texto = RE_LINK.sub(link, texto)
    texto = html.escape(texto, quote=False)
    texto = RE_AUTO.sub(lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>', texto)
    texto = RE_BOLD.sub(r"<strong>\1</strong>", texto)
    texto = RE_ITAL.sub(r"<em>\1</em>", texto)
    for _ in range(3):
        texto = re.sub(r"\x00(\d+)\x00", lambda m: guard[int(m.group(1))], texto)
    return texto


RE_LISTA = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
RE_TITULO = re.compile(r"^(#{1,4})\s+(.*?)\s*#*$")
CAIXAS = {
    "exemplo": "Exemplo",
    "painel": "O painel lê",
    "afavor": "A favor",
    "contra": "Contra",
    "nota": "Nota",
}


def eh_inicio_bloco(linha, prox=None):
    s = linha.strip()
    if not s:
        return True
    if s.startswith(("```", "~~~", ":::", "$$", ">")):
        return True
    if RE_TITULO.match(s) or RE_LISTA.match(linha):
        return True
    if s.startswith("|") and prox is not None and re.match(r"^\s*\|?\s*:?-{2,}", prox or ""):
        return True
    if s == "{{mapa}}":
        return True
    return False


def render_tabela(linhas):
    def cel(l):
        l = l.strip()
        if l.startswith("|"):
            l = l[1:]
        if l.endswith("|"):
            l = l[:-1]
        # separa por | não escapado
        partes = re.split(r"(?<!\\)\|", l)
        return [p.strip().replace("\\|", "|") for p in partes]

    cab = cel(linhas[0])
    sep = cel(linhas[1])
    alin = []
    for s in sep:
        if s.startswith(":") and s.endswith(":"):
            alin.append("center")
        elif s.endswith(":"):
            alin.append("right")
        else:
            alin.append("")

    def attr(i):
        return f' style="text-align:{alin[i]}"' if i < len(alin) and alin[i] else ""

    out = ['<div class="tabela-wrap"><table><thead><tr>']
    out += [f"<th{attr(i)}>{inline(c)}</th>" for i, c in enumerate(cab)]
    out.append("</tr></thead><tbody>")
    for l in linhas[2:]:
        cs = cel(l)
        out.append("<tr>" + "".join(f"<td{attr(i)}>{inline(c)}</td>" for i, c in enumerate(cs)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_lista(linhas):
    """linhas: bloco de lista (pode ter subitens indentados e continuação)."""
    base = len(RE_LISTA.match(linhas[0]).group(1).expandtabs(4))
    ordenada = RE_LISTA.match(linhas[0]).group(2)[0].isdigit()
    itens, atual = [], None
    for l in linhas:
        m = RE_LISTA.match(l)
        ind = len(l) - len(l.lstrip(" ")) if l.strip() else 999
        if m and len(m.group(1).expandtabs(4)) <= base + 1:
            atual = [m.group(3)]
            itens.append(atual)
        elif atual is not None:
            atual.append(l[min(ind, base + 2):] if l.strip() else "")
    tag = "ol" if ordenada else "ul"
    inicio = ""
    if ordenada:
        n = int(re.match(r"\d+", RE_LISTA.match(linhas[0]).group(2)).group(0))
        if n != 1:
            inicio = f' start="{n}"'
    out = [f"<{tag}{inicio}>"]
    for it in itens:
        if len([x for x in it if x.strip()]) == 1 or not any(RE_LISTA.match(x) or x.strip() == "" for x in it[1:]):
            out.append("<li>" + inline(" ".join(x.strip() for x in it if x.strip())) + "</li>")
        else:
            # primeiro parágrafo inline, resto como blocos
            primeiro, resto = [it[0]], []
            i = 1
            while i < len(it) and it[i].strip() and not RE_LISTA.match(it[i]):
                primeiro.append(it[i].strip())
                i += 1
            resto = it[i:]
            out.append("<li>" + inline(" ".join(primeiro)) + render_blocos(resto) + "</li>")
    out.append(f"</{tag}>")
    return "".join(out)


def render_blocos(linhas):
    blocos = []  # (tipo, html)
    i, n = 0, len(linhas)
    while i < n:
        linha = linhas[i]
        s = linha.strip()
        if not s:
            i += 1
            continue
        # cercas de código
        if s.startswith("```") or s.startswith("~~~"):
            cerca = s[:3]
            lang = s[3:].strip().lower()
            j = i + 1
            cont = []
            while j < n and not linhas[j].strip().startswith(cerca):
                cont.append(linhas[j])
                j += 1
            i = j + 1
            if lang == "grafico":
                for rel in [c for c in cont if c.strip()]:
                    blocos.append(("graf", render_grafico(rel, PAGINA_ATUAL[0])))
            else:
                blocos.append(("pre", f"<pre><code>{html.escape(chr(10).join(cont))}</code></pre>"))
            continue
        # caixas :::
        if s.startswith(":::") and len(s) > 3:
            m = re.match(r"^:::\s*(\w+)\s*(.*)$", s)
            tipo = m.group(1).lower() if m else "nota"
            titulo = m.group(2).strip() if m else ""
            prof, j, cont = 1, i + 1, []
            while j < n:
                t = linhas[j].strip()
                if re.match(r"^:::\s*\w", t):
                    prof += 1
                elif t == ":::":
                    prof -= 1
                    if prof == 0:
                        break
                cont.append(linhas[j])
                j += 1
            if prof != 0:
                aviso(f"{PAGINA_ATUAL[0].src}: caixa :::{tipo} não fechada")
            i = j + 1
            if tipo not in CAIXAS:
                aviso(f"{PAGINA_ATUAL[0].src}: caixa :::{tipo} desconhecida")
            rot = CAIXAS.get(tipo, tipo.capitalize())
            cab = f'<div class="box-rotulo">{html.escape(rot)}</div>'
            if titulo:
                cab += f'<div class="box-titulo">{inline(titulo)}</div>'
            blocos.append((tipo, f'<div class="box box-{tipo}">{cab}{render_blocos(cont)}</div>'))
            continue
        if s == ":::":
            i += 1
            continue
        # fórmula em bloco
        if s.startswith("$$"):
            cont = s[2:]
            j = i
            if cont.rstrip().endswith("$$") and len(cont.strip()) >= 2:
                tex = cont.rstrip()[:-2]
            else:
                partes = [cont]
                j = i + 1
                while j < n and not linhas[j].rstrip().endswith("$$"):
                    partes.append(linhas[j])
                    j += 1
                if j < n:
                    partes.append(linhas[j].rstrip()[:-2])
                tex = "\n".join(partes)
            i = j + 1
            blocos.append(("math", f'<div class="math-bloco"><span class="math" data-display="1">{html.escape(tex.strip())}</span></div>'))
            continue
        if s == "{{mapa}}":
            blocos.append(("mapa", "{{MAPA}}"))
            i += 1
            continue
        m = RE_TITULO.match(s)
        if m:
            nivel = max(2, len(m.group(1)))
            txt = inline(m.group(2))
            blocos.append(("h", f'<h{nivel} id="{slug(txt)}">{txt}</h{nivel}>'))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            blocos.append(("hr", "<hr>"))
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", linhas[i + 1]):
            j = i
            cont = []
            while j < n and linhas[j].strip().startswith("|"):
                cont.append(linhas[j])
                j += 1
            i = j
            blocos.append(("tab", render_tabela(cont)))
            continue
        if s.startswith(">"):
            j = i
            cont = []
            while j < n and linhas[j].strip().startswith(">"):
                t = linhas[j].strip()[1:]
                cont.append(t[1:] if t.startswith(" ") else t)
                j += 1
            i = j
            ref = ""
            nao_vazias = [k for k, c in enumerate(cont) if c.strip()]
            if len(nao_vazias) >= 2:
                ult = cont[nao_vazias[-1]].strip()
                if ult.startswith("(") and ult.endswith(")"):
                    ref = f'<p class="ref">{inline(ult)}</p>'
                    cont = cont[:nao_vazias[-1]]
            blocos.append(("bq", f"<blockquote>{render_blocos(cont)}{ref}</blockquote>"))
            continue
        if RE_LISTA.match(linha):
            j = i
            cont = []
            while j < n:
                l = linhas[j]
                if not l.strip():
                    # continua se a próxima não-vazia for item ou indentada
                    k = j + 1
                    while k < n and not linhas[k].strip():
                        k += 1
                    if k < n and (RE_LISTA.match(linhas[k]) or linhas[k].startswith("  ")):
                        cont.append("")
                        j += 1
                        continue
                    break
                if cont and not RE_LISTA.match(l) and not l.startswith(" ") and eh_inicio_bloco(l, linhas[j + 1] if j + 1 < n else None):
                    break
                cont.append(l)
                j += 1
            i = j
            blocos.append(("lista", render_lista(cont)))
            continue
        # parágrafo
        j = i
        cont = []
        while j < n and linhas[j].strip():
            if cont and eh_inicio_bloco(linhas[j], linhas[j + 1] if j + 1 < n else None):
                break
            cont.append(linhas[j].strip())
            j += 1
        i = j
        blocos.append(("p", f"<p>{inline(' '.join(cont))}</p>"))
    # junta afavor + contra lado a lado
    out, k = [], 0
    while k < len(blocos):
        t, h = blocos[k]
        if t == "afavor" and k + 1 < len(blocos) and blocos[k + 1][0] == "contra":
            out.append(f'<div class="disputa">{h}{blocos[k + 1][1]}</div>')
            k += 2
            continue
        if t == "contra" and k + 1 < len(blocos) and blocos[k + 1][0] == "afavor":
            out.append(f'<div class="disputa">{blocos[k + 1][1]}{h}</div>')
            k += 2
            continue
        out.append(h)
        k += 1
    return "\n".join(out)


def markdown(texto):
    return render_blocos(texto.split("\n"))


# ---------------------------------------------------------------- páginas HTML

def nav_arvore(raiz, atual, caminho_ids):
    def item(p, nivel):
        cls = ' class="atual"' if p is atual else ""
        num = f'<span class="num">{p.id}</span> ' if p.id != "0" else ""
        a = f'<a href="{p.arquivo}"{cls}>{num}{html.escape(p.titulo)}</a>'
        if not p.filhos:
            return f"<li>{a}</li>"
        aberto = " open" if (p.id in caminho_ids or p is atual) else ""
        sub = "".join(item(f, nivel + 1) for f in p.filhos)
        return f'<li><details{aberto}><summary>{a}</summary><ul>{sub}</ul></details></li>'

    return "<ul class=\"arvore\">" + "".join(item(f, 1) for f in raiz.filhos) + "</ul>"


def mapa_html(raiz):
    def item(p):
        res = f'<span class="mapa-resumo">{inline(p.resumo)}</span>' if p.resumo else ""
        est = f' <span class="estado estado-{slug(p.estado)}">{html.escape(p.estado)}</span>' if p.estado else ""
        sub = f"<ul>{''.join(item(f) for f in p.filhos)}</ul>" if p.filhos else ""
        return (f'<li><a href="{p.arquivo}"><span class="num">{p.id}</span> {html.escape(p.titulo)}</a>'
                f"{est}{res}{sub}</li>")

    return '<nav class="mapa" aria-label="Mapa do painel"><ul>' + "".join(item(f) for f in raiz.filhos) + "</ul></nav>"


TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo_head}</title>
<meta name="description" content="{descricao}">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
<script>try{{var t=localStorage.getItem("tema");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
</head>
<body>
<header class="topo">
  <button class="btn-menu" type="button" aria-controls="lateral" aria-expanded="false">☰ <span>Mapa</span></button>
  <a class="marca" href="index.html">{site}</a>
  <button class="btn-tema" type="button" aria-label="Alternar tema claro ou escuro">◐</button>
</header>
<div class="layout">
<aside class="lateral" id="lateral" aria-label="Navegação">
  <a class="lateral-inicio{inicio_cls}" href="index.html">Início</a>
  {arvore}
</aside>
<main class="conteudo">
  <nav class="trilha" aria-label="Trilha">{trilha}</nav>
  <article>
    <h1>{num_titulo}{titulo}</h1>
    {resumo}
    {corpo}
    {filhos}
  </article>
  <nav class="pager" aria-label="Anterior e próxima">{pager}</nav>
  <footer class="rodape">
    <p>{site}. Revisão bibliográfica e evidência com fonte; textos e dados em
    <a href="{repo}" target="_blank" rel="noopener">{repo_curto}</a>. Página gerada em {hoje}
    a partir de <code>{src}</code>. Nenhum número entra sem fonte e data; onde o painel interpreta, ele diz.</p>
  </footer>
</main>
</div>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="assets/app.js"></script>
</body>
</html>
"""


def render_pagina(p, raiz, ordem_lin):
    PAGINA_ATUAL[0] = p
    GRAF_N[0] = 0
    anc = ancestrais(PAGINAS, p)
    caminho_ids = {a.id for a in anc}
    corpo = markdown(p.corpo)
    if "{{MAPA}}" in corpo:
        corpo = corpo.replace("{{MAPA}}", mapa_html(raiz))
    elif p.id == "0":
        corpo += "<h2 id=\"mapa\">Mapa do painel</h2>" + mapa_html(raiz)
    filhos = ""
    if p.filhos and p.id != "0":
        itens = "".join(
            f'<li><a href="{f.arquivo}"><span class="num">{f.id}</span> {html.escape(f.titulo)}</a>'
            f'{"<span class=\"mapa-resumo\">" + inline(f.resumo) + "</span>" if f.resumo else ""}</li>'
            for f in p.filhos)
        filhos = f'<section class="filhos"><h2 id="nesta-secao">Nesta seção</h2><ul class="mapa-lista">{itens}</ul></section>'
    trilha = " <span aria-hidden=\"true\">›</span> ".join(
        [f'<a href="{a.arquivo}">{html.escape("Início" if a.id == "0" else a.id + " " + a.titulo)}</a>' for a in anc]
        + [f'<span aria-current="page">{html.escape("Início" if p.id == "0" else p.id + " " + p.titulo)}</span>'])
    k = ordem_lin.index(p)
    ant = ordem_lin[k - 1] if k > 0 else None
    prox = ordem_lin[k + 1] if k + 1 < len(ordem_lin) else None
    pager = ""
    if ant:
        pager += f'<a class="ant" href="{ant.arquivo}"><span>Anterior</span>{html.escape(ant.id + " " + ant.titulo if ant.id != "0" else "Início")}</a>'
    if prox:
        pager += f'<a class="prox" href="{prox.arquivo}"><span>Próxima</span>{html.escape(prox.id + " " + prox.titulo)}</a>'
    resumo = f'<div class="resumo">{inline(p.resumo)}</div>' if p.resumo else ""
    descricao = re.sub(r"\s+", " ", re.sub(r"[*`$\[\]]|\(pagina:[^)]*\)", "", p.resumo))[:300]
    return TEMPLATE.format(
        titulo_head=html.escape(p.titulo if p.id == "0" else f"{p.id} {p.titulo} · {SITE_TITULO}"),
        descricao=html.escape(descricao),
        site=html.escape(SITE_TITULO),
        inicio_cls=" atual" if p.id == "0" else "",
        arvore=nav_arvore(raiz, p, caminho_ids),
        trilha=trilha,
        num_titulo="" if p.id == "0" else f'<span class="num">{p.id}</span> ',
        titulo=html.escape(p.titulo),
        resumo=resumo,
        corpo=corpo,
        filhos=filhos,
        pager=pager,
        repo=REPO_URL,
        repo_curto="github.com/r7carvalho/juros-convencao-brasil",
        hoje=date.today().strftime("%d/%m/%Y"),
        src=html.escape(p.src),
    )


def main():
    checar = "--check" in sys.argv
    global PAGINAS
    PAGINAS = carregar_paginas()
    raiz = PAGINAS["0"]
    ordem_lin = preordem(raiz)
    soltas = [p for p in PAGINAS.values() if p not in ordem_lin]
    for p in soltas:
        erro(f"{p.src}: página fora da árvore (ciclo de pais?)")
    saidas = {}
    for p in ordem_lin:
        saidas[p.arquivo] = render_pagina(p, raiz, ordem_lin)
    # relatório
    total = sum(p.palavras for p in ordem_lin)
    print(f"{len(ordem_lin)} páginas, {total:,} palavras".replace(",", "."))
    if "--palavras" in sys.argv:
        for p in ordem_lin:
            print(f"  {p.id:8} {p.palavras:6}  {p.titulo}")
    for a in AVISOS:
        print("AVISO:", a)
    for e in ERROS:
        print("ERRO:", e)
    if checar:
        sys.exit(1 if ERROS else 0)
    os.makedirs(DOCS, exist_ok=True)
    # limpa html antigos
    for f in glob.glob(os.path.join(DOCS, "*.html")):
        os.remove(f)
    for nome, conteudo in saidas.items():
        with open(os.path.join(DOCS, nome), "w", encoding="utf-8") as f:
            f.write(conteudo)
    destino = os.path.join(DOCS, "assets")
    os.makedirs(destino, exist_ok=True)
    for f in glob.glob(os.path.join(ASSETS_SRC, "*")):
        shutil.copy(f, destino)
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    print(f"gravado em {os.path.relpath(DOCS, ROOT)}/")


if __name__ == "__main__":
    main()

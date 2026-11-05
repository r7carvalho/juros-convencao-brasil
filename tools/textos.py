#!/usr/bin/env python3
"""Baixa páginas públicas (artigos, colunas, reportagens) e grava o texto em dados/brutos/textos/.

Roda no GitHub Actions (.github/workflows/textos.yml), porque a rede da sessão de nuvem bloqueia a
maior parte dos sites. Só biblioteca padrão. Páginas com paywall ou que recusam o acesso ficam
registradas com o erro.

Uso: python3 tools/textos.py URL1 URL2 ...   (ou um arquivo com uma URL por linha: --lista arq)
Saída: <slug>.json com url, título, data de coleta, status, texto extraído e o HTML bruto em .html.
"""
import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser

SAIDA = os.path.join("dados", "brutos", "textos")
UA = "Mozilla/5.0 (X11; Linux x86_64) painel-juros-convencao (coleta de textos publicos)"


class Extrator(HTMLParser):
    BLOCOS = {"p", "h1", "h2", "h3", "h4", "li", "blockquote", "br", "div", "section", "article"}
    IGNORAR = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form", "aside"}

    def __init__(self):
        super().__init__()
        self.partes, self.pilha_ign, self.titulo, self.no_titulo = [], 0, "", False
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.IGNORAR:
            self.pilha_ign += 1
        if tag == "title":
            self.no_titulo = True
        if tag == "meta":
            chave = a.get("property") or a.get("name") or ""
            if chave in ("og:title", "article:published_time", "og:site_name", "author",
                         "article:author", "description", "og:description", "date"):
                self.meta[chave] = a.get("content")
        if tag in self.BLOCOS:
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in self.IGNORAR and self.pilha_ign:
            self.pilha_ign -= 1
        if tag == "title":
            self.no_titulo = False
        if tag in self.BLOCOS:
            self.partes.append("\n")

    def handle_data(self, data):
        if self.no_titulo:
            self.titulo += data
        elif not self.pilha_ign:
            self.partes.append(data)

    def texto(self):
        t = html.unescape("".join(self.partes))
        linhas = [re.sub(r"\s+", " ", x).strip() for x in t.split("\n")]
        return "\n".join(x for x in linhas if len(x) > 1)


def slug(url):
    base = re.sub(r"^https?://(www\.)?", "", url)
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-")[:80]
    return base + "-" + hashlib.sha1(url.encode()).hexdigest()[:6]


def baixar(url):
    reg = {"url": url, "coleta": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}
    nome = slug(url)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "pt-BR,pt"})
        with urllib.request.urlopen(req, timeout=40) as r:
            reg["status"] = r.status
            reg["url_final"] = r.geturl()
            bruto = r.read()
            tipo = r.headers.get("Content-Type", "")
        if bruto[:5] == b"%PDF-" or "pdf" in tipo.lower():
            with open(os.path.join(SAIDA, nome + ".pdf"), "wb") as f:
                f.write(bruto)
            reg["tipo"] = "pdf"
            try:
                import io
                from pypdf import PdfReader
                leitor = PdfReader(io.BytesIO(bruto))
                paginas = [pg.extract_text() or "" for pg in leitor.pages]
                reg["paginas"] = len(paginas)
                reg["texto"] = "\n\n".join(f"[p. {i + 1}]\n{t}" for i, t in enumerate(paginas))
                reg["palavras"] = len(reg["texto"].split())
            except Exception as e:  # noqa: BLE001
                reg["erro_pdf"] = repr(e)[:300]
            with open(os.path.join(SAIDA, nome + ".json"), "w", encoding="utf-8") as f:
                json.dump(reg, f, ensure_ascii=False, indent=1)
            print(reg.get("status"), reg.get("palavras", 0), url, "pdf", flush=True)
            return
        cod = "utf-8"
        m = re.search(rb'charset=["\']?([\w-]+)', bruto[:3000])
        if m:
            cod = m.group(1).decode()
        doc = bruto.decode(cod, "replace")
        ex = Extrator()
        ex.feed(doc)
        reg["titulo"] = ex.titulo.strip()
        reg["meta"] = ex.meta
        reg["texto"] = ex.texto()
        reg["palavras"] = len(reg["texto"].split())
        with open(os.path.join(SAIDA, nome + ".html"), "w", encoding="utf-8") as f:
            f.write(doc)
    except Exception as e:  # noqa: BLE001
        reg["erro"] = repr(e)[:400]
    with open(os.path.join(SAIDA, nome + ".json"), "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    print(reg.get("status", "ERRO"), reg.get("palavras", 0), url, reg.get("erro", ""), flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("urls", nargs="*")
    p.add_argument("--lista")
    a = p.parse_args()
    urls = list(a.urls)
    if a.lista:
        with open(a.lista, encoding="utf-8") as f:
            urls += [x.strip() for x in f if x.strip() and not x.startswith("#")]
    os.makedirs(SAIDA, exist_ok=True)
    for u in urls:
        baixar(u)
        time.sleep(2)
    return 0


if __name__ == "__main__":
    sys.exit(main())

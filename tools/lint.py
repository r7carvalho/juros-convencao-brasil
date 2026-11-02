#!/usr/bin/env python3
"""Checagem mecânica de estilo e de regras do painel (complementa a revisão humana).

Uso: python3 tools/lint.py [arquivo.md ...]   (sem argumentos: todo conteudo/)
Relata, por página: palavras, travessões fora de citação, vocabulário vetado de ESTILO.md,
"não é X, é Y", metadiscurso, marcas [a conferir], parágrafos sem número de fonte etc.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VETADAS = [
    "crucial", "robusto", "robusta", "cenário", "jornada", "potencializar", "desafio",
    "fundamental", "nesse sentido", "vale destacar", "é importante ressaltar", "em suma",
    "vale ressaltar", "vale lembrar", "cabe destacar", "em resumo", "neste texto",
    "segue abaixo", "vamos entender", "configura-se", "apresenta-se como", "mergulhar",
    "panorama", "intrincad", "multifacetad", "pilar", "em última análise",
]
RE_NAO_E = re.compile(r"\bnão (?:é|foi|era|são)\b[^.;:]{1,60}[,;] (?:mas )?(?:é|foi|era|são)\b", re.I)


def checar(path):
    txt = open(path, encoding="utf-8").read()
    corpo = txt.split("\n---", 1)[1] if txt.startswith("---") else txt
    linhas = corpo.split("\n")
    sem_cit = "\n".join(l for l in linhas if not l.lstrip().startswith(">"))
    palavras = len(re.findall(r"\w+", corpo))
    trav = len(re.findall(r"\s—\s", sem_cit))
    achados = []
    low = sem_cit.lower()
    for v in VETADAS:
        n = len(re.findall(r"\b" + re.escape(v), low))
        if n:
            achados.append(f"{v}×{n}")
    nao_e = len(RE_NAO_E.findall(sem_cit))
    conferir = len(re.findall(r"\[a conferir", corpo, re.I))
    citacoes = len(re.findall(r"^>\s*[\"“]", corpo, re.M))
    graficos = corpo.count("```grafico")
    para_ler = "## Para ler" in corpo
    return dict(palavras=palavras, trav=trav, vet=achados, nao_e=nao_e, conferir=conferir,
                cit=citacoes, graf=graficos, para_ler=para_ler)


def main():
    arqs = sys.argv[1:] or sorted(
        p for p in glob.glob(os.path.join(ROOT, "conteudo", "**", "*.md"), recursive=True)
        if not any(x.startswith("_") for x in os.path.relpath(p, os.path.join(ROOT, "conteudo")).split(os.sep)))
    print(f"{'arquivo':48} {'pal':>6} {'—':>3} {'nãoé':>4} {'conf':>4} {'cit':>3} {'gráf':>4} PL  vetadas")
    for a in arqs:
        r = checar(a)
        nome = os.path.relpath(a, os.path.join(ROOT, "conteudo"))
        print(f"{nome[:48]:48} {r['palavras']:6} {r['trav']:3} {r['nao_e']:4} {r['conferir']:4} {r['cit']:3} "
              f"{r['graf']:4} {'sim' if r['para_ler'] else 'NÃO'} {' '.join(r['vet'])}")


if __name__ == "__main__":
    main()

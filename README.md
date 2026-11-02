# Juros, convenção e dívida no Brasil

Painel de revisão bibliográfica e evidência sobre por que os juros reais brasileiros estão entre os
mais altos do mundo. Testa a hipótese de que o patamar do juro virou convenção social e prendeu o
investimento, e apresenta com o mesmo rigor a leitura de dominância fiscal e prêmio de risco.

- `BRIEF.md`: o pedido e as regras de trabalho.
- `TOPOLOGIA.md`: a árvore de páginas.
- `CONTEXTO.md`: o debate que originou o painel e o que já foi corrigido.
- `ESTILO.md`: como se escreve aqui.
- `insumos/`: dados já levantados no painel irmão [Alarmismo × Fatos](https://r7carvalho.github.io/alarmismo-x-fatos/)
  (dívida, economia real, mercado e eleições, decomposição da dívida, juros, economia estrutural).
- `conteudo/`, `dados/`: o texto e os dados de cada página. `docs/`: o site gerado (GitHub Pages).

## Como gerar o site

```bash
python3 tools/build.py            # gera docs/ (só biblioteca padrão do Python 3.12+)
python3 tools/build.py --check    # valida frontmatter, gráficos e links sem gravar
python3 tools/build.py --check --palavras   # idem, com contagem de palavras por página
```

O formato das páginas (frontmatter, Markdown aceito, caixas, gráficos) está em
`conteudo/_CONVENCOES.md`. Os gráficos são desenhados no navegador a partir do JSON embutido em
cada página, com a tabela de dados sempre disponível como alternativa.

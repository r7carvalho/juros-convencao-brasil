# Relatório do coordenador

Estado em 02/11/2026. Site: https://r7carvalho.github.io/juros-convencao-brasil/ (GitHub Pages, `main:/docs`).
Este relatório é atualizado a cada rodada; a seção "Último item feito" no fim diz onde parar e retomar.

## O que está pronto

**96 páginas publicadas, cerca de 308 mil palavras e 109 gráficos**, em todas as macroáreas da
topologia original (0 a 9) e nos primeiros itens dos blocos novos (10 e 11) do `PLANO.md`.

| Área | Páginas | Palavras (aprox.) | Estado |
|---|---|---|---|
| 0 Início e "como ler" | 2 | 4.900 | 1ª versão (depende da conclusão) |
| 1 Fundamentos teóricos | 23 | 57.000 | revisadas |
| 2 Juros no Brasil | 7 | 27.000 | revisadas |
| 3 Dívida pública | 6 | 22.000 | revisadas |
| 4 Inflação | 6 | 24.000 | revisadas |
| 5 Investimento | 8 | 20.000 | revisadas |
| 6 Contrapontos ortodoxos | 14 | 35.000 | revisadas |
| 7 Caminhos de política | 10 | 31.000 | revisadas |
| 8 Conclusão e matriz | 2 | 9.700 | 1ª versão (refazer após blocos 10–12) |
| 9 Método, fontes, glossário, linha do tempo | 5 | 44.000 | 9.1, 9.3, 9.4 revisadas; 9.2 gerada por script |
| 10 Política monetária | 11 | 38.500 | 1ª versão (10, 10.1–10.1.2, 10.2–10.2.5; 10.2.6 em curso) |
| 11 Finanças públicas | 2 | 7.500 | 1ª versão (11 e 11.1 em curso) |

O contraponto ortodoxo (área 6) ficou mais extenso que qualquer área de 2 a 5, como o briefing pede.

**Revisão independente.** Cada área de 1 a 7 e a 9 foi lida por um revisor que não escreveu nada
(relatórios em `conteudo/_revisao/<área>.md`, 1.130 achados no total), e um corretor aplicou os
achados (cerca de 95%; os não aplicados têm o motivo registrado no topo de cada relatório).
Nenhuma pessoa privada é citada. As alusões à conversa de origem, as fontes internas ("Frente X",
"insumo") e as marcas "[a conferir]" foram retiradas do texto público.

**Dados primários.** A rede da sessão de nuvem bloqueia os sites oficiais. A solução foi um coletor
(`tools/coletar.py`) que roda no GitHub Actions (`.github/workflows/coletar-dados.yml`, toda
segunda e sob demanda) e grava em `dados/brutos/` o bruto das APIs: 45 séries do SGS do BCB, o
Focus pela API Olinda, tabelas do SIDRA (PIB trimestral pelas óticas, IPCA por grupo, PNAD), o BIS
(taxas de política e CPI de 13 países), o Tesouro (CKAN) e arquivos do IBGE. As revisões
conferiram contra esses brutos as séries que as páginas usam; as divergências e as decisões de
número estão em `conteudo/_divergencias.md`.

**Achados que a evidência impôs ao painel** (detalhe na matriz 8.1):
- O diferencial de juro real para os pares é real e grande: 6,6 p.p. em 2000–2009, 3,1 em
  2010–2019 e 5,5 em 2023–2026 (BIS); de 5 a 8 p.p. em 2003–2008, com superávit primário. Quase
  sumiu em 2018–2021.
- O Focus subestimou a inflação em média (1,0 p.p., 2002–2025): pesa contra a ideia de projeções
  enviesadas para cima.
- Em 2007–2019 o retorno do capital (PWT) superou o juro real; em 1995–1999 e 2003–2006 o juro
  ficou acima; em 2025–2026 quase empata.
- A inflação teve componente de demanda e de mercado de trabalho em 2011–2014 e 2024–2026 e foi
  sobretudo choque externo em 2002–2003 e 2020–2021.
- Os juros apropriados explicam cerca de 90% da alta da dívida bruta desde 2022.
- Há um resíduo de 2 a 4,5 p.p. no juro que nenhuma explicação medida fecha; convenção é candidata
  plausível, com confiança baixa.

## O que ficou raso ou sem fonte

- **Textos integrais não abertos.** Literatura e relatórios do BC citados por paráfrase quando o
  PDF não abriu (SciELO, BCB, NBER, sites dos autores). Recortes entre aspas só onde o texto foi
  visto. As listas por área estão em `conteudo/<área>/_notas.md`, seção "Pendências após a revisão"
  (cerca de 140 itens no total, 104 deles na área 9, sobretudo URLs de leis e datas finas).
- **Contas nacionais.** A TRU de 2023 está pelas Contas Trimestrais (SIDRA 1846). A CEI com juros
  (D.41) por setor institucional não foi coletada: a 5.4.3 usa o SCN 2020 e diz isso. O coletor foi
  ajustado para baixar o Sistema de Contas Nacionais 2023 do FTP do IBGE.
- **Boxes de decomposição da inflação do BC** (2015, 2022–2025): só os valores que apareceram em
  busca; a tabela completa não foi aberta.
- **Hiato do produto do BC** não está nos brutos; a 10.2.5 usa filtro HP no IBC-Br, declarado como
  aproximação.
- **Textos de 2026** (Lara Resende, "Eu acuso"; Oreiro): só paráfrase com link, sem aspas.
- **Gráficos de séries longas anteriores a 1999** (Selic meta antes do Copom, base monetária antes
  de 2001) ainda faltam.
- **Bloco 12 (vozes do debate)** não começou; a linha P9c (alarmismo) e parte da P8 da matriz
  dependem dele.

## O que fazer na próxima rodada

1. Seguir o `PLANO.md`: terminar o bloco 10 (10.2f, 10.3a–h, 10.4, 10.5, 10.R), o bloco 11
   (11.2 a 11.8, 11.R) e o bloco 12 (vozes do debate, com as regras próprias do bloco: só fala
   pública com link e data, princípio da caridade, mesmo tratamento para heterodoxos).
2. Refazer a conclusão (8 e 8.1) e a página inicial depois dos blocos 10 a 12; regenerar a 9.2 com
   `python3 tools/analises/9.2_bibliografia.py --relatorio`.
3. Passada de consistência entre áreas: aplicar em todas as páginas as decisões de
   `_divergencias.md` que ainda aparecem em páginas de outra área (lista em cada seção
   "Decisões da correção da área N"), sobretudo a convenção única do juro real ex-ante.
4. Coleta: SIDRA 1621 (FBCF dessazonalizada), CEI e TRU do SCN 2023, saldos de compulsório
   (SGS 1828, 1847–1849), TJLP/TLP (SGS 256, 27572), EMBI+ pelo Ipeadata. O coletor já tem esses
   itens; basta rodar o workflow.
5. Liberar na rede do ambiente os domínios oficiais (bcb.gov.br, ibge.gov.br, tesouro, IFI, BIS,
   FMI, SciELO) para abrir textos integrais e fechar as pendências de paráfrase.

## Como reproduzir

```bash
python3 tools/build.py            # gera docs/
python3 tools/build.py --check    # valida
python3 tools/lint.py             # vícios de estilo e resíduos de produção
python3 tools/coletar.py sgs      # coleta (precisa de rede aberta; ou rode o workflow no GitHub)
```

## Último item feito

Item 10.2e (regra de Taylor) e 11.0 publicados; 10.2f e 11.1 em execução; conclusão e página
inicial em 1ª versão.

## Identidades deduzidas

- Item 12.2b: o pedido por voz citava "Márcio … do INPE". Nenhum economista ligado ao INPE participa do debate de juros e dívida. A página 12.2.2 trata de **Marcos Lisboa** (ex-presidente do Insper, ex-secretário de Política Econômica da Fazenda, colunista da Folha), com confiança moderada: "Marcos" ≈ "Márcio", "Insper" ≈ "INPE", presença alta no debate de 2023–2026 e parceria com Samuel Pessôa, da mesma lista. Alternativa mais forte: Marcio Pochmann (ex-presidente do Ipea, presidente do IBGE desde 2023), nome exato e "Ipea" ≈ "INPE", sem fala recente localizada sobre Selic e dívida; se for ele, a página cabe no ramo 12.5. Também considerados Márcio Holland (FGV EESP) e Márcio Garcia (PUC-Rio). Detalhes em `conteudo/12-vozes/_notas.md`, seção 12.2b.

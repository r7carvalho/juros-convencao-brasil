# Notas da área 5: Investimento refém do juro

Primeira rodada de 02/11/2026; revisão independente (conteudo/_revisao/5.md, 102 achados) aplicada em
02/11/2026. A Penn World Table 10.0 foi relida do espelho do pacote R `pwt10` no GitHub
(raw.githubusercontent.com/cran/pwt10) com `pyreadr` no scratchpad. IBGE, Ipea, rug.nl, dataverse.nl,
Poder360 e o site do IEDI seguem bloqueados para fetch.

## Páginas (contagem do lint, que inclui tabelas, fórmulas e "Para ler")

| id | arquivo | palavras |
|---|---|---|
| 5 | 5-investimento-refem-do-juro.md | ~1.440 |
| 5.1 | 5.1-juro-real-x-retorno-do-capital.md | ~3.660 |
| 5.2 | 5.2-fbcf-capital-por-trabalhador.md | ~3.400 |
| 5.3 | 5.3-indexacao-das-decisoes.md | ~3.210 |
| 5.4 | 5.4-contas-nacionais.md | ~1.120 |
| 5.4.1 | 5.4.1-tabela-de-recursos-e-usos.md | ~2.740 (com duas tabelas novas) |
| 5.4.2 | 5.4.2-valor-adicionado-e-financas.md | ~2.740 (com tabela nova) |
| 5.4.3 | 5.4.3-contas-economicas-integradas.md | ~2.680 |

Gráficos próprios (11): 5.1-retorno-capital-x-juro-real (juro real agora de 1995 a 2026),
5.1-colchao-retorno-juro-paises, 5.2-taxa-de-investimento (dona da série FBCF/PIB),
5.2-fbcf-internacional, 5.2-capital-por-ocupado, 5.2-relacao-capital-produto, 5.3-desembolsos-bndes,
5.4.1-componentes-demanda, 5.4.2-financeiras-x-transformacao (série completa 1996–2026),
5.4.2-financas-e-juro-real (novo), 5.4.3-juros-setor-publico (set/2026).
Gráficos de outras áreas usados por JSON dono: 2.4-lft-na-dpf e 2.4-credito-direcionado (em 5.3),
3.3-detentores-ago2026 (em 5.4.3). Removidos: 5.3-direcionado-e-lft, 5.4.3-detentores-divida,
5.1-cemec-retorno-custo (duas observações, viraram linha de tabela).

## Dados calculados pelo painel (todos com consulta em 02/11/2026)

- Juro real ex-post dezembro a dezembro (SGS 4390 e 433): 1995 25,06; 1996 16,28; 1997 18,57; 1998 26,69;
  1999 15,28; ... 2025 9,66; 12 meses até set/2026 9,46. Contra a irr da PWT 10.0 (11,7 a 14,0 em
  1995–1999), o juro ficou 2,48 (1999) a 13,36 (1995) pontos acima.
- BIS, média de 2010–2019 do juro real de política (média dos meses): Brasil 3,93; México 1,04; Chile 0,45;
  Colômbia 0,83; Índia 0,79; África do Sul 0,86; EUA −1,13. Irr média 2010–2019 (PWT 10.0): 10,41; 11,84;
  11,45; 12,17; 11,57; 10,29; 7,44.
- SIDRA 1846: atividades financeiras no VA de 1996 a 2026 (9,3 em 1996; 6,0 em 2013; 5,8 em 2021; 8,5 em
  2025; 8,8 no 1º sem/2026). Correlação com o juro real ex-post: 0,77 (1996–2025) e 0,52 (2000–2025).
- Correlação juro real × FBCF/PIB: −0,18 (nível, 2000–2025), −0,11 (defasagem de um ano), −0,36 (variação
  anual da taxa de investimento, 2001–2025).
- TRU 2023 pela ótica da despesa (SIDRA 1846, R$ bi): C 6.886,0; G 2.083,9; FBCF 1.795,9; ΔE −71,2;
  X 1.966,4; M 1.717,8; VA 9.558,6; impostos 1.384,8; PIB 10.943,3.
- Juros nominais do setor público, 12 meses até set/2026: 8,99% do PIB, R$ 1.204,8 bi (SGS 5727 − 5793;
  4382).

## Divergências de número

1. Participação das finanças no VA: fechada com o SIDRA 1846 (divergência nº 15 de _divergencias.md).
2. K/Y: Ipea (2,04 em 2025, queda desde 2016) contra PWT 11.0 (4,37 em 2019 e 2023). A 5.1 mostra as duas
   leituras na estimativa da folga de 2025–2026.
3. Juro real do setor público em 2025: 5,5% do PIB (área 3). O número de 5,3% sem fonte saiu da 5.4.3.
4. Juro real médio de 2010–2019: 3,9% (BIS) ou 3,8% (SGS, dezembro a dezembro); a 5.1 diz qual usa.
5. Exemplo I/Y = (δ + n + k)·K/Y em 5.2 sugere aprofundamento do capital com 16,8% do PIB; o Ipea mostra
   capital por ocupado caindo 0,8% a.a. em 2022–2025. A conciliação não foi quantificada.

## Pendências após a revisão

- 5.1: irr de 2020–2023 na PWT 11.0 (rug.nl e dataverse bloqueados); com ela, a estimativa da folga de
  2025–2026 deixa de depender do K/Y.
- 5.1: retirados por falta de fonte localizada: ROE de 27,5% do IEDI em 2003; Carta IEDI n. 1375 e as
  margens industriais de 2014, 2018, 2019, 2023, 2024 e 2025; "37,4% do nível de 1950" (Marquetti et al.);
  rendimento líquido da Selic de ~3,9% na Nota CEMEC-FIPE 09/2020; significância do juro real em
  Luporini e Alves (2010). Avritzer, Freitas e Braga (2021) não localizado; substituído por Braga (2020),
  *Review of Keynesian Economics* 8(3), confirmado por busca.
- 5.1: ROE de 15,6% (3º tri 2024) segue com a CNN Brasil como fonte; falta nomear quem consolidou os balanços
  e o conceito (anualizado ou 12 meses). Grazziotin, Fornari e Marquetti sem ano (s.d.).
- 5.1: spread de pessoas jurídicas (SGS a coletar) para trocar o spread total no argumento do WACC.
- 5.2: repetro como componente do pico de 2021–2022 (falta a nota do IBGE); estoque de capital público de 35%
  do PIB e o grupo de comparação no PIMA do FMI (2018), com página.
- 5.2 e 4.3: o pico da FBCF no 2º tri de 2013 depende da série com ajuste sazonal (SIDRA 1621, não coletada);
  no SIDRA 1620 sem ajuste o pico é o 3º tri de 2013 e a queda até o 4º tri de 2016 é de 32,8%.
- 5.3: TJLP trimestral de 2010 a 2017 (SGS 256, não coletado; o SGS 1178 do coletor é a Selic, não a
  TJLP); participação das debêntures indexadas ao DI (ANBIMA); distribuição das metas atuariais dos fundos
  (Previc). A faixa "IPCA mais 4% a 6%" saiu do texto; ficou o corredor das Portarias Previc 343/2025 e
  324/2026 (vértice de 1 ano), confirmado por busca.
- 5.4.1: produção e consumo intermediário da TRU 2023: resolvido no refino com o SCN 2023 (seção abaixo).
- 5.4.3: D.41 pago e recebido por setor institucional na CEI, D.44 e saldo de renda primária; a edição de 2023
  do SCN no FTP não traz a CEI (ver "Refino com SCN 2023"); a página segue com o dado por setor do SCN 2020
  (capacidade de financiamento das financeiras em 2019 e 2020) e diz que ele vale só para esses anos.

## Achados da revisão não aplicados ou aplicados de outro modo

- Cartão do coordenador fala em "3 a 13 p.p." para 1995–1999; o texto usa 2,5 a 13,4, porque 1999 dá 2,48.
- 5.1 nº 9 e macro nº 4: "3 a 5 pontos" aplicado; com os valores sem arredondar a distância é de 3,0 a 4,9.
- 5.1 nº 17 e macro nº 9: com a retirada dos pontos de 2003 (IEDI) e 2025 (Carta 1375), a tabela das
  empresas tem seis pontos, e o texto diz "três dos seis".
- 5.1 nº 19: spread de PJ não está nos brutos; mantido o total com a ressalva de que superestima.
- 5.4.3 nº 9: o gráfico de juros em % do PIB foi mantido (a 3.3 tem só a série em reais), já com set/2026.

## Refino com SCN 2023 (02/11/2026)

Fontes novas em dados/brutos/: Sistema de Contas Nacionais 2023 do IBGE (FTP, pasta
Contas_Nacionais/Sistema_de_Contas_Nacionais/2023/, arquivos .ods; os .xls são cópias) e séries do Ipeadata
(ipea-*.json). Leitura e contas em tools/analises/5.4_scn2023.py (biblioteca padrão; zipfile + content.xml;
`--gravar` refaz dados/5.4.2-financeiras-x-transformacao.json).

O que cada tabela sinótica coletada contém (título da primeira linha):

| arquivo | conteúdo |
|---|---|
| tab01 | Visão sintética da economia mundial e nacional, 2000–2023 (PIB, óticas em volume, poupança, FBCF/PIB, capacidade/necessidade de financiamento da economia/PIB, setor externo, Selic, IPCA, carga tributária) |
| tab02 | Economia nacional, conta de bens e serviços, 2000–2023 (produção, importação, impostos, CI, demanda final) |
| tab05 | Componentes do PIB sob as três óticas, valores correntes e constantes, 2000–2023 (ótica da renda vazia em 2022–2023) |
| tab06 | PIB, PIB per capita, população residente e deflator, 1996–2023 |
| tab07 | FBCF, valores correntes e constantes, e taxa de investimento, 1995–2023 |
| tab09 | Variação em volume do VA e contribuição por grupo de atividades, 2011–2023 |
| tab10_1 | VA constante e corrente por grupo de atividades, 2000–2023 |
| tab11_1 | Variação em volume do VA por grupo de atividades, 2001–2023 |
| tab12_1 | Variação de preços do VA por grupo de atividades, 2001–2023 |
| tab13_1 | Participação no VA a preços básicos por grupo de atividades, 2000–2023 |

As TRU (12_tab1_2023 a 12_tab4_2023, TRU2023resumo) têm 12 atividades × 12 produtos; 12_tab1/2 em valores
correntes, 12_tab3/4 a preços do ano anterior. Remunerações e excedente vêm zerados (edição reduzida).
12_tab2_2023 e 12_tab4_2023 carregam abas antigas (2m02, 2n02, 2o02) com a TRU de 2001 em 55 atividades; não
foram usadas.

Por página:

- 5.4.1: TRU de 2023 completa pelas óticas da produção e da despesa com fonte "IBGE, Sistema de Contas
  Nacionais 2023, TRU de 2023, tabelas 1 e 2". Produção 19.821,1; CI 10.262,5 (51,8% da produção); VA 9.558,6;
  importações 1.717,8; impostos 1.384,8 (ICMS 696,2; IPI 58,1; imposto de importação 54,1; outros 576,4);
  recursos = usos = 22.923,7 (R$ bi). Tabela nova por atividade (produção, CI, VA, VA/produção). Serviços
  financeiros na TRU: oferta 1.223,9; CI das atividades 633,8 (6,2% do CI total); consumo das famílias 575,1.
  Anual × trimestral: a soma dos quatro trimestres de 2023 no SIDRA 1846 difere da TRU em no máximo R$ 1,3
  milhão por componente (arredondamento). Número corrigido: consumo de famílias e governo = R$ 82,00 de cada
  R$ 100 de PIB (era 81,90, soma de parcelas arredondadas; o exato é 81,97).
- 5.4.2: série das financeiras e da transformação conferida contra a tabela 13.1: coincide na primeira casa
  em 2000–2023 (maior diferença 0,02 ponto, financeiras em 2022: 7,00 na 13.1, 6,98 nos trimestres; a própria
  13.1 soma 99,97 em 2022). Gráfico refeito com a 13.1 em 2000–2023 e SIDRA 1846 em 1996–1999 e 2024–2026 (os
  valores não mudaram). Correlações refeitas com a série combinada: 0,771 (1996–2025) e 0,519 (2000–2025), sem
  mudança. Novo: volume e preço do VA financeiro (tabelas 11.1 e 12.1): em 2015, 2016 e 2022 o volume caiu
  (−1,2; −3,4; −0,2) e o preço relativo subiu 8,4; 11,4 e 24,4%; correlação do preço relativo com a variação da
  Selic acumulada no ano (SGS 4390) de 0,61 em 2001–2023; com o volume, −0,29.
- 5.4.3: nenhuma tabela sinótica coletada traz contas por setor institucional, renda de propriedade ou D.41.
  A tabela 1 só traz a capacidade/necessidade de financiamento da economia inteira (−0,8% do PIB em 2023,
  −2,3% em 2022). A página diz que a CEI não está na pasta de 2023 e mantém o SCN 2020 com a ressalva.
  Caminhos do FTP a coletar: (a) https://ftp.ibge.gov.br/Contas_Nacionais/Sistema_de_Contas_Nacionais/2023/indice_tabelas_sinoticas.pdf
  (listado em dados/brutos/scn-listagem-74.json e não baixado; diz se as sinóticas 3, 4, 8 e 14 em diante
  existem para 2023); (b) a pasta da última edição completa, https://ftp.ibge.gov.br/Contas_Nacionais/Sistema_de_Contas_Nacionais/2022/
  e, se ela também vier reduzida, .../2021/, subpastas tabelas_ods/ (ou tabelas_xls/) com as Contas Econômicas
  Integradas e as sinóticas por setor institucional (listar a pasta antes, porque os nomes dos arquivos não
  foram conferidos).
- 5.2: as séries de estoque e K/Y (DIMAC_CFELCTOT, DIMAC_CFELCMQEQ, DIMAC_CFRCP, DIMAC_CFINVLQMQEQ) estão só nos
  metadados (R$ de 2025, atualizadas em 03/08/2026): o coletor baixa só as 40 primeiras séries da busca
  (`sel[:40]` em tools/coletar.py) e elas ficaram de fora. Conferido com o que veio: taxa de investimento
  (PAN_FBKFPIBV = SIDRA 1846 = SCN tabela 7 na primeira casa, 1996–2025); 1º semestre de 2026 (PAN4_FBKFPIBV4,
  SCN104_FBKFG104: −1,4% e +1,4% nos dois trimestres, média zero); depreciação de máquinas (DIMAC_CFDPRMQEQ):
  R$ 657,8 bi em 2025, cerca de 16% do estoque do fim de 2024 (11,7% em 1995). Estoque, capital por ocupado e
  K/Y seguem com os valores do Ipeadata consultados em 28/10/2026, agora citados pelo código da série.
  Número corrigido: "investimento líquido em máquinas negativo de 2021 a 2023 e levemente positivo em 2024"
  (vintage antiga da Carta de Conjuntura) virou, pela série DIMAC_CFELCMQEQ, estoque em queda em todos os anos
  de 2015 a 2024, exceto 2019 (parado), e alta pequena em 2025. Para conferir sem depender da consulta de
  28/10, acrescentar a IPEA_SERIES do coletor: DIMAC_CFELCTOT, DIMAC_CFELCMQEQ, DIMAC_CFRCP, DIMAC_CFINVLQMQEQ,
  DIMAC_CFINVBRMQEQ, DIMAC_CFDPRTOT.
- 5.4: parágrafos da TRU e do VA com as fontes anuais; nota "O que falta medir" reescrita.
- Lint: a palavra vetada que resta em 5.1 está no título de uma nota da CEMEC-FIPE no "Para ler" e ficou. Os
  usos econômicos da palavra que o lint confunde com fonte interna, em 5.4, 5.4.1, 5.4.2 e 5.4.3, foram
  trocados por "consumo intermediário" ou "bens intermediários".

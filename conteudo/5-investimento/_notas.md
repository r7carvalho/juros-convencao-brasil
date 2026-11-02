# Notas da área 5: Investimento refém do juro

Rodada de 02/11/2026. Rede: IBGE, BCB, Ipea, SciELO, Poder360 e WordPress não abriram por fetch; a busca web
funcionou até esgotar a cota da sessão (compartilhada entre agentes), o que interrompeu a pesquisa da CEI e da
TRU. A Penn World Table 10.0 foi lida do espelho do pacote R `pwt10` no GitHub
(raw.githubusercontent.com/cran/pwt10), com `pyreadr` instalado no scratchpad.

## Páginas entregues (contagem do build, que inclui tabelas e "Para ler"; prosa entre parênteses)

| id | arquivo | palavras (build) | prosa aprox. |
|---|---|---|---|
| 5 | 5-investimento-refem-do-juro.md | ~1.170 | ~980 |
| 5.1 | 5.1-juro-real-x-retorno-do-capital.md | ~5.200 | ~4.000 |
| 5.2 | 5.2-fbcf-capital-por-trabalhador.md | ~2.880 | ~2.250 |
| 5.3 | 5.3-indexacao-das-decisoes.md | ~3.010 | ~2.550 |
| 5.4 | 5.4-contas-nacionais.md | ~950 | ~790 |
| 5.4.1 | 5.4.1-tabela-de-recursos-e-usos.md | ~1.840 | ~1.350 |
| 5.4.2 | 5.4.2-valor-adicionado-e-financas.md | ~1.960 | ~1.510 |
| 5.4.3 | 5.4.3-contas-economicas-integradas.md | ~2.360 | ~1.850 |

Gráficos (13): 5.1-retorno-capital-x-juro-real, 5.1-colchao-retorno-juro-paises, 5.1-cemec-retorno-custo,
5.2-taxa-de-investimento, 5.2-fbcf-internacional, 5.2-capital-por-ocupado, 5.2-relacao-capital-produto,
5.3-direcionado-e-lft, 5.3-desembolsos-bndes, 5.4.1-componentes-demanda, 5.4.2-financeiras-x-transformacao,
5.4.3-juros-setor-publico, 5.4.3-detentores-divida.

## Dado novo desta área

- PWT 10.0, variável irr (taxa interna de retorno real do capital), Brasil 1995–2019, e médias 2010–2019 para
  México, Chile, Colômbia, Índia, África do Sul e EUA. Brasil 10,4%; folga sobre o juro real BIS de 6,5 p.p.
  contra 9,4 a 11,3 nos emergentes e 8,6 nos EUA. Cálculo do painel com a série BIS da Frente K.
- Correlação juro real ex-post × FBCF/PIB, 2000–2025: −0,18 (mesmo ano) e −0,11 (defasagem de 1 ano).
  Cálculo do painel com Frente K e Frente L.

## Divergências de número

1. Participação das atividades financeiras no valor adicionado. SCN 2017 (informativo IBGE): 6,8% (2010), 6,0%
   (2013), 6,4% (2014), 7,1% (2015), 7,9% (2016). PIB dos Municípios 2021 (IBGE): 6,9% (2020), 5,8% (2021),
   com cabeçalho ambíguo no trecho lido. A busca sobre a Tabela III.2 das Contas Nacionais Trimestrais do 3º tri
   de 2025 devolveu uma sequência de 13 valores (9,2; 8,6; 9,0; 9,8; 10,7; 10,3; 9,6; 9,9; 9,7; 8,7; 10,4;
   11,1; 10,7), incompatível em nível com as contas anuais; provavelmente outra linha da tabela ou erro de
   extração. Não usada. A Fin (Confederação Nacional das Instituições Financeiras) dá 4,8% do PIB em 2024 num
   recorte mais estreito. Resolver na tabela 13.1 do SCN.
2. K/Y: Ipea (2,04 em 2025, queda desde 2016) contra PWT 11.0 (4,37 em 2023, alta desde 2010). Mantida a
   escolha da Frente L (Ipea como referência).
3. Juro real do setor público em 2025: área 3 calcula ~R$ 700 bi, ~5,5% do PIB; CONTEXTO.md traz 5,3%.
   5.4.3 usa 5,5% com remissão a 3.3 e cita o 5,3% como número do debate.
4. Juro real ex-post do Brasil em 2010–2019: 3,9% no painel BIS (média de médias anuais) e média próxima na
   conta Selic/IPCA dez-dez da Frente K; o painel usa a BIS na comparação entre países e a SGS nos anos.
5. Exemplo de brinquedo da fórmula I/Y = (δ + n + k)·K/Y em 5.2 sugere que 16,8% do PIB bastariam para
   aprofundar o capital; o Ipea mostra capital por ocupado caindo 0,8% a.a. em 2022–2025. A página explica a
   diferença (depreciação efetiva por ativo, parte residencial da FBCF), mas a conciliação não foi quantificada.

## [a conferir]

- 5.1: irr de 2020–2023 na PWT 11.0 (só a 10.0 foi lida); rendimento da Selic líquida em 12 meses na Nota
  CEMEC-FIPE 09/2020 (~3,9% a.a.); proporção de empresas com ROE acima da Selic em 2010 (~75%, trecho
  fragmentado; retirada do texto); significância do juro real em Luporini e Alves (2010).
- 5.1: os números do CEMEC-FIPE vêm de reportagem (InfoMoney) e de título de página do CEMEC; as notas originais
  não abriram. IEDI e CNN Brasil lidos por trechos de busca.
- 5.3: fator de convergência e cronograma da TLP (Lei 13.483/2017); valores trimestrais da TJLP 2010–2017;
  limites do intervalo da taxa atuarial (Resolução CNPC 30/2018) e taxas parâmetro anuais da Previc;
  distribuição das metas atuariais; participação das debêntures indexadas ao DI (ANBIMA); nível das NTN-B
  longas em 2023–2026 (o exemplo usa IPCA + 7% como ilustração).
- 5.4.1: produção, consumo intermediário, consumo do governo, exportações e importações da TRU 2023; valor
  anual definitivo do consumo das famílias (~63% do PIB).
- 5.4.2: participação das financeiras em 2000–2009 e 2017–2023 (tabela 13.1 do SCN); 2020 e 2021.
- 5.4.3: D.41 pago e recebido por setor institucional (governo geral, sociedades não financeiras, sociedades
  financeiras, famílias) na CEI 2000–2023; D.44; saldo de renda primária por setor; SIFMI por setor usuário.

## Sugestões para a próxima rodada

1. Baixar as planilhas do SCN 2023 (TRU 12×12, tabela 13.1, CEI) e preencher 5.4.1, 5.4.2 e 5.4.3; montar o
   indicador do IBGE "renda de juros / valor adicionado" e a taxa de lucro das sociedades não financeiras
   (excedente operacional bruto da CEI sobre o estoque de capital do Ipea) para cruzar com a Selic real.
2. Ler a PWT 11.0 (irr até 2023) e atualizar 5.1; se possível, série anual CEMEC-FIPE de ROIC e WACC 2010–2025.
3. Abrir os PDFs do IEDI (série de ROE industrial) e das notas CEMEC para trocar a tabela pontual de 5.1 por série.
4. Conferir com a área 4 (4.3) a queda de 32% da FBCF do pico de 2013 ao fim de 2016, usada em 5.1 e 5.2.

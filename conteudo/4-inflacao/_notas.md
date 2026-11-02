# Notas da área 4, "Inflação: de onde vem"

Data de referência: 02/11/2026. Acesso direto a IBGE, BCB e demais sites bloqueado na sessão (WebFetch e curl); o orçamento de buscas web (compartilhado entre os subagentes) acabou no meio da rodada. Por isso parte dos números está marcada `[a conferir]`.

## Páginas entregues

| Página | Arquivo | Palavras (corpo sem "Para ler", `wc -w`) | Palavras (`tools/lint.py`, corpo inteiro) |
|---|---|---|---|
| 4 Inflação: de onde vem (macro) | 4-inflacao.md | ~1.120 | 1.311 |
| 4.1 Decomposição do IPCA, 2003–2026 | 4.1-decomposicao-ipca.md | ~4.050 | 4.920 |
| 4.2 Pandemia, 2020–2022 | 4.2-pandemia-2020-2022.md | ~3.190 | 3.729 |
| 4.3 2011–2016 | 4.3-2011-2016.md | ~3.150 | 3.617 |
| 4.4 2023–2026 | 4.4-2023-2026.md | ~3.000 | 3.772 |
| 4.5 Teste da tese | 4.5-teste-da-tese.md | ~3.050 | 3.364 |

A 4.1 passa um pouco de 4.000 palavras pelo critério do lint (que conta URLs, tabelas e números decimais como várias palavras). Se o coordenador quiser cortar, o candidato é o quadro `:::painel` da seção "Livres e administrados", que antecipa a conclusão da 4.5.

## Gráficos (dados/)

- `4.1-ipca-meta-teto.json` (linha): IPCA anual, centro, teto e piso, 2003–2026 (2026 = Focus).
- `4.1-livres-administrados.json` (barras): livres × administrados em 2015, 2021, 2022, 2024, 2025.
- `4.1-alimentos-ipca.json` (barras): IPCA × Alimentação e bebidas, 2019–set/2026.
- `4.1-decomposicao-bc-2021.json` (empilhadas): desvio de 2021 decomposto pelo BC.
- `4.2-selic-ipca-2019-2026.json` (linha mensal): Selic meta × IPCA 12 meses, jan/2019–out/2026. Também usado na 4.4.
- `4.2-juro-real-pares.json` (linha): juro real ex-post BIS, Brasil, México, Chile, EUA, zona do euro, 2017–2026.
- `4.3-ipca-selic-2010-2017.json` (linha): IPCA, Selic de fim de ano e juro real ex-post.
- `4.3-fbcf-pib.json` (linha): FBCF/PIB 2003–2026.
- `4.4-juro-real-ex-ante.json` (linha): juro real ex-ante 2010–out/2026 com neutro de 5%.
- `4.4-componentes-2024-2025.json` (barras): IPCA, alimentação no domicílio, serviços, administrados em 2024 e 2025.
- `4.5-desocupacao-ipca.json` (linha): desocupação média × IPCA, 2015–2025.

Não construído: o gráfico pedido de "contribuições por grupo nos anos-chave em barras empilhadas". Faltam os pesos e as contribuições por grupo conferidos (IBGE/BCB inacessíveis). Em seu lugar há o empilhado da decomposição do BC para 2021. Pendência prioritária para a próxima rodada.

## Números que divergem ou têm versões diferentes

| Número | Versão A | Versão B | Decisão |
|---|---|---|---|
| Início da queda do IPCA 12 meses em 2011 | CONTEXTO: 6,97% em out/2011 | pico de 7,31% em set/2011 (também em `dados/6.2.1-selic-ipca-2010-2014.json`) | usei os dois: pico 7,31% (set) e 6,97% (out) |
| Administrados 2025 | 5,28% (IBGE via InfoMoney, 09/01/2026) | 5,29% (relatório de banco) | 5,28% |
| Juro real ex-ante em out/2026 | 8,72% (série da frente K, 23/10/2026) | 8,45% (ranking MoneYou/Lev, 16/09/2026, DI de 1 ano) e ~8,8% (conta de brinquedo com Selic meta 13,75% e Focus 4,53%) | texto diz "cerca de 8,7%"; diferenças explicadas pela taxa (Selic over × meta × DI) e pela data |
| Desvio de 2021 em relação à meta | 6,31 p.p. (10,06 − 3,75; boxe do RI mar/2022) | 5,54 p.p. (aparece num resumo de busca, sem origem clara) | 6,31 p.p. |
| Administrados 2021 | 16,90% (série SGS 4449, memória do painel, a conferir) | 13,05% (resumo de imprensa; provavelmente é o grupo Habitação do IPCA) | 16,90% marcado `[a conferir]` |
| Desvio de 2,35 p.p. com expectativas 0,58 p.p. | carta aberta de jul/2025 (IPCA 12 meses de jun/2025, 5,35%) | boxe de 2024 (desvio de 1,83 p.p.) | não é divergência: são referências diferentes; o texto separa as duas |
| IPCA 12 meses jan–ago/2026 | compilações (calctool, debit): 4,44; 3,81; 4,14; 4,39; 4,72; 4,64; 4,44; 4,22 | QuintoAndar com datas deslocadas (ex.: 4,39% atribuído a junho) | usei a primeira; set/2026 (4,58%) confere com os insumos |

## O que ficou `[a conferir]`

Preços e índices:
- Administrados e livres de 2021 (16,90% e 7,71%) e 2022 (−3,83% e 9,38%), SGS 4449 e 11428; livres de 2024 sem valor. Ideal: série completa 2003–2026 para refazer o gráfico de livres × administrados com todos os anos.
- Serviços (SGS 10844) de 2011–2014 ("entre 8% e 9%") e de 2022; industriais de 2021, 2022 e 2025 (2,39%).
- Deflação de jul, ago e set/2022 (−0,68%, −0,36%, −0,29%).
- Energia elétrica no IPCA de 2015 (~51%).
- IC-Br (SGS 27574), variação anual 2020–2026.
- Número de subitens e peso dos administrados na estrutura vigente do IPCA.
- PTAX de dez/2023 (4,84).
- IPCA 12 meses mensal de 2019 a 2024 no gráfico Selic × IPCA: valores da série oficial transcritos pelo painel e não reconferidos na API; os de dez de cada ano, abr/2025 e 2026 estão conferidos.

Decomposições do BC:
- Tabelas completas dos boxes de 2015 (RI mar/2016), 2022 (RI mar/2023), 2023 (RI mar/2024), 2024 (RPM mar/2025) e 2025 (RPM mar/2026). Só trechos foram recuperados por busca (valores citados: 2021 completo; 2022 expectativas 1,02 p.p.; 2023 inércia 0,61 p.p.; jul/2025 expectativas 0,58 p.p.).
- Em 2021, a diferença de ~1,0 p.p. entre o desvio e os componentes nomeados (o boxe tem outros itens).

Atividade, emprego, hiato:
- Hiato da IFI 2024–2026 (RAF).
- Desemprego mínimo da PME em dez/2014 (4,3%); PIB de 2008 e 2010; déficit primário de 2014 (−0,56% do PIB).
- Trajetória da mediana Focus para o IPCA de 2021.

Literatura e fontes:
- Texto exato da análise do FGV IBRE ("maior parte oferta, BC subestimou"): só consta do CONTEXTO; não localizada.
- Estudo do DIEESE/CUT sobre a Lava Jato (título, data, link); outras estimativas (GO Associados etc.).
- Páginas de Barbosa Filho (2017) e Paula e Pires (2017) em *Estudos Avançados* 31(89); paginação de Serrano e Summa (2015) em *Nova Economia*.
- Link estável de Almeida, Lisboa e Pessôa (2015), "O ajuste inevitável".
- Data da retirada da orientação futura do Copom (início de 2021).

Comparação internacional (4.2):
- Picos de inflação de Chile (14,1%, ago/2022), México (8,70%, set/2022), zona do euro (10,6%, out/2022) e taxas básicas mínimo → pico e datas de início da alta fora do Brasil: registrados pelo painel a partir das estatísticas oficiais, sem reconferência nesta sessão. Há `:::nota` na página. EUA (9,1%) conferido nos insumos (BLS).

## Recortes citados

Recortes entre aspas usados só quando o trecho veio de busca com a fonte primária identificada: boxes do BC (RI mar/2022, mar/2023, mar/2024; RPM mar/2025), RI set/2013, carta de jan/2023, Ipea (Carta de Conjuntura, mai/2016). A literatura de 2011–2016 (Serrano e Summa, Carvalho, Barbosa Filho, Pessôa e Lisboa, Holland) está parafraseada, sem aspas, porque o texto não foi aberto nesta sessão. Próxima rodada: trazer recortes curtos dessas obras com página.

## Sugestões para a próxima rodada

1. Baixar SGS 4449, 11428, 10844, 10841 (alimentação no domicílio), 10843 (industriais), 4466 (média dos núcleos), 21379 (difusão) e 27574 (IC-Br) e montar: (a) livres × administrados 2003–2026 completo; (b) serviços × desocupação 2012–2026, o gráfico mais forte para a 4.5; (c) contribuições por grupo em 2003, 2015, 2021, 2022, 2024 e 2025 em barras empilhadas.
2. Abrir os PDFs dos boxes de decomposição e montar uma tabela única 2015–2025 com todos os componentes (inércia, expectativas, importada, hiato, choques, resíduo), e um gráfico empilhado com todos os anos.
3. Hiato do BC e da IFI lado a lado, 2014–2026.
4. Taxa de participação e decomposição dos serviços (indexados × intensivos em trabalho) para fechar a seção "O que mudaria a conclusão" da 4.5.
5. Conferir com a área 6 (6.2 e 6.2.1) e a área 2 (2.1, 2.3) os números comuns: Selic 2010–2017, juro real ex-ante e ex-post, neutro de 5%. Os valores usados aqui vêm dos mesmos insumos (frente K) e batem com `dados/6.2.1-*` e `dados/6.2-desinflacao-2016-2017.json`.

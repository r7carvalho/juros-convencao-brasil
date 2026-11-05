# Aplicação (05/11/2026)

Aplicação do relatório conteudo/_revisao/13b.md (41 achados) em 13.8, 13.9 e 13.10, com as decisões de
conteudo/_divergencias.md ("Decisões da revisão do bloco 13" e "Decisões da revisão de 13.8 a 13.10").
As três páginas passam a `estado: revisada`. `python3 tools/build.py --check` sem ERRO (166 páginas);
`python3 tools/lint.py` nas três páginas: zero travessão, zero contraste vetado pelo regex do lint, zero palavra vetada.

Arquivos editados: as três páginas; tools/analises/13.8_islm.py (nota do gráfico de Hazell e contas novas de
brinquedo); tools/analises/13.10_risco.py (testes extras e gráficos); dados/13.8-hazell-inclinacao.json e os
seis dados/13.10-*.json regerados pelos scripts (13.10-dispersao-divida.json saiu igual); tools/assets/app.js
(função `dispersao`, usada só pela 13.10); conteudo/13-lara-resende/_notas.md (seção nova com pendências);
conteudo/_divergencias.md (um item ao fim da seção de 13.8 a 13.10).

## 13.8

| Nº | Grav. | Situação | O que mudou |
|---|---|---|---|
| 1 | 2 | Aplicado | "Sobretudo pelo câmbio" passa a procede em parte (canal relevante, independe de Phillips; ser o principal não tem medida; o modelo do BC tem os dois canais), na tabela e na caixa do painel |
| 2 | 3 | Aplicado | A MP de Romer responde ao produto e é inclinada; brinquedo novo com a regra i = 5 + 0,05 (Y − 1.050): gasto +15 leva a renda a 1.070 e o juro a 6%; a faixa da proposta achata a MP (13.4, elo 6). Resumo corrigido. Texto do JEP segue fora do acervo (pendência) |
| 3 | 3 | Aplicado | Sob ouro e câmbio fixo a moeda é endógena ao balanço de pagamentos; metas monetárias dos anos 1970 e começo dos 1980 (Bundesbank 1975, Fed 1979–1982), abandonadas com a procura por moeda instável |
| 4 | 3 | Aplicado | Dezembro vira ilustração (procura acomodada, "moeda elástica" de 1913); a prova é a over 0,10 abaixo da meta em 3.221 dias úteis de 2014 a 2026, salvo seis (−0,08 e −0,09 em ago/2014 e abr/2015), conferido no SGS 1178 contra o 432 |
| 5 | 4 | Aplicado | "Inclinação agregada" no lugar de "correlação"; queda à metade com erros-padrão (0,0080 e 0,0040) e "not statistically significant"; κ da amostra inteira 0,0062 (0,0028); estimativa com instrumento; nota do gráfico corrigida no script |
| 6 | 4 | Aplicado | "IS pouco sensível" vira linha montada pelo painel com a meia-entrada (6.2.2, 7.9) e Bonomo e Martins |
| 7 | 4 | Aplicado | Frase sobre juro real (IS) e nominal (LM) na seção 3 |
| 8 | 4 | Aplicado | A outra metade de Poole, com brinquedo: investimento +15 dá 1.080 com juro fixo e 1.075 com moeda fixa |
| 9 | 4 | Aplicado | Summa (2011) "citado por referência"; McLeay e Tenreyro "segundo Hazell et al. (p. 4)" |
| 10 | 4 | Aplicado | Condição "reservas abundantes e remuneradas" (regime desde 2008, compromissadas) antes da aspa, na abertura e na seção 6 |
| 11 | 5 | Aplicado | Curso legal e impostos, com a ênfase cartalista atribuída; Fed: letras até 1947, teto dos longos até março de 1951 |
| 12 | 5 | Aplicado | Cortes de metadiscurso e da pergunta de preparação; frase de 2022 explicada (reabertura e inércia); convenção de página do Bulletin: a da revista nas duas páginas (13.9 passou a p. 14 e 15) |

## 13.9

| Nº | Grav. | Situação | O que mudou |
|---|---|---|---|
| 1 | 2 | Aplicado | A crítica ortodoxa é julgada pelo que o painel mede sobre o nível (O1b e P2 da 8.1, 4,5 pontos de 2006–2013 com superávit, 13.10); a bola de neve aparece como identidade contábil, com o nome da decisão; sai "mais citada" |
| 2 | 3 | Aplicado | Alternativas: neutro por filtro segue o juro por construção; 2019 com IPCA de 4,31% contra meta de 4,25% e 10,06% em 2021; 2016–2017 ambíguo (Selic nominal de 14,25% para 7% junto com a inflação). Também no A favor e na caixa do painel |
| 3 | 3 | Aplicado | Quadro das famílias com "Direção e força (9.1)" e "Classe", e um parágrafo com a régua |
| 4 | 3 | Aplicado | 43,9% é o direcionado inteiro, com o BNDES; o "1 ponto" é conta de brinquedo da 6.2.2 sobre a alta de 3,8 pontos; 9,7% com a medida dita (e 9,09% do BIS) |
| 5 | 4 | Aplicado | Tese de 2019 "segundo os trechos reproduzidos por Calabrez e o resumo de Muinhos" |
| 6 | 4 | Aplicado | McLeay e Tenreyro alinhados à 13.8 (choques de demanda cancelados; choques de custo) |
| 7 | 4 | Aplicado | Franke com as duas metades (estabilidade ou instabilidade com parâmetros plausíveis, dinâmica lenta), no corpo e no A favor |
| 8 | 4 | Aplicado | Frase da Casa das Garças reproduzida por Muinhos (p. 2), conferida no texto; também usada na abertura da 13.10 |
| 9 | 5 | Aplicado | 3.727 e 3.896 palavras; Poder360 de 08/02/2023 sobre o *Valor* de 07/02; aspa do BoE até "price of reserves" e tradução; título de Oreiro citado; Woodford (1995) no texto e no Para ler |

A atribuição a Lisboa e Pessôa ficou como o Amado Mundo a escreve: a frase entre aspas é do relato do site, e não fala direta dos dois.

## 13.10

| Nº | Grav. | Situação | O que mudou |
|---|---|---|---|
| 1 | 2 | Aplicado | Duas proposições com grau único: (a) distância de 2023–2026, confiança alta, com 2019 a −0,2; (b) rating, CDS, dívida e inflação recente não a explicam, a favor, moderada, procede em parte. Resumo, conclusão, grau de confiança, tabela-resumo e caixa do painel alinhados; sai "derruba"; a comparação não testa o canal das expectativas e do neutro |
| 2 | 3 | Aplicado | Caso sem o Peru: coeficiente 3,93 (ep 9,78, t 0,4, 6 gl), histórico do Brasil 2,5 vezes o maior da amostra, IC do resíduo de −23,2 a +26,6; "a amostra não testa o histórico". Barras "M3 sem o Peru" saíram do gráfico, com a razão na nota |
| 3 | 3 | Aplicado | Validação do M2 (Turquia −25,45, Japão −8,53, Brasil 5,87, terceiro) e caudas do M1 (Brasil e Japão acima de 4) |
| 4 | 3 | Aplicado | Seção "Colinearidade, mediação e amostra pequena": VIF de 1,3 a 1,9, correlação rating × dívida −0,45, M4 com dívida negativa, mediação (mau controle), heterogeneidade; série 2007–2023 com erros-padrão (1,16 e 1,89), 5 e 4 gl, VIF 1,35 a 1,79; tendência na correlação de −0,47 |
| 5 | 3 | Aplicado | Causalidade reversa nos dois sentidos (conta de juros × credibilidade, carry e reservas) |
| 6 | 3 | Aplicado | Bola de neve com o nome da decisão; primário 3,6 |
| 7 | 3 | Aplicado em parte | CDS de ago/2026 marcado como página não aberta (texto, gráfico, script, Para ler, A favor); origem das dívidas de Peru, Indonésia e Coreia dita na nota de fontes; Suíça, Suécia e Dinamarca testadas no M1 (resíduo 5,0, IC 1,7 a 8,3). Não aplicado: baixar do DataMapper, porque a rede bloqueou a API do FMI (pendência no _notas) |
| 8 | 4 | Aplicado | Notas de 2026 × juro de 2025; teste com ratings de 2025 (4,85 a 4,92 no M1; 5,83 a 5,88 no M2; com a Colômbia em BB+, distância de 4,3) |
| 9 | 4 | Aplicado | "Intervalo de 95% do resíduo"; previsão de 0,6% a 7,8%; hipóteses do intervalo |
| 10 | 4 | Aplicado | Parágrafo sobre a variável dependente (risco de crédito, regra de reação, Blanchard 2004, LFT) e o juro real longo como teste ausente |
| 11 | 4 | Aplicado | "De 3,3 (ex-ante) a 5,7 pontos"; "forte em 2023–2026; em 2019, não" |
| 12 | 4 | Aplicado | México como sugestão da entrevistadora aceita como exemplo de corte moderado (10:37 e 55:19), sem o nome dela |
| 13 | 4 | Aplicado | Colômbia (poupança de 13,6%, juro menor) como contraexemplo; sai "nenhuma variável medida fecha" |
| 14 | 4 | Aplicado | O teste do anúncio decide num sentido só (Keynes, política "experimental"; equilíbrios múltiplos) |
| 15 | 4 | Aplicado | "Sinal estável"; no M3 o histórico tem o t maior (2,06 contra 1,7), puxado pelo Brasil |
| 16 | 5 | Aplicado | 0,999; `eixo_x` curto com a escala na nota; `eixo_y` desenhado; rótulos que se sobrepõem são deslocados; reta cortada nos limites do eixo y (app.js); cortes de "o argumento mais forte", "consenso não garante racionalidade" e "as cinco seções seguintes"; coluna de classe na tabela-resumo. Mantido: abaixo de 420 px só o Brasil tem rótulo (a tabela resolve) |

Ressalva do CDS de 93 pontos (fev/2020): aplicada, como único fechamento mensal e comparação frágil.

## Fora das três páginas (coerência)

| Nº | Grav. | Situação | Por quê |
|---|---|---|---|
| 1 | 4 | Não aplicado | 13.7 e macro 13 estão com outro corretor. A fazer lá: linhas 11 a 18 da matriz (em _divergencias), argumentos A11, A12, C11, C12, armadilhas, ordem da macro, "o teste mais citado" sem fonte |
| 2 | 4 | Não aplicado | 8.1 e 2.5 estão com outro corretor. A fazer: citar a 13.10 em P2, O1b, O8, P3 e nos testes pendentes; link da 2.5 para a 13.10 |
| 3 | 4 | Aplicado | As medidas novas já estão em _divergencias; acrescentado um item com os testes de sensibilidade, o CDS não aberto e a origem das dívidas |
| 4 | 5 | Não aplicado | 13.7 (A5 e linha 6) e 13.2 (tabela de previsões, "0,25% em dez/2019 sem inflação acima da meta") estão fora do escopo; a ressalva a levar é: IPCA de 4,31% em 2019 contra meta de 4,25%, dentro do intervalo |

## Pendências

- Romer (2000) no JEP, para conferir a forma da regra.
- Dívidas de Peru, Indonésia, Coreia, Suíça, Suécia e Dinamarca no DataMapper do FMI (API bloqueada em 05/11/2026).
- CDS de ago/2026 numa fonte aberta, com o dia.
- Rating S&P da Colômbia no começo de 2025.
- Extensão de prosa da 13.9 e da 13.10 acima de 4.500 palavras.

## Números que mudaram

- Nenhum número que outra área usa mudou. A distância para os pares de rating igual ou pior (4,6 em 2025; 5,7 em 2026; 3,3 no ex-ante; −0,2 em 2019) e o resíduo de 2,4 a 8,2 seguem os mesmos.
- Novos na 13.10 (todos do script): previsão do M1 para o Brasil de 0,6% a 7,8%; M3 sem o Peru com coeficiente do histórico de 3,93 (ep 9,78) e IC do resíduo de −23,2 a +26,6; ratings de 2025 com resíduo de 4,85 a 4,92 (M1) e 5,83 a 5,88 (M2) e distância de 4,3 com a Colômbia em BB+; M1 com Suíça, Suécia e Dinamarca com resíduo de 5,0 (IC 1,7 a 8,3).
- Corrigidos na 13.10: correlação do brinquedo de 0,998 para 0,999; o gráfico do resíduo perdeu as duas barras do M3 sem o Peru (1,7 e 0,6), que seguem no texto como extrapolação.
- Novos na 13.8: over 0,10 abaixo da meta em 3.221 dias úteis de 2014 a 2026, salvo seis; contas de brinquedo da regra de reação (1.070 e 6%) e de Poole (1.080 e 1.075); κ de Hazell et al. com erros-padrão.
- Na 13.9: "Eu acuso" com 3.727 palavras (Grabois) e 3.896 (RED), no lugar de "cerca de 3.300"; Poder360 em 08/02/2023.

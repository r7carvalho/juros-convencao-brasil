---
id: 10
titulo: Política monetária: instrumentos convencionais e não convencionais
pai: 0
ordem: 8
resumo: Mapa dos instrumentos com que um banco central age (taxa básica, mercado aberto, redesconto, compulsório, câmbio, comunicação e, no limite, compra maciça de títulos, juros negativos e crédito dirigido), dos canais por onde cada um chega à inflação e dos regimes que lhes dão alvo. Um balanço de brinquedo mostra o que cada operação muda, lançamento por lançamento; o balanço real do BCB mostra compromissadas de 10,3% e conta única de 13,5% do PIB em agosto de 2026. O Brasil nunca encostou no piso de zero, e isso limita o que se pode importar das receitas de fora.
estado: 1ª versão
---

Um instrumento de política monetária é o que o banco central controla diretamente: a taxa das próprias operações, os títulos que compra e vende, o empréstimo aos bancos, a fração dos depósitos que os bancos deixam presa com ele, os dólares que vende ou compra, o que ele diz. Um canal é o caminho pelo qual esse movimento chega à inflação e à atividade: o juro dos empréstimos e da curva longa, o volume de crédito, o preço dos ativos, o câmbio e as expectativas. A divisão entre instrumento, alvo operacional e canal segue Mishkin (2019).

Quase todo banco central moderno fixa um preço, a taxa de um dia, e deixa a quantidade de moeda se ajustar. Poole (1970) mostrou por quê: quando a demanda por moeda oscila de forma imprevisível, fixar a quantidade faz o juro oscilar junto e leva o choque para a economia, enquanto fixar o juro absorve o choque no balanço do banco central. No Brasil o preço é a Selic, decidida pelo Copom, e o BC fornece as reservas que o sistema pede a essa taxa, como o Banco da Inglaterra descreve em McLeay, Radia e Thomas (2014) (ver [Moeda](pagina:1.1)).

## O balanço de brinquedo

No ativo do banco central ficam títulos do Tesouro, reservas internacionais e redesconto aos bancos. No passivo, a base monetária (papel-moeda mais as reservas que os bancos mantêm no BC), as operações compromissadas (o BC vende um título e se obriga a recomprá-lo em prazo curto, retirando reservas nesse intervalo) e a conta única do Tesouro.

:::exemplo Um banco central com números redondos (R$ bilhões)
| Ativo | | Passivo | |
|---|---|---|---|
| Títulos do Tesouro | 300 | Papel-moeda | 100 |
| Reservas internacionais | 500 | Reservas bancárias | 100 |
| Redesconto | 0 | Compromissadas | 300 |
| | | Conta única do Tesouro | 250 |
| | | Patrimônio | 50 |
| Total | 800 | Total | 800 |

Os bancos precisam de 100 em reservas para o compulsório e os pagamentos. Com 130, oferecem a sobra e a taxa de um dia cai abaixo da meta; com 70, disputam reservas e ela sobe. O BC acerta a quantidade todo dia para manter a taxa na meta.
:::

1. Compromissada de 20 (o BC toma reservas): reservas bancárias −20, compromissadas +20. A base cai 20; é o ajuste fino diário.
2. Compra definitiva de 50 em títulos: títulos +50 no ativo, reservas +50 no passivo. Para a sobra não derrubar a taxa, o BC faz uma compromissada de 50 e termina com títulos +50 e compromissadas +50. O balanço cresceu e a taxa não mudou: é o princípio da separação de Borio e Disyatat (2009), pelo qual juro e balanço se conduzem de forma independente. O QE é essa operação em escala de trilhões.
3. Redesconto de 10 a um banco sem liquidez: redesconto +10 no ativo, reservas +10 no passivo, a uma taxa acima da Selic. É o emprestador de última instância de Bagehot (1873).
4. Compulsório sobe e prende 30 a mais: as reservas totais não mudam, mas 30 deixam de estar livres e a taxa sobe. Para segurá-la na meta, o BC resgata compromissadas: compromissadas −30, reservas +30. Troca-se um passivo que paga Selic por outro só em parte remunerado, e o canal é o crédito: sobra menos para emprestar.
5. Venda de US$ 10 bilhões no câmbio, a R$ 5: reservas internacionais −50, reservas bancárias −50. O BC devolve os reais resgatando compromissadas (−50) e sobra a troca de reservas internacionais por compromissadas, a intervenção esterilizada. O swap cambial, pago em reais pela variação do dólar, age no câmbio sem tocar nas reservas.
6. Tesouro gasta 40 da conta única: conta única −40, reservas +40 nos bancos de quem recebeu. O BC enxuga com compromissadas: +40.
7. Depósito voluntário remunerado de 20, criado pela [Lei 14.185/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/L14185.htm): reservas −20, depósitos remunerados +20. Faz o trabalho da compromissada sem exigir título como lastro.

A comunicação não tem lançamento: o anúncio do caminho da taxa muda os juros futuros antes de qualquer operação, pelo canal das expectativas. A regra de Taylor (1993) dá a referência numérica de quão alta a taxa deveria estar diante da inflação e do hiato.

## O balanço real do Banco Central do Brasil

Em agosto de 2026, pela tabela especial de dívida do BCB (Divggnp, consulta em 28/10/2026) e pelo SGS: compromissadas de 10,3% do PIB; conta única do Tesouro de 13,5%; reservas internacionais de US$ 372,6 bilhões (SGS 3546), cerca de 14,5% do PIB; e títulos do Tesouro livres na carteira do BC de 11,7% do PIB, que é a diferença entre a dívida bruta no conceito do FMI (94,5%) e no do BCB (82,9%). Somando os títulos livres aos que lastreiam as compromissadas, a carteira de títulos do BC fica perto de 22% do PIB (cálculo aproximado do painel). Na mesma data, a base monetária restrita somava R$ 432,7 bilhões e os depósitos voluntários remunerados, R$ 165,7 bilhões (BCB, SGS 1788 e 28964, coleta de 02/11/2026).

```grafico
dados/10-compromissadas-conta-unica.json
```

O gráfico mostra os lançamentos 5 e 6 na prática. As compromissadas foram de 3,2% do PIB em 2006 para 16,7% em 2016, com o BC esterilizando a compra de reservas. Entre dezembro de 2025 e agosto de 2026 a conta única caiu de 16,2% para 13,5% do PIB e as compromissadas subiram de 7,8% para 10,3%, porque o Tesouro gastou caixa (BCB, tabela especial Divggnp). Desde 2002 o BCB não pode emitir título próprio (LRF, art. 34), e por isso enxuga reservas com títulos do Tesouro. A Constituição proíbe o financiamento direto do Tesouro e autoriza o mercado aberto:

> "É vedado ao banco central conceder, direta ou indiretamente, empréstimos ao Tesouro Nacional e a qualquer órgão ou entidade que não seja instituição financeira."
> (Constituição Federal, 1988, art. 164, § 1º; [texto no Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm))

## Quando o convencional não basta

Os instrumentos convencionais mexem na taxa de um dia e contam com sua propagação pela curva, interrompida por dois problemas: o piso de zero, abaixo do qual o papel-moeda rende mais que o depósito, e a pane de mercado, em que a taxa básica está certa e o crédito para mesmo assim. Daí os não convencionais. O forward guidance promete o caminho futuro da taxa. O QE compra títulos longos para derrubar o prêmio de prazo; o Fed levou o balanço de cerca de US$ 0,9 trilhão em 2008 para US$ 4,5 trilhões em 2015, com inflação abaixo de 2% na maior parte do período (Federal Reserve, ativo total, série WALCL, via FRED). O Banco do Japão juntou compra maciça e controle da curva de 2016 a março de 2024. Juros negativos rebaixam o piso; o credit easing financia o mercado que travou. Borio e Disyatat (2009) classificam essas políticas de balanço pelo mercado que elas atacam: câmbio, dívida pública, crédito privado e reservas bancárias. Bernanke (2020) conclui que forward guidance e QE, juntos, dão algo como 3 pontos percentuais adicionais de espaço quando o juro neutro nominal está entre 2% e 3%, e que, com neutro bem mais baixo, a política fiscal precisa ajudar.

## O Brasil nunca chegou ao zero

A menor Selic da série foi 2%, de agosto de 2020 a março de 2021. O Copom indicou no comunicado de 05/08/2020 (233ª reunião) que o espaço remanescente para cortes, se houvesse, era pequeno, porque num emergente o piso efetivo fica acima de zero: antes dele o câmbio e o prêmio de risco reagem. Em 2020 o BCB usou linhas de liquidez e redução de compulsório; a EC 106/2020 o autorizou a comprar títulos públicos e privados no mercado secundário durante o estado de calamidade, mas não há registro de compra sob essa autorização ([Brasil 2020](pagina:10.3.7)). Em 2026 o problema é o oposto: a Selic ficou em 15% de junho de 2025 a março de 2026 e estava em 13,75% em outubro (BCB, SGS 432), com juro real ex-ante perto de 8,7% ([Método](pagina:9.1)).

Isso pesa para quem quer importar receitas. As não convencionais nasceram para dar estímulo quando o corte acabou, em países cuja moeda é procurada como reserva e cuja dívida é longa e prefixada. No Brasil a taxa tem espaço de sobra para cair, a LFT, título que paga a própria Selic, era 52,7% da dívida federal em agosto de 2026 (Tesouro, RMD de agosto), e uma compra de LFT pelo BC muda pouco o prêmio de prazo porque a LFT quase não tem prazo de juro. O que viaja sem custo são as linhas de liquidez, o swap cambial e a disciplina de comunicação.

:::painel
O balanço liga o bloco à pergunta do painel. Compromissadas, depósitos remunerados, parte do compulsório e a LFT pagam a Selic, então cada ponto de alta da taxa básica aumenta no mesmo mês a conta de juros do setor público, que somou 8,99% do PIB, R$ 1.204,8 bilhões, nos 12 meses até setembro de 2026 (BCB, SGS 5727 − 5793 e SGS 4382). Se essa conta alimenta a percepção de risco fiscal e o prêmio sobe, o instrumento perde parte do efeito, que é o mecanismo da dominância fiscal ([Prêmio fiscal e dominância](pagina:6.1)). Se a taxa fica alta porque o mercado e o BC convergiram num patamar tido como normal, o problema está na convenção. O bloco 10 não decide entre as duas leituras; ele descreve as peças que as páginas [2.3](pagina:2.3) e [2.4](pagina:2.4) usam para testá-las.
:::

## O que o bloco cobre

[Regimes e a meta](pagina:10.1) trata do alvo final. O Brasil passou do câmbio fixo, que quebrou em janeiro de 1999, às metas de inflação, cumpridas em 18 de 26 anos até 2024, com o IPCA acima do centro em 21 de 27; desde 2025 a meta é contínua, de 3%, e a LC 179/2021 fixou o mandato do BC. A literatura sobre o nível ótimo dá uma faixa, e não um número: o painel lê o 3% como ponto focal institucional, com ótimo provável entre 3% e 4%, e nota que Chile, Colômbia e México têm a mesma meta e juro real menor, de modo que o número da meta não explica a distância do juro brasileiro (ver também [Meta de inflação maior](pagina:7.1)).

[Instrumentos convencionais](pagina:10.2) desmonta cada lançamento. A Selic é taxa administrada no sentido literal, com a over 0,10 ponto abaixo da meta desde 2014; a mecânica de compromissadas e depósitos remunerados é neutra para o nível do juro num dado dia e cara pela escala; redesconto e compulsório funcionaram em 2008 e 2020; a regra de Taylor dá a direção da Selic e não o nível, porque o neutro implícito foi de 12,7% em 2003–2005 a 0,8% em 2020–2021 e de volta a 9,3% em 2025–2026; e a comunicação do Copom move a curva e o Focus em dias, como ponto focal no sentido de Morris e Shin (2002).

[Instrumentos não convencionais](pagina:10.3) percorre forward guidance, QE (Fed, Banco da Inglaterra, BCE), o Japão, juros negativos, credit easing, câmbio, o Brasil de 2020 e o financiamento monetário. A orientação futura de agosto de 2020 moveu o Focus por três meses e não segurou a ponta longa; a EC 106 autorizou compras que o BC não fez; reservas e swaps poupam juro no repasse cambial e não na demanda, com diferencial de carregamento de cerca de 1,2% do PIB ao ano em 2003–2025 (cálculo do painel); o financiamento monetário esbarra no art. 164 e na moeda periférica.

[Blanchard por inteiro](pagina:10.4) segue um autor citado pelos dois lados do debate e mostra que as posições dele mudaram menos do que o juro do mundo. Aplicada ao Brasil de 2026, com r − g de quase 6 pontos, a obra dá razão à preocupação fiscal e não confirma o efeito perverso do juro que ele achou em 2002, porque em 2025 a Selic a 15% valorizou o real; do livro de 2023 sai a ideia de dois equilíbrios de juro com os mesmos fundamentos, a versão formal da convenção.

[O que é transponível ao Brasil](pagina:10.5) aplica aos 14 instrumentos quatro traços brasileiros: moeda não reserva e repasse cambial, LFT em 52,74% da dívida federal e compromissadas de 10,3% do PIB, crédito direcionado em 43,9% do saldo (BCB, SGS 20593 e 20539, ago/2026) e histórico de inflação e indexação. Seis instrumentos se transpõem como estão, quatro em parte e quatro não (QE, QQE e controle da curva, juros negativos e financiamento monetário). O bloco reforça que a política monetária funciona com menos potência e mais custo do que nos pares e deixa o nível do juro sem decisão entre convenção e prêmio fiscal, com cinco experimentos que poderiam separá-los.

## Para ler

- Banco Central do Brasil. [Relatório de Política Monetária](https://www.bcb.gov.br/publicacoes/rpm); [Divggnp.xlsx](https://www.bcb.gov.br/content/estatisticas/Documents/Tabelas_especiais/Divggnp.xlsx), consulta em 28/10/2026; [SGS](https://www3.bcb.gov.br/sgspub/), séries 432, 1788, 3546, 4382, 5727, 5793 e 28964, coleta de 02/11/2026.
- Bagehot, W. (1873). *Lombard Street*. Londres: Henry S. King.
- Bernanke, B. (2020). "The New Tools of Monetary Policy". *American Economic Review*, 110(4), p. 943–983.
- Borio, C.; Disyatat, P. (2009). "Unconventional monetary policies: an appraisal". BIS Working Papers, n. 292.
- Brasil. Lei Complementar 101/2000 (LRF), art. 34; Lei Complementar 179/2021; Lei 14.185/2021; Emenda Constitucional 106/2020.
- McLeay, M.; Radia, A.; Thomas, R. (2014). "Money creation in the modern economy". *Bank of England Quarterly Bulletin*, 2014 Q1.
- Mishkin, F. (2019). *The Economics of Money, Banking and Financial Markets*. 12ª ed. Pearson, cap. 15, "Tools of Monetary Policy".
- Poole, W. (1970). "Optimal choice of monetary policy instruments in a simple stochastic macro model". *Quarterly Journal of Economics*, 84(2), p. 197–216.
- Taylor, J. (1993). "Discretion versus policy rules in practice". *Carnegie-Rochester Conference Series on Public Policy*, 39, p. 195–214.

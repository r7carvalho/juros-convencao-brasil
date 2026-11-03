# Aplicação do relatório 12c às vozes heterodoxas (12.5, 12.5.1 a 12.5.7)

## Aplicação (03/11/2026)

Escopo: as seções 12.5 e 12.5.1 a 12.5.7 de `_revisao/12c.md`, mais os achados transversais que atingem essas páginas (correções 1, 2, 3 e 5 do resumo) e as decisões das partes A, B e C em `_divergencias.md`. O relatório 12c.md não foi editado. As oito páginas estão com estado "revisada". `build.py --check` passou sem ERRO (155 páginas), e `lint.py` saiu limpo nas oito páginas.

### Régua única (correção 1), aplicada como no ramo 12.2

- 12.5.1-5d (achado alto). O "pode levar a uma recessão muito séria" (Band, 12/02/2023) é fala de risco. Continua como proposição própria e passa de "não procede" para "procede em parte": o mecanismo era plausível na data (juro real perto de 8%, Focus de janeiro com PIB de 0,79%), o tamanho não tinha apoio e o risco não se materializou. É a mesma classe do "risco de crise severa" de Lisboa na 12.2.2, segundo o corretor da 12.2. A parte "esfriava sem combater a inflação" saiu do texto da proposição, porque não está na fala reproduzida.
- 12.5.2-3b. Continua "não procede" como proposição própria, porque o "nunca/nenhum" tem contraexemplo (Collor em 1990, Rússia em 1998). A conta por trás dela fica em 3a, que procede. É o mesmo recorte do "nenhum país" de Mansueto na 12.2.3.
- 12.5.2-2b. "O aperto derrubava a economia" vem do título da entrevista à FPA, e os trechos lidos não datam nem dimensionam a queda. Passa de "não procede" para "falta evidência", com o resultado pesando contra (decisão A sobre títulos).
- 12.5.5-2d. É contrafactual que a própria página diz que ninguém mediu. Passa de "não procede" para "falta evidência" (decisão C).
- 12.5.5-3c. "Postura política do Copom contra o governo" é proposição de intenção. Passa de "não procede" para "falta evidência"; o padrão de 2025 aparece como peso contra (decisão C). As de intenção nas 12.5.2-5a, 12.5.3-4a e 12.5.7-1c, 2b e 3b já estavam em falta evidência, e o texto agora diz que a intenção não se mede e que o padrão de decisões pesa contra.
- 12.5.6-3b. "Os sinais de recessão se acumulam" descreve uma recessão em curso, e não um risco. Fica como previsão de recessão, "não procede" pelo resultado, e o texto explica por que a classe difere da 12.5.1-5d.
- 12.5.3-8c. "Poderia levar à recessão em 2027" é fala de risco condicional sobre o futuro. Fica em falta evidência, e o texto passa a chamá-la assim.
- 12.5.4-4a, recessão no 1º semestre de 2021, "desfecho mais provável". É previsão de recessão e continua "não procede".

### Achados por página

Aplicados:

- 12.5
  - 1: a comparação "17 em 128 contra 7 em 144" saiu. A página diz que a comparação com a 12.2 fica para a recontagem do bloco na página 12.
  - 2: rótulos trocados por links.
  - Contagem refeita.
  - Acrescentados a regra das aspas (só trecho conferido; o resto é paráfrase com link) e a régua das previsões.
- 12.5.1
  - 1 (alto): ver acima.
  - 2: a aspa de 13/01/2017 virou paráfrase com link para a resenha de Aggio.
  - 4: a frase sobre local e ano de nascimento saiu.
  - 5: cortes na teoria e nos parágrafos 4b, 6b e 6c. Os cinco números repetidos aparecem uma vez cada.
- 12.5.2
  - 1: régua aplicada; 3b mantida, ver acima.
  - 2: a frase do DR com Demori virou paráfrase, assim como a frase sobre o ativo de última instância.
  - 3: "bicho de pé" virou paráfrase com link.
  - 4: acrescentado "e voltou a subir em 30/10".
  - 5: link da Exame de 14/01/2016; o alerta de 2015–2016 é tratado como fala de risco que não se materializou.
  - 6: teoria e falas 2, 4 e 6 encurtadas.
  - 2b em falta evidência (título).
- 12.5.3
  - 1: o episódio da Grécia (2013) e o link da IstoÉ saíram.
  - 2 e 3: as aspas do Senado (18/06/2024) e do IHU (2021) viraram paráfrase com link.
  - 4: "primeiro de 40" tem agora link para a 2.1 (MoneYou e Lev, 16/09/2026).
  - 5: a fala 1 se apoia só na coluna de 04/10/2019; a coluna de 2018 aparece só como antecedente, e o resumo e a 12.5 passam a dizer "2019 a 2026".
  - 6: saiu o brinquedo das reservas (a conta ficou numa frase com link para a 10.3.6), e 6b foi encurtada com link para a 3.2.
- 12.5.4
  - 1: "Eu nunca disse..." e "About 53 per cent..." / "Even if the Selic..." viraram paráfrase.
  - 2: o brinquedo e a dedução do limiar saíram, com remissão à 12.4.2; ficou o limiar de 0,87.
- 12.5.5
  - 1: no resumo e na 12.5 as falas são separadas por data, sem ligação com o cargo. O painel diz só que desde ago/2024 ele fala como diretor-executivo do FMI e que essas falas são classificadas como as demais. Saíram "Já no FMI" e "Depois de assumir o cargo".
  - 2: 2d em falta evidência.
  - 3: 4c passa a ser "provavelmente fecharia".
  - 4: as aspas da CartaCapital de 28/10/2021 e do X de 24/05/2024 viraram paráfrase com link.
  - 5: o modelo de conflito ficou numa frase com remissão à 1.2.1 e um brinquedo curto; a nota técnica de 2020 foi resumida, com remissão à 10.2.2.
  - Também: 3c em falta evidência (intenção).
- 12.5.6
  - 1: a proposição explica a diferença de régua (inflação do ano corrente contra Focus de 12 meses) e diz que o ex-post decide.
  - 2: as aspas do Hora do Povo de 19/06/2020 e 23/03/2023 viraram paráfrase com link.
  - 3: "jun/2026" no lugar de "Copom de 17 de junho".
  - 4: teoria e falas 5 a 7 encurtadas.
  - Também: o CDS passou de "entre 110 e 152" para "de 120,2 para 151,6 pontos em 26/10/2026".
- 12.5.7
  - 1: "Há 20 anos, afirmo..." virou paráfrase.
  - 2: o resumo diz agora "entre 6% e 7%, faixa que o painel confirma desde 1999 e acha maior, 8,1%, desde 1995"; a proposição 4a também passou a dizer isso, e a classe continua "procede".
  - 3: a vírgula dupla foi corrigida.
  - 4: "dispensa a hipótese de ação coordenada".
  - 5: teoria encurtada.
  - Também: o local e o ano de nascimento saíram (decisão B), e o CDS foi corrigido para 120,2 → 151,6.

Transversais:

- A relação comercial ficou só em "Quem é" nas sete páginas; não havia frase dela fora dessa seção.
- Os parágrafos sobre o acesso às fontes saíram das sete páginas, e a regra das aspas ficou uma vez na 12.5.
- Rótulos 12.4a a 12.4j: viraram links nas oito páginas (a → 12.4.1 … j → 12.4.10), e saiu a frase "Os rótulos 12.4a a 12.4j são os do mapa".
- Os cinco números repetidos (10,1 de 11,2; 96%; R$ 61,7 bi; −1,0 do Focus; 4,38 de 6,31) aparecem no máximo uma vez por página, com link para a página dona; nas demais menções viraram remissão sem número.
- As páginas não citam Ibovespa nem DI jan/29.

### Aspas conferidas por WebSearch (modo standard, 03/11/2026)

Oito buscas foram feitas. Nenhum dos trechos literais abaixo apareceu, e todos viraram paráfrase fiel com link:

- Bresser-Pereira, "Há 20 anos, afirmo...". A busca acha a tese no PDF do artigo da Ilustríssima de 18/12/2024, que situa a quase estagnação em 30 anos, mas não acha a frase.
- Lara Resende, "sólidas credenciais analíticas", 13/01/2017.
- Belluzzo, "bicho de pé", 12/05/2022. A URL do Vermelho tem o título, mas o texto da fala não foi conferido.
- Carvalho e Stiglitz, "53 per cent" e "Even if the Selic...", 20/10/2026.
- Roncaglia, CartaCapital de 28/10/2021 e X de 24/05/2024.
- Oreiro, Hora do Povo de 19/06/2020 e de 23/03/2023.

Pelo relatório, viraram paráfrase também os trechos com conteúdo confirmado e texto literal não confirmado: Belluzzo no DR com Demori (as duas frases), Nogueira Batista Jr. no Senado em 18/06/2024 e no IHU em 2021, e Carvalho no Vermelho em 24/06/2018.

### Não aplicados

- 12.5.1-3: a variante "fatos" do PDF do site de Bresser-Pereira, contra "dados" no Conjur. A aspa fica com o texto do Conjur, que o revisor verificou, e a variante fica registrada aqui.
- 12.5.2-1, alternativa "fundir 3a e 3b". Não foi aplicada porque a régua do ramo 12.2 separou o "nenhum país" de Mansueto e o classificou como "não procede", e a régua única pede o mesmo recorte.
- Limite de 3.500 palavras. As páginas caíram de 4.331–4.716 para 4.007–4.428 (wc), sem atingir o limite. O que resta é sobretudo a tabela-resumo (de 16 a 20 proposições), o Para ler e as falas com dados; cortar mais tiraria falas ou proposições, e a decisão C diz que cortar substância não é objetivo.

### Pendências

- Conferir na fonte original, quando houver acesso, as aspas que ficaram como citação sem verificação pelo revisor. São as que o relatório chama de "demais trechos": IHU de 22/12/2024 (Belluzzo), *El País* e IHU de 2018 e Project Syndicate de 10/06/2026 e 14/10/2026 (Carvalho), blog Sobre Economia de 2021 e *Correio Braziliense* de 2025 (Roncaglia), *Revue de la régulation*, Phenomenal World e *Insight Inteligência* (Bresser-Pereira).
- A recontagem do bloco e a comparação entre escolas ficam para o item próprio da página 12. Elas só entram na 8.1 com a contagem nova.

### Contagem nova do ramo 12.5 (somada das tabelas por script)

| Página | Total | Procede | Em parte | Não procede | Falta evidência |
|---|---|---|---|---|---|
| 12.5.1 Lara Resende | 17 | 5 | 7 | 3 | 2 |
| 12.5.2 Belluzzo | 19 | 7 | 8 | 1 | 3 |
| 12.5.3 Nogueira Batista Jr. | 20 | 10 | 7 | 1 | 2 |
| 12.5.4 Carvalho | 20 | 9 | 9 | 1 | 1 |
| 12.5.5 Roncaglia | 18 | 3 | 8 | 3 | 4 |
| 12.5.6 Oreiro | 18 | 4 | 7 | 4 | 3 |
| 12.5.7 Bresser-Pereira | 16 | 5 | 7 | 0 | 4 |
| Ramo | 128 | 43 | 53 | 13 | 19 |

Antes eram 128 = 43 / 52 / 17 / 16. O balanço em `_divergencias.md` ("Achados do bloco 12 para a matriz final") ainda traz os números antigos e a comparação suspensa; cabe ao item de recontagem atualizá-lo.

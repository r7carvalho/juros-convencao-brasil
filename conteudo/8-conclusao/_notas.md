# Notas do bloco 8 (Conclusão)

## Itens 8.1 e 8.2 do PLANO, 1ª versão (02/11/2026)

Escrita antes dos blocos 10 (completo), 11 e 12, porque o painel precisava ser publicado inteiro. As duas
páginas têm `estado: 1ª versão` e uma `:::nota` no topo avisando que serão revistas.

### Páginas entregues

| Id | Arquivo | Palavras |
|---|---|---|
| 8 | 8-conclusao.md | 3.341 por `wc -w` (com frontmatter e Para ler); cerca de 2.600 de prosa no corpo |
| 8.1 | 8.1-matriz.md | 5.498 por `wc -w` (inclui os separadores das 25 tabelas e os alvos dos links); cerca de 3.950 palavras de texto no corpo, sem o Para ler |

Gráfico: `dados/8.1-matriz.json` (barras horizontais, valor = direção × força, de −3 a +3; mista = 0).

### Régua usada

Dois eixos: direção (a favor, contra, mista) e força (forte, moderada, fraca), com os cinco critérios da 9.1
(fonte, replicação, identificação causal, tamanho, estabilidade). A 9.1 ainda descreve quatro graus
(forte, moderada, fraca, contrária); a 8.1 explica a correspondência ("contrária" = direção contra, com
força própria). Sugestão: atualizar a seção "Força da evidência" da 9.1 para os dois eixos e trocar o
exemplo "cerca de três pontos acima de pares desde 2010" pela série por década (6,6 / 3,1 / 5,5).

### Proposições e classificação

| Linha | Proposição | Direção | Força | Páginas-fonte principais |
|---|---|---|---|---|
| P1 | Juro real persistentemente acima dos pares | A favor | Forte | 2.1, 6, 9 |
| P2 | Patamar não explicado pelo fiscal corrente | A favor | Moderada | 2.2, 2.5, 6.1 |
| P3 | Convenção que se autorreforça | Mista | Fraca | 2.3, 2.4.1, 2.5, 1.2.3, 5.3, 6.4.2, 10.1.2, 10.2.1 |
| P4a | Política monetária perdeu a eficácia | Contra | Forte | 2.4, 6.2, 6.4.3 |
| P4b | Perdeu potência e ficou cara | A favor | Moderada | 2.4, 6.2, 6.2.2 |
| P5a | Decisões indexadas ao juro de um dia | A favor | Forte | 5.3, 3.3, 10.2.2, 2.5 |
| P5b | Juro supera há anos o retorno do capital | Contra (a favor em 1995–99 e 2003–06) | Moderada | 5.1, 5 |
| P5c | Margem comprimida frente aos pares | A favor | Moderada | 5.1, 6.1 |
| P6a | Juro alto reduz o investimento | A favor | Moderada | 5.2, 1.6 |
| P6b | Juro é o freio principal | Contra | Fraca | 5.2, 4.3, 5.4.2, 2.5 |
| P7a | Juro como motor da dívida | A favor | Forte | 3.2, 3.1, 3.4 |
| P7b | Dívida → prêmio → juro (dominância ganha peso) | Mista | Moderada | 6.1, 6.1.1, 1.5, 1.5.2, 3.4 |
| P8a | Credores recebem renda grande | A favor | Forte | 3.3, 5.4.2, 5.4.3 |
| P8b | Quem lucra sustenta o patamar | Contra | Fraca | 2.4.1, 6.4.1, 2.5 |
| P9a | Picos de inflação vêm de choques | A favor | Forte | 4.1, 4.2, 4.3, 4.5 |
| P9b | Inflação sem componente de demanda | Contra | Forte | 4.3, 4.4, 4.5 |
| P9c | Alarme desproporcional aos dados | Mista | Fraca | 4.5, 6.2, 2.4.1 |
| P10 | Focus enviesado para cima | Contra | Forte | 2.4.1, 6.4.1 |
| O1a | Prêmio fiscal move as oscilações | A favor | Forte | 2.2, 6.1.1, 1.5.2 |
| O1b | Prêmio fiscal explica o patamar | Contra | Moderada | 6.1, 6.1.1, 3.4 |
| O2a | Selic afeta crédito, câmbio e inflação | A favor | Forte | 6.2 |
| O2b | Selic com custo comparável ao dos pares | Contra | Moderada | 6.2, 6.2.2, 4.4, 4 |
| O3 | Poupança baixa e neutro alto | Mista | Fraca | 6.3, 6.3.1, 6.3.2 |
| O4 | Não cortar sem âncora fiscal | A favor | Moderada | 6.2.1, 4.2, 6.4, 6.4.2, 6.4.3 |

### Fontes internas usadas

BRIEF.md, CONTEXTO.md, conteudo/_divergencias.md (todas as seções de decisão, inclusive a convenção única do
juro real ex-ante e o viés do Focus), 9.1; páginas macro 1, 2, 3, 4, 5, 6, 7 e 10; todas as caixas
`:::painel`, `:::afavor` e `:::contra` de conteudo/*/*.md (219 caixas, extraídas por script); páginas filhas
abertas para número ou nuance: 2.4.1 (robustez do teste do Focus: +0,7 sem 2002, +0,5 só com dezembros,
t ≈ 2,2, −0,2 em 2015–2019), 2.5 (tabela de previsões da convenção e tabela do resíduo), 2.1 (ranking de
16/09/2026). Resumos de conteudo/_revisao/*.md lidos no topo.

### O que rever depois dos blocos 10 a 12

- Bloco 10: a 10.2.5 (regra de Taylor; já há `dados/10.2.5-selic-regra-taylor.json` e
  `10.2.5-neutro-implicito.json`) pode entrar em P2, P3 e O2b. A 6.2 já diz que a regra com os coeficientes
  de Taylor (1993) e neutro de 5% dá Selic perto de 10,5% em out/2026, contra 13,75%; a 8.1 não usou o número
  porque a página dona ainda não existe. A 10.2.6 (comunicação) entra em P3 (sistema autorreferente); a 10.5
  (transponível) entra na direção de política da página 8; a 10.4 (Blanchard) em P7b.
- Bloco 11: 11.5 (risco fiscal), 11.6 (regras) e 11.7 (sustentabilidade) entram em P7b e O1b; 11.4
  (armadilhas conceituais) pode afetar P7a (conceito de dívida e de juros).
- Bloco 12: é a única fonte possível para P9c ("alarmismo" no discurso público) e parte de P8b (quem fala e
  com que interesse); 12.3 (economistas de mercado e Focus) entra em P10 e P8b; 12.4j (jargões do outro lado:
  "inflação é só choque externo", "o BC trabalha para os bancos", "metade do orçamento vai para juros") entra
  em P9a, P8b e P7a com o mesmo rigor; 12.5 (vozes heterodoxas) pode trazer formulações de P3 que possam
  perder.
- Testes que mudariam linhas e não foram feitos (listados nas duas páginas): estudo de evento diário com
  comparação a outras moedas emergentes; decomposição da curva em prêmio a termo; neutro dos pares pelo mesmo
  método; retorno do capital pós-2019; CEI completa; comparação com países de risco fiscal semelhante e
  histórico inflacionário diferente.

### Divergências e pendências notadas em outras páginas (não editadas)

- 1.4, `:::painel`: "três pontos acima dos pares mesmo em anos de superávit primário (como em 2003–2008)";
  pela decisão da revisão da área 1, 2003–2008 é 5 a 8 p.p. A 8.1 usa 5 a 8.
- 6.1, `:::contra`: "5,6 a 9,1 pontos acima da média dos pares" em 2003–2008 (por ano) e 6 macro "5 a 9
  pontos"; a decisão de _divergencias.md é 5 a 8 p.p. (média do período). A 8.1 e a 8 usam 5 a 8.
- 2.5, tabela do resíduo: "LFT em 52,74% da DPF em ago/2026, recorde"; a decisão é não usar "recorde".
- Juro real ex-ante acima de 9%: "maio de 2025 a agosto de 2026" (2.2, 2.4) e "jun/2025 a ago/2026" (6.2,
  Selic meta). A 8 e a 8.1 escrevem "de meados de 2025 a agosto de 2026".
- Juro real ex-ante de 2012: 1,68% (média anual, JSON 2.3) e 1,55% (dez/2012, 6.2.1 e 6 macro). A 8.1
  escreve "1,5% a 1,7%, conforme o método".
- 10 macro: citava as frentes de coleta pelo nome e tinha marcas de pendência; resolvido depois, na passada de consistência.
- Nenhum número novo entrou nas páginas 8 e 8.1: todos vêm de páginas já revisadas ou de
  _divergencias.md.

## 2ª versão (03/11/2026)

Itens 8.1 e 8.2 refeitos depois dos blocos 10, 11 e 12 (e da conclusão do bloco 12, item 12.C). Também atualizadas as páginas 0 e 0.1. As quatro páginas ficam com `estado: 2ª versão`: os números foram conferidos com as páginas donas e com `_divergencias.md` (seções dos blocos 10 e 11, do bloco 12, das revisões A, B e C e do item 12.C), mas a forma nova não passou por revisor independente.

### O que mudou na matriz (8.1)

| Linha | 1ª versão | 2ª versão | Motivo |
|---|---|---|---|
| P7b | mista, moderada | a favor, moderada | IFI (RAF 116: 3,16 p.p. do prêmio de 5 anos atribuídos à dívida bruta), RPM jun/2025 (dívida bruta significativa), FMI (um terço da depreciação de 2024). O efeito perverso de 2004, que deixava a linha mista, foi para a P7c. |
| P7c | (dentro de P7b) | contra, moderada (nova) | Dominância como regime: 2025 (Selic 15%, real de 6,19 para 5,50, IPCA 5,53 → 4,26), 12.4.4 (as duas ondas de 2015 e fim de 2024 terminaram com inflação caindo; 4 de 10 ciclos com real em queda, sempre com choque), 10.4; teste fraco por dólar fraco no mundo. |
| P9c | mista, fraca | mista, moderada | Alarme medido no bloco 12: 35 de 113 sentidos de jargão não procedem; alarme de quebra nos títulos e jargões, não nas proposições; nenhuma previsão de recessão procedeu; Focus erra a inflação para baixo (2.4.1, 12.3.1, 12.4.5: 13 de 16 anos acima da projeção de 3 anos). Fica mista porque o exagero é das frases prontas e mais fiscal que inflacionário. |
| O5 | não existia | a favor, forte (nova) | Trajetória da dívida: i − g +3,5 (2023–2025) e +6,2 (prévia 2026) (11.7); estabilizador 2,9–3,4 contra déficit 0,52; DBGG 71,7 → 82,9; meta de 1,5% em 2030 estabiliza só com juro real de 3,9% (12.4.9). Contra: 1 p.p. de juro real = 0,8 p.p. de superávit. |
| O6 | não existia | a favor, moderada (nova) | Teste de Bohn (11.7): ρ +0,062 na DLSP em 2002–2013, nulo depois, abaixo dos 0,04 das taxas de 2025; sem quebra com a DBGG; meta alterada em 12 de 21 anos (11.6). |

Sem mudança de nota, com evidência nova: P1 (mandatos 0,8 a 7,5 p.p. acima dos pares, 12.4.7); P2 (Lula 1 superávit 3,5% e juro 11,3%, Bolsonaro déficit 2,3% e juro 0,2%; Taylor 2025–2026 acima da regra com o neutro da ASA, 1,3 p.p., e do BC, 4,3 p.p.; primário reagia em 2003–2008 com juro já o mais alto); P3 (Morris e Shin e a fala do Copom, 10.2.6; orientação futura de 2020, três meses, 10.3.1; Focus 16 de 24 anos fora da faixa e erro de 3 a 4 desvios-padrão, 12.3.2; neutro que segue o juro observado, 12.4.5; WP 637; Blanchard 2023, equilíbrios múltiplos; contra: consenso preso ao patamar do dia, alto ou baixo, Selic abaixo da regra em 2012–2014 e 2018–2021, neutro implícito circular); P4a (resposta mais que um para um, 10.2.5; previsões heterodoxas de 2021 que falharam); P4b (reservas: R$ 189,5 bi = 1,41% do PIB em 12 meses até set/2026, um sexto dos juros, R$ 19 bi por ponto; custo líquido de R$ 66 bi em 2012–2025); P5a (over 0,10 abaixo da meta desde 2014); P7a (59% real, 11.2; i − g; 12.4.2 e 12.4.10; 16 de 20 proposições do bloco 12 procedem); P8a (juro real 6,23% do PIB, R$ 834 bi; preço relativo do VA financeiro, correlação 0,61; ROE bancário máximo em 2021); P8b (12.3.1 sem viés de Selic, 13 abaixo e 10 acima; projeção de 8% não mexeu na mediana; Copom indicado por Lula levou a Selic a 15%; intenção em falta evidência em 9 de 10); P9a, P9b (12.4.10); P10 (15 de 17 anos acima da projeção de dois anos, 13 de 16 da de três); O1a (11.5; 12.4.3, 7 de 12 saltos desfeitos em um ano, 1 em um mês; 22 de 27 proposições); O1b (risco legal 57,2 → 37,9% enquanto o prêmio subia; mandatos; fiscal como causa do nível procede em parte em 21 de 22); O2a; O2b (reservas, Taylor); O3 (neutro do BC 3% → 5%; Japão; quem escolhe o neutro escolhe o veredito); O4 (orientação futura de 2020 condicionada ao regime fiscal; períodos abaixo da regra seguidos de inflação acima do teto).

Total: 27 linhas (24 da 1ª versão + P7c, O5, O6). Gráfico `dados/8.1-matriz.json` refeito (27 barras, consulta 2026-11-03).

### Decisões

- **P11 (consenso das projeções) não ficou como linha própria.** Chegou a ser escrita como "as projeções erram juntas e se ancoram no presente e no Copom", a favor, moderada. Foi fundida na P3 para seguir a conclusão do bloco 12 (página 12, "O que isso diz das teses em teste": a forma fraca pertence à P3) e a 12.4.5, que deixa "consenso autorreferente que ancora num patamar" em falta evidência. A evidência dela (12.3.2, 12.3.1, 10.2.6, 10.2.5, Coibion e Gorodnichenko) está nas células de P3, e a leitura de P3 diz que a forma fraca procede como descrição das expectativas.
- **Reservas sem linha própria.** O custo das reservas é uma face do custo da Selic e entra em P4b e O2b; o custo líquido com o câmbio (R$ 66 bi em 2012–2025) quase zera o argumento como proposição da tese ou da ortodoxia.
- **r − g e Bohn como linhas ortodoxas (O5, O6)**, porque reforçam a preocupação fiscal sem explicar o nível; ficam separadas porque uma é identidade e a outra é estimativa de comportamento, com forças diferentes.
- **Dominância fiscal separada em P7b e P7c.** O elo dívida → prêmio tem estimativa oficial; o regime em que o juro perde efeito não aparece em 2025. A 12.4.4 dá "procede em parte" ao fiscal no prêmio porque a Selic também entra; a matriz registra isso na leitura de P7b, que mostra o círculo passando pelo prêmio.
- **P8b fica contra, fraca**, e não moderada: os canais medidos vão contra, mas a influência em si não tem medida, e o bloco 12 deixou as falas de captura e coalizão em "falta evidência" (régua: contra com força fraca = falta evidência).
- **Resíduo não chamado de convenção.** A 8 diz explicitamente que o painel não usa o nome para o resíduo; a convenção aparece como candidata e, no sentido fraco, como descrição das expectativas.
- **Balanço do bloco 12**: contagem por script do item 12.C (12.1 = 113 = 54/39/4/16; pessoas 387 = 153/162/22/50, 5,7%; lado crítico 149, 10,1%; demais 238, 2,9%; 17 das 22 "não procede" são previsões ou conjuntura; linhas de previsão 15 de 47, demais 7 de 224). A contagem de 112/15 não é usada. Links para as âncoras `pagina:12#balanco-das-classificacoes`, `#matriz-pessoa-argumento-classificacao` e `#o-que-o-bloco-conclui`.
- **Regra de Taylor**: usado o par do resumo e da 10.5 (Selic de 2025–2026 1,3 p.p. acima da regra com o neutro de 8% da ASA e inflação do Focus; 4,3 p.p. com o de 5% do BC). A caixa da 10.2.5 traz outra forma (3,3 a 5,0 com o BC; 0,3 a 2 com a ASA, médias anuais por duas medidas de inflação); as duas convivem na página dona. A decisão de `_divergencias` fala em "acima em 2003–2010 e 2025–2026 e abaixo em 2011–2021"; a página revisada diz 2004–2009 e 2023–2026 acima e 2012–2014 e 2018–2021 abaixo, e a 8.1 segue a página.
- **FMI, primário estabilizador de 1,5%**: não usado, porque a 11.7 diz que o número veio de resumo secundário e não foi conferido.

### Página 8 (8.2)

Reescrita: o que cada área e cada bloco (10, 11, 12) mostrou; o que a evidência sustenta da tese e da leitura ortodoxa (seções de extensão parecida); o que nenhuma das duas explica (2018–2021, pares, neutro, desancoragem de 46 meses); seção nova "O que mudou desde a 1ª versão"; seção "O que pode mudar a conclusão" (estudo de evento, decomposição do prêmio do WP 637, neutro dos pares pelo mesmo método, comparação com países de risco semelhante, teste de manada com dados do Focus, retorno do capital, CEI, e acontecimentos que mudariam P7c e O1b). Direção com três parcelas e confiança declarada (alta, moderada/baixa, moderada/baixa), conjunto moderado. Saíram as notas de "será revista" e o parágrafo sobre blocos em construção.

### Páginas 0 e 0.1

0: resumo, caixa da direção, "Como o painel trabalha" (régua das quatro classificações), "Por onde começar" (blocos 11 e 12), e a seção "O que ainda está em construção" trocada por "O que o painel ainda não mediu" (lacunas de conteúdo, cada uma com link). 0.1: P3, P4b, P7b, P7c, P9c, P10, P8b, O4, O5, O6 atualizadas, com as âncoras novas conferidas pelo `build.py --check` (que agora verifica âncoras); seção nova "Como ler uma página do debate público" com a tabela das quatro classificações, as regras próprias e o balanço; estado "2ª versão" explicado no parágrafo de estados.

### Pendências

- Revisão independente das quatro páginas (8, 8.1, 0, 0.1) antes de marcá-las "revisadas".
- A caixa `:::painel` da 12.1 ainda diz 112 e 15 (fora do escopo; registrado no item 12.C).
- A 9.1 ainda descreve quatro graus de força; a correspondência com os dois eixos e com as quatro classificações do bloco 12 está na 8.1 e na 0.1.
- O link de O5 termina em hífen porque o `slug` corta o título em 60 caracteres; funciona, mas um título mais curto deixaria a âncora mais limpa (exigiria trocar o link na 0.1).
- A 8.1 tem cerca de 8.600 palavras no corpo, por causa das 27 tabelas; a 8 tem cerca de 5.000 de prosa.

## Revisão aplicada (03/11/2026)

Correção feita a partir de `conteudo/_revisao/8.md` (62 achados) e da seção "Decisões da revisão da conclusão" de `conteudo/_divergencias.md`. As quatro páginas (8, 8.1, 0, 0.1) passam a `estado: revisada`. O resumo da aplicação está no topo de `conteudo/_revisao/8.md`.

### O que mudou desde a 1ª versão (texto que saiu da página 8)

A 1ª versão da conclusão, de 02/11/2026, foi escrita antes dos blocos 11 e 12 e com parte do bloco 10. A direção geral não mudou: soma de causas, com confiança moderada no conjunto. Mudaram estas coisas, da 1ª para a versão revisada:

- P7b: de mista, moderada para a favor, moderada. As estimativas da IFI (RAF 116) e do BC (RPM de jun/2025) deram tamanho ao elo dívida → prêmio; a dominância como regime saiu para a linha nova P7c (contra, moderada).
- O5 (trajetória da dívida, a favor, forte) e O6 (primário que deixou de reagir, a favor, moderada) entraram com o bloco 11.
- P9c: na 1ª versão, mista e fraca; na 2ª versão, mista e moderada (com evidência tirada sobretudo das contagens do bloco 12); na versão revisada, dividida em P9c (alarme sobre a inflação: contra, moderada) e P9d (alarme fiscal, quebra e recessão: mista, fraca), cada uma com evidência primária (IPCA, Focus, PIB realizado, composição e trajetória da dívida).
- O7 (as expectativas do Focus como âncora técnica: mista, moderada) e O8 (causas estruturais do nível: meia-entrada, indexação e histórico de inflação, incerteza jurisdicional: mista, fraca) entraram na revisão para dar ao lado ortodoxo as linhas que faltavam.
- P3 ficou mista e fraca em todas as versões. Na 2ª versão a leitura dizia que "a forma fraca procede"; na revisada, o padrão das expectativas é "compatível com" uma convenção no sentido fraco e com rigidez de informação e choques comuns, e não conta como acerto da tese.
- P4b mudou de título ("perdeu potência e ficou cara" → "tem menos potência e custa mais que nos pares"); P5a passou a incluir "e às taxas do Tesouro".
- O custo das reservas, a regra de Taylor e a reação do Focus à fala do Copom entraram em P2, P3, P4b e O2b sem mudar a nota dessas linhas.

### Decisões da revisão

- Resíduo: forma da 2.5 em todas as páginas ("um resíduo que o fiscal corrente não explica, de cerca de 2 pontos (modelo do FMI, dados até cerca de 2011) a 4,5 (distância bruta para os pares em 2006–2013, sem controles)"). A distância para a regra de Taylor (0,3 a 2 com a ASA; 3,3 a 5,0 com o BC; corpo da 10.2.5) e os 3,16 pontos da IFI aparecem como medidas separadas, sem soma.
- Contagens do bloco 12: saíram das colunas de evidência de P3, P7a, P9a, P9b, P9c, O1a, O1b e O2a. Ficam na seção própria "O balanço das vozes do debate", como descrição do debate ("as vozes dos dois lados concordam"), sem "reforça".
- Fato comum: P1, P5a, P8a e O5 marcados no quadro, no texto da linha e na nota do gráfico.
- Régua: definição de forte, moderada e fraca copiada da 9.1; saiu a frase sobre o grau "contrária". Tradução para o bloco 12 com a condição "nenhuma evidência forte contra".
- O6 ficou moderada (achado 16 sugeria fraca se os estudos não fossem nomeados): os quatro estudos da 11.7 com métodos diferentes (Luporini, 2015; Campos e Cysne, 2019; Campos, Cysne e Madureira, 2022; Oliveira, Nobrega e Maia, 2022) passaram a constar na linha e no Para ler, com Mendonça, Santos e Sachsida (2009) como exceção.
- O8 é uma linha só, como decidido em `_divergencias.md`, e não as três (O8 a O10) que o revisor propôs; a leitura da linha separa a força de cada mecanismo.
- Não entrou coluna "No bloco 12" no quadro-resumo (achado 4 da 8.1): as diferenças de classificação estão explicadas nas linhas P3, P7b e O6.
- Tabelas de duas colunas da 8.1 trocadas por `:::afavor` / `:::contra` com listas curtas, seguidas de um parágrafo "Classificação: ..." com a direção, a força e a leitura. A coluna "Na 1ª versão" saiu.
- Gráfico `dados/8.1-matriz.json` refeito com 30 barras (P9c −2, P9d 0, O7 0, O8 0) e nota de fato comum.

### Pendências após a revisão

- A página 12 (tabela "Tese × o que o bloco mediu", linha "Alarme (P9c)", e a leitura "fica de pé a forma fraca ... que pertence à P3") deve passar a citar P9c (inflação, contra, moderada) e P9d (alarme fiscal, mista, fraca) e a dizer "compatível com" no lugar de "fica de pé". Fora do escopo desta correção.
- 12.2.2 (linha 124) e a caixa da 6.2.2 tratam o "cerca de 1 ponto" do direcionado como explicação; pela decisão, é conta de brinquedo. Ajustar a 12.2.2 para "numa conta ilustrativa".
- Extensão: a 8 tem cerca de 3.600 palavras de prosa (era 5.200), a 8.1 cerca de 9.400 no corpo (30 linhas), a 0 cerca de 1.800 e a 0.1 cerca de 3.100, todas acima das faixas de `_CONVENCOES.md`. A 8.1 encurtaria mais se as leituras de cada linha fossem reduzidas a uma frase.
- As pendências da 2ª versão sobre a 9.1 ("ainda descreve quatro graus") e sobre a caixa da 12.1 (112 e 15) estão obsoletas: a 9.1 já usa dois eixos e a 12.1 já diz 113 e 16.

## Integração da 13.10 na 8.1 (05/11/2026)

A 8.1 passou a citar a [13.10](pagina:13.10) em P2, P3, O1b, O8 e na lista "O que pode mudar a matriz", uma frase em cada, sem mudar classificação. Registro completo em `conteudo/_revisao/13b-integracao.md`.

Proposta de classificação: nenhuma. As razões, linha a linha:
- P2 (a favor, moderada): a comparação de 13 países aponta no mesmo sentido, com força moderada (uma seção transversal, rating como medida principal, reversão de 2018–2021), e não chega a forte porque não testa o risco que age pelas expectativas e pelo neutro.
- O1b (contra, moderada): mesmo argumento, do outro lado; a 13.10 não decompõe o prêmio e não muda a força.
- P3 (mista, fraca): a regressão mede o que sobra e não mede convenção; a 13.10 dá à convenção a mesma classe (falta evidência).
- O8 (mista, fraca): o Peru é contraexemplo único ao histórico de inflação, e sem ele o histórico não se estima; indexação e direcionado seguem sem medida comparável.
- Se um painel maior de países, com indexação, direcionado e histórico de inflação medidos, mantiver o resíduo brasileiro, P2 pode subir a forte e O8 descer a contra, fraca; até lá, nada muda.

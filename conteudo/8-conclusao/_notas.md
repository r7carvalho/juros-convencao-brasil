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
- 10 macro: ainda cita "Frente J" e "Frente K" e tem marcas "[a conferir]"; fora do escopo deste item.
- Nenhum número novo entrou nas páginas 8 e 8.1: todos vêm de páginas já revisadas ou de
  _divergencias.md.

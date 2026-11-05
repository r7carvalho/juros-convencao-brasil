# Cartão do bloco 13 (a proposta de Lara Resende para os juros)

Vale para todo item do bloco 13, junto com conteudo/_CARTAO_BASE.md e as regras de
conteudo/_CARTAO_PESSOA.md (fala pública com link e data, caridade, mesma régua).

## O que é o bloco

Um estudo da proposta de André Lara Resende para o juro brasileiro, publicada em "Eu acuso: uma
proposta para eliminar os juros absurdos" (25/09/2026) e explicada por ele em vídeos, entrevistas e
artigos. O objetivo é que o leitor entenda a proposta na forma mais forte, julgue a qualidade e a
coerência dela com a evidência do painel e saiba argumentar a favor e contra. A recepção na imprensa
foi majoritariamente crítica; o bloco julga a proposta pelo que ela diz, e não pela recepção, e julga
as críticas com a mesma régua.

## Leia antes

conteudo/_CARTAO_BASE.md; conteudo/_CARTAO_PESSOA.md; a seção 13 do PLANO.md; a página
conteudo/12-vozes/12.5.1-andre-lara-resende.md (o que o painel já concluiu sobre o autor, com 17
proposições classificadas); conteudo/7-politica/7.8-*.md (coordenação fiscal-monetária, onde a
proposta já está descrita); conteudo/_divergencias.md (números e decisões que valem para o painel,
inclusive a definição do resíduo e a régua única do bloco 12); conteudo/13-lara-resende/_notas.md
(o dossiê de fontes do bloco, quando existir).

## O que a proposta diz (base para todos os itens; confirme no texto e no dossiê)

- Transição: Selic de 13,75% para cerca de 7,5% ao ano em cerca de doze meses.
- Regra permanente: Selic numa faixa entre a meta de inflação (piso, 3%) e o crescimento nominal
  potencial do PIB (teto, 5,5%); fora da faixa só em caso excepcional autorizado por um conselho.
- Conselho Fiscal e Monetário Nacional, com metas conjuntas de juro, inflação e trajetória fiscal para
  quatro a cinco anos.
- Diagnóstico: o juro, e não o gasto primário, é o principal fator do desequilíbrio fiscal; o corte
  levaria o déficit nominal de mais de 10% para perto de 6% do PIB.
- Teoria: o juro é escolha do BC; juro nominal alto pode manter a inflação alta (leitura
  neo-fisheriana e teoria fiscal do nível de preços); recusa da teoria quantitativa e da âncora fiscal
  como pré-condição.

## Postura de método (vale para 13.8 a 13.10 e para qualquer correção)

- O objetivo é mostrar por que a proposta pode ser um argumento teórico consistente e onde ele para,
  sem afirmar que está certa ou errada antes do teste. Tirar dogmatismo dos dois lados: nem "juro
  alto é sempre racional porque o mercado decide", nem "juro alto é só convenção porque é alto".
- Correlação não é causalidade. Toda associação mostrada (juro × dívida, juro × risco, juro ×
  inflação) vem com as explicações alternativas: causalidade reversa, variável omitida, choque comum.
- Colinearidade: dívida, risco, inflação passada, câmbio e juro andam juntos no Brasil; quando duas
  variáveis se movem juntas, a regressão não separa o peso de cada uma, e a página diz isso.
- Economia é ciência social: poucas observações, regimes que mudam, expectativas que reagem à própria
  política (crítica de Lucas). A página diz o grau de confiança e o que mudaria a conclusão.

## Forma

Página com id 13.N, pai 13, ordem N, entre 2.500 e 4.500 palavras de prosa. Exemplo de brinquedo antes
do dado; recortes citados com link e data (vídeo com minutagem `mm:ss`); gráfico SVG com fonte e
data quando houver série (formato em _CONVENCOES.md, dados em dados/13.N-*.json); quadro A favor /
Contra com extensão equivalente; caixa `:::painel` com a leitura do painel separada de fato e de autor;
Para ler. Estado: 1ª versão.

## Regras

- Atribuição: só o que Lara Resende disse ou escreveu, com link e data; o que é leitura do painel vai
  na caixa `:::painel` ou em "o painel lê". A tese dos rentistas é de Bresser-Pereira, não dele; o
  "conservadorismo intelectual" é dele.
- Críticos e defensores com o mesmo tratamento: forma mais forte, link e data, classificação
  (procede / procede em parte / não procede / falta evidência).
- Nenhuma pessoa privada. Nenhuma alusão a quem pediu o estudo.
- Números: os de conteudo/_divergencias.md; o que for novo, com fonte primária ou cálculo do painel
  reproduzível (script em tools/analises/13.N_*.py, se houver conta).
- Português do Brasil, sem travessão no texto, sem "não é X, é Y", sem palavras vetadas do lint.

## Ao terminar

Notas na seção do item ao fim de conteudo/13-lara-resende/_notas.md (fontes usadas e descartadas,
linhas para a matriz da 13.7). Marque o item [x] no PLANO.md. `python3 tools/build.py --check` sem
ERRO e `python3 tools/lint.py <arquivo>` limpo. Não rode git nem o build sem --check.

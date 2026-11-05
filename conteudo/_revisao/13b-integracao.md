# Integração de 13.8, 13.9 e 13.10 ao bloco 13 e ao painel

## Aplicação da integração (05/11/2026)

Base: seção "O que a 13.7 (e a macro) precisam incorporar" e "Coerência com o resto do bloco e do painel" de conteudo/_revisao/13b.md; seção "Decisões da revisão de 13.8 a 13.10 (05/11/2026)" de conteudo/_divergencias.md (tabela das linhas 11 a 18). As páginas 13.8, 13.9 e 13.10 não foram editadas; os números citados foram conferidos no texto atual delas e em dados/13.10-resultados.json.

### Aplicado

**13.7 (conteudo/13-lara-resende/13.7-como-argumentar.md)**
- Matriz: linhas 11 a 18 com direção, força e classe da tabela de _divergencias, evidência a favor e contra e links para 13.8, 13.9, 13.10 e páginas donas (10.2.1, 4.4, 4.5, 6.2.2, 12.4.5, 13.4, 13.5, 2.1, 2.5, 10.2.5, 12.3.2, 8.1). A linha 13 virou 13a (custo do juro alto: mista, moderada) e 13b (corolário "o corte tem custo inflacionário pequeno": contra, fraca, falta evidência), como 8a e 8b. A matriz tem 20 linhas.
- Introdução da matriz, linha de fonte (13.1 a 13.6 e 13.8 a 13.10, com os scripts 13.8_islm.py e 13.10_risco.py) e parágrafo de contagem novo: as linhas novas não mudam direção nem força das linhas 1 a 10; a 15 e a 16 apoiam o diagnóstico; a 13b e a 14 pesam do lado da linha 6; a linha teórica da 13.9 (dois andares) entra como nota às linhas 3 e 6; as medidas da 13.10 não se somam às da 2.5 nem à da 10.2.5.
- dados/13.7-matriz.json: nove barras novas (11 +3, 12 0, 13a 0, 13b −1, 14 +2, 15 +3, 16 +2, 17 0, 18 −2), fonte e nota atualizadas.
- Argumentos novos A11 (pares de risco igual ou maior), A12 (Phillips plana barateia o corte pela demanda), C11 (a planura vem em parte da ancoragem; conserto cinco vezes mais caro com κ = 0,1) e C12 (a comparação mede o que sobra e não mede convenção; não testa o canal pelas expectativas e pelo neutro). Extensão: A11 e A12 com cerca de 440 palavras, C11 e C12 com cerca de 390; as duas mãos inteiras com cerca de 1.820 e 1.780.
- Armadilhas novas: do lado a favor, "o BC fixa o juro, logo qualquer nível serve" e "a curva de Phillips morreu"; do lado contra, "o juro é alto porque o risco é alto" e "o mercado decide" (a quarta vem do relatório, para manter cinco de cada lado; cerca de 480 e 515 palavras).
- Ressalvas da 13.9: no A5, o neutro por filtro segue o juro por construção (13.9; 10.2.5); na linha 6, o IPCA de 2019 foi de 4,31% com meta de 4,25%, e 2016–2017 aparece nas duas colunas como ambíguo (Selic nominal de 14,25% a 7% junto com a inflação, lida a favor pelo neo-fisheriano; juro real alto, lida pela convencional).
- Direção de conclusão: parágrafo novo "O que as páginas 13.8 a 13.10 mudam". A direção não muda; a premissa e o diagnóstico ficam mais firmes; a comparação de risco reforça o diagnóstico e não autoriza a inferência de que o corte por decisão funcione (crítica de Lucas); a Phillips plana corta dos dois lados e encarece a aposta nas expectativas. "Grau de confiança no conjunto" segue moderado, com a distância incluída no que os dois lados devem reconhecer. "O que mudaria a conclusão" ganhou os testes das linhas 12, 13, 16 e 17.
- Resumo, abertura (lista das páginas lidas, "síntese do bloco"), A favor / Contra (um item novo de cada lado), `:::painel` (duas frases sobre as três páginas) e Para ler (McLeay e Tenreyro, Hazell et al., Lucas; links para 13.8 a 13.10; scripts).

**Macro (conteudo/13-lara-resende/13-a-proposta-de-lara-resende.md)**
- "fecha o bloco" saiu: a 13.7 é "a síntese do bloco", e a matriz "reúne também as três páginas seguintes". No resumo, "termina com um guia" passou a "reúne tudo num guia".
- "o teste mais citado a favor da proposta" saiu; ficou "a comparação do juro brasileiro com o de países de risco igual ou maior".
- `:::painel`: cinco frases com o veredito das três páginas (premissa procede e não diz o nível; Phillips plana com apoio, ancoragem como ativo em risco; distância de 4,6 pontos em 2025 que o risco medido não explica, causa em aberto, sem autorizar o corte por decisão).

**8.1 (conteudo/8-conclusao/8.1-matriz.md)**: uma frase com link para a 13.10 em P2, P3, O1b, O8 e em "O que pode mudar a matriz", sem mudar classificação. Nenhuma proposta de mudança de classe; razões em conteudo/8-conclusao/_notas.md, seção "Integração da 13.10 na 8.1".

**2.5 (conteudo/2-juros/2.5-convencao-no-brasil.md)**: uma frase no fim da caixa `:::painel`, depois da sugestão de comparar com países de risco semelhante e histórico diferente: a 13.10 faz parte dessa comparação, o resíduo de 2,4 a 8,2 pontos é medida nova que não se soma às da página, e o Peru contraria o histórico de inflação como explicação.

### Não aplicado, e por quê

- O registro em _divergencias das medidas novas (achado 3 de "Coerência") já está na seção "Decisões da revisão de 13.8 a 13.10"; não editei _divergencias.
- A tabela de previsões da 13.2 ("0,25% em dez/2019 sem inflação acima da meta", achado 4 de "Coerência") pede a mesma ressalva da 13.9, e fica fora do escopo desta integração.

### Pendências e divergências notadas

- _divergencias diz "3,3 na média do período" para a distância aos pares de nota igual ou pior. Pelo script (dados/13.10-resultados.json, `risco_igual_ou_maior.ex_ante`) e pela 13.10, 3,3 (3,28) é a distância no juro ex-ante de 16/09/2026. A 13.7 usa "3,3 no ex-ante de 16/09/2026". Convém corrigir a frase em _divergencias.
- A 13.5 (linha do Brasil 2017–2019 e resumo dos precedentes) diz "inflação dentro da meta nos três anos", mas o IPCA de 2017 (2,95%) ficou abaixo do piso de 3%, como a própria 13.5 registra nas condições. A A6 da 13.7 herda a expressão; fica para a 13.5.
- A 13.8 diz agora que nenhum dos dois períodos de Hazell et al., sozinho, dá inclinação significativa. A 13.7 segue a classe decidida (linha 12: inclinação "pequena e não nula", procede em parte); se a 13.8 mudar essa leitura, rever a linha 12 e a A12.
- O CDS de agosto de 2026 (Colômbia acima do Brasil) ficou fora da 13.7, porque o relatório aponta que vem de página que o painel não abriu.
- Extensão: a 13.7 ganhou cerca de 2.000 palavras de prosa (lint: de 8.634 para 12.382 tokens no corpo) e fica acima das 4.500 do cartão. É a página de síntese e reúne nove páginas; o corte fica para a passada de estilo.

### Verificação

`python3 tools/build.py --check`: 166 páginas, sem ERRO. `python3 tools/lint.py` na 13.7, na macro, na 8.1 e na 2.5: zero travessão, zero contraste negativo, zero palavra vetada; as quatro com "Para ler" (a 2.5 mantém as 6 marcas de citação que já tinha).

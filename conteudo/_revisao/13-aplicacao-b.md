# Aplicação (05/11/2026), parte B: páginas 13.5, 13.6 e 13.7

Corretor da parte B do bloco 13. Aplicado o relatório conteudo/_revisao/13.md (seções das páginas 13.5 e 13.6 e
"O que a 13.7 precisa reconciliar"), com as decisões de conteudo/_divergencias.md, "Decisões da revisão do bloco
13 (05/11/2026)", e a subseção "Classes únicas escolhidas" gravada pelo corretor da parte A. O 13.md não foi
editado. Páginas 13.5, 13.6 e 13.7 passaram a "revisada". `python3 tools/build.py --check`: 163 páginas, sem ERRO;
`python3 tools/lint.py` nas três páginas: zero travessão, zero "não é X, é Y", zero vetadas, todas com "Para ler".
Nenhum script mudou: as contas novas (84% dos meses de 2017 a set/2026 com IPCA acima de 3%, 98 de 117) foram
conferidas com o SGS 13522 e batem com a 13.4 já corrigida; a LFT de 30,1% em 2011 vem da 7.2.

## 13.5 (precedentes)

Aplicados:
1. (g2) Resumo, condições de 2026 (linha da régua), seção 2017–2019, tabela e seção "Quais precedentes pesam":
   IPCA de 4,58% em set/2026 "acima do teto de 4,5% e subindo" (4,22% em agosto), Focus de 5,19% para 2026,
   primário deficitário; a partida de 2026 lida como mais parecida com a de 2011. A transição "tem precedente
   (2017–2019) em condições que 2026 não reúne". A caixa `:::painel` diz o mesmo. Um parágrafo novo declara a
   régua nos dois sentidos, e cada força tem o motivo de não subir (2017–2019: inflação abaixo da meta e teto de
   gastos; 2011–2013 e 2020–2021: causas sobrepostas e fiscal de 2011 melhor).
2. (g3) Item do Contra "Em todos os casos [...] a alta da inflação encerrou o regime" trocado pela forma do
   relatório (Japão saiu com a meta ao alcance; 2017–2019 sem choque); a frase equivalente da caixa também.
   Para manter o quadro equilibrado, um item novo de cada lado (Contra: partida de 2026 como a de 2011; A favor:
   juro real de cerca de 2,8% já sustentado).
3. (g3) LFT de 2011: "30,1% em 2011, 18,7% em 2014 ([7.2])" no texto e na tabela.
4. (g4) Turquia: "levou o juro real a cerca de −34% em 2022".
5. (g5) O exemplo de brinquedo foi para `:::exemplo`, e o 8,73% ficou fora da caixa.

Não aplicado: corte de extensão (cerca de 5.200 palavras de prosa). As correções acrescentaram texto e cortar
agora tiraria evidência dos episódios; fica para a passada de estilo do bloco.

## 13.6 (críticas e respostas)

Aplicados:
1. (g1) Régua única. FPA: citação literal ("O risco é de o Brasil resvalar numa recessão [...]"), tratada como
   fala de risco e classificada procede em parte, como a 5d da 12.5.1. Diário do Poder (dólar acima de R$ 9):
   falta evidência (número sem fonte, contrafactual não medido), na objeção 10, na seção das defesas e na tabela.
   A tabela de defesas virou "Defesa ou fala fora das dez objeções", com coluna de lado; entram a *Gazeta do Povo*
   (contra, procede) e o Diário do Poder (contra, falta evidência).
2. (g2) Gleisi Hoffmann: intenção ("ofensiva") em falta evidência; como juízo do alarme fiscal, procede em parte,
   alinhada com a P9d da 8.1 (mista, fraca).
3. (g2) NeoFeed lido com a frase seguinte, nas duas citações; "2020 desmente" virou "a intervenção não impediu a
   alta do dólar, num choque global que não isola o efeito do corte"; no balanço, a fala de 2022 lida inteira fica
   em falta evidência.
4. (g2) Alívio fiscal pela 13.3: R$ 193 bi no ano 1 (cerca de 1,4% do PIB), R$ 386 bi (2,9%) a partir do ano 2
   contra a Selic parada; 1,1%, 2,4% e 4,0% do PIB em 2027, 2028 e 2030 contra o Focus. Sai "2,9% em doze meses,
   menos que os 4%". A resposta do autor é julgada pela recessão (falta evidência) e procede no tamanho. Caixa A
   favor alinhada.
5. (g3) Crítica de Mauro Miranda à LFT na objeção 7, com a concessão ("No modelo de Cochrane, ele tem razão"),
   a citação literal ("Dívida que se reprecifica todos os dias depende, também todos os dias, da boa vontade de
   quem a carrega [...]"), a resposta do painel (caixa do Tesouro de 13,5% do PIB em ago/2026, 3.2; troca por
   compromissadas, 10.2.2) e a classe procede em parte.
6. (g3) Objeção 2: o teste de "recessão não reduz a inflação" passou a 2016–2017 e à 4.5; classe mantida em não
   procede, com força moderada e a ressalva dos administrados. Saiu "perdeu potência, não eficácia".
7. (g3) Objeção 8: procede em parte (evidência de longo prazo, Mishkin 1992 e Uribe 2022; nenhuma no Brasil).
   O resumo agora conta sete objeções em procede em parte e nenhuma em procede (fora a do fato legal).
8. (g3) Classes únicas: câmbio "neutralizados" não procede e "suavizar" procede; LFT neutraliza o repique, procede
   em parte; "coordenação, e não dominância", procede em parte, com Leeper para o conselho de maioria fiscal e
   Sargent e Wallace só para o financiamento monetário, que a proposta não prevê.
9. (g4) Vale: "procede em parte: a inflação subiu ao teto depois do corte, como ele diz; o 'desastre' e a cadeia
   até 2015–2016 juntam administrados e outros choques".
10. (g4) CEBRI: relato de segunda mão do Brasil 247 (01/11/2026) na abertura e na objeção 3, citado como fala do
    relato; caixa `:::painel` ajustada (resposta às reservas de segunda mão e genérica; real × nominal e rolagem da
    LFT sem resposta dele).
11. (g4) Oreiro "pelo resumo do Brasil 247 citado na 12.5.6; o original não foi lido".
12. (g4) Decisão do Copom de 04/11: fonte trocada pela manchete do BPMoney consultada em 05/11/2026; o SGS 432
    fica só para os cinco cortes.
13. (g4) "Uma dirigente partidária e um economista do programa de governo, que apoiou o conselho e não a faixa".
14. (g4) Opinião contra e a favor descritas pelo tipo de veículo, sem a ocupação do autor.
15. (g4) Aspas só em citação literal ("Não se trata de dominância fiscal, mas de coordenação"; "o efeito seria
    nenhum").
16. (g5) Exemplo de brinquedo na abertura (um credor, um devedor e uma regra de juro); "4%, número redondo", com
    as folgas de 9,5% e 3,5% pelos 3,875%; contraste "e sim no próprio artigo" reescrito.
Também: bola de neve com o primário (10,1 e 3,6 dos 11,2 pontos) na objeção 5, em Calabrez e em Gleisi.

Não aplicado: corte de extensão (cerca de 5.400 palavras de prosa), pelo mesmo motivo da 13.5.

## 13.7 (como argumentar), reconciliação

Aplicados os itens 1 a 9 da seção "O que a 13.7 precisa reconciliar":
1. Prêmio do DI jan/29: linha de base de 0,6 a 0,9 ponto em 19 e 20/10 e cerca de 3,3 pontos em 26/10 (números
   recalculados pela parte A: 0,61 a 0,85 e 3,28), em A4, na nota antes da matriz, na linha 8b e no indicador.
   Sai a divergência "5 contra 3,2", que as páginas 13.3 e 13.4 já resolveram.
2. Alívio: A2, linha 8a, direção de conclusão e caixa A favor com R$ 193 bi, R$ 386 bi (2,9%) a partir do ano 2 e
   1,1%, 2,4% e 4,0% contra o Focus.
3. NeoFeed: nenhuma linha dá "não procede" ao "efeito nenhum"; C3 cita a frase seguinte.
4. Conselho: procede em parte (linha 4, A8, C9), com Leeper no lugar de Sargent e Wallace para o veto da maioria
   fiscal.
5. Câmbio: "suavizar" procede, "neutralizados" não procede (linha 5). LFT: procede em parte (linha 6 e armadilha).
6. Regra de reação: "pela leitura convencional" em C1, na linha 7, no gráfico e na direção; 84% (98 de 117 meses
   de 2017 a set/2026) e os 21 meses da meta contínua no lugar dos 92% desde 2005.
7. Régua única: um parágrafo antes das armadilhas com FPA, Gleisi e Diário do Poder; a crítica de Mauro Miranda à
   LFT entra em C6, na linha 6 e na armadilha da LFT.
8. Precedentes: linhas 2 e 10, A6, C4, caixa A favor e `:::painel` com a condição que 2026 não cumpre.
9. "Único motor": linha 1, A1 e armadilha com a bola de neve (90%) e o primário (32%), com link para a 3.2.

Extensão das duas mãos depois das correções: A1 a A10 com 1.288 palavras e C1 a C10 com 1.338; armadilhas a
favor 259 e contra 258.

Matriz depois da correção: nenhuma direção ou força mudou, e o gráfico dados/13.7-matriz.json mantém os valores
(+3, 0, −2, 0, −2, −1, −3, +2, −2, −3, −2), com nota e rótulo da linha 7 atualizados. Mudaram as classes da
linha 4 (falta evidência para procede em parte), a peça da LFT na linha 6 (procede em parte) e a condição das
linhas 2 e 10.

Direção de conclusão: muda num ponto, a transição. A versão anterior dizia que quem defende com honestidade
defende "a transição condicionada"; a corrigida diz que o precedente favorável (2017–2019) ampara uma transição
que comece quando a inflação voltar ao intervalo e o primário tiver número, porque a partida de 2026 se parece
com a de 2011, e a caixa do painel põe essa condição na versão que a evidência sustenta. O resto se mantém, com
duas nuances: o tamanho do alívio confere com o texto (4% do PIB em 2030 contra o Focus), e o prêmio do DI tinha
linha de base baixa antes da eleição. Confiança no conjunto: moderada.

Não aplicado: item 10 (fora do bloco: 12.5.1, 7.8 e o nome da RED na 12.5.6). Está fora do escopo deste corretor;
fica para a revisão 13.R. Nas três páginas, a RED aparece só como "RED", sem o nome errado.

## Pendentes

- Corte de extensão da 13.5 e da 13.6.
- Os originais de Oreiro (Substack) e do post de Vescovi seguem não lidos; a fala do CEBRI segue de segunda mão.
- Números que outras áreas usam: nenhum mudou fora do bloco. Dentro do bloco, a LFT de 2011 (13.5: de "18,7% em
  2014" para "30,1% em 2011, 18,7% em 2014", Tesouro via 7.2) e a contagem da regra de reação (13.7: de 92% desde
  2005 para 84% em 2017–2026, SGS 13522, igual à 13.4).

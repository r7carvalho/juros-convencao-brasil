# Aplicação do relatório 12c às páginas de jargão (12.4 e 12.4.1 a 12.4.10)

Arquivo à parte do 12c.md, que outro corretor usa para as páginas 12.5.x.

## Aplicação (03/11/2026)

Base: conteudo/_revisao/12c.md (seções 12.4 a 12.4.10 e as correções transversais 1, 3, 4 e 5 do resumo), _CARTAO_CORRECAO.md, _CARTAO_JARGAO.md, _CARTAO_PESSOA.md e as decisões das partes A, B e C do bloco 12 em _divergencias.md. Todas as onze páginas passaram a "revisada". `tools/lint.py` sem vocabulário vetado, sem travessões e sem o contraste vetado; `tools/build.py --check` sem ERRO (155 páginas).

### Aplicados

**12.4**
- O parágrafo de 1.037 palavras virou cinco parágrafos curtos por grupo (fiscal; mercado e BC; moeda e vizinhos; outro lado; síntese), sem os números das filhas e com link para cada uma. A página foi de 2.322 para cerca de 1.380 palavras.
- Dennett saiu do Para ler, porque o texto não o cita.

**12.4.1**
- Teste de Bohn unificado pela 11.7: o primário reagiu até 2013 e deixou de reagir depois. Vale no texto e no quadro A favor; 12.4.4 e 12.4.9 seguem a mesma data.
- Datas completas: Diário do Nordeste, 06/01/2021; Fraga, 14/09/2021. A fala de Haddad (24/10/2025, seminário do IASP) passou a ter o link da Agência Brasil.
- CDS de 120,2 → 151,6 em 26/10/2026, no lugar de "110 em 9/10 → 152".
- DI jan/29 na forma única da parte B.
- O 96% aparece uma vez, com link para a 3.3; o 10,1 de 11,2, uma vez, com link para a 3.2.
- A fala de Raul Sena virou paráfrase.
- A pedido do coordenador, o título "colapso" do Economista Sincero passou a "falta evidência", como na 12.1.4 corrigida.

**12.4.2**
- Brinquedo: 3,1 → 3,3 pontos.
- Pessôa ("gastança") e Zema viraram paráfrase.
- O 10,1 de 11,2 aparece uma vez, com link para a 3.2, e saiu do resumo e do quadro Contra. O 96% aparece uma vez, com link para a 3.3.
- Cortes de redação.

**12.4.3**
- Gleisi em 28/11/2024, com a nota do PT no mesmo dia, e Diário de Pernambuco (28/11/2024) no Para ler.
- A Selic em 13,75% até o fim de 2026 aparece como hipótese: "supondo a Selic em 13,75%".
- Galípolo virou paráfrase sem a imagem do marinheiro, e Mendlowicz também virou paráfrase.
- Adrian, Crump e Moench saíram do Para ler.
- DI jan/29 na forma única. O 96% aparece uma vez, com link para a 3.3.
- Equilíbrio político:
  - as falas do governo caíram de cinco para três (Lula, Gleisi com a nota do PT, Lindbergh) e saiu a de Haddad;
  - entrou Rogério Marinho (Agora RN, dez/2024);
  - a página diz que a busca de 03/11/2026 não achou fala de político da oposição, com link e data exata, que use "o mercado reagiu/está nervoso" como veredito.
- Salto passou a ter data completa (17/09/2026).

**12.4.4**
- Lara Resende: a hipótese neo-fisheriana, "assim como" a dominância, em paráfrase, porque a aspa não foi conferida.
- As seções (c) e (f) ficaram em um parágrafo com link cada (12.4.3, 6.1, 11.5; 3.2, 8.1).
- "Desde o Plano Real", com a base legal (CF art. 164, § 1º; LRF art. 34), no resumo e no texto. "A partir de 2014" no texto, na tabela e no quadro.
- Veloso saiu. Otta (*Valor*) aparece como "sem link aberto".
- O R$ 61,7 bi aparece uma vez, no brinquedo, com link para a 2.4.
- Zeina, Ramos e Kliass viraram paráfrase.

**12.4.5**
- Horizontes refeitos com o script `12.4.5_desancoragem.py`:
  - três anos: 46 meses seguidos; entre +0,50 e +0,875 desde jun/2023; média de +0,71 em 2025;
  - quatro anos: 45 de 46 meses, com +0,43 em mar/2024; entre +0,43 e +0,85;
  - os dois em +0,50 desde out/2025.
  Valem no resumo, na tabela, no texto, na linha da classificação e no quadro A favor. Saiu o "mais raso, com 0,5 ponto".
- A proposição (d) "ficção de modelo para justificar juro alto" virou "o neutro segue o juro observado e não tem medida independente" (procede em parte). A intenção fica registrada como sem medida.
- A seção (d) foi resumida com link para a 10.2.5 e a 6.3.2. A tabela de revisões ficou.
- Fraga e Schwartsman viraram paráfrase.
- Juro real ex-ante "perto de 8,7%", pela convenção do painel, com link para a 2.1.

**12.4.6**
- (b) reclassificada: "a inflação brasileira recente vem principalmente da quantidade de moeda" passou de "procede em parte" a "não procede". A página remete à versão geral de Perini na 12.1.3.
- QE padronizado pela divergência nº 20: base de US$ 847,6 bi (ago/2008) a US$ 4.075 bi (ago/2014), ×4,8, nos três lugares.
- As seções (b) e (c) foram resumidas com link para 1.1.2, 10.3.7 e 10.3.8.
- O 4,38 de 6,31 aparece uma vez, com link para a 4.2.
- Campos Neto e Lula viraram paráfrase.
- Saíram a cédula de R$ 200 e a segunda fala de Guedes.

**12.4.7**
- A proposição de intenção "(e) para prejudicar o governo" passou a "falta evidência", como as demais de intenção do bloco. Entrou a proposição de resultado "o nível de 2023 era próprio daquela diretoria", que não procede.
- Equilíbrio político:
  - as falas do governo caíram para Lula (02/02/2023 e a CBN de 18/06/2024, aspa conferida) e Boulos (21/01/2026);
  - saíram Tebet, Ana Paula Lobato, o "adversário" de 21/06/2024, a segunda fala de Boulos e Lindbergh;
  - entrou Rogério Marinho (reação de fev/2023 à fala de Lula sobre a autonomia, Poder360);
  - a página diz que a busca não achou político da oposição que acuse a diretoria de Galípolo de motivo político.
- A checagem da Lupa saiu, sem link. "Herdeiro" virou "governo Bolsonaro".
- Fraga (*Veja*), Mendes, Zema, Campos Neto e Lula ("cavalo de pau") viraram paráfrase.

**12.4.8**
- Juro real argentino refeito pelo método da parte C: a Leliq de 28 dias reaplicada em cada trecho de 2023, com 75% em janeiro, 78% em 16/03, 81% em 20/04, 91% em 27/04, 97% em 15/05, 118% em 14/08, 133% em 12/10 e passes a 100% em 18/12. O rendimento foi de cerca de 162% no ano, contra 211,4% de inflação de dezembro a dezembro, o que dá real ex-post de cerca de −16% (antes, −25%). As taxas vêm dos comunicados do BCRA e do El Economista; a conta é do painel.
- A Turquia aparece como medida indicativa com a inflação passada. A coluna da Turquia saiu da tabela.
- "Guedes disse que exagerara" saiu, sem fonte.
- O Para ler foi completado com cerca de quinze fontes e ordenado.
- O resumo diz "quase toda em reais".
- Ibovespa −13,88% a 176.608 pontos, e PTAX +9,19% no lugar de "dólar".
- Zeina, Milei e Tarcísio viraram paráfrase, com as datas completadas. A Venezuela foi cortada para o essencial.

**12.4.9**
- Uma régua só, a do juro implícito 3,5 a 6,2 pontos acima do crescimento nominal, no lugar de "3,3 a 5,9 real".
- "Almoços menos visíveis" e o histórico do arcabouço ficaram em uma frase com link cada (10.3.6, 7.5, 7.9; 11.6).
- O R$ 61,7 bi aparece uma vez, com link para a 2.4. O 10,1 de 11,2 aparece uma vez, com link para a 3.2.
- Bohn "até 2013".
- Giambiagi, Reis, Mendes, Schwartsman, Leal de Barros e Haddad viraram paráfrase.
- Saíram Amorim, Salto e a matéria da Agência Brasil.

**12.4.10**
- "Metade do orçamento" foi reduzida aos números-chave com link para a 3.5, e a narração da tabela de inflação foi cortada.
- Galípolo (Expert XP) virou paráfrase.
- O 4,38 de 6,31 aparece uma vez, com link para a 4.2, e o Focus −1,0 também uma vez.
- Gleisi, Belluzzo (duas falas), Roncaglia e Sardenberg viraram paráfrase.
- A pedido do coordenador, saiu o post de Nigro de 12/06/2025. Saiu o resíduo de produção sobre a rede de consulta.
- Saiu o Sindicato dos Bancários.

### Não aplicados (e por quê)
- 12.4.1, Raul Sena (26/10/2026): o relatório pedia manter. A fala ficou como paráfrase, porque o post não foi verificado.
- Limite de 2.800 palavras: só a 12.4 e a 12.4.1 chegaram perto (12.4.1 com cerca de 2.890 palavras sem o Para ler). As demais caíram de 5% a 15% e seguem entre 3.200 e 4.400 palavras sem o Para ler. Foram cortadas as repetições e a narração que refaziam outras páginas. O que sobra é teste, tabela, classificação e exemplo com link, que a decisão da parte C manda preservar.

### Pendências
- Rogério Marinho na 12.4.3 (Agora RN, dez/2024) e na 12.4.7 (Poder360, fev/2023): a busca confirmou a fala e o sentido, mas os sites não abriram para conferir o texto e o dia exato. Por isso as duas falas estão em paráfrase e com o mês.
- 12.4.8:
  - o juro real argentino usa a sequência de taxas confirmada por comunicados do BCRA e pela imprensa; a data do degrau de 118% (14/08/2023) não apareceu na busca;
  - Guedes no Primo Rico (02/03/2021) segue não verificado;
  - "Jornal PP (2026)" está sem dia.
- Seguem como paráfrase, sem conferência literal, todas as aspas que o 12c lista como não verificadas. Ficam entre aspas só as conferidas (Tombini, a ata de 04/02/2025, Lula na CBN, Bolsonaro e Fraga na 12.4.1, Mansueto em 12/02/2025) e os títulos de matérias.

### Classificações que mudaram
- 12.4.6 (b), "a inflação brasileira recente vem principalmente da quantidade de moeda": procede em parte → não procede.
- 12.4.7 (e), "o Copom de 2023 mantinha o juro alto para prejudicar o governo": não procede → falta evidência (intenção). Entrou "o nível de 2023 era próprio daquela diretoria", que não procede. Saiu a linha "o BC tem lado político, nos motivos" (falta evidência), absorvida pela de intenção. A contagem da página não muda.
- 12.4.5 (d): reformulada para "segue o juro observado e não tem medida independente". Segue procede em parte.
- 12.4.1: a página cita o título do Economista Sincero como "falta evidência", seguindo a 12.1.4.

Contagem nova das tabelas do ramo 12.4 (10 páginas): 113 proposições = 28 procede / 33 em parte / 35 não procede / 17 falta evidência.

### Números que mudaram e que outras áreas usam
- Juro real argentino em 2023: cerca de −25% → cerca de −16% (ex-post, Leliq acumulada contra o IPC de dez/dez; 12.4.8). A faixa "−25% a −87%" saiu da 12.4. Se a 6.4.3 ou a 10.3.8 usam −25%, convém alinhar.
- Distância do Focus à meta (12.4.5): três anos entre +0,50 e +0,875 desde jun/2023, média de +0,71 em 2025; quatro anos em 45 de 46 meses. A conta é do script 12.4.5.
- CDS em 26/10/2026: 120,2 → 151,6 (12.4.1), conforme a decisão da parte A.
- QE americano: ×4,8 de ago/2008 a ago/2014 (12.4.6, divergência nº 20).
- Teste de Bohn: reação até 2013 em 12.4.1, 12.4.4 e 12.4.9, conforme a 11.7.

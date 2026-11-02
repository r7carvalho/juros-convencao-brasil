# Notas do bloco 12 (Vozes do debate)

## 12.0

Página entregue: `conteudo/12-vozes/12-vozes-do-debate.md` (id 12, pai 0, ordem 10, estado 1ª versão). Cerca de 2.100 palavras de prosa fora das tabelas, da citação, das fórmulas e do "Para ler"; o `tools/lint.py` conta cerca de 3.300 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada. `build.py --check` sem erro; avisos só para os links de 12.1 a 12.5, que ainda não existem.

Estrutura: por que o bloco existe (Keynes, cap. 15, p. 203, recorte já usado na 1.4; Orléan e a saliência, por paráfrase, com links para 1.4 e 1.4.3; contraponto de 6.4.2 de que opinião sem fundamento não sustenta a curva; ligação com as linhas P9c e P8b da 8.1, que ficaram à espera deste bloco); regras do bloco em prosa (fala pública com link e data, nada de vida privada nem ataque pessoal, relação comercial pública registrada sem juízo de sinceridade, princípio da caridade com Wilson 1959 e as regras de Rapoport em Dennett 2013, concordar quando procede, previsão julgada ex-ante e ex-post com Tetlock 2005, jargões repetidos remetidos a 12.4, critérios de seleção das falas, identidade confirmada antes de escrever, heterodoxos com a mesma régua); exemplo de brinquedo "o Brasil vai quebrar em dois anos" com números inventados (dívida 80% do PIB, 95% em moeda própria, juro real 7%, crescimento 2%, déficit primário 0,5%, caixa para sete meses), desmontado em A1 (não procede), A2 (procede), A3 (procede em parte), A4 (falta evidência), com a fórmula de 3.1 e conta resolvida (80 → 84,42 → 89,06; primário estabilizador 3,92%); tabela da régua das quatro classificações com a correspondência para direção e força da 9.1; estrutura 12.1 a 12.5, um parágrafo cada; matriz pessoa × argumento × classificação só com o cabeçalho (oito colunas) e nota de preenchimento; mapa dos jargões 12.4a a 12.4j com o que será testado e as páginas de evidência, sem classificação; caixa `:::painel`.

Nenhuma pessoa do debate é nomeada. Autores citados só como teoria ou método: Keynes, Orléan, Wilson, Dennett (e Rapoport, por ele), Tetlock.

Fontes principais: Keynes (1936, cap. 15, p. 203, mesma tradução da 1.4); Orléan (2011), por paráfrase via 1.4 e 1.4.3; Dennett (2013); Wilson (1959); Tetlock (2005); páginas 1.4, 1.4.3, 3.1, 6.4.2, 7.7, 8.1, 9.1, 11.7.

Lacunas e pendências:
- Dennett, Wilson e Tetlock entram por paráfrase de conhecimento geral das obras, sem recorte entre aspas; conferir capítulo e página das regras de Rapoport em *Intuition Pumps* se a revisão 12.R quiser recorte.
- Os ids das filhas seguem `_CONVENCOES.md` (12.1 a 12.5, com netas 12.x.y). O PLANO usa rótulos de item 12.4a a 12.4j; a página de cada jargão terá id 12.4.x e o mapa da 12 deve ganhar os links quando elas existirem (hoje cita só os rótulos do plano).
- 12.4h: a Venezuela não tem página no painel; a evidência de hoje cobre Argentina e Turquia (6.4.3, 7.7). O item 12.4h precisa trazer dados próprios da Venezuela.
- 12.4b: a analogia "o governo é como uma família" não tem tratamento direto em nenhuma página; 7.7 (dívida em moeda própria) e 11.2 dão a base. O item terá de escrever a parte da analogia.
- A matriz pessoa × argumento × classificação começa vazia; cada página de pessoa deve acrescentar as suas linhas na tabela da página 12 (e a conta por grupo para a P9c, prometida no texto, só faz sentido com várias páginas publicadas).
- A `_CONVENCOES.md` dá 800 a 1.500 palavras para página macro; o cartão do item pediu 1.500 a 2.500, e a página segue o cartão.

Números que divergem de outras páginas: nenhum. A página não usa dado real; os números do exemplo são inventados e a fórmula é a da 3.1.

## 12.1a

Páginas entregues: `conteudo/12-vozes/12.1-influenciadores.md` (id 12.1, pai 12, ordem 1, 1ª versão; cerca de 990 palavras de prosa fora do "Para ler") e `conteudo/12-vozes/12.1.1-investidor-sardinha.md` (id 12.1.1, pai 12.1, ordem 1, 1ª versão; cerca de 2.700 palavras de prosa, contando a tabela-resumo fora). `lint.py` sem travessão, sem "não é X, é Y", sem palavra vetada; `build.py --check` sem erro, com avisos só para 12.1.2 e 12.1.3, que ainda não existem.

Confirmação de identidade: confirmada. O canal no YouTube se chama "Investidor Sardinha l Raul Sena" (youtube.com/@investidorsardinha); o site da AUVP (auvp.com.br) diz que a escola foi fundada em 2020 por Raul Sena, "também conhecido pelo canal o Investidor Sardinha"; a conta no X é @oraulsena, com bio de fundador da AUVP Capital; perfis do Investidor10 (set/2025) e do Melhor Investimento (ago/2025) dizem o mesmo. Livro: nenhum confirmado. Um site de baixa confiança (Sopa Cultural) cita um livro "Lucro FC" e outro (Gorila) cita o guia "Me Poupe!", que é de outra autora; nenhum dos dois entrou.

Rede: YouTube, Investidor10, Melhor Investimento, Monitor do Mercado, Contadores.cnt.br, Jornal Opção, zeno.fm e videohighlight.com não abriram por fetch. Tudo veio de WebSearch (trechos e paráfrases reproduzidos pela página de busca). Datas de posts no X tiradas do id do post (snowflake): 18/09/2025, 19/10/2026, 26/10/2026 (dois posts) e 14/10/2026.

Falas usadas (cinco, onze proposições):
1. Contadores.cnt.br, 04/09/2024 (data na URL): Selic alta encarece crédito e pesa no setor produtivo; varejo, aviação e construção sofrem mais. Paráfrase da matéria. 1a procede; 1b falta evidência.
2. Monitor do Mercado, resumo do vídeo do canal "Como dobrar seu dinheiro sem fazer nada: a regra da Selic em 15%". Data: 29/08/2025 por um resultado de busca; outro indicava "cerca de 422 dias" antes de 02/11/2026, o que daria início de setembro de 2025. Conferir na 12.R. Link e minutagem do vídeo não encontrados. 2a procede; 2b procede em parte; 2c procede.
3. X, 26/10/2026 (status 2114767959709065714), citação literal completa. 3a procede em parte; 3b falta evidência.
4. Jornal Opção, "Lula 4: economista alerta para baixo crescimento, enquanto investidor vê oportunidades em Goiás". Data dada como 1º/11/2026 porque a busca de 02/11/2026 indicava "um dia atrás"; conferir. Três ideias em discurso indireto, atribuídas nominalmente a Sena ("Para Raul Sena, o principal desafio do próximo governo será controlar o crescimento da dívida pública"; "Raul Sena também considera que a incerteza fiscal pode retardar a redução dos juros e prolongar o encarecimento do crédito"; "Raul Sena considera que o crescimento das despesas obrigatórias reduz o espaço disponível no orçamento para investimentos e outras políticas públicas"). Na página, por paráfrase. 4a, 4b e 4c procedem.
5. Jornal Opção, mesma matéria: a reação negativa do mercado foi influenciada por apostas feitas antes da votação; parte dos investidores considerava mais provável a vitória do candidato da oposição. Procede (6.1.1).

Falas descartadas:
- Jornal Opção, mesma matéria: "O desafio é matemático: ou corta despesa, coisa que ele nunca fez na vida, ou aceita que a dívida continua subindo e o juro fica alto" e "tem medo de governo que gasta pra ganhar eleição e deixa o rombo pro próximo presidente". A busca atribuiu as frases ora a Sena, ora a "um economista" da matéria, que também ouve a economista Greice Guerra. Atribuição incerta: fora. Se a 12.R abrir a matéria e confirmar que são de Sena, a primeira reforça a fala 4 e pode entrar como recorte (sem o trecho sobre a pessoa).
- X, 26/10/2026 (status 2114740079843545291): "Compra de voto você diz com as medidas populistas pré-eleição? Mas isso foi fato. Isso não é fraude das urnas." Juízo político sem proposição econômica além da fala 3.
- X, 19/10/2026: diz que leria a proposta econômica do candidato da oposição em vez de ver o debate. Sem conteúdo.
- X, 05/05/2026 e 14/10/2026: sobre faturamento da AUVP e correção pela Selic numa resposta. Fora do tema.
- YouTube, cortes de terceiros: "ECONOMIA À BEIRA DE UM COLAPSO? RAUL SENA - Inteligência Ltda. Podcast #1942" (set/2026; youtube.com/watch?v=t0xq1uTi1cc); "RAUL SENA EXPÕE O CAMINHO PARA O PAÍS NÃO QUEBRAR!" (set/2026; watch?v=xcplYQQH6x8); "A ECONOMIA DO BRASIL É MATEMATICAMENTE IMPOSSÍVEL [com Raul Sena]" (corte do Flow; watch?v=vBthwngRM-g); "Raul Sena afirma que Congresso é desqualificado: 'Foram eleitos para fazer corte'" (out/2026; watch?v=j4nMnPjnSfc); "LULA VENCE AS ELEIÇÕES E COMO FICA A ECONOMIA DO BRASIL? FT. RAUL SENA" (watch?v=jXRpukTcvI8); "O PROJETO de POBREZA no BRASIL" (watch?v=S1EdzyUsgOA); short "A esquerda brasileira é a única esquerda do planeta" (watch C-z4b7TovqA). Títulos e descrições de editores de corte, sem transcrição. Os de "colapso" e "não quebrar" são os candidatos naturais ao jargão 12.4a e devem ser assistidos com minutagem numa rodada com acesso ao YouTube.
- "Raul Sena explica por que o Brasil pode enfrentar mais inflação em janeiro" (fim de out/2026; watch?v=T-d5jfkPFw0): a descrição fala em pressão inflacionária em janeiro e fevereiro, sem o argumento. Previsão a julgar em fev/2027.
- Flow #651 (18/09/2026, "Investidor Sardinha ensina como salvar o Brasil"), Flow #512, Ticaracaticast #525 (19/11/2024), Mundo Rico (1º/10/2026, plano econômico do candidato da oposição): só descrições; citados na página como presença pública, sem conteúdo atribuído.
- Nenhuma fala confirmável de 2022 ou 2023 sobre juros, dívida ou "Brasil quebrado".

Fontes principais: posts do X de @oraulsena; Jornal Opção (nov/2026); Monitor do Mercado (ago/2025); Contadores.cnt.br (set/2024); AUVP; Investidor10; OutlierKit (1,7 milhão de inscritos e 327,2 milhões de visualizações, consulta 02/11/2026); ANBIMA FInfluence 10 (904 influenciadores, 310,7 milhões de seguidores, 2º sem/2025; 266 e 74 milhões em 2020; Bruno Perini lidera o ranking geral de pessoas físicas); Tesouro, balanço do Tesouro Direto de set/2026 (3.924.677 investidores ativos, 36,7 milhões de cadastrados, estoque R$ 279,3 bi, 46,7% em índices de preços); Folha (post de 18/10/2026, R$ 290 bi em medidas de olho nas eleições, valores de 2026 e 2027; não conferido pelo painel); BCB SGS 432, 5793 e 13762 (consulta 02/11/2026); páginas 2.2, 2.4, 3.1, 3.2, 3.3, 4.4, 6.1.1, 6.1.2, 6.2, 11.5, 11.6, 11.7.

Linhas para a matriz da página 12 (não acrescentadas lá, porque o escopo do item eram as duas páginas; a 12.R ou o coordenador pode colar). A coluna da matriz 8.1 fica vazia: nenhuma fala confirmável trata de alarme inflacionário (P9c) nem de quem lucra com o juro (P8b); as ligações com as linhas O da 8.1 ficam para quando a 8.1 for refeita.
| Raul Sena (Investidor Sardinha) | Influenciador | Contadores.cnt.br, 04/09/2024 | Juro alto encarece o crédito e reduz consumo e produção | | Procede | Canal do crédito | 2.4, 6.2 |
| Raul Sena (Investidor Sardinha) | Influenciador | Monitor do Mercado, 29/08/2025 | A Selic cairia de 15% (exemplo: 11%) e prefixados ganhariam | | Procede em parte | Preço do título prefixado | SGS 432, 6.1.1 |
| Raul Sena (Investidor Sardinha) | Influenciador | X, 26/10/2026 | Medidas da campanha consumiram espaço fiscal; vem uma crise | | Procede em parte; falta evidência | Aritmética da dívida | SGS 5793, 6.1.1 |
| Raul Sena (Investidor Sardinha) | Influenciador | Jornal Opção, 01/11/2026 | Conter a dívida é a tarefa principal; incerteza fiscal retarda a queda do juro; despesa obrigatória comprime o orçamento | | Procede | Prêmio fiscal; contrato social | 3.1, 3.2, 6.1.1, 6.1.2 |
| Raul Sena (Investidor Sardinha) | Influenciador | Jornal Opção, 01/11/2026 | Parte da queda pós-eleição foi desmonte de apostas | | Procede | Estudo de evento | 6.1.1 |

Lacunas:
- Nenhuma minutagem: o YouTube não abre nesta rede. A fala 2 vem de matéria que resume o vídeo; as falas em vídeo ficaram todas descartadas.
- Alcance só por agregador (OutlierKit) e portal (Melhor Investimento); conferir no próprio canal. Instagram e TikTok sem número confirmado.
- A posição de Sena nos rankings FInfluence da ANBIMA não apareceu nos trechos de busca; ler o PDF da 10ª edição.
- A data exata da matéria do Jornal Opção e da do Monitor do Mercado.
- A 12.1 cita Primo Rico e Bruno Perini com links para 12.1.2 e 12.1.3, ainda inexistentes; o ranking da ANBIMA (Perini em 1º) vem do comunicado da ANBIMA via busca.

Números que divergem de outras páginas: nenhum. Dívida bruta 71,7% (dez/2022) e 82,9% (set/2026), SGS 13762, como na 11.6; déficit primário de 0,52% do PIB em 12 meses até set/2026 e juros de 8,99% do PIB, como na 6.1.2; Selic de 13,75% desde 17/09/2026 (SGS 432); dados do pregão de 26/10/2026 copiados da 6.1.1. O juro real ex-ante de "cerca de 8,7%" da 12.1 segue a convenção da _divergencias (8,73% em 23/10/2026).

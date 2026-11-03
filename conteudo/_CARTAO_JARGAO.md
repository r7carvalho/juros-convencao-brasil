# Cartão de página de jargão (bloco 12, ramo 12.4)

Vale para todo item de jargão do bloco 12, junto com conteudo/_CARTAO_BASE.md e as regras de
conteudo/_CARTAO_PESSOA.md.

## Leia antes

conteudo/_CARTAO_BASE.md; conteudo/_CARTAO_PESSOA.md; a seção do bloco 12 em PLANO.md;
conteudo/12-vozes/12-vozes-do-debate.md (mapa dos jargões: o que cada um testa e as páginas de
evidência); conteudo/12-vozes/12.4-jargoes.md e 12.4.1-brasil-vai-quebrar.md (modelo de estrutura e
tom); conteudo/12-vozes/_notas.md (as linhas da matriz preparadas pelas páginas de pessoa dizem quem
usou cada jargão, com link e data).

## Forma

Uma página por jargão (ou grupo de frases do mesmo item), id 12.4.N (pai 12.4, ordem N), 1.500 a 2.800
palavras: exemplo de brinquedo novo antes do dado; o que a frase pode querer dizer (cada sentido
separado); a forma mais forte de cada sentido; o teste de cada sentido com a evidência do painel (links
para as páginas onde ela está, sem repetir a análise); quem usa a frase e como (exemplos com link e
data, de preferência os das páginas de pessoa, sem refazer a análise delas; os do outro lado também);
classificação de cada sentido (procede / procede em parte / não procede / falta evidência); tabela-resumo
sentido × evidência × classificação; quadro A favor / Contra; caixa `:::painel`; Para ler. Estado:
1ª versão.

## Ao terminar

Troque na página 12 o rótulo do jargão no mapa (12.4b, 12.4c...) pelo link pagina:12.4.N; nas
páginas de pessoa que remetem a esse rótulo com link para pagina:12, troque o link para pagina:12.4.N
(só o link, sem mexer no texto). Atualize na 12.4 o "resultado até aqui". Notas: seção do item ao fim
de conteudo/12-vozes/_notas.md, com exemplos usados e descartados e as linhas para a matriz. Marque o
item [x] no PLANO.md. `python3 tools/build.py --check` sem ERRO e `python3 tools/lint.py <arquivo>`
limpo. Não rode git nem o build sem --check.

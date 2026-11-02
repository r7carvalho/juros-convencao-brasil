# Cartão de página de pessoa (bloco 12, vozes do debate)

Vale para todo item de pessoa do bloco 12, junto com conteudo/_CARTAO_BASE.md.

## Leia antes

conteudo/_CARTAO_BASE.md; a seção do bloco 12 em PLANO.md (regras próprias); as páginas
conteudo/12-vozes/12-vozes-do-debate.md (método, régua das quatro classificações, mapa dos jargões),
a página do ramo (12.1, 12.2, 12.3 ou 12.5) e duas páginas de pessoa já publicadas como modelo de
estrutura e tom (12.1.1 e 12.2.1, se existir); conteudo/12-vozes/_notas.md.

## Regras

1. Confirme a identidade por busca antes de escrever (nome, canal ou veículo, cargo). Se não confirmar,
   não escreva a página: registre a dúvida nas notas e no RELATORIO.md e encerre o item.
2. Só fala pública com link e data (coluna, post, vídeo com minutagem quando possível, entrevista,
   relatório, livro). Nada de vida privada, nada de ataque pessoal, nenhum adjetivo sobre a pessoa.
3. Princípio da caridade: cada argumento na forma mais forte antes de ser avaliado.
4. Cada fala vira uma ou mais proposições testáveis, cada uma classificada em procede / procede em
   parte / não procede / falta evidência, com a base teórica e a evidência do painel ao lado (link para a
   página onde a evidência está: 1.x, 2.x, 3.x, 4.x, 5.x, 6.x, 8.1, 10.x, 11.x). Concordar quando procede.
5. Argumento recorrente entre pessoas: remeta ao jargão pelo rótulo do mapa (12.4a a 12.4j) com link
   para pagina:12 (as páginas de jargão terão ids 12.4.x).
6. Previsões são julgadas pelo que se sabia na data e pelo resultado, com o dado primário.
7. Relação comercial com produtos de investimento, se houver, com fonte; sem insinuação.

## Forma

id, pai e ordem dados pelo item; 1.500 a 3.000 palavras (acadêmicos e autoridades até 3.500); seções:
quem é no debate (alcance com fonte e data; posição pública; relação comercial); as falas (4 a 8,
de 2022 a 2026 salvo indicação, cada uma com citação curta literal ou paráfrase fiel, link e data;
forma mais forte; proposições e classificação; o que procede); tabela-resumo fala × proposição ×
classificação; caixa `:::painel`; Para ler. Estado: 1ª versão.

## Ao terminar

Atualize na página do ramo só o parágrafo da pessoa (uma ou duas frases com o que a página conclui).
Notas: seção do item ao fim de conteudo/12-vozes/_notas.md, com identidade, falas usadas e
descartadas (e por quê) e as linhas prontas para a matriz pessoa × argumento × classificação da
página 12. Marque o item [x] no PLANO.md. `python3 tools/build.py --check` sem ERRO e
`python3 tools/lint.py <arquivo>` limpo. Não rode git nem o build sem --check.

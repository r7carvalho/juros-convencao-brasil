# Notas do bloco 0 (início)

## Item 0 e 0.1: página inicial e "A tese em teste e como ler o painel" (02/11/2026)

Páginas entregues:

- `0-inicio.md` (id 0, pai vazio, ordem 0, estado 1ª versão): cerca de 1.450 palavras de texto corrido (sem a seção Para ler e sem os endereços dos links), mais o mapa gerado por `{{mapa}}` sob o título "Mapa do painel". Gráfico de abertura reaproveitado: `dados/2.1-juro-real-brasil-pares.json` (BIS, juro real da taxa básica, Brasil e pares, 2000–2026).
- `0.1-como-ler.md` (id 0.1, pai 0, ordem 1, estado 1ª versão): cerca de 2.100 palavras de texto corrido. Traz P1 a P10 (com as divisões a/b/c da 8.1) e O1 a O4 (O1a, O1b, O2a, O2b, O3, O4), cada linha com link para a página onde é testada e para a âncora da linha na 8.1 (`pagina:8.1#p1-...`); as âncoras foram conferidas renderizando as páginas em memória com `tools/build.py`. Mini-glossário de 12 termos com âncoras para os verbetes da 9.3 (também conferidas).

Fontes principais: conteudo/8-conclusao (8 e 8.1), 9.1, macros 1 a 7, 9, 10 e 11; `dados/2.1-juro-real-brasil-pares.json` (BIS, consulta 02/11/2026); ranking MoneYou/Lev de 16/09/2026; BCB SGS 1178, 4382, 5727, 5793; Tesouro, RMD de ago/2026. Nenhum número novo: todos vêm das páginas já publicadas e de `_divergencias.md`.

Números usados (todos já decididos em `_divergencias.md`): juro real ex-ante de 8,73% em 23/10/2026 (convenção única); ranking 8,45% contra média de 1,62%; distância para cinco emergentes de 6,6 / 3,1 / 5,5 p.p. (2000–09, 2010–19, 2023–26); juro real BIS de 2025: Brasil 9,09, México 4,28, Colômbia 3,99, África do Sul 3,84, Índia 3,48, Chile 0,61 (arredondados a uma casa no texto); LFT 52,74% da DPF (ago/2026); juros nominais de R$ 1.204,8 bi = 8,99% do PIB em 12 meses até set/2026; DBGG 82,9% (94,5% FMI) em ago/2026; déficit primário 0,52%; primário estabilizador 2,9% a 3,4%; poupança 14,1% (IBGE, 2024); neutro 5% (BC) a 8% (ASA); IPCA 5,53% → 4,26% em 2025; Focus com erro médio de +1,0 p.p. em 2002–2025, +0,7 sem 2002, +0,5 só dezembros, −0,2 em 2015–2019.

Recorte citado: só um, o art. 164, § 1º, da Constituição, usado na 0.1 como exemplo de formato (mesmo texto já citado na página 10, com link para o Planalto).

Lacunas e pendências:

- A página inicial descreve o estado dos blocos 10, 11 e 12 em 02/11/2026; quando os blocos fecharem e a 8/8.1 forem revistas, atualizar a seção "O que ainda está em construção" e a direção (que repete a da 8, 1ª versão).
- Se a 8.1 mudar os títulos das linhas P/O, as âncoras da 0.1 quebram (o build não checa âncoras): refazer os links.
- A 0.1 descreve P9c como dependente do bloco 12 (medida do discurso público), como a 8.1.
- `tools/lint.py` conta 1.883 e 2.836 "palavras" porque inclui endereços de links e números partidos por vírgula; a contagem de texto corrido fica dentro das faixas do cartão (900–1.500 e 1.500–2.500).

Divergências: nenhuma nova. O texto arredonda os valores do BIS de 2025 a uma casa (9,1; 4,3; 4,0; 3,8; 3,5; 0,6).

## 2ª versão (03/11/2026)

Atualizadas junto com a 2ª versão de 8 e 8.1 (detalhes em `conteudo/8-conclusao/_notas.md`). Na 0: resumo, caixa da direção, régua das quatro classificações em "Como o painel trabalha", entradas dos blocos 10 a 12 em "Por onde começar" e a seção de lacunas de conteúdo "O que o painel ainda não mediu" no lugar de "O que ainda está em construção". Na 0.1: linhas novas P7c, O5 e O6, notas novas de P7b e P9c, P3 com a forma fraca da convenção nas expectativas, seção "Como ler uma página do debate público" e o estado "2ª versão". As âncoras para a 8.1 foram conferidas pelo `build.py --check`. Estado das duas páginas: 2ª versão.

## Revisão aplicada (03/11/2026)

Aplicado o relatório `conteudo/_revisao/8.md` (achados das páginas 0 e 0.1). Estado das duas páginas: revisada. Na 0: resumo e caixa da direção com o resíduo na forma da 2.5, as duas confianças do prêmio fiscal (alta nas oscilações, moderada no nível) e a convenção no sentido fraco como "compatível com"; primeira leitura no condicional ("nessa leitura"); desinflação de 2025 "com a ajuda do real valorizado"; 2,9% (IFI, neutro de 6,1%) a 3,4% (taxas de 2025); "Por onde começar" encurtado; saiu a frase sobre o estado de produção. Na 0.1: P3, P4b (âncora nova), P9c (contra, moderada), P9d, O7 e O8 novas; fato comum em P1, P5a, P8a e O5; resíduo e glossário na forma da 2.5; quadro de exemplo sem "ganham com juro alto"; contagem do bloco 12 descrita como não evidência das linhas factuais; "Procede" com "nenhuma evidência forte contra"; "fala contrariada pelos dados"; parágrafos de gráfico e Para ler encurtados; saiu a frase sobre links para páginas não escritas. Extensão: cerca de 1.800 (0) e 3.100 (0.1) palavras de prosa, ainda acima do cartão.

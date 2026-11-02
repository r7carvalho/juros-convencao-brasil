# Notas da área 9 (Método, fontes, glossário e linha do tempo)

Data: 02/11/2026.

## Páginas entregues

| Id | Arquivo | Palavras (aprox., com frontmatter, tabelas e URLs) |
|---|---|---|
| 9 | 9-metodo-fontes-glossario.md | 1.070 |
| 9.1 | 9.1-metodo-evidencia.md | 3.450 (prosa ~3.000) |
| 9.3 | 9.3-glossario.md | 4.300 (73 verbetes) |
| 9.4 | 9.4-linha-do-tempo.md | 3.430 (cerca de 95 linhas de cronologia) |

A 9.2 (bibliografia consolidada) não foi escrita, conforme instrução; a macro e as demais já linkam `pagina:9.2`.

Dados gravados:

- `dados/9.1-juro-real-ex-ante-ex-post.json` (Frente K: ex-post 2000–set/2026, ex-ante 2001–set/2026; ref. juro neutro 5%).
- `dados/9.1-divida-tres-conceitos.json` (DBGG BCB e DLSP da Frente A; DBGG FMI da Frente J; 2015–ago/2026).
- `dados/9.4-selic-ipca-longo.json` (IPCA anual 1995–2025 e set/2026; Selic meta fim de ano 1999–2025 e set/2026).

`python3 tools/build.py --check` passa para as quatro páginas (só avisos de links para páginas ainda inexistentes). Observação: antes de saber que `--help` não existe, rodei `python3 tools/build.py --help`, que executou o build completo e gravou `docs/`. O coordenador deve regerar `docs/` no build final.

## Divergências e escolhas

- Data da eleição de 2026: o pedido do coordenador fala em "eleição de 26/10/2026"; a Frente I registra o segundo turno em 25/10/2026 (domingo) e a reação do mercado em 26/10 (segunda). A 9.4 segue a Frente I: segundo turno em 25/10, queda de 13,88% do Ibovespa em 26/10. Primeiro turno em 04/10/2026 (inferido da Frente I: pesquisa de 03/10 "antes do voto" e alta de 05/10 "depois do 1º turno").
- Taxa implícita da DBGG em 2025: a Frente J traz 12,55% na série e 12,69% no texto analítico. O glossário evita o número; a página 3.1 deve escolher um.
- Juro real ex-ante de 23/10/2026: 8,72% (Frente K, Selic over ~13,65%) contra 8,82% se calculado com a meta de 13,75%. A 9.1 explica a diferença (over cerca de 0,10 ponto abaixo da meta).
- Juro real ex-post de 2025: 9,66% (Selic acumulada / IPCA dez-dez, Frente K) contra 9,09% (régua BIS de médias anuais). As duas aparecem na 9.1 com a explicação.
- IPCA de 1994: compilações dão 916,43% e 916,46%; o número não foi usado no texto.
- Selic ao assumir 15% em jun/2025: fontes divergem se foi o maior nível "desde julho de 2006" ou "desde maio de 2006"; o texto diz "desde 2006".

## A conferir

- Gráfico `9.4-selic-ipca-longo.json`: IPCA de 2015 a set/2026 e Selic de 2019 a set/2026 vêm dos insumos. IPCA de 1995 a 2014 e Selic meta de fim de ano de 1999 a 2018 foram transcritos dos valores oficiais conhecidos e cotejados por busca web com compilações secundárias (falazuki.com, advfn, AASP, debit.com.br), sem acesso à SIDRA 1737 nem ao histórico do Copom. Conferir na fonte primária quando a rede permitir. A nota do JSON declara isso.
- Data e documento do PAI: a busca achou referência de documento da Fazenda de 1993 que data o lançamento em junho (um site educativo diz julho). A 9.4 usa "jun/1993" e cita "Ministério da Fazenda, documentos do Plano Real (1993)" sem URL. Conferir na Exposição de Motivos do Plano Real (dez/1993).
- LBC (1986): a norma de criação não foi localizada; a 9.4 só registra que o DL 2.376/1987 já a menciona.
- Criação do sistema Selic em 1979: URL do BCB citada sem verificação (site inacessível).
- Circular BCB 2.698/1996 (criação do Copom) e Selic a 45% em mar/1999: confirmadas apenas por fonte secundária; a URL citada é a do histórico do Copom (do insumo C).
- Cortes da Selic em 2026: 14,75% (18/03, CNN) e 14,25% (junho, Agência Brasil) confirmados por imprensa; 14,50% (abril) e 14,00% (julho/agosto) só em blogs, por isso não listados individualmente.
- URLs de leis no Planalto montadas pelo padrão do site (Lei 4.380, 4.595, 6.151, DL 2.283, 2.335, Lei 7.730, 8.024, 8.177, 8.880, 9.069, Decreto 3.088, LC 101, 179, 194, 200, EC 95, 103, 106, 114): datas e números conferidos, endereços não abertos nesta sessão.
- Eventos de 1964–1994 sem norma (PAEG, choques do petróleo, moratória de 1987, Brady, crise de 1982) citam Abreu (org.), 2014, sem página; a 9.2 pode completar capítulo e página.
- "Perda do grau de investimento em set/2015" e datas do impeachment de 2016 citam fontes genéricas (insumo I; portal de notícias do Senado). Conferir links específicos.
- Tarifas dos EUA em 2025: só o dado da Frente C (vendas do agro para os EUA −5,6%); data e alíquota não conferidas.

## Sugestões para a próxima rodada

- Quando a rede permitir, baixar SIDRA 1737 e SGS 432 e regerar o gráfico longo direto da fonte; estender o IPCA para 1980–1994 num gráfico em escala logarítmica, se o motor gráfico suportar.
- A 9.2 pode reaproveitar as listas "Para ler" desta área e as `referencias_bibliograficas` das Frentes I e K.
- Alinhar com as áreas 2 e 3 os números de taxa implícita (12,55% × 12,69%) e de juro real ex-ante (meta × over).
- Revisar os links internos da 9.3 quando as netas definitivas das áreas 1 a 7 existirem (alguns apontam para filhas, por exemplo `pagina:2.4` para Focus).

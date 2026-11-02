# Notas da área 9 (Método, fontes, glossário e linha do tempo)

Data: 02/11/2026.

## Páginas entregues

| Id | Arquivo | Palavras (aprox., com frontmatter, tabelas e URLs) |
|---|---|---|
| 9 | 9-metodo-fontes-glossario.md | 1.230 (após a revisão) |
| 9.1 | 9.1-metodo-evidencia.md | 4.810 com tabelas (após a revisão) |
| 9.3 | 9.3-glossario.md | 6.510 (87 verbetes, após a revisão) |
| 9.4 | 9.4-linha-do-tempo.md | 4.720 (cerca de 105 linhas, após a revisão) |

A 9.2 (bibliografia consolidada) não foi escrita, conforme instrução; a macro e as demais já linkam `pagina:9.2`.

Dados gravados:

- `dados/9.1-juro-real-ex-ante-ex-post.json`: refeito em 02/11/2026 por `tools/analises/9.1_juro_real.py` a partir de dados/brutos/ (SGS 4390, 13522, 1178; Focus 12 meses não suavizada, base 0). Ex-post 2000–set/2026; ex-ante 2001–set/2026 e 23/10/2026.
- `dados/9.1-divida-tres-conceitos.json`: DBGG BCB (SGS 13762) e DLSP (SGS 4513) conferidas nos brutos; DBGG FMI da tabela Divggnp (BCB), 2015–ago/2026.
- `dados/9.4-selic-ipca-longo.json`: conferido ponto a ponto com SGS 432 e 13522; acrescentada a Selic over de dezembro de 1995–1998 (SGS 4189).

Regra de redação: "Frente X", "insumo" e "painel irmão" não aparecem nas páginas nem nos campos fonte/nota dos JSON; cita-se a fonte primária.

## Divergências e escolhas

- Eleição de 2026: segundo turno em 25/10 (domingo), reação do mercado em 26/10 (segunda); primeiro turno em 04/10, primeiro domingo de outubro (Constituição, art. 77).
- Juro real ex-ante: a área segue a convenção única de _divergencias.md (SGS 1178 sobre Focus 12 meses não suavizada): 8,39% em 30/09/2026 e 8,73% em 23/10/2026. Suavizada (8,65% em set/2026) e Selic meta (8,82% em 23/10) só como comparação na 9.1.
- Juro real ex-post de 2025: 9,66% (Selic acumulada / IPCA dez-dez) contra 9,09% (BIS, médias anuais). As duas aparecem na 9.1 com o método.
- IPCA de 1994: 916,46% pelo SGS 13522 (resolve a dúvida 916,43 × 916,46).
- Selic a 15% em jun/2025: "maior nível desde julho de 2006" (SGS 432: 15,25% vigorou até 19/07/2006).
- Cortes de 2026: os cinco cortes estão no SGS 432 (14,75; 14,50; 14,25; 14,00; 13,75).
- Compromissadas em 2006 (3,2% do PIB) e 2016 (16,7%): retiradas do verbete do glossário porque a página de destino não traz esses números e a série não está no acervo; ficou o dado de ago/2026 (10,3%), que está na 10.2.1.

## Pendências após a revisão (02/11/2026)

- PAI: data (jun/1993) e documento da Fazenda sem URL; conferir na Exposição de Motivos do Plano Real (dez/1993).
- LBC: norma de criação não localizada; a 9.4 diz "meados dos anos 1980" e cita a menção no DL 2.376/1987.
- Circular BCB 2.698/1996 (criação do Copom): confirmada só por fonte secundária.
- Acordo com o FMI de ago/2002 (US$ 30 bilhões): a 9.4 cita a carta de intenções de 29/08/2002; o comunicado do FMI com o valor não foi aberto.
- Tarifa dos EUA de 30/07/2025 (40% adicionais, em vigor em 06/08/2025): confirmada por resumos de escritórios (EY, Thompson Hine) do texto da ordem executiva; o texto na Casa Branca não foi aberto. O número de queda das vendas do agro para os EUA (5,6%) saiu da página por falta de fonte primária (MAPA/Agrostat ou Secex).
- Lei 15.270/2025, EC 113, 123 e 126: URLs do Planalto montadas pelo padrão do site, não abertas.
- Resultados eleitorais de 2002, 2014, 2022 e 2026 e cotações de Polymarket (23/10/2026) e Kalshi (24/10/2026): citados pelo TSE e pelas plataformas, mas as páginas não foram abertas; os percentuais vêm de compilação conferida em outubro de 2026.
- CDS de 5 anos em 26/10/2026: 9.3 e 9.4 usam 151,6 pb (InfoMoney); a 6.1.1 dá 151,7 no texto. Alinhar.
- Ibovespa (SGS 7) e EMBI+ (Ipeadata) não estão na coleta automática; sugerir incluir no coletor.
- Forward guidance do Copom: data exata da retirada (início de 2021) não conferida no comunicado.
- Eventos de 1964–1994 sem norma citam Abreu (org.), 2014, sem página; a 9.2 pode completar.

## Achados da revisão não aplicados (com motivo)

- Nenhum achado foi rejeitado no mérito. Escolhas entre alternativas propostas pelo revisor: dívida em três conceitos mantida em agosto de 2026 (os três andam juntos); régua ex-ante refeita na série não suavizada, em vez de manter a suavizada; Taylor ligada à 10.2.5, que já existe.

## Sugestões para a próxima rodada

- Estender o IPCA para 1980–1994 (SGS 13522) num gráfico em escala logarítmica, se o motor gráfico suportar.
- A 9.2 pode reaproveitar as listas "Para ler" desta área.
- Trocar na 9.3 os links de forward guidance e QE para 10.3.1 e 10.3.2, e o de swap cambial para 10.3.6, quando essas páginas existirem.

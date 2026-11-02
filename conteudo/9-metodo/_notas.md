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

## 9.2 Fontes e bibliografia (item 9.3 do PLANO, parte bibliografia), 02/11/2026

Arquivo: `9.2-fontes-e-bibliografia.md`, estado 1ª versão. Introdução de 487 palavras; a página inteira tem cerca de 26.600 palavras contando URLs, porque é lista. Gerada por `tools/analises/9.2_bibliografia.py` (só biblioteca padrão): `python3 tools/analises/9.2_bibliografia.py --relatorio` grava a página e imprime contagens, divergências e incompletas; `--seco` só imprime. Lint: "cenário×1" e "desafio×2" são falsos positivos dentro de títulos que não podem mudar (CEMEC-FIPE 2023, "Cenário tem virada..."; revista do Ipea *Desafios do Desenvolvimento* e sua URL). `build.py --check` sem erro.

Base: 1.065 itens de "Para ler" em 91 páginas (ignorando `_*` e a própria 9.2) e as fontes de 105 gráficos `dados/*.json`. Durante a execução apareceram páginas novas escritas em paralelo (8, 8.1, 10.2.5, 11), e 9.1, 9.3 e 9.4 estavam em correção: a página deve ser regerada quando essas rodadas fecharem e de novo depois dos blocos 10 a 12. Gráficos de páginas ainda inexistentes não entram (hoje só `10.2.6-*`).

### Contagens

- Fontes primárias: 202 itens. São 31 códigos do SGS e 7 tabelas do SIDRA (quadros), 36 itens de legislação e normas e 128 documentos e séries agrupados por instituição (BCB 48 linhas incluindo os subitens de RI/RPM e cartas abertas, IBGE 17, Tesouro 7, IFI 2, Ipea 6, FGV IBRE 7, BIS 3, FMI 9, Banco Mundial 1, PWT 1, bancos centrais e estatísticas estrangeiras 25, Congresso/Receita/BNDES/outros 12; as linhas de remissão a trabalhos com autor não contam).
- Literatura: 351 obras, das quais 117 juntam duas ou mais citações diferentes da mesma obra.
- Imprensa e outras secundárias: 55 entradas, mais uma frase com os veículos citados só nas fontes dos gráficos.
- Excluídas por serem remissão interna sem obra: 2.2 e 2.4 ("Para o contraponto/lado ortodoxo...") e dois itens da página 8 (links para 8.1 e 9.1).

### Decisões de classificação

- Estudos assinados por organizações não oficiais (Auditoria Cidadã, DIEESE, Inesc, IEDI, CEMEC-FIPE, Fin, Itaú) e textos de autor reproduzidos por terceiros (Lara Resende 2026, "Eu acuso") ficaram na Literatura. Entrevistas (Holland 2018 e 2026), o vídeo de Kobori (2026), o ranking MoneYou/Lev, a Peterson Foundation, o relato da Unicamp e checagens ficaram em imprensa e outras secundárias.
- Trabalhos com autor publicados por BCB, Ipea, IFI, Tesouro, BIS, FMI e FGV IBRE estão na Literatura; a seção de cada instituição remete a eles pelo nome.
- SGS 1178 descrita como Selic over anualizada, base 252, conforme `_divergencias.md` (o índice da coleta ainda a chama de TJLP "conferir"). SGS 13761 ficou com descrição genérica ("DBGG, citada junto com a 13762"), porque a página 3.2 não diz a unidade. Códigos do acervo marcados "conferir" e não citados aparecem só pelo número.
- Citações compostas (várias normas ou documentos numa linha só, como as de 10.2.3, 10.2.4 e 10.2.5) entram inteiras em "Outros documentos citados" da instituição; o script não as desmonta.
- Quatro obras têm texto canônico escrito no script com dados que já estavam nas páginas, porque as citações diferiam só no capítulo ou no subtítulo: Keynes (1936), capítulos 7, 11, 12, 14, 15 e 17 (as faixas 194–209 em 1.4.1 e 147–164 em 1.4.2 são capítulos diferentes, não divergência); Giambiagi et al. (2011), caps. 5 a 7; Mishkin (2019); Almeida, Lisboa e Pessôa (2015), título completo de 4.3 com os links de 6.1.2.

### Divergências entre citações da mesma obra

Nenhuma divergência de ano, volume(número) ou páginas entre citações da mesma obra. Divergências de forma (a página usa a versão de página revisada mais completa):

- Arida, P.; Lara Resende, A. (1985): título com e sem subtítulo ou com grafias diferentes
- Fisher, I. (1911): título com e sem subtítulo ou com grafias diferentes
- Lopes, F. L. (1986): autores grafados de formas diferentes: Lopes, F | Lopes, F. L
- Uribe, M. (2022): título com e sem subtítulo ou com grafias diferentes
- Cochrane, J. H. (2023): autores grafados de formas diferentes: Cochrane, J | Cochrane, J. H
- Sims, C. A. (1994): autores grafados de formas diferentes: Sims, C | Sims, C. A
- García-Schmidt, M.; Woodford, M. (2019): título com e sem subtítulo ou com grafias diferentes
- Taylor, J. B. (1993): autores grafados de formas diferentes: Taylor, J | Taylor, J. B
- Bogdanski, J.; Tombini, A.; Werlang, S. (2000): autores grafados de formas diferentes: Bogdanski, J.; Tombini, A. A.; Werlang, S. R. C | Bogdanski, J.; Tombini, A.; Werlang, S
- Coibion, O.; Gorodnichenko, Y.; Wieland, J. (2012): título com e sem subtítulo ou com grafias diferentes
- Bagehot, W. (1873): título com e sem subtítulo ou com grafias diferentes
- Fisher, Irving (1930): autores grafados de formas diferentes: Fisher, I | Fisher, Irving
- Gonçalves, F.; Holland, M.; Spacov, A. (2007): autores grafados de formas diferentes: Gonçalves, F. M.; Holland, M.; Spacov, A. D | Gonçalves, F.; Holland, M.; Spacov, A
- Bonomo, M.; Martins, B. (2016): título com e sem subtítulo ou com grafias diferentes
- Laubach, T.; Williams, J. C. (2003): autores grafados de formas diferentes: Laubach, T.; Williams, J | Laubach, T.; Williams, J. C
- Castro, P. H. S. (2019): título com e sem subtítulo ou com grafias diferentes
- Lara Resende, A. (2017): título com e sem subtítulo ou com grafias diferentes
- Lisboa, M.; Pessôa, S. (orgs.) (2019): título com e sem subtítulo ou com grafias diferentes
- Souza Júnior, J. R. C.; Cornelio, F. M. (2020): título com e sem subtítulo ou com grafias diferentes
- Bruno, M.: título com e sem subtítulo ou com grafias diferentes
- Kydland, F.; Prescott, E. (1977): título com e sem subtítulo ou com grafias diferentes
- Alesina, A.; Summers, L. (1993): título com e sem subtítulo ou com grafias diferentes
- Oreiro, J. L. (2026): título com e sem subtítulo ou com grafias diferentes
- DIEESE (2017): título com e sem subtítulo ou com grafias diferentes
- Angrist, J.; Pischke, J.-S. (2010): título com e sem subtítulo ou com grafias diferentes

### Referências incompletas em todas as páginas que as citam (ficaram incompletas)

- Goodhart, C. (1975): sem páginas (1.1.1)
- Kaldor, N. (1970): sem páginas (1.1.4)
- Bacha, E. (1994): sem páginas (1.2, 1.2.1, 1.2.2)
- Bresser-Pereira, L. C. (2010): sem páginas (1.2, 1.2.1)
- Pastore, A. C. (1997): sem páginas (1.2.1)
- Carvalho, C.; Minella, A. (2012): sem páginas (1.3)
- QuantEcon.: sem ano (1.5.1)
- Brito, R. (2010): sem páginas (10.1.2)
- Summers, L. (1991): sem páginas (10.1.2)
- Barbosa, F. F.; Terra, F. (2025): sem páginas (10.2.1, 10.2.2)
- Fattorelli, M.: sem ano (10.2.1)
- Keister, T.; Martin, A.; McAndrews, J. (2008): sem páginas (10.2.1)
- Oreiro, J. L.; Paula, L. F.; Silva, G. J. C.; Amaral, R. Q. (2012): sem páginas (10.2.2)
- de Mello, J. M. P.; Garcia, M. (2011): sem título do artigo (10.2.3)
- Leite Júnior, C. A. (2016): sem título da dissertação (10.2.3)
- Tucker, P. (2020): sem páginas, sem título do artigo (10.2.3)
- Yale Program on Financial Stability.: sem ano, sem títulos das fichas (10.2.3)
- Montoro, C.; Moreno, R. (2011): sem volume, sem páginas (10.2.4)
- Fasolo, A.: sem ano (10.2.5)
- Kalecki, M. (1943): sem páginas (2.2, 3.3, 5.3)
- Pessôa, S.; Cariello, R. (2026): sem título do artigo, só o veículo e o mês (2.2)
- Aggio, G. O. (2018): sem volume, sem páginas (2.5)
- Auditoria Cidadã da Dívida.: sem ano (3)
- Auditoria Cidadã da Dívida.: sem ano (3.5)
- Paula, L. F.; Pires, M. (2017): sem páginas (4.3)
- Revista de Economia Política.: sem ano, sem autor; só título e link (4.3)
- CEMEC-FIPE.: sem ano, sem número das notas (5)
- Oreiro, J. L. (2017): sem páginas (5.1)
- Luporini, V.; Alves, J. (2010): sem páginas (5.1)
- Ribeiro, M. B.; Teixeira, J. R. (2001): sem páginas (5.1)
- Bruno, M.: sem ano (5.3, 5.4.2)
- Bresser-Pereira, L. C. (2018): sem páginas (5.3)
- Feijó, C.: sem ano (5.4, 5.4.1, 5.4.3)
- Sistema financeiro e contas nacionais (UFRJ, repositório Pantheon).: sem ano, sem autor; só título e link (5.4.2)
- Adrian, T.; Crump, R.; Moench, E. (2013): sem páginas (6.1.1)
- Minella, A. (2003): sem páginas (6.2)
- Minella, A.; Souza-Sobrinho, N. (2013): sem páginas (6.2)
- Kydland, F.; Prescott, E. (1977): sem páginas (6, 6.2.1, 6.4)
- Carvalho, C.; Ferrero, A.; Nechio, F. (2016): sem páginas (6.3.1)
- Feldstein, M. (1974): sem páginas (6.3.1)
- Summers, L. (2014): sem páginas (6.3.1)
- Holston, K.; Laubach, T.; Williams, J. (2017): sem páginas (6.3.2)
- Alesina, A.; Summers, L. (1993): sem páginas (6, 6.4)
- Barro, R.; Gordon, D. (1983): sem páginas (6.4)
- Cukierman, A.; Webb, S.; Neyapti, B. (1992): sem páginas (6.4)
- Klomp, J.; de Haan, J. (2010): sem páginas (6.4)
- Rogoff, K. (1985): sem páginas (6.4)
- Lara Resende, A. (2026): texto reproduzido; veículo original não registrado (7, 7.1, 7.2, 7.6, 7.8)
- Vergnhanini, R.; De Conti, B. (2017): sem páginas (7.7, 7.8)
- Mankiw, N. G. (2020): sem páginas (7.8)
- Torres Filho, E. T.; Costa, F. N. (2012): sem páginas (7.9)

### Para a próxima rodada

- Completar nas páginas de origem as referências acima (é lá que o dado deve entrar; a 9.2 só reflete) e regerar.
- Catalogar em `CATALOGO` os grupos que hoje caem em "Outros documentos citados", sobretudo legislação (36 linhas, várias compostas) e bancos centrais estrangeiros (22).
- Unificar a grafia de autores nas páginas (Fisher, I. × Fisher, Irving; Taylor, J. × Taylor, J. B.; Lopes, F. × Lopes, F. L.).
- O código "117" que o extrator achou junto de SGS vem de "RAF 117" e foi descartado; "2265" é variável do SIDRA, não tabela.


# Notas da área 6: Contrapontos ortodoxos

Data de referência: 02/11/2026. Contagem pelo `tools/build.py --palavras`.

## Páginas entregues

| id | arquivo | palavras | gráficos |
|---|---|---|---|
| 6 | 6-contrapontos-ortodoxos.md | 1.229 | 6-juro-real-pares |
| 6.1 | 6.1-premio-fiscal-e-dominancia.md | 3.827 | 6.1-dbgg, 6.1-juros-pares |
| 6.1.1 | 6.1.1-eventos-fiscais-e-curva.md | 2.517 | 6.1.1-cds-datas, 6.1.1-di-2026 |
| 6.1.2 | 6.1.2-contrato-social-e-gasto.md | 1.928 | (sem gráfico) |
| 6.2 | 6.2-a-politica-monetaria-funciona.md | 3.163 | 6.2-ipca-meta, 6.2-inflacao-periodos, 6.2-desinflacao-2016-2017 |
| 6.2.1 | 6.2.1-o-que-2011-2012-ensinou.md | 1.778 | 6.2.1-selic-ipca-2010-2014 |
| 6.2.2 | 6.2.2-direcionado-lft-meia-entrada.md | 1.909 | 6.2.2-direcionado-lft |
| 6.3 | 6.3-poupanca-baixa-e-juro-neutro.md | 2.696 | 6.3-poupanca-implicita, 6.3-poupanca-pares (+ reuso de 6-juro-real-pares) |
| 6.3.1 | 6.3.1-poupanca-e-demografia.md | 1.411 | 6.3.1-demografia |
| 6.3.2 | 6.3.2-o-juro-neutro.md | 1.988 | 6.3.2-exante-neutro |
| 6.4 | 6.4-autonomia-e-credibilidade.md | 2.753 | 6.4-ipca-pos-autonomia |
| 6.4.1 | 6.4.1-focus-e-captura.md | 1.593 | (sem gráfico) |
| 6.4.2 | 6.4.2-critica-ortodoxa-a-convencao.md | 2.066 | (sem gráfico) |
| 6.4.3 | 6.4.3-turquia-e-argentina.md | 1.631 | 6.4.3-turquia, 6.4.3-argentina |
| **Total** | 14 páginas | **≈30.490** | 17 JSON em `dados/` |

Cada página tem exemplo de brinquedo, fórmula com exemplo resolvido (exceto 6.1.2 e 6.4.3, que usam conta simples), quadro `:::afavor`/`:::contra`, caixa `:::painel` e `## Para ler`.

## Dados construídos pelo painel (método declarado no JSON)

- `6-juro-real-pares`: médias simples por período das séries BIS da Frente K.
- `6.1-dbgg`: DBGG conceito BCB de 2006 a 2014 reconstruída para trás a partir de 65,5% (dez/2015, SGS 13762) e das variações anuais da Frente J; bate com os valores citados pela Frente J (55,5% em 2006; 51,5% em 2013).
- `6.2-inflacao-periodos`: média geométrica e desvio-padrão do IPCA anual (IBGE). IPCA anual de 1980 a 2025 e metas de 1999 a 2025 digitados de memória a partir da série do IBGE e do histórico do BCB; conferir no SIDRA 1737 quando a rede permitir.
- `6.2-desinflacao-2016-2017` e `6.2.1-selic-ipca-2010-2014`: Selic meta e IPCA 12 meses mensais digitados de memória a partir dos históricos do Copom e do IBGE; conferir no SGS 432 e 13522.
- `6.3-poupanca-implicita`: FBCF/PIB (IBGE) + saldo em transações correntes (Banco Mundial/BCB), ambos da Frente L. Ignora variação de estoques: dá 13,9% em 2024 e 2025, contra 14,1% e 14,4% oficiais do IBGE.
- Poupança do governo em 2025 ≈ −5,6% do PIB (6.3): déficit nominal 8,34% (SGS 5727) menos investimento público 2,71% (FGV IBRE). Aproximação que mistura conceitos fiscais e de contas nacionais; está dito no texto.

## Números que divergem ou foram alinhados ao registro do coordenador

| Número | Versão usada | Outra versão | Observação |
|---|---|---|---|
| DI jan/29 em 26/10/2026 | ≈15,03% (Cadaminuto; registro de divergências #12) | 15,25% (Frente B, citada na Frente K) | 15,25% seria o jan/31; ponto de 27/10 (15,13%) retirado do gráfico por provável mesma confusão |
| Primário estabilizador (IFI) | 2,9% com neutro de 6,1% (RAF 117, 29/10/2026) | 2,1% (RAF 113, Frente J) | Citei os dois com data na 6.1 |
| Juro implícito da DBGG em 2025 | "cerca de 12,6%" | 12,55% (série) e 12,69% (texto da Frente J) | Divergência #2 do coordenador |
| Juro neutro do BC | 3% (abr/2021), 4,5% até mai/2024, 4,75% (jun/2024), 5,0% desde dez/2024 | — | Alinhado com a página 2.3 |
| Participantes do Focus | ≈165 (jul/2026) e ≈172 (out/2026) | — | Divergência #13 |
| Poupança bruta Brasil 2024 | 14,5% (Banco Mundial, via compilação) | 14,1% (outra compilação; e IBGE revisado) | Diferença de fonte e revisão; dito na nota do gráfico |
| CDS 2015 | 462,5 em 22/09/2015 (Estado de Minas/Broadcast) | pico de 494 ou 539,4 em set/2015 (imprensa, sem origem) | Uso só o ponto documentado; pico citado como "cerca de 540, sem fonte de mercado localizada" |
| Poder360 "CDS fechou 2015 em 287,9" | lido como alta no ano (202 → ≈490) | lido como fechamento | Fontes ambíguas; não uso o número |
| Gap juro real Brasil × pares em 2003–2008 | 5,6 a 9,1 p.p. sobre a média de MX, CL, CO, IN, ZA (BIS) | Frente K fala em "cerca de três pontos" desde 2010 | Períodos diferentes |

## Itens a conferir (o texto já sinaliza)

- Medianas do Focus no início de 2015 (≈6,5%), 2017 (≈4,8%), 2021 (≈3,3%) e 2023 (≈5,3%) usadas em 6.4.1: de memória, não reextraídas.
- Administrados de 2015 = 18,07% (6.2.1): de memória; conferir no SGS 4449.
- Série de inflação implícita (prefixado × NTN-B) para comparar com o Focus (6.4.1): não obtida.
- Estimativas de prêmio a termo do BCB/Tesouro/IFI (6.1.1): sites bloqueados; nenhuma estimativa reproduzida. É a principal pendência da 6.1.1.
- Turquia: CPI e taxa de nov/2025 (≈31,1% e 39,5%) vêm de imprensa; 2021–2024 de memória da série TurkStat/TCMB (pico 85,51% em out/2022 e 75,45% em mai/2024 confirmados em busca).
- Argentina 2017–2022 (INDEC) de memória; 2023–2025 confirmados em busca. BCRA de 133% (dez/2023) a 40% (mai/2024) e inflação mensal de ≈25% a ≈4%: de memória.
- Meta de 3% da África do Sul anunciada em 2025: de memória.
- Pastore, *Inflação e crises: o papel da moeda*: confirmar ano (2014 ou 2015) e editora.
- Minella e Souza-Sobrinho (2013, *Economic Modelling* 30) e Minella (2003, RBE 57(3)): referências de memória, sem resultado numérico citado.
- "Holland e Padovani": não localizei trabalho conjunto; usei Gonçalves, Holland e Spacov (2007) e as entrevistas de Márcio Holland de ago/2026 (livro *Taxa de juros no Brasil*). O coordenador deve confirmar a referência que tinha em mente.
- Expressão "contrato social da redemocratização" de Pessôa: apresentada como paráfrase; o texto exato da coluna não foi localizado.
- Lisboa "não existe ortodoxia única": paráfrase da posição em *O valor das ideias* (2019) e do debate na Folha (2016); nenhuma citação entre aspas.

## Fora de alcance nesta rodada

- A cota de buscas web da sessão esgotou no meio do trabalho (limite compartilhado entre agentes). Não consegui: série diária de CDS e DI para estudo de evento formal; DI longo de dez/2024; mediana do neutro no Questionário Pré-Copom; série histórica da taxa de poupança do IBGE antes de 2024.
- `www.bcb.gov.br`, `api.bcb.gov.br`, `api.worldbank.org`, `en.wikipedia.org` bloqueados no proxy da sessão.

## Sugestões para a próxima rodada

1. Estudo de evento com séries diárias (DI jan+3 e jan+10, CDS 5 anos, câmbio, e uma cesta de moedas emergentes como controle) para 31/08/2015, 09/09/2015, 28/11/2024, 18/12/2024, 05/10/2026 e 26/10/2026.
2. Decomposição da curva em expectativa de Selic e prêmio a termo com dados do BCB (boxes do RPM) e comparação com México e Chile.
3. Comparar estimativas de juro neutro de Brasil, México, Chile e Colômbia pelo mesmo método (Holston-Laubach-Williams ou o do BIS) para testar a circularidade apontada em 6.3.2.
4. Gráfico de dispersão poupança × juro real entre emergentes (o build não tem tipo dispersão; seria preciso acrescentar).
5. Links pendentes para páginas que ainda não existiam no build: 8, 10.4 e 12.3.

## Revisão aplicada (02/11/2026)

Conferências feitas na aplicação do relatório conteudo/_revisao/6.md (substituem as marcas "de memória" acima):

- IPCA anual 1980–2025, IPCA 12 meses, administrados de 2015 (18,07%, SGS 4449) e Turquia: conferem com os brutos.
- Selic do JSON 6.2-desinflacao-2016-2017: jul/2017 = 9,25 e out/2017 = 7,50 (SGS 432, vigente no fim do mês); corrigidos.
- Medianas Focus da primeira pesquisa do ano (focus-anuais_ipca.json): 6,56 (02/01/2015), 4,86 (02/01/2017), 3,32 (04/01/2021), 5,30 (02/01/2023); usadas na 6.4.1.
- Juro real ex-ante 2018–2019 (Selic over SGS 4189, média do mês, sobre a mediana Focus suavizada de 12 meses do último dia do mês): entre 1,95% e 2,75% em 2018 e entre 0,83% e 2,72% em 2019; dez/2019 = 0,83% (0,65% pelo método da 2.3, com SGS 1178). IPCA: 3,75% (2018, centro 4,5%) e 4,31% (2019, centro 4,25%). O texto diz "abaixo do centro em 2018 e praticamente no centro em 2019", porque 2019 ficou 0,06 ponto acima do centro.
- BIS (WS_CBPOL, WS_LONG_CPI), fórmula de Fisher, 2026 = jan–set: Brasil 8,8 / 3,9 / 8,3; Chile 1,4, Índia 1,7 e África do Sul 3,0 em 2023–2026 (JSON corrigido); distância para a média de MX, CL, CO, IN, ZA: 6,6 (2000–2009), 3,1 (2010–2019), 5,5 (2023–2026); por ano, 1,2 (2018), 0,3 (2019), −0,1 (2020), −1,6 (2021).
- Turquia pelo BIS: 38,22% em jun/2023 (taxa 8,5% até 22/06), 75,43% em mai/2024, 31,07% em nov/2025, 30,9% em dez/2025 (taxa 38%), 29,73% em set/2026 (taxa 37%).
- Poupança nacional bruta 2024 (NY.GNS.ICTR.ZS, via Statistics of the World): Brasil 14,1 (= IBGE), Chile 21,8, México 19,3, Colômbia 13,6. Índia, Indonésia, China e Coreia continuam da compilação anterior (sem reconferência).
- Pessôa: coluna "Bolsonaro mantém contrato social da redemocratização" listada na página do autor no Blog do IBRE e na *Conjuntura Econômica* de set/2020; texto de 2019 no blog sobre o mesmo contrato.
- Debate na *Ilustríssima* (Folha), 2016: resposta de L. F. de Paula e E. Jabbour em 21/08/2016; de Oreiro e Gala em 23/10/2016. Título e data exatos do artigo de Lisboa e Pessôa não localizados.
- Bacha, Holland e Gonçalves (2009), RBE 63(4), confirmado no RePEc; versão no WBER 23(1), pp. 101–117. Resumo não lido; a 6.3 cita sem resultado.
- Pastore, Gazzano e Pinotti, *Inflação e crises: o papel da moeda*, Elsevier, 2014 (não 2015).
- África do Sul: meta de 3% ±1 anunciada pelo National Treasury em 12/11/2025, depois de o SARB passar a mirar 3% em jul/2025.

### "Holland e Padovani" (bastidor, fora do texto público)

O briefing citava "Holland e Padovani" como referência. Nenhuma obra conjunta foi encontrada; "Padovani" no debate público é Roberto Padovani, economista-chefe do BV, com entrevistas, e não com trabalho acadêmico com Holland. A referência acadêmica de Márcio Holland sobre o juro alto é Bacha, Holland e Gonçalves (2009, RBE 63(4); WBER 23(1)), agora na 6.3, ao lado de Gonçalves, Holland e Spacov (2007, RBE 61(1), pp. 49–75), que saiu do Para ler da 6.2. O coordenador deve confirmar se tinha outra obra em mente.

### Pendências após a revisão

- Pastore: o painel resume a posição dele sem página; falta citar um texto com data (coluna ou capítulo de *Inflação e crises*).
- Bacha, Holland e Gonçalves (2009): ler o resumo e acrescentar uma frase sobre o resultado.
- Artigo de Lisboa e Pessôa na *Ilustríssima* de 2016: título e data.
- CDS de 112 e 110 pontos (set e 09/10/2026): falta a data exata da matéria do InfoMoney.
- DI jan/27 em 28/11/2024: o ajuste da B3 não foi conferido; o texto diz "perto de 14%".
- Pontos de 14 e 15/10/2026 do DI jan/29 vêm de blog (O Cafezinho); trocar pelo ajuste da B3.
- Poupança de Índia, Indonésia, China e Coreia: reconferir na base do Banco Mundial.
- Expectativas de consumidores (Sondagem do Consumidor, FGV) e inflação implícita (prefixado × NTN-B): séries não reunidas (6.4.1).
- Estimativas de prêmio a termo (BCB, Tesouro, IFI) para a 6.1.1.
- Prazo médio da DPF em 2020–2021 (RMD) para a frase sobre o encurtamento da dívida na pandemia (6.1.1, hoje como leitura do painel).
- Carga tributária no início dos anos 1990 (6.1.2 cita só 33,7% em 2005, Receita Federal via Ipea, TD 1350).
- Estudo sobre a reforma previdenciária chilena e a poupança nacional (Holzmann, 1997, ou outro) para a 6.3.1.
- Abertura da LFT por detentor (RMD, tabela por indexador e detentor) para a 6.2.2.
- Link para 10.4 (6.1) e para 8 (6, 6.4.2): páginas ainda inexistentes.

### Achados de que a aplicação discordou ou aplicou de outro modo

- 6.2.1 nº 10 (método da Selic no mês da decisão): mantido o método e explicado no texto e no JSON, em vez de trocar pelo fim do mês.
- 6.2.2 nº 8 (LFT de 30,1% em 2011): mantido, porque o JSON dono (2.4-lft-na-dpf) traz o ponto de 2011 com fonte no RMD.
- 6.3.2 nº 8: a seção de estimativas foi reduzida a um parágrafo com link para a 2.3, mas o gráfico próprio foi mantido, com a diferença de método dita no texto e na nota.
- Coordenador pediu "inflação abaixo da meta" em 2018–2019: 2019 ficou em 4,31% contra centro de 4,25%; o texto diz "abaixo do centro em 2018 e praticamente no centro em 2019".
- Debate Lisboa × Pessôa: o coordenador indicou out/2016; a busca confirma que o debate correu de agosto a outubro de 2016 (resposta de Oreiro e Gala em 23/10/2016); o texto dá as duas datas.

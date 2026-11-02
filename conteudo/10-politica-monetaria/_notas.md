# Notas do bloco 10 (não vira página)

## Páginas entregues

- 10 Política monetária: instrumentos convencionais e não convencionais (página macro), 1ª versão, 1.995 palavras pela contagem do build (02/11/2026). Gráfico: `dados/10-compromissadas-conta-unica.json` (compromissadas do BC e conta única do Tesouro, % do PIB, dez/2006 a ago/2026, da tabela Divggnp.xlsx do BCB via insumo Frente J, consulta 28/10/2026).

## Fontes principais usadas

- BCB, tabela especial Divggnp.xlsx (compromissadas, conta única, DBGG conceitos BCB e FMI), via `insumos/frente-J.json`.
- Reservas de US$ 372,6 bi e 14,5% do PIB em ago/2026: texto de análise da Frente J.
- Selic (15% de jun/2025 a mar/2026; 13,75% em out/2026), juros nominais de 8,86% do PIB (SGS 5727 e 5793), crédito direcionado de 43,9% (SGS 20593/20539), LFT de 52,74% da DPF (RMD ago/2026), balanço do Fed de US$ 0,9 tri (2008) a US$ 4,5 tri (2015): `insumos/frente-K.json`.
- Juro real ex-ante de 8,7% (23/10/2026): página 9.1.
- Literatura citada sem recorte entre aspas (paráfrase): Poole (1970), McLeay, Radia e Thomas (2014), Borio e Disyatat (2009, BIS WP 292: princípio da separação e classificação das políticas de balanço), Bernanke (2020, AER: cerca de 3 p.p. de espaço adicional com neutro nominal de 2% a 3%), Taylor (1993), Bagehot (1873), Mishkin (2019, 12ª ed., cap. 15).
- Único recorte entre aspas: Constituição, art. 164, § 1º.

## Limites desta sessão

A cota de WebSearch da sessão estava esgotada quando o item começou, e WebFetch não resolveu bcb.gov.br, bis.org nem aeaweb.org. Nada foi conferido na web neste item; tudo o que tem número vem dos insumos ou de páginas já escritas.

## [a conferir]

- Base monetária e saldo de depósitos voluntários remunerados em ago/2026 (demonstrações financeiras do BCB de jun/2026; SGS 1788 para a base). Com eles, o balanço real da página fica completo.
- Carteira total de títulos do BC "perto de 22% do PIB" é aproximação do painel: títulos livres (11,7 p.p. = DBGG FMI 94,5% menos DBGG BCB 82,9%) mais compromissadas (10,3%), supondo lastro igual ao saldo das compromissadas. Conferir com o balancete do BCB.
- Comunicado do Copom de agosto de 2020 dizendo que o espaço remanescente para cortes, se houvesse, seria pequeno (paráfrase de memória; conferir texto e data).
- EC 106/2020 "não virou programa relevante" de compra de títulos: afirmação da Frente K, que ela mesma registra como não conferida em fonte primária.
- Texto literal do art. 164, § 1º, da Constituição: reproduzido sem abrir o Planalto nesta sessão; conferir a literalidade.
- URLs não abertas nesta sessão: página do RPM (`https://www.bcb.gov.br/publicacoes/rpm`) e Lei 14.185/2021 no Planalto (`.../2021/lei/L14185.htm`).
- Mishkin: capítulo 15 ("Tools of Monetary Policy") na 12ª ed. (2019) citado sem página; conferir numeração do capítulo na edição usada.
- Página BCB de instrumentos de política monetária e Relatório de Política Monetária (exigidos no cartão) não foram lidos; a página os cita só como referência geral.

## Divergências

- Reservas internacionais: US$ 372,6 bi em ago/2026 (Frente J, texto de análise, convertidas em R$ 1,93 tri e 14,5% do PIB) contra US$ 362,8 bi em set/2026 (Frente A, SGS 3546, conceito liquidez). A diferença pode ser de mês ou de conceito (total × liquidez); a página usa o dado da Frente J porque os demais itens do balanço são de ago/2026. Registrar em `_divergencias.md` se o coordenador quiser.

## Para a próxima rodada

- Montar o balanço real completo do BCB (ativo e passivo em R$ e % do PIB) a partir das demonstrações financeiras semestrais, e um gráfico longo da base monetária.
- Acrescentar um quadro instrumento × alvo operacional × canal de transmissão se a página ganhar folga de palavras (hoje está no teto de 2.000).
- Incluir recortes literais de Borio e Disyatat (2009) e Bernanke (2020) quando o texto puder ser aberto.
- Links para 1.1.3 (QE e juros sobre reservas), 1.1.4 (moeda endógena), 2.3 (juro neutro) e 2.4 (transmissão): a página liga hoje 1.1, 2.3, 2.4, 6.1, 7.1 e 9.1; trocar por netas específicas quando existirem.

## 10.1a

### Páginas entregues (02/11/2026)

- 10.1 Regimes e a meta (página-ponte), 1ª versão, 1.099 palavras pela contagem do build. Sem gráfico; tabela dos três regimes.
- 10.1.1 Regimes monetários e o caso brasileiro, 1ª versão, 3.498 palavras pela contagem do build (que conta URLs e a tabela; a prosa fica perto de 3.000). Gráficos: `dados/10.1.1-ipca-meta-1999-2025.json` (IPCA anual × centro, piso e teto, 1999–2025) e `dados/10.1.1-ipca-12m-meta-continua.json` (IPCA de 12 meses mês a mês, dez/2024 a set/2026, com faixas de 1,5%, 3% e 4,5%). Tabela ano × meta × intervalo × IPCA × cumpriu, 1999–2026.

### Fontes principais

- Metas e intervalos 1999–2024: tabela "Histórico de Metas para a Inflação no Brasil" do BCB (`bcb.gov.br/pec/metas/tabelametaseresultados.pdf`), lida por WebSearch (o site do BCB não abre por fetch), conferida contra `dados/4.1-ipca-meta-teto.json`, `6.2-ipca-meta.json` e `7.1-ipca-meta.json`. Revisões de 2003 (Res. CMN 2.972, de 27/06/2002: 3,25% ±2 para 4% ±2,5) e 2004 (Res. 3.108, de 25/06/2003: 3,75% para 5,5% ±2,5).
- IPCA anual: IBGE, SIDRA 1737 (via insumo Frente C para 2015–2025 e dados já publicados do painel para 1999–2014).
- IPCA de 12 meses 2025–2026: Planejamento (mai/2025 5,32%), Agência Brasil/Congresso em Foco (nov/2025 4,46%, 13 meses acima do teto), tabela da UFMS (jan–mar/2025), notas de imprensa com dados do IBGE (jun–out/2025, ago/2026), Frente C (set/2026 4,58%) e agregador Investidor10 (jan, mar, abr, jun, jul/2026).
- Decreto 3.088/1999 (art. 2º citado; texto confirmado por busca em Planalto/Câmara/Poder360); Decreto 12.079/2024 (art. 3º citado; antecedência de 36 meses; revogação do 3.088 em 01/01/2025); Resolução CMN 5.141/2024 (3% ±1,5 desde jan/2025; texto reproduzido em lex.com.br); nota da Fazenda de jun/2024; carta aberta de 10/07/2025 e nota do RPM de dez/2025; LC 179/2021 (art. 1º citado; mandatos de quatro anos, presidente a partir do 3º ano do mandato presidencial, diretores escalonados); STF, ADI 6696, 8 a 2, 26/08/2021 (via Migalhas).
- Literatura: Bernanke e Mishkin (1997, JEP 11(2), recorte do resumo, "constrained discretion"); Svensson (1997, EER 41(6), recorte do resumo); Goodhart (1975/1984, recorte na forma consagrada); Mishkin (1999, JME 43(3): Bundesbank errou as faixas de moeda em cerca de metade das vezes); Mishkin e Posen (1997); Bogdanski, Tombini e Werlang (2000, BCB WP 1, paráfrase do resumo); Obstfeld, Shambaugh e Taylor (2005); Friedman (1968); Sargent e Wallace (1975); Brash (1999, RBNZ) para a Nova Zelândia; levantamento de 41 países com metas de inflação 1990–2024 (*Data in Brief*, 2025).
- 1998–1999: pacote de US$ 41,5 bi com US$ 18 bi do FMI (FMI e Casa Branca, nov/1998); reservas de US$ 74,66 bi em abr/1998 (BCB via Gazeta do Povo); Selic de 39% para 45% em 04/03/1999 (Comunicado BCB 6.629); dólar médio de dez/1998 e fev/1999 de `dados/1.2.3-cambio-1994-1999.json`.

### [a conferir]

- Reservas no fim de 1998: fontes dão entre US$ 40 e 45 bi (texto usa a faixa, marcada); conferir SGS 3546.
- Causas citadas carta a carta (2001, 2002, 2015, 2017, 2021, 2022, 2024): o texto resume os choques de cada episódio a partir das páginas 4.2 e 7.1 e da memória comum dos episódios; não li as cartas. A causa de 2025 (inércia, expectativas desancoradas, bandeiras de energia) está conferida por busca.
- IPCA de 12 meses de jan, mar, abr, jun e jul/2026 vem de agregador; conferir na SIDRA 1737.
- Mishkin (2019): capítulo de estratégia citado como "parte IV", sem número de capítulo nem página; a lista das cinco peças do regime é a do manual, de memória.
- Frase de Gerald Bouey sobre o M1 ("we did not abandon M1, M1 abandoned us") foi retirada do texto por não ter fonte primária conferida (aparece em Freedman, conferência do Fed de Boston, ano não confirmado).
- Recortes traduzidos de Bernanke e Mishkin e de Svensson vêm dos resumos (NBER/AEA e RePEc), não do corpo dos artigos; página do recorte de Goodhart não confirmada.

### Lacunas e sugestões

- 10.1.2 (nível ótimo da meta) ainda não existe; as duas páginas já apontam para ela (AVISO do build).
- 6.4 (autonomia do BC) ainda não existe; 10.1.1 aponta para ela.
- Falta um quadro com as expectativas Focus de prazo longo × meta desde 2001 (série do BCB) para medir a ancoragem; ficaria bem em 10.1.1 ou em 2.4.1.
- Se o site do BCB abrir, ler as nove cartas abertas e trocar o parágrafo de causas por uma tabela ano × causa citada pelo BC × presidente do BC.

## 10.1b

### Página entregue (02/11/2026)

- 10.1.2 O nível ótimo da meta, 1ª versão, 3.492 palavras pela contagem do build (que conta URLs, fórmulas e a tabela; a prosa fica perto de 2.900). Gráfico: `dados/10.1.2-metas-emergentes.json` (barras horizontais, centro da meta de 10 emergentes mais Fed e BCE). Tabela de metas com fonte por linha; dois exemplos de brinquedo (salário nominal rígido; probabilidade de piso com $i^* = r^* + \pi^*$); conta da razão de sacrifício para 4,5% → 3% e 4,5% → 4%; quadro A favor/Contra; caixa "o painel lê".

### Fontes principais (todas por WebSearch em 02/11/2026; WebFetch não resolveu federalreserve.gov, nber.org, brookings.edu nem readkong)

- Recortes literais: Fed 2012 (texto reproduzido pelo Fed de Cleveland); BCE 2021, simetria (reproduzido pelo Banco da Finlândia); Ball (2014, resumo do IMF WP 14/92); Yehoue (2012, resumo do IMF WP 12/189); Blanchard, Dell'Ariccia e Mauro (2010, p. 11, mesmo recorte da página 7.1, confirmado por busca). Fed 2020 ("inflation that averages 2 percent over time") citado em linha, conferido em CRS e Central Banking.
- Fed 2025 (22/08/2025, retirada da média e da ênfase no piso; 2% fora do escopo da revisão): release do Fed e nota FEDS de 22/08/2025, lidos por busca.
- Boskin (1996): 1,1 ponto (0,8 a 1,6), relatório reproduzido em ssa.gov. Gordon (2006): 0,8 ponto, via CSLS (não entrou no texto final por espaço).
- Nova Zelândia: Brash (1999, RBNZ) e Hoover Institution; Douglas na TV em 01/04/1988; 1 ponto somado pelo viés de medida.
- Coibion, Gorodnichenko e Wieland (2012): "abaixo de 2%" (o resumo diz "< 2%"; a faixa "1,5% a 2%" do cartão não foi encontrada em texto e não entrou). Kiley e Roberts (2017): até 40% do tempo no piso, contra menos de 5% na visão pré-crise.
- Metas: Índia (notificação de 25/03/2026, 4% com 2% a 6%, abr/2026 a mar/2031, via Trading Economics e outros); África do Sul (12/11/2025, 3% ±1, via SAnews e imprensa); Indonésia (2,5% ±1, PMK 31/2024, via Pajakku e falas do BI); Turquia (5% de médio prazo; intermediárias de 24% para 2026, 15% para 2027 e 9% para 2028, via intellinews e Turkish Minute); Rússia (4%, diretrizes 2027–2029 do Banco da Rússia); México (3% ±1 desde 2003, Central Banking/Bloomberg Tax set/2026); Colômbia (3%, faixa de 2% a 4% desde 2010, BanRep); Peru (2% ±1 desde 2007, BBVA Research); Chile (3% ±1, horizonte de dois anos, IPoM de set/2007).
- Brasil: Werlang (Bloomberg Línea, 25/01/2023: 4% ou 4,5%); Borges e Araújo (Bloomberg Línea, sem data visível: inflação ótima de ~4% com dívida perto de 70% do PIB); Borges no blog do IBRE (simulação do BC: corte de 0,75 ponto na meta reduziu juros nominais em ~0,40 ponto em 2019–2021, juro real +0,3; dívida ~2 p.p. do PIB maior em 2030 com meta de 3%); Gonçalves e Carvalho (2009, JMCB) × Brito (2010, JMCB); Ipea, nota técnica de dez/2015 (Cavalcanti et al. 2015, razão de sacrifício num DSGE depende da regra fiscal).
- Peso de Alimentação e bebidas no IPCA: 21,75% (IBGE, IPCA de jun/2026, via Diário de Pernambuco). Revista Oeste dá 19,3%, sem data; não usado.
- Insumos: Frente C (IPCA set/2026 4,58%; Focus de 23/10/2026: 5,19% para 2026 e 4,34% para 2027; PIB 2025 +2,3%); Frente K / CONTEXTO (LFT 52,7% da DPF, ago/2026); página 2.3 (neutro de 5% do Copom desde dez/2024).

### [a conferir]

- Valores numéricos da razão de sacrifício na nota técnica do Ipea de dez/2015 (um trecho visto em busca falava em ~4,5 em três anos numa réplica do SAMBA; não entrou como fato).
- Boxe ou documento do BC de onde vem a simulação citada por Borges (redução de 0,75 ponto da meta → juros nominais −0,40 ponto em 2019–2021). Post do blog do IBRE de 2020 citado pela página de autor, sem URL do post.
- Data da entrevista de Bráulio Borges à Bloomberg Línea (meta contínua, núcleo, 4% com dívida de 70%).
- Ano de início da meta chilena de 3% com intervalo de ±1 (2001 pela literatura).
- Número da simulação de Akerlof, Dickens e Perry (1996) para o desemprego com inflação zero: o texto diz só "vários pontos", conforme crítica posterior; conferir tabela do artigo.
- Summers (1991): páginas (RePEc dá 625–631; outro registro dá 619–624). Não citei a faixa de inflação ótima que ele propôs porque não a confirmei.
- Bernanke e Mishkin (1997): a leitura de que metas ficam acima de zero por viés de medida e risco de deflação é paráfrase de memória do artigo; conferir passagem e página.
- Autoria da How-To Note do FMI de 2026 sobre metas em emergentes (busca indicou Carter, Kamber e Otten) e conteúdo do boxe sobre Balassa-Samuelson; Masten (2005) citado pelo resumo.
- URLs das fontes secundárias da tabela sem link no corpo: BBVA Research (Peru) https://www.bbvaresearch.com/wp-content/uploads/epub/67403_159457.epub; Pajakku (Indonésia) https://pajakku.com/artikel/berapa-target-sasaran-inflasi-tahun-2025-2026-dan-2027; intellinews (Turquia) https://www.intellinews.com/turkey-hikes-end-2026-official-inflation-forecast-to-28-461006/.

### Lacunas e sugestões

- Falta estimativa de viés de medida do IPCA (nenhuma achada) e evidência brasileira de rigidez de salário nominal para baixo (há trabalhos com RAIS; procurar).
- Falta a estimativa do próprio BC de razão de sacrifício (Relatório de Inflação/RPM); se o site do BCB abrir, procurar boxes de "custo da desinflação" e "redução das metas" (2017).
- O cartão pedia CGW "ótimo entre 1,5% e 2%"; a fonte encontrada diz "abaixo de 2%", e o texto ficou com isso.
- A página está no teto de 3.500 palavras pela contagem do build; para crescer, mover a tabela de metas para JSON-tabela ou cortar URLs da tabela.

## 10.2a

### Páginas entregues (02/11/2026)

- 10.2 Instrumentos convencionais (página-ponte), 1ª versão, 1.001 palavras pela contagem do build. Exemplo de brinquedo (caixa-d'água com seis registros), um parágrafo por neta 10.2.1 a 10.2.6, caixa "o painel lê". As netas 10.2.2 a 10.2.6 ainda não existem (AVISO do build).
- 10.2.1 Taxa básica e corredor, 1ª versão, 3.493 palavras pela contagem do build (no teto; a prosa sem "Para ler" e URLs fica perto de 3.100). Gráficos: `dados/10.2.1-meta-menos-over.json` (meta menos over, média mensal das diferenças diárias, mar/1999 a out/2026), `dados/10.2.1-compromissadas-depositos.json` (compromissadas e depósitos voluntários, % do PIB, dezembros 2006–2025 e ago/2026), `dados/10.2.1-depositos-voluntarios.json` (saldo mensal em R$ bi, out/2021 a set/2026). Exemplo de brinquedo dos dois bancos, fórmula de anualização com exemplo resolvido, quadro A favor/Contra (subsídio a bancos?), caixa "o painel lê".

### Fontes principais

- Dados: `dados/brutos/` SGS 432, 11, 12, 4189, 3546, 4382 e 28964 (consulta em 02/11/2026); BIS, taxas de política, Brasil, fim de mês (para a meta de 2000–2009); tabela Divggnp.xlsx do BCB lida pela Frente J (compromissadas e conta única, consulta em 28/10/2026).
- Recortes literais: definição da Selic over (BCB, Plano diretor de acompanhamento da taxa Selic, via busca); ementa da Lei 14.185/2021; declaração do FOMC de 30/01/2019 (tradução do painel; texto conferido em citações do NY Fed e do próprio Fed); título do texto de Fattorelli e da NT Ipea Dides 05/2022.
- Fed: implementation note de 16/09/2026 (intervalo 3,75%–4,00%, IORB 3,90%, ON RRP 3,75%, redesconto e SRF 4,00%) e de 28/10/2026 (IORB mantida), por busca. BCE: comunicado de 13/03/2024 (DFR como taxa diretora, spread MRO–DFR de 15 pb desde 18/09/2024). BoE: Quarterly Bulletin 2013 (reservas remuneradas à Bank Rate desde mar/2009) e discussion paper de 2024 (repo-led).
- Literatura: Borio (1997, BIS Economic Papers 47), Bindseil (2014, OUP), Keister, Martin e McAndrews (2008, FRBNY EPR 14(2)), Borio (2023, BIS WP 1100), Silva Jr. (2012, BCB TD 278: over abaixo da meta em 100% dos dias de 2007 a 2010), Pellegrini (2017, IFI EE 3: reservas desde 2007 e resgate líquido do Tesouro explicam as compromissadas), Barbosa e Terra (2025, *Economia e Sociedade* 34(2): juros foram o fator principal do crescimento de 2002 a 2020). Todas parafraseadas a partir de resumos e buscas; nenhum PDF aberto (WebFetch não resolve bcb.gov.br, senado.leg.br, ipea.gov.br nem scielo.br).
- Debate: Auditoria Cidadã (Fattorelli), Schwartsman (via clipping da Abras), Goldenstein (via Nogueira da Costa, 2023), Agência Brasil (ago/2021) e Poder360 (fev/2022) para a regulamentação e o acesso ampliado; Oreiro (2026, Substack) sobre a proposta de Lara Resende.

### Contas do painel (conferir se o coordenador quiser)

- Compromissadas de ago/2026 em reais: 10,28% × PIB de 12 meses de R$ 13,34 tri (SGS 4382) ≈ R$ 1,37 tri.
- Depósitos voluntários: R$ 165,7 bi em ago/2026 = 1,24% do PIB; R$ 192,2 bi em set/2026 = 1,43%.
- Custo bruto anual das compromissadas: estoque médio ~9% do PIB (7,8% em dez/2025, 10,3% em ago/2026) × over de 14,6% (SGS 4189, 12 meses até ago/2026) ≈ 1,3% do PIB, ~R$ 170 bi; depósitos ≈ R$ 23 bi. Ordem de grandeza, sem descontar o que o BC recebe.
- "Perto de 15% da conta de juros": 1,3 / 8,9 (juros nominais de 12 meses até ago/2026, SGS 5727 e 5793, via página 10).
- Meta menos over: a cópia de `sgs-432.json` não traz 2000–2009 (a API limita a 10 anos por consulta); usei a meta de fim de mês do BIS só nos meses em que ela não mudou. Desde 2014 a média mensal fica entre 0,098 e 0,100 ponto (154 meses).

### [a conferir]

- Por que a distância over–meta se fixou em exatamente 0,10 ponto desde 2014: não achei explicação oficial; a hipótese dos fundos que emprestam abaixo da meta está marcada como hipótese.
- Lei 13.820/2019: o parágrafo sobre resultado do BC foi cortado por espaço; ficaria bem na neta 10.2.2 com os valores dos repasses ao Tesouro de 2019 a 2025.
- Custo de carregamento das reservas (compromissadas à Selic × rendimento das reservas): falta fonte primária (notas de política fiscal do BCB).
- Tratamento estatístico dos depósitos voluntários: o texto diz que ficam fora da DBGG no conceito do BCB (deduzido do desenho e dito por Agência Câmara, Ipea e Insper); conferir na nota metodológica das Estatísticas Fiscais.
- Resolução BCB 129/2021: data (19/08/2021 em duas fontes, 14/07/2021 num ofício do BCB ao Senado que parece confundir com a lei) e modalidades (a prazo, até 12 meses; Poder360 fala também em depósitos de um dia). Não li a norma.
- Borio (2023): a leitura "defende sair do piso pelo custo de juros de um balanço grande" é do título e da memória do texto; conferir o resumo.
- Bindseil "dirigiu a área de operações de mercado do BCE": conferir cargo e período.
- SGS 27815 (no arquivo bruto como "base monetária", valores de R$ 16 tri em 2026) parece ser a base monetária ampliada, não a restrita; não usei. A base restrita (SGS 1788) segue faltando para o balanço real da página 10.
- Proposta de Lara Resende (nov/2026): só imprensa e agregadores (faixa de 3% a 5,5%, trajetória até 7% ou 7,5% em 12 meses, números divergentes); o texto cita a proposta sem números.

### Sugestões

- 10.2.2 deve retomar o resultado do BC (Lei 13.820/2019), a emissão de títulos do Tesouro para a carteira do BC e o balanço real completo.
- Se o site do BCB abrir: ler o PDA-TS e o Relatório de Administração do Selic para a explicação oficial dos 0,10 ponto e o volume das operações de nivelamento.

## 10.2b

### Página entregue (02/11/2026)

- 10.2.2 Operações de mercado aberto e a carteira do BC, 1ª versão, 3.495 palavras pela contagem do build (inclui tabelas, fórmula e "Para ler"). Gráficos: `dados/10.2.2-dbgg-bcb-fmi.json` (DBGG conceito BCB, conceito FMI e diferença, dezembros 2006–2025 e ago/2026) e `dados/10.2.2-carteira-bc.json` (carteira estimada do BC: títulos livres = FMI menos BCB; títulos em compromissadas = saldo das compromissadas). Exemplo de brinquedo (BC com 100 de títulos, banco que precisa de 10 por uma semana; preço de recompra $10 \times 1{,}15^{5/252} = 10{,}028$; regra de 4%/5% resolvida, $x = 2{,}1$), quadro do que entra em cada medida de dívida, tabela de resultados do BC 2018–2025, quadro A favor/Contra, caixa "o painel lê".

### Fontes principais

- Dados: BCB, SGS 13762 (DBGG BCB), 4513 (DLSP), 4382 (PIB 12 meses) e 3546 (reservas), consulta em 02/11/2026; tabela especial Divggnp.xlsx (DBGG FMI, compromissadas, conta única), lida em 28/10/2026 e já usada nas páginas 3.x e 10; juro real ex-post de `dados/2.1-juro-real-1995-2026.json` (médias 1995–2001 = 17,4% e 2003–2025 = 5,4%, cálculo do painel).
- Lei: LRF art. 34 (único recorte entre aspas, texto confirmado por busca em agregador jurídico) e art. 39 § 2º; CF art. 164 §§ 1º a 3º (parafraseados); Lei 11.803/2008 (origem na MP 435/2008); Lei 13.820/2019, arts. 3º a 5º e 7º (4%/5% da carteira livre; § 1º define "livres"), por busca em Planalto/Câmara/Senado/JusBrasil/Migalhas.
- FMI: Country Report 23/289 (2023, Selected Issues, medida do FMI = medida do BCB anterior a 2008); Country Report 26/191 (Artigo IV de 2026: carteira do BC de 22,4% do PIB em abril de 2026, que confere com a estimativa do painel de 21,9% em agosto); Artigo IV de 2023 (Lei 13.820 aproxima o Brasil da prática internacional sobre ganhos não realizados). GFSM 2014 parafraseado (banco central fora do governo geral).
- Resultado do BC: Exame/Meon (lucro de R$ 165,9 bi no 1º sem. 2018, regra de ouro de 2019); Agência Brasil (2018, 2023, 2024 e 2025); imprensa e nota do CMN de 27/08/2020 (R$ 325 bi; pedido de R$ 445 bi via Reuters; 1º sem. 2020 cambial R$ 478,5 bi e demais R$ 24,7 bi); Terra, Roncaglia, Bianchini e Leão (2020, FGV EAESP NT 1/2020: equalização positiva em 9 semestres, R$ 694 bi; negativa em 14, ≈ R$ 662 bi, 2008 a 1º sem. 2019).
- Literatura: Pellegrini (2017, IFI EE 3: hipótese de gestão segmentada; natureza monetária das compromissadas), Barbosa e Terra (2025), Leister (2016, Tesouro TD 26), Lopreato (2018, IE/Unicamp TD 327; o TD 139 sobre moeda indexada aparece só por busca), Oreiro, Paula, Silva e Amaral (2012, REP 32(4): LFT de duração zero e efeito riqueza), Bindseil (2014). Tudo parafraseado; nenhum PDF aberto (WebFetch não resolve gov.br, camara.leg.br, fgv.br, imf.org espelhos).
- Internacional: Fed, Monetary Policy Report de jul/2026 (ativo diferido ≈ US$ 236 bi); BCE, comunicado de 26/02/2026 (prejuízo de € 7,944 bi em 2024 e € 1,254 bi em 2025); Chile (BCCh: PDBC, BCP, BCU; LOC art. 27; Leis 21.253 e 21.265 de 2020); Coreia (MSB de 107,29 tri de wons no fim de 2025 para 95,16 tri em mar/2026, Aju Press, ago/2026).

### Contas do painel (conferir se o coordenador quiser)

- Carteira do BC ≈ (DBGG FMI − DBGG BCB) + compromissadas: 11,66 + 10,28 = 21,94% do PIB em ago/2026, ≈ R$ 2,9 tri sobre PIB de R$ 13,34 tri. Supõe lastro igual ao saldo das compromissadas e trata a diferença FMI − BCB como títulos livres (há pequenas diferenças de valoração).
- Diferença FMI − BCB: mínimo 5,34 p.p. (2014), máximo 14,69 (2025), média 10,8 em 2016–ago/2026 e 9,2 em 2006–ago/2026. O cartão falava em "cerca de 12 p.p."; o texto usa 11,7 (ago/2026) e a faixa.
- R$ 325 bi ≈ 4,3% do PIB de 2020 (SGS 4382, R$ 7,61 tri).

### Lacunas e [a conferir] (nada disso entrou como fato)

- "Episódio de 2019–2020" do cartão: o que se achou foi a transferência do lucro do 1º sem. 2018 (Lei 11.803, usada na regra de ouro de 2019) e a de R$ 325 bi em ago/2020 (Lei 13.820, art. 5º). Não se achou quanto dos R$ 325 bi foi efetivamente usado em resgates, nem se houve nova transferência em 2021 (uma manchete fala em "repassar R$ 71,7 bi" do lucro de 2021; outra diz que a reserva foi esgotada em 2022 com R$ 85,9 bi; números conflitantes, não usados).
- Saldo da reserva de resultado depois de 2025: R$ 112,82 bi (Agência Brasil); um site dá R$ 122,82 bi. Usado o da Agência Brasil, que fecha com 263,08 − 150,26.
- Destino do resultado positivo das demais operações (R$ 30,29 bi) em 2025, ano de prejuízo total: não confirmado; o texto não diz.
- Datas exatas de vencimento dos últimos BBC, LBC e NBC-E (há NBC-E com vencimento em nov/2005 em registros de mercado). O texto diz só que o BCB informa que todos foram resgatados.
- Texto literal do Manual de Estatísticas Fiscais ("estreita relação") e da NT 47 visto só por paráfrase em fonte secundária (Jaloretto, Corecon-DF).
- O "relatório de gestão do BCB de 2018" como fonte da regra de 4%/5% no regime anterior veio de resumo de busca; conferir o dispositivo da Lei 11.803 ou MP que a criou.
- Afirmação de que a dívida americana em poder do público inclui os títulos do Fed e de que o RMD mede a DPF em poder do público sem a carteira do BC: conhecimento padrão, sem fonte aberta nesta busca.
- Blog do IBRE "Três erros sobre o repasse cambial do BC ao Tesouro": título e trecho (repasse não afeta o primário) vistos por busca; autor e data não confirmados.
- IFI: o box do RAF de abril de 2017 sobre a relação Tesouro–Bacen e a apresentação "Relacionamento Tesouro Nacional–Banco Central" de Pellegrini foram localizados mas não lidos.

### Divergências

- Compromissadas e DBGG FMI vêm da Divggnp (consulta 28/10/2026); DBGG BCB do SGS 13762 (consulta 02/11/2026). Mesmo valor de ago/2026 (82,87) nas duas fontes; nenhuma divergência com 3.1, 3.2, 10 e 10.2.1.
- O gráfico `dados/3-divida-conceitos.json` reconstruía a DBGG BCB de 2006–2014 pelos fatores condicionantes; o SGS 13762 bruto agora cobre desde dez/2006 e os valores batem com diferença de até 0,05 p.p. Sugestão: a área 3 pode trocar a reconstrução pelo SGS.
- Página 10 diz "Desde 2002 o BCB não pode emitir título próprio (LRF, art. 34)": consistente (maio de 2002).

## 10.2c

### Página entregue (02/11/2026)

- 10.2.3 Redesconto e assistência de liquidez, 1ª versão: cerca de 3.050 palavras de prosa antes do "Para ler" (3.891 pela contagem do lint, que inclui tabela, fórmulas e referências). Gráfico `dados/10.2.3-linhas-2020.json` (barras: potencial anunciado × uso da LTEL-LFG e do Novo DPGE). Exemplo de brinquedo (banco com R$ 100 de empréstimos, R$ 5 de reservas, saques de R$ 20; venda forçada a 70% com perda de 6,4 contra redesconto a Selic + 1 por 10 dias úteis, custo $15 \times (1{,}16^{10/252}-1) = 0{,}09$; versão insolvente com capital −10), tabela de modalidades e custos, conta do custo extra de R$ 1 bi por um dia a Selic + 0,35 (≈ R$ 12 mil), quadro A favor/Contra, caixa "o painel lê".

### Fontes principais

- Bagehot (1873), cap. VII: recorte em inglês confirmado só por reprodução em Goodhart (1999) e na Wikipedia; a segunda regra ("as largely as the public ask for them") não foi confirmada e ficou fora das aspas. Goodhart (1999), *International Finance* 2(3); Tucker (2014, BIS Papers 79) e Tucker (2020, JFC 2(2), recorte do resumo); Mishkin (2019) e Minsky (1986) parafraseados.
- Brasil, normas: Lei 4.595/1964 art. 10, V e LRF art. 28 § 2º (parafraseados de memória e de resumos de questões; texto do Planalto não aberto); Res. CMN 2.949/2002 e Circular 3.105/2002 (modalidades intradia, 1 dia, 15 dias úteis, 90 dias corridos); Res. BCB 175/2021 (redesconto intradia e de um dia); Res. BCB 220/2022 (revoga o regime de 2002 a partir de 02/05/2022, segundo a nota de revogação na própria Res. 2.949); Res. BCB 110/2021 e 374/2024 (LFL).
- Custos: página "Liquidity facilities" do BCB (por busca): intradia sem juros; um dia a Selic + 35 p.b.; LLI 65 p.b. e LLT 90/65/55 p.b. desde 02/01/2023 (antes 60 e 75/50/40). BIS Markets Committee Compendium (2019) e FMI CR 18/345 davam 100 p.b. para o de um dia.
- PROER: CPI do PROER, relatório final, cap. 2 (total ≈ R$ 20,4 bi; Nacional 5,9, Econômico 5,2, Bamerindus 3,3; BC admitia perda ≥ R$ 10 bi); Res. CMN 2.208 e MP 1.179 de 03/11/1995, Lei 9.710/1998; Maia (1999, BIS Policy Papers 6).
- PROES: MP 1.514/1996; BCB, tabela de títulos emitidos (R$ 61.922,68 milhões); Salviano Jr. (2004, livro do BCB). Custos em % do PIB: de Mello e Garcia (2011, Valor) ≈ 0,9% PROER e 5,7% PROES; média de 12,8% do PIB em 40 países (Banco Mundial, via Leite Júnior, 2016, dissertação UnB).
- 2008: Mesquita e Torós (2010, BCB TD 202): R$ 116 bi de compulsório liberado em 2009 (p. 13, via citação secundária), redesconto "não chegou a ser utilizado", vendas à vista US$ 14,5 bi, leilões com recompra US$ 11,8 bi, empréstimos com reservas US$ 12,6 bi (tabela 2, via reprodução em artigo da SciELO); MP 442 (Lei 11.882/2008), MP 443 (Lei 11.908/2009); swap do Fed de US$ 30 bi (Fed, 29/10/2008), nunca sacado (Yale YPFS).
- 2020: Res. CMN 4.785, 4.786 e 4.795; Carta-Circular 4.042 (Selic + 0,6); potencial total R$ 1.274 bi = 17,5% do PIB (BCB, Evolução Recente do Crédito no SFN, 29/01/2021; TCU); LTEL-LFG potencial R$ 670 bi, 245 operações, 51 IFs, R$ 121,9 bi, últimas liquidadas em 07/12/2022, sem inadimplência (nota do BCB de 23/12/2022 via Legismap e Reuters); saldo ≈ R$ 46 bi em dez/2020 e predominância de S3/S4 (apresentações técnicas das reuniões 233 e 235 do Copom); Novo DPGE R$ 22,6 bi em 74 IFs até o início de nov/2020, potencial R$ 200 bi (dados do BCB via Estadão/Terra); compulsório 25% → 17% (R$ 68 bi, gov.br 23/03/2020); swap do Fed de US$ 60 bi não sacado (Yale JFC 2023).
- Fed: comunicados de 15/03/2020 (crédito primário no teto do intervalo) e 12/03/2023 (BTFP pelo valor de face); Bernanke (2010, ≈ US$ 1,5 tri de crédito no fim de 2008); GAO-21-180 (≈ US$ 24 bi usados nos programas da Lei CARES até 15/11/2020); Klee, Kotidis e Siemer (2025, FEDS 2025-099: fim das novas operações em 11/03/2024, tudo pago até 07/03/2025). BCE: LTROs de 3 anos (€ 489,2 bi, 523 bancos; € 529,5 bi, 800 bancos; Yale YPFS); procedimentos da ELA (2014).
- Banco Master: liquidação em 18/11/2025; garantias do FGC ≈ R$ 40,6 bi (imprensa de set/2026; InfoMoney e IstoÉ Dinheiro para o "maior acionamento").

### Lacunas (nada disso entrou como fato)

- O cartão cita a "Resolução CMN 4.581/2017" como norma do redesconto. A 4.581, de 07/06/2017, trata de subdirecionamento de recursos de LCA (MCR 6-7), não de redesconto. A página usa a cadeia Res. CMN 2.949/2002 → Res. BCB 175/2021 → Res. BCB 220/2022 → LFL (Res. BCB 110/2021 e 374/2024). Não li o texto da Res. BCB 220; o que ela regula além da revogação ficou sem confirmação.
- O cartão cita "Maia 2003"; a referência localizada é Maia (1999), BIS Policy Papers 6, p. 106–123.
- Sites do BCB, ANBIMA, IE/UFRJ, Gutenberg e blogs não abriram (DNS bloqueado); tudo veio de busca. Não li o REF 2008–2009 e 2020, o Relatório de Gestão/Integrado de 2020 nem o boxe "Resultado da oferta de liquidez pelo BC 2020–2023" do REB 2023 (reb2023b8p.pdf), que provavelmente traz o uso consolidado por modalidade e o resultado financeiro das linhas. Ele é a fonte para trocar o gráfico por um completo.
- Uso efetivo da LTEL-Debêntures (potencial R$ 91 bi), das compromissadas com títulos soberanos em dólar (potencial R$ 50 bi) e das compras da EC 106: não confirmado. Uma tabela do BCB reproduzida por de Paula (2021, IE/UFRJ TD 016) dá "implementado" de R$ 310,1 bi contra potencial de R$ 1.221,8 bi, com LTEL-LFG 41,3 e DPGE 23,2, sem data visível; outra apresentação do BCB dá R$ 427,1 bi implementados contra R$ 1.274 bi. Não usados por falta de data e de detalhamento.
- Compulsório liberado em 2008: R$ 116 bi (Mesquita e Torós, 2010, p. 13, via citação) contra R$ 82 bi (apresentação do BCB de 23/03/2020). O texto dá os dois e diz que são de data e conceito diferentes; a neta 10.2.4 deve fixar o número.
- Pico do saldo do BTFP (fala-se em US$ 165–168 bi no início de 2024): não confirmado no H.4.1; não usado.
- Lucro ou resultado do BC com as linhas de 2020: não confirmado; o texto diz só "sem inadimplência".
- Valores das compras do BB (Votorantim) e da Caixa (Panamericano) em 2008–2009: não confirmados; o texto cita as operações sem valor.
- PROES: o "integral se privatizado/extinto, metade se mantido" vem de resumo (Wikipedia); conferir na MP 1.514.

### Divergências

- Nenhuma com 10, 10.2, 10.2.1 e 10.2.2. Selic over de 13,65% (out/2026) e redesconto do Fed no teto do intervalo são os mesmos de 10.2.1.
- Custo do PROES: 5,7% do PIB (de Mello e Garcia) contra 2,1% do PIB numa apresentação do BCB (Goldfajn, 2002) e "R$ 90 bi" num texto do PET-UFF; a página usa só a estimativa de 5,7% e os R$ 61,9 bi de títulos do BCB.

## 10.2d

### Página entregue (02/11/2026)

- 10.2.4 Recolhimento compulsório, 1ª versão: cerca de 2.900 palavras de prosa antes do "Para ler" (3.050 contando parênteses de fonte; 4.118 pela contagem do lint, que inclui tabela, fórmulas e referências). Gráfico `dados/10.2.4-aliquotas.json` (linha: alíquotas nominais à vista, a prazo e poupança, nov/2017 a out/2026). Exemplo de brinquedo (R$ 100 à vista, 21% sem remuneração, Selic 15%: cunha de 3,99 pontos; CDB com recolhimento remunerado pela Selic: cunha zero; poupança: cunha menor), fórmula $c = \alpha i/(1-\alpha)$ com Selic de 15%, 13,75% e 2%, multiplicador $1/r$ e por que deixou de valer (link 1.1.4), tabela das modalidades, história 1994–2026, crises de 2008, 2020 e 2026, aperto de dez/2010, peso no spread, comparação internacional, quadro A favor/Contra e caixa "o painel lê".

### Decisão sobre 2008 (R$ 116 bi × R$ 82 bi)

- R$ 99,8 bi: liberação efetiva do saldo de recolhimentos entre 24/09/2008 e 19/01/2009 (BCB, Relatório Anual 2008, cap. 2, frase reproduzida pela busca). É o número que a página adota para "quanto saiu do BC"; 3,2% do PIB de 2008 (SGS 4382, R$ 3,11 tri; conta do painel).
- R$ 116 bi (≈ 4% do PIB de 2009): contrafactual de Mesquita e Torós (2010, TD 202, p. 13): exigível pelas regras pré-crise no fim de ago/2009 (≈ R$ 295 bi) menos o efetivamente recolhido (R$ 179 bi). Inclui o aumento adiado (Circular 3.405) e o crescimento dos depósitos. A página o usa para "quanto o BC deixou de recolher".
- R$ 82 bi: apresentação do BCB de 23/03/2020 ("durante a crise de 2008 a liberação de liquidez totalizou um montante de R$ 82 bilhões"), sem método. Próximo dos ≈ R$ 80 bi que o REBC 2009 atribui às medidas de outubro de 2008; o Relatório de Gestão 2008 dá ≈ R$ 90 bi até meados de novembro. Lido como a primeira rodada.
- Torós (apresentação "Selic 30 anos") também cita R$ 99,8 bi, consistente com o Relatório Anual. A 10.2.3 dá 116 e 82 e remete para cá; o coordenador pode querer acrescentar lá os R$ 99,8 bi.

### Fontes principais (todas por WebSearch; bcb.gov.br e newbagehot.yale.edu não abriram por WebFetch)

- BCB: EE 72/2020 (funções; à vista R$ 45,5 bi e alíquota efetiva 19,6% em dez/2019, ≈ 0,5% do PIB); EE 92/2020 (alíquota efetiva total 26,2% → 22,0% de 2016 a 2019); Res. BCB 145/2021, 188/2022, 189/2022 (21% à vista), 512/2025 (dedução de até 5% na poupança), 551/2026 (dedução de antecipações ao FGC, até R$ 30 bi em 2026); Circulares 2.440, 2.441, 2.474/1994; 3.405/2008; 3.513, 3.514, 3.515/2010; 3.916/2018; 3.951/2019; Voto 244/2018; Relatório Anual 2008 e 2010; REBC 2009 e 2010; RI jun/2011 (boxe de medidas macroprudenciais); apresentação de 07/02/2017 (spread 2011–2016: inadimplência 53,5%, lucro 23,8%, impostos diretos 15,8%, custo administrativo 5,1%, compulsórios e encargos fiscais 1,8%); REB 2017 seção 3.4 e boxe 6 (liberar 10% dos compulsórios: ICC 22,2% → 22,1%; liberar 10% do direcionado: −1,3 p.p. na taxa do crédito livre), números via resumo do IE/Unicamp.
- Imprensa para atos do BC: Agência Brasil (dez/2017 45→40 e 36→34; mar/2018 40→25 e poupança 24,5→20, R$ 25,7 bi; mar/2021 prorrogação dos 17%); Reuters/Correio Braziliense/Money Times (20/02/2020: 31→25, R$ 49 bi; LCR R$ 86 bi; total R$ 135 bi); gov.br (23/03/2020: 25→17, R$ 68 bi); Poder360 (volta a 20% em 22/11/2021, R$ 42 bi); Gazeta do Povo (R$ 61 bi em dez/2010); Money Times, Metrópoles, InvestNews (FGC, mar/2026); BPMoney e FAEP (exigibilidade rural à vista 30% → 31,5% em 2025/26); FGV IBRE, CNN, Prognum/Valor (plano de zerar o compulsório da poupança em ≈ 10 anos a partir de 2027).
- Literatura: Garcia (1994, PUC-Rio); Cavalcanti e Vonbun (2013, Ipea TD 1826); Mesquita e Torós (2010); Robitaille (2011, Fed IFDP 1021); Montoro e Moreno (2011, BIS QR); Brei e Moreno (2019, JIMF / BIS WP 741); Tovar, Garcia-Escribano e Vera Martin (2012, IMF WP 12/142); Cantú, Gondo e Martínez (2024, BIS WP 1182); Barbosa (2018, Blog do IBRE); McLeay, Radia e Thomas (2014).
- Internacional: Fed, comunicado de 15/03/2020 (zero a partir de 26/03/2020; antes 0%/3%/10%); BCE, comunicado de 27/07/2023 (remuneração 0% a partir de 20/09/2023) e Bundesbank (1% desde 18/01/2012, 2% desde 1999); China: recorde de 21,5% nos grandes bancos (Fox Business, 2012), 17% em abr/2018 (Bloomberg), 12,5% em jan/2020, média de 6,3% em jan/2026 (China Daily).

### Contas do painel

- Cunha $c = \alpha i/(1-\alpha)$: 3,99 p.p. (Selic 15%), 3,66 (13,75%), 0,53 (2%).
- Imposto implícito hipotético: R$ 45,5 bi (saldo à vista de dez/2019) × 15% = R$ 6,8 bi/ano = 0,09 p.p. da carteira de R$ 7,44 tri de set/2026 (SGS 20539). Spread de set/2026: 21,61 p.p. (SGS 20783).
- 2020: 49 + 68 = R$ 117 bi = 1,5% do PIB de 2020 (SGS 4382, R$ 7,61 tri). 1,8% de um spread de ≈ 17 p.p. ≈ 0,3 p.p.

### Lacunas (nada disso entrou como fato)

- Saldo atual dos recolhimentos por modalidade e total: as séries SGS 1848 (poupança em espécie, remunerado) e 1849 (à vista em espécie, não remunerado) existem, além da 1828 (depósitos compulsórios em espécie na base ampliada) e outras citadas no TD 296 do BCB, mas não estão em dados/brutos. Sugestão: acrescentar 1828, 1847, 1848, 1849 e as séries de recursos a prazo ao `tools/coletar.py` e trocar a nota da página por um gráfico do saldo em % do PIB (o pico de ≈ 7% do PIB em 2017 citado por Barbosa, 2018, e os "4,5% do PIB" atribuídos a um diretor do BC não foram confirmados e ficaram fora).
- Histórico longo das alíquotas (1994–2016): o BCB tem `historico-aliquotas-pt.pdf`, que não abriu. O gráfico começa em nov/2017 para não interpolar. Os meses de vigência de dez/2017 e nov–dez/2018 são aproximados (mês do anúncio ou da vigência, como diz a nota do JSON).
- Remuneração do compulsório da poupança: a página diz "remuneração da própria poupança" com base em resumo de texto da Res. BCB 188/2022 e fontes secundárias; uma fonte de imprensa dizia "Selic". Conferir no texto da resolução.
- O plano de zerar o compulsório da poupança em dez anos a partir de 2027 vem de imprensa; norma não localizada.
- Relatório de Estabilidade Financeira: não foi lido; nenhum número dele entrou. O REF de nov/2008 e o de 2020 devem ter a avaliação do uso do compulsório como colchão e o efeito no LCR.
- Decomposição do spread com linha de compulsório nos REBC de 2005 a 2012 (compulsório + subsídio cruzado + encargos fiscais): números variam entre fontes secundárias (um texto fala em 28,39% em média de 2004 a 2010 para o agregado com subsídios); não usados.
- Apresentação de fev/2017: o próprio BC revisou depois a decomposição de 2011–2016; a página avisa, mas não traz a versão revista.
- Razão do BCE para zerar a remuneração em 2023 (reduzir o juro pago sobre reservas preservando a transmissão) foi parafraseada de memória do comunicado; conferir a frase.
- Exigibilidade adicional: criação "nos anos 2000" e extinção em maio de 2017 (Yale YPFS, via busca); a data exata de criação (2001–2002) não foi conferida e ficou fora.

### Divergências

- Compulsório de 2008: ver decisão acima (116 × 99,8 × 82).
- Taxa sobre depósitos à vista em dez/2010: um resumo de busca dizia "à vista de 8% para 12%"; o Relatório Anual 2010 diz que os 8% → 12% são da exigibilidade adicional sobre recursos à vista e a prazo. A página segue o Relatório Anual.
- Spread: a 2.4 usa 21,2 p.p. (ago/2026); a 10.2.4 usa 21,6 p.p. (set/2026), ambos do SGS 20783.

## 10.2e

### Página entregue (02/11/2026)

- 10.2.5 Regra de Taylor e os modelos do BC, 1ª versão: cerca de 3.460 palavras de prosa antes do "Para ler", sem contar parênteses de fonte e fórmulas (3.630 contando-os; 5.480 pela contagem do lint, que inclui tabela, fórmulas e referências). Três gráficos: `dados/10.2.5-selic-regra-taylor.json` (linha mensal, jan/2003 a ago/2026: Selic meta × regra de Taylor com IPCA 12m, r* de 4,5% e 5%), `dados/10.2.5-selic-menos-regra.json` (barras anuais: Selic − regra, r* = 5%, versões IPCA e Focus) e `dados/10.2.5-neutro-implicito.json` (linha anual: r* que faria a regra igual à Selic). Exemplos de brinquedo: regra com π = 5, meta 3, hiato +1, r* = 5 → 11,5% (11% com r* 4,5; 14,5% com 8); princípio de Taylor (resposta 1,5 × 0,8); variantes (expectativas 10,75%; suavização ρ = 0,8 → 10,3% e 10,54%; balanced approach 12%); leitura de projeção condicional. Tabela por período, quadro A favor/Contra, duas caixas "o painel lê".
- Código reproduzível: `tools/analises/10.2.5_taylor.py` (biblioteca padrão + numpy; `--resumo` imprime as contas usadas no texto). Grava os três JSON.

### Método e números do painel (cálculo próprio, coleta de 02/11/2026)

- Selic: SGS 432 é a Selic **meta** (o cartão dizia "Selic efetiva (SGS 432)"); usada a meta vigente no último dia do mês. A over fica 0,10 abaixo (10.2.1), o que não muda nada relevante.
- Inflação: IPCA 12m (SGS 13522) ou mediana Focus 12 meses à frente (série suavizada, baseCalculo 0, último registro do mês). Meta: centro do CMN ponderado pelos meses da janela (2003 = 4,0% oficial, não a "ajustada" de 8,5%; 2004 = 5,5%; 3,0% desde 2024).
- Hiato: filtro HP (λ = 129.600) sobre 100·ln(IBC-Br dessazonalizado, SGS 24364), jan/2003–ago/2026, média móvel de 3 meses. Declarado como aproximação. Mínimo em jun/2020 (−11,1% na média móvel). Ago/2026: −1,2% contra +0,4% do BC (RPM set/2026); 2019: +1,5% contra ≈ −2% do BC (via Blog do IBRE).
- Resultados (r* = 5%, Selic − regra, média dos meses): IPCA/Focus = 2003–05 +2,8/+7,7; 2006–10 +2,3/+2,7; 2011–12 −2,0/−1,2; 2013–16 −2,5/−0,2; 2017–19 −0,8/−1,5; 2020–21 −6,9/−4,2; 2022–24 −0,4/+1,7; 2025–ago/2026 +3,8/+4,3. Média geral −0,25/+1,39. Meses com Selic acima da regra: 48%/63% (r* 5) e 54%/68% (r* 4,5). Correlação Selic × regra: 0,56/0,46.
- Anos: 2013 −4,7/−4,2; 2021 −10,5/−4,9; 2025 +3,3/+3,8; 2026 (jan–ago) +4,6/+5,0. Mai/2003: Selic 26,5, regra IPCA 29,1, regra Focus 15,0. Out/2012: regra ≈ 11,4 com Selic 7,25. Mar/2021: regra 12,3 (IPCA) e 9,3 (Focus) com Selic 2,75. Ago/2026: Selic 14,0, regra Focus 9,7 (≈ 10,5 com o hiato do BC).
- Neutro implícito médio (Focus/IPCA): 2003–05 12,7/7,8; 2006–10 7,7/7,3; 2011–19 entre 2,5 e 4,8; 2020–21 0,8/−1,9; 2022–24 6,7/4,6; 2025–26 9,3/8,8.
- MQO (Selic − πe) = a + b(πe − meta) + c·hiato: 2003–2010 a 8,83, b 1,65, c −0,14 (R² 0,31); 2011–2016 a 5,05, b 0,59, c −0,70 (0,41); 2017–2026 a 3,64, b 2,49, c 0,10 (0,44). Amostra inteira instável (b cai de 1,52 para 1,00 tirando 2003); por isso o texto só usa os subperíodos e chama a conta de ilustrativa.

### Fontes principais (todas por WebSearch; bcb.gov.br, stanford.edu e crei.cat não abriram por WebFetch)

- Taylor (1993): fórmula e variáveis por fontes secundárias (CRS, Yellen 19/01/2017); "hypothetical but representative" via Orphanides (2003, FEDS 2003-36). Clarida, Galí e Gertler (2000): 0,83 (1960–1979) e 2,15 (Volcker–Greenspan) via reprodução em busca. Taylor (1999) e o peso 1,0 da balanced approach via Nakamura e Riblier (Fed de Kansas City). Fed MPR: boxe de regras desde jul/2017; ed. jul/2026 (Box 4) com Taylor (1993), ajustada, balanced approach e primeira diferença.
- Minella, Freitas, Goldfajn e Muinhos (2003): só o resumo (metas coordenaram expectativas; BC "reacted strongly" às expectativas). Holland e Gomes (2003, EconomiA 4(2)); Barbosa, Camêlo e João (2016, RBE 70(4): neutro = juro externo + risco país + risco cambial; R² 98%; princípio de Taylor vale); Barcellos Neto e Portugal (2009; ≈7% e ≈9,5% para 2000–2005 segundo Santos, 2011, Anpec); Cortes e Paiva (2017, JIMF 74); Bonomo et al. (2024, JME 145).
- BCB: boxes do modelo agregado (jun/2017; set/2020 e dez/2020 com estimação bayesiana; dez/2021 revisão; jun/2024 atualização); cinco equações (Phillips, IS, regra, paridade, expectativas) pelo resumo do boxe de dez/2020. Regra do modelo de dez/2021 sem hiato e suavização 0,91 (amostra 2003T4–2019T4) e resposta de 1,3 ao desvio: via Blog do IBRE (portal FGV), não pelo boxe. SAMBA: WP 239 (abr/2011), BRE 35(2) 2015, Estudo Especial 39/2019, WP 578 / LAJCB 5(2) 2024 (Fasolo, Araújo, Jorge, Kornelius, Marinho). Bogdanski, Tombini e Werlang (2000, WP 1).
- Projeções: ata 279 (jun/2026) com o recorte "a trajetória para a taxa de juros é extraída da pesquisa Focus e a taxa de câmbio parte de R$5,10/US$, evoluindo segundo a paridade do poder de compra (PPC)"; comunicado de 16/09/2026 (câmbio R$ 5,15; 5,2% 2026; 3,9% 2027; 3,2% no 1º tri de 2028) via okai.com.br e Correio Braziliense; RI dez/2011 com câmbio R$ 1,80 e Selic 11% constantes via Estado de Minas.
- Críticos: Summa (2011, Pesquisa & Debate 22(2), p. 157–183; só introdução lida, conclusão não citada como fato); Arestis e Sawyer (2008, CJE 32(5)); Orphanides (2001, AER 91(4)); Taylor (2007, Jackson Hole) e (2009, Getting Off Track); Blog do IBRE (nove regras de Borges; FMI com 27 regras, fim de 2020).

### Lacunas (nada disso entrou como fato)

- Coeficientes numéricos de Minella et al. (2003) e de Holland (2005, "postura agressiva", citado em Anpec 2006): não confirmados; Holland (2005) ficou fora do texto.
- Coeficientes do boxe de dez/2021 e do de jun/2024 não lidos na fonte; o "1,3" do BC vem de um post do Blog do IBRE que pode se referir a outro parâmetro (um segundo resumo de busca achou o rótulo ambíguo). Conferir no PDF ri202112b7p.
- Data em que o BC trocou a projeção de referência (Selic e câmbio constantes → Selic Focus e câmbio PPC): um resumo de busca (Mais Retorno) fala em 2021; atas de 2022 já usam PPC. O texto não dá a data.
- Hiato do BC como série: não coletado. Sugestão: extrair do RPM (gráfico do hiato, planilha de dados dos gráficos) e trocar o filtro HP; e calcular a regra em tempo real com as estimativas de cada RPM (crítica de Orphanides).
- Autor e data dos posts do Blog do IBRE "Avaliando a postura..." e "FMI aponta..." não confirmados (só o de nove regras foi atribuído a Bráulio Borges pela página de autor). O Artigo IV/Selected Issues do FMI de 2020 com as 27 regras não foi localizado.
- Gráfico do Fed com as prescrições das regras em 2026: não usado.

### Divergências

- 2.3 e 6.2 usam a regra com hiato do BC (+0,4%) e chegam a ≈ 10,5–10,6% em set–out/2026; a 10.2.5 com o hiato HP dá 9,7% em ago/2026 e diz que, com o hiato do BC, chega a ≈ 10,5%. Consistente, com método declarado.
- Neutro do Copom: a 10.2.5 diz "3% em 2021 e 5% desde dez/2024" e "4,5% até mai/2024" (como 6.3.2 e 2.3); a data da passagem de 3% para 4,5% não foi confirmada e não é citada.
- Nenhuma outra divergência com 10, 10.2, 10.2.1, 2.3, 6.2 e 6.3.2.

## 10.2f

### Página entregue (02/11/2026)

- 10.2.6 Comunicação convencional, 1ª versão: cerca de 3.040 palavras de prosa sem parênteses de fonte, fórmulas, tabela e citações em bloco (≈ 3.800 com os parênteses; 5.240 pela contagem do lint, que inclui tabela e referências). Exemplo de brinquedo (três bancos centrais mantêm 10%; taxa de dois anos $i_2 \approx (i_1 + E[i_1'])/2 + \phi$: 9,3% antes, 10,3% com fala dura, 8,8% com fala branda, 10,05% com fala ambígua e prêmio de 0,8), tabela dos canais do Copom, fórmula do peso do sinal público em Morris e Shin, $\kappa = \alpha/(\alpha + \beta(1-r))$, com exemplo resolvido ($\alpha = 1$, $\beta = 3$: 0,25 / 0,40 / 0,625 para $r$ = 0 / 0,5 / 0,8), revisão dos estudos brasileiros, três episódios (2016–2017, 2020–2021, 2024–2026), seção sobre Selic longe da regra e fala × ação, quadro A favor/Contra e duas caixas "o painel lê".
- Dois gráficos novos, do bruto `dados/brutos/focus-anuais_selic.json` (Focus, API Olinda, baseCalculo 0, coleta de 02/11/2026): `dados/10.2.6-focus-selic-2021.json` (mediana da Selic de fim de 2021 e de 2022, diária, set–nov/2021) e `dados/10.2.6-focus-selic-2024.json` (mediana da Selic de fim de 2025, diária, nov/2024–fev/2025, com linha de referência em 14,25%). Script em scratchpad, não versionado; a extração é um filtro direto do bruto por DataReferencia e Data.

### Números do painel (BCB, Focus, API Olinda, mediana, base de 30 dias)

- Fim de 2017: 10,25% em 11/01/2017 (dia da 204ª reunião), 10,0% em 12/01, 9,75% em 13/01, 9,50% em 20/01.
- Fim de 2018: 6,25% até 21/05/2018; 6,50% a partir de 22/05 (214ª reunião em 16/05).
- Fim de 2021: 8,25% de 17/09 a 21/10/2021 (= 6,25 + 1 + 1, a orientação de setembro); 8,75% em 22/10; 9,25% em 29/10. Desvio-padrão 0,09–0,10 em meados de outubro e 0,41 em 22/10.
- Fim de 2022: 9,0% em 20/10/2021; 9,5% em 22/10; 10,0% em 27/10; 10,5% em 01/11; 11,25% em 30/11. Desvio-padrão 0,61 (20/10) → 1,04 (22/10).
- Fim de 2025: 11,50% em 01/11/2024; 13,50% em 11/12/2024; 14,0% em 13/12; 14,75% em 23/12; 15,0% em 02/01/2025. Desvio-padrão 0,95 (11/12/2024) → 0,74 (06/01/2025) → 0,64 (07/02/2025).
- Datas de vigência da Selic (SGS 432) usadas para as decisões de 2016–2026; números das reuniões contados a partir da 279ª (17/06/2026, ata no site do BCB) e da 281ª (16/09/2026, página do BCB em inglês): 202ª 19/10/2016; 204ª 11/01/2017; 214ª 16/05/2018; 234ª 28/10/2020; 236ª 20/01/2021; 239ª 16/06/2021; 241ª 22/09/2021; 242ª 27/10/2021; 262ª 08/05/2024; 264ª 31/07/2024; 267ª 11/12/2024; 271ª 18/06/2025; 276ª 28/01/2026; 277ª 18/03/2026.

### Fontes principais (todas por WebSearch; bcb.gov.br, nber.org, scielo.br, arxiv.org, econ.puc-rio.br, economics.mit.edu e larseosvensson.se não abriram por WebFetch)

- Teoria: Blinder et al. (2008, JEL 46(4)), recorte "an important and powerful part of the central bank's toolkit" confirmado em reprodução do resumo; Woodford (2005, Jackson Hole), argumento contra Morris e Shin por resumo do Herald Business (13/10/2026); Morris e Shin (2002); Svensson (2006) e Morris, Shin e Tong (2006) pelos resumos (Svensson: o resultado só vale para precisão pública "implausivelmente baixa" em relação à privada; resposta: sinais privados correlacionados); Amato, Morris e Shin (2002, OxREP 18(4)); Gürkaynak, Sack e Swanson (2005), citado de memória só no qualitativo (fatores de alvo e de trajetória; o segundo pesa mais nos longos).
- Brasil: Costa Filho e Rocha (2010, Economia Aplicada 14(3); TD-E 17/2008 FEA-RP/USP); Janot e Mota (2012, BCB TD 265); Carvalho, Cordeiro e Vargas (2013, RBE 67(4)); Chague, De-Losso, Giovannetti e Manoel (2015, RBE 69(2)); Cabral e Guimarães (2015, RBE 69(3)); Montes e Nicolay (2016, Análise Econômica 34(66)); Ramos e Portugal (2021, PPP 47, Ipea); Montes e Nicolay (2017, Applied Economics 49(32)) só na bibliografia.
- Normas e calendário: Circular 2.698/1996; Res. BCB 61/2021 (ata em até 4 dias úteis; conteúdo da ata, recorte via Abrapp; período de silêncio); nota do BCB de 21/11/2016 sobre o período de silêncio (Jornal do Comércio); mudanças de jul/2016 (Agência Brasil, Monitor Mercantil); atas desde a 21ª reunião, jan/1998 (Portal de Dados Abertos do BCB); RPM v.1 n.1 mar/2025; cartas abertas 2001–2003, 2015, 2017, 2021, 2022, 2024 e jun/2025 (Agência Brasil, 10/07/2025; Poder360).
- Recortes de comunicados e atas reproduzidos pela imprensa: 236ª (Investing.com), 267ª (IstoÉ Dinheiro), 271ª ("não hesitará em prosseguir no ciclo de ajuste caso julgue apropriado", Jornal de Brasília/CGN), ata de set/2025 ("por período bastante prolongado", Agência Brasil), 234ª ("o espaço remanescente...", texto reproduzido por busca, sem página de imprensa identificada). Galípolo: DGABC 14/10/2024 ("dependente de dados") e Reuters/InfoMoney 2025 (recorte em bloco).
- 2026: Woodford e Hall, Nobel (O Povo, 13/10/2026); Shin no Banco da Coreia (BIS, 20/04/2026); Warsh e a orientação futura (BBVA Research, jun/2026; Kitco, 17/06/2026).

### Lacunas (nada disso entrou como fato)

- Data exata da entrevista de Galípolo com o recorte "Se por acaso você entendeu..." (Reuters/InfoMoney; fontes divergem entre "quarta-feira" e "terça-feira (12)"); o texto diz só 2025.
- Texto literal da orientação de março de 2024 (corte de 0,5 "na próxima reunião"): a página usa a leitura da Bloomberg Línea de que os votos vencidos seguiam a orientação.
- Comunicado de março de 2018 (sinal de "flexibilização moderada adicional"): não confirmado; a página usa só a surpresa de maio (Metrópoles) e o Focus.
- Sinal de outubro de 2021 para dezembro: imprensa diverge entre 1,25 e 1,5 ponto; a página não cita.
- Desde quando o comunicado traz os nomes de quem votou e quando o Copom passou a oito reuniões (InfoMoney: 2006; Agência Brasil/Monitor Mercantil: mensais até 2015): não citados.
- Costa Filho e Rocha na RBE 63(4), 2009: volume vem de lista de referências do RePEc; título e ano a conferir no site da RBE.
- Reação dos DI (pontos-base) aos comunicados citados: não coletada; a página usa o Focus. Sugestão: acrescentar ao coletor a taxa referencial DI × pré da B3 (ou ETTJ da ANBIMA) e fazer um estudo de evento com janela de um dia em torno de cada comunicado, nos moldes de Carvalho, Cordeiro e Vargas.
- Gürkaynak, Sack e Swanson (2005): proporção da variância explicada pelo fator de trajetória não conferida; o texto só diz que pesou mais nos juros longos.

### Divergências

- Nenhuma com 10.2, 10.2.5, 4.2, 6.3 e 6.4.1. Orientação de 2020 e sua retirada em 20/01/2021 coincidem com 4.2. A distância Selic − regra (3 a 5 pontos em 2025–2026; até 10 pontos abaixo em 2021 com IPCA passado) é a da 10.2.5.
- O 10.2 diz que a comunicação "mexe nos juros futuros antes de qualquer operação"; a 10.2.6 dá a evidência e as ressalvas (perda de efeito sob Tombini).

## 10.3a

### Páginas entregues (02/11/2026)

- 10.3 Instrumentos não convencionais (ponte), 1ª versão: cerca de 1.220 palavras de prosa sem parênteses de fonte e sem "Para ler" (1.620 pela contagem do lint). Exemplo de brinquedo (piso e cano entupido), limite inferior efetivo (com o piso emergente e a Selic mínima de 2% de 06/08/2020 a 17/03/2021, SGS 432), pane de mercado (Borio e Disyatat, 2009; princípio da separação), Bernanke (2020), um parágrafo por neta 10.3.1 a 10.3.8, a pergunta para o Brasil com link para 10.5 e uma caixa "o painel lê".
- 10.3.1 Forward guidance, 1ª versão: cerca de 3.530 palavras de prosa sem parênteses de fonte, tabela, fórmulas e citações em bloco (≈ 3.730 com os parênteses; 5.400 pela contagem do lint, que inclui tabela e referências). Exemplo de brinquedo (juro zero por dois anos: taxa de dois anos de 1,2% para 0,2%; dez anos de 3,4% para 3,2% e 3,0% com promessa pós-recuperação; hipoteca de 5,4% para 5,2% e 5,0%; terceiro desfecho délfico), fórmula da hipótese das expectativas com exemplo, recortes de Campbell et al. (2012), FOMC 09/08/2011 e 12/12/2012, BCE 04/07/2013, Del Negro et al., Copom (ata 233, em inglês) e RBA (2022); tabela da orientação do Fed 2008–2015; equação do "forward guidance puzzle" com exemplo resolvido (0,25 sem desconto; 0,25 × 0,9^20 ≈ 0,03 com desconto); seção sobre o Copom 2020–2021 com dois gráficos; armadilhas (Fed 2021, RBA 2021, Copom out/2021); caixa "o painel lê" sobre convenção declarada × âncora fiscal; quadro A favor/Contra.
- Dois gráficos novos, do bruto (consulta 02/11/2026): `dados/10.3.1-focus-selic-orientacao.json` (Selic meta, SGS 432, e mediana Focus da Selic de fim de 2021 e de 2022; um ponto por semana, jun/2020–jun/2021) e `dados/10.3.1-focus-ipca-orientacao.json` (mediana Focus do IPCA de 2021 e de 2022 com as metas de 3,75% e 3,50% como referência). Script em scratchpad, não versionado: filtro direto de `focus-anuais_selic.json`, `focus-anuais_ipca.json` (baseCalculo 0, último dia de cada semana ISO) e `sgs-432.json`.

### Números do painel (BCB, Focus, API Olinda, mediana com base de 30 dias)

- Selic fim de 2022: 5,0% em 05/08/2020; 4,5% de 17/08/2020 a 08/01/2021; 4,75% em 13/01/2021; 5,0% em 22/01/2021; 6,0% em 19/03/2021.
- Selic fim de 2021: 3,0% em 05/08/2020; 2,5% em 11/09/2020; 2,75% em 23/10; 3,0% em 20/11; 3,5% em 18/01/2021; 4,0% em 17/02; 5,0% em 19/03; 6,5% em 17/06/2021. Desvio-padrão de 0,77 (ago/2020) para 0,69 (jan/2021).
- IPCA 2021: 3,0% de jul a out/2020; 3,45% em 18/01/2021; 3,62% em 12/02; 3,82% em 19/02 (passa a meta de 3,75%); 4,60% em 12/03; 6,0% em 29/06/2021. IPCA 2022: 3,50% (a meta) de jun/2020 a mar/2021; 3,78% no fim de jun/2021.
- Selic meta (SGS 432): 2,25% → 2,00% em 06/08/2020; 2,75% em 18/03/2021 (decisão de 17/03).

### Fontes principais (todas por WebSearch; federalreserve.gov e chicagofed.org não abriram por WebFetch)

- Campbell, Evans, Fisher e Justiniano (2012, BPEA, p. 1–80): recorte da distinção odisseica × délfica pelo resumo reproduzido em busca. Campbell, Fisher, Justiniano e Melosi (2017, NBER Macro Annual 31): só a conclusão qualitativa (efeito em boa parte délfico).
- FOMC: 09/08/2011 (texto via MNI/investingLive; três votos contrários; Kocherlakota no Fed de Minneapolis; Treasury de dois anos a 0,19% em 10/08/2011, CNN Money); 12/12/2012 (limiares, via Mortgage News Daily); datas de jan/2012, set/2012, dez/2013, mar/2014 e dez/2015 pela linha do tempo do Fed citada em busca e pelo conhecimento do calendário (não reabertas no site do Fed).
- Swanson (2021, JME 118: 32–53), pelo resumo do autor; Del Negro, Giannoni e Patterson (NY Fed SR 574; JPE Macro 1(1): 43–79, 2023), recorte do resumo da versão de trabalho.
- BCE 04/07/2013 (OFCE, VoxEU); Banco da Inglaterra 07/08/2013 (comunicado do BoE, LSE, OBR).
- BCB: ata da 233ª (16/09/2020, em inglês) com a cláusula fiscal e a intenção assimétrica; ata da 235ª (09/12/2020) com as três condições; comunicado da 236ª (20/01/2021) via Poder360, Forbes e Investing.com; Estudo Especial 101/2021 (boxe do RI de dez/2020: taxa de dois anos de 3,42% para 3,30%, cerca de 60% atribuído à orientação, equivalente a surpresa de 11 pb; via busca no PDF e Forbes/Reuters); Estudo Especial 112/2021 (boxe do RI de set/2021: decisões coerentes com a orientação).
- Debate brasileiro: Campos Neto em 25/03/2021 (Mais Retorno: BC não estava atrás da curva) e em 27/09/2023 na CFT da Câmara (CNN Brasil: a queda a 2% foi um erro). Tesouro, RAD 2020: DPF vencendo em 12 meses de 18,7% (2019) para 27,6% (2020), maior fim de ano desde 2007.
- Armadilha: English e Sack (2024, BPEA 55(2): 3–26) e Romer e Romer (2024, BPEA 55(2): 59–87, pelos slides); RBA, *Review of the Yield Target* (jun/2022), recorte via Reuters/Investing.com.

### Lacunas (nada disso entrou como fato)

- Texto literal do comunicado da 232ª reunião (05/08/2020): a página parafraseia as condições pela ata da 235ª e pela imprensa. Conferir no PDF do BCB e, se possível, trocar a paráfrase por recorte.
- A frase sobre reavaliação "mesmo que o teto de gastos nominal continue de pé" foi atribuída à ata de dezembro de 2020 (09/12/2020, versão em inglês) pelo resultado de busca, que não ligou o trecho a uma ata com certeza; pode ser da ata de outubro (234ª). Conferir.
- Estudo Especial 101: a busca trouxe também um "−0,27 p.p." para a taxa de dois anos que não foi confirmado; a página usa 3,42% → 3,30% e "cerca de 60%". Conferir no PDF a base dos 60% (queda total do dia ou só da janela da reunião).
- Reação dos DI longos em ago–dez/2020 em pontos-base: não coletada. A página remete a 6.1.1 (curva inclinada) e usa o dado do RAD. Sugestão: estudo de evento com a ETTJ da ANBIMA ou a taxa referencial DI × pré da B3.
- Woodford (2012, Jackson Hole): argumento contra a data e a favor de condição citado de memória, sem recorte; páginas do volume não conferidas.
- Data em que o desemprego americano chegou a 6,5% e a passagem do BoE para a "fase 2" em fev/2014: só qualitativo (a página não dá a data do mês em que o desemprego cruzou o limiar).
- Andrade, Gaballo, Mengus e Mojon (2019) e Nakamura e Steinsson (2018): citados pelo resultado conhecido, sem recorte.

### Divergências

- Nenhuma de número com 10, 10.2.6, 4.2 e 6.1.1. A data da retirada (20/01/2021, 236ª reunião) coincide com 4.2 e 10.2.6. O glossário (9.3, verbete "Forward guidance") diz "retirada no início de 2021": pode ganhar a data exata e o link para 10.3.1.
- A página macro 10 tem "[a conferir: comunicado de agosto de 2020]" sobre o espaço pequeno para cortes; 10.2.6 já cita o trecho do comunicado de 28/10/2020, e 10.3.1 traz a assimetria e os limites prudenciais pela ata de 16/09/2020. A marca na página 10 pode ser resolvida com link para 10.2.6 e 10.3.1.

## 10.3b

### Página entregue (02/11/2026)

- 10.3.2 Quantitative easing, 1ª versão: cerca de 3.570 palavras de prosa sem parênteses de fonte, títulos, tabelas, fórmulas e citações em bloco (≈ 3.820 com os parênteses; 5.490 pela contagem do lint, que inclui tabelas e referências). Fica no teto do cartão (3.500), na mesma medida da 10.3.1.
- Conteúdo: QE × mercado aberto convencional (tabela, link para 10.2.2 e para o lançamento 2 do balanço de brinquedo da página 10); exemplo de brinquedo (BC compra 100 de 1.000 títulos de dez anos com cupom 3; lançamentos no BC, no banco e no fundo; preço 100 → 102,6 → 104,4, taxa 3% → 2,7% → 2,5%; 30 p.b. de prêmio e 20 de sinal); fórmula linear de hábitat preferido $\Delta\phi \approx -\theta\,Q/PIB$ com exemplo; programas do Fed (QE1, QE2, *Operation Twist*, QE3, 2020–2022), do BoE (APF) e do BCE (APP/PSPP, PEPP); tabela do ativo do Fed em % do PIB; canais (carteira, sinalização, liquidez, sete canais de KVJ, multiplicador fora); tabela de estimativas normalizadas por 1% do PIB; quadro A favor/Contra; inflação 2010s × 2021–2022; custo para Fed, BCE e BoE (indenização do HM Treasury); QT; transposição ao Brasil com link para 10.5, 7.3, 6.1, 7.8 e 10.3.7; caixa "o painel lê".
- Sem gráfico. FRED, DBnomics e os sites dos bancos centrais não abriram (curl 403; WebFetch sem resolução de brookings.edu). Os pontos do ativo do Fed em % do PIB vieram de fontes diferentes (Waller 2025: 6% em ago/2007; Judson e Weiss 2026: pouco mais de 25% em 2014; Wright 2022 e CaixaBank: 34% a 37% no pico; FEDS Notes de jan/2026: 21% em dez/2025) e ficaram numa tabela no texto. Sugestão: acrescentar ao `tools/coletar.py` as séries WALCL e GDP do FRED e o total de ativos do Eurosistema (BCE, ILM) para um gráfico `dados/10.3.2-balancos-pib.json`.

### Números do painel e fontes principais (todas por WebSearch, consulta em 02/11/2026)

- Gagnon, Raskin, Remache e Sack (2011, IJCB 7(1)): −91 p.b. no Treasury de 10 anos em oito anúncios (nov/2008–nov/2009, via FEDS 2014-07); regressões de 38 a 82 p.b.; faixa resumida de 30 a 100 p.b. para US$ 1,725 tri.
- Krishnamurthy e Vissing-Jorgensen (2011, BPEA): recorte do resumo confirmado em NBER/SSRN/Brookings; QE1 pouco mais de 100 p.b. (107 deduzido de slide dos autores: spread agência-Tesouro de 200 − 107 = 93 p.b.); QE2 entre 16 e 18 p.b.
- Joyce, Lasaosa, Stevens e Tong (BoE WP 393, 2010; IJCB 7(3), 2011): recorte "about 100 basis points" do resumo.
- Eser et al. (2019, ECB WP 2293): −95 p.b. no prêmio de 10 anos, meia-vida de cinco anos.
- Bernanke (2020): recorte do resumo ("roughly 3 percentage points of policy space"); QE1 −34, MEP −28, QE3 −31 p.b. (slides da conferência); regra ELR de US$ 500 bi → −17/−20/−7 p.b. em 5/10/30 anos.
- Gagnon (2016, PIIE PB16-4): mediana de cerca de 50 p.b. por 10% do PIB (via Kansas City Fed e FEDS 2020-083).
- Engen, Laubach e Reifschneider (2015, FEDS 2015-005): desemprego −1,25 ponto (início de 2015) e inflação +0,5 ponto (início de 2016).
- Greenlaw, Hamilton, Harris e West (2018, USMPF; NBER WP 24687, título "A Skeptical View of the Impact of the Fed's Balance Sheet"): juros sobem nos dias de notícia do Fed posteriores às grandes surpresas.
- Normalização por 1% do PIB: cálculo do painel com PIB nominal dos EUA (BEA, de memória: US$ 14,5 tri em 2009, 15,0 em 2010, 21,5 em 2019). Faixa de 2,5 a 9 p.b., mediana perto de 5.
- Fed: QE1 (25/11/2008 e 18/03/2009, US$ 1,75 tri anunciado; Boston Fed, BIS); QE2 US$ 600 bi; QE3 (13/09/2012, US$ 40 bi MBS + US$ 45 bi Treasuries desde dez/2012, fim em out/2014; linha do tempo do Fed); 2020–2022 (US$ 80 + 40 bi/mês desde jun/2020, fim em mar/2022; CRS IN11792); pico de US$ 8,965 tri em 13/04/2022; QT de jun/2022 a 01/12/2025 (tetos 30/17,5 → 60/35 → 25 → 5; fontes secundárias concordantes); compras de gestão de reservas desde 12/12/2025 (NY Fed, 10/12/2025).
- Custos: ativo diferido do Fed US$ 243 bi no fim do 3º tri de 2025 (CRS R48390), pico acima de US$ 245 bi em jan/2026 e volta ao lucro em 2026 (Bipartisan Policy Center), US$ 236 bi em jul/2026 (já em 10.2.2, Fed MPR); repasses de US$ 47,4 bi (2009) e cerca de US$ 109 bi (2021). BCE: −€ 1,3 bi (2023, após € 6,6 bi de provisões), −€ 7,9 bi (2024), −€ 1,25 bi (2025). BoE: £ 123,8 bi do APF ao Tesouro de jan/2013 a set/2022 (BoE APF QR 2025 Q2; o OBR dá £ 123,9 bi); £ 110,72 bi do Tesouro ao APF desde out/2022 (resposta HL3519, set/2026); perda vitalícia de £ 126 bi (boxe do OBR posterior a jul/2023).
- BoE: APF criado em 29/01/2009; £ 200 bi em fev/2010; £ 375 bi até 2012 (House of Lords); +£ 60 bi em 2016; £ 895 bi em nov/2020; £ 19,3 bi nas operações LDI (28/09–14/10/2022); estoque a £ 488 bi até set/2026; efeito do QT de 20 a 30 p.b. no gilt de 10 anos (Ramsden, set/2026).
- BCE: APP anunciado em 22/01/2015 (€ 60 bi/mês desde 09/03/2015), cerca de € 2,6 tri até dez/2018 (Benigno et al., 2023), retomada em nov/2019; PEPP de € 750 bi a € 1,85 tri; Eurosistema perto de 65% do PIB em meados de 2022 (CaixaBank Research); APP € 2,32 tri e PEPP € 1,42 tri no fim de 2025 (contas anuais do BCE).
- Inflação de pico: EUA 9,1% (BLS, jun/2022), zona do euro 10,6% (Eurostat, out/2022), Reino Unido 11,1% (ONS, out/2022); os dois últimos de memória, sem reabrir a fonte.

### Lacunas (nada disso entrou como fato)

- Estimativa de quase 175 p.b. de compressão do prêmio de 10 anos por APP + PEPP no relatório do BCE de 2025 (Occasional Paper 372?): apareceu num resumo de busca e não se confirmou numa segunda busca; ficou de fora.
- Total comprado pelo Fed em 2020–2022 (US$ 4,6 tri?) e no QE3 (US$ 1,6 tri?): não confirmados; o texto dá só os ritmos mensais.
- Data e valor exatos do boxe do OBR com £ 126 bi; perda do Fed em cada ano (2023 cerca de US$ 114 bi, 2024 cerca de US$ 75–80 bi, só em blog): não usados.
- Ponto de partida de £ 75 bi do BoE em mar/2009 usado só como exemplo de anúncio (fonte secundária: politics.co.uk).
- Decomposição de Bauer e Rudebusch (2014) entre sinal e prêmio: só qualitativa.
- PIB nominal dos EUA (BEA) usado na normalização foi tomado de memória; conferir com a série GDP do FRED quando o coletor a trouxer.

### Divergências

- Ativo diferido do Fed: 10.2.2 usa US$ 236 bi em jul/2026 (Fed MPR); 10.3.2 acrescenta US$ 243 bi (CRS, 3º tri de 2025) e o pico acima de US$ 245 bi em jan/2026 (BPC). Coerentes.
- Prejuízos do BCE iguais aos de 10.2.2 (€ 7,9 bi em 2024; € 1,3 bi em 2025, aqui com a casa decimal € 1,25 bi).
- Balanço do Fed: as páginas 1.1, 10, 10.3, 7.8 e o glossário usam "US$ 0,9 tri (2008) → 4,5 tri (2014–2015) → 8,97 tri (2022)"; 10.3.2 usa US$ 870 bi em ago/2007 (Waller, 2025) e as razões sobre o PIB. Não conflitam (datas diferentes).
- Transferências APF → Tesouro: £ 123,8 bi (BoE) contra £ 123,9 bi (OBR); a página usa o número do BoE.

## 10.3c

### Página entregue (02/11/2026)

- 10.3.3 Japão: QQE e controle da curva de juros, 1ª versão: cerca de 3.570 palavras de prosa sem parênteses de fonte, tabelas, fórmulas e citações em bloco (≈ 3.910 com os parênteses; 5.000 pela contagem do lint, que inclui tabelas e referências). Fica no teto do cartão, na mesma medida de 10.3.1 e 10.3.2.
- Conteúdo: exemplo de brinquedo (banco central que compra qualquer quantidade de título de dez anos sem cupom a 0%; $P = 100/(1+y)^{10}$: 100 / 95,1 / 90,5 / 86,2 / 82,0 / 74,4 para 0 / 0,5 / 1 / 1,5 / 2 / 3%; dois desfechos, crível e não crível; regra da duração $\Delta P/P \approx -D\,\Delta y$); deflação 1995–2012, juro zero de 1999–2000, QE de 2001–2006; Krugman (1998), Ito e Mishkin (2006), Shirakawa (2021) e o quadro do BIS sobre crescimento por pessoa em idade ativa; Abenomics e QQE de 04/04/2013, ampliação de 31/10/2014, imposto sobre consumo; juro negativo de 29/01/2016 (link para 10.3.4); YCC de 21/09/2016 com tabela das bandas até 19/03/2024; tabela das decisões de 19/03/2024 a 30/10/2026; resultados (inflação, estimativas do próprio BoJ, revisão de dez/2024, *shunto*, salário real, iene, fatia do BoJ na dívida, perda não realizada); quadro A favor/Contra sobre a eficácia; seção sobre a norma de inflação zero (Watanabe e Watanabe 2018, Ueda 2023 e 2024, Watanabe 2026); comparação Japão × Brasil (poupança, credor, memória de inflação, contrato; o que a comparação permite e o que não permite; FTPL e Sims 2016); quadro A favor/Contra sobre o "espelho" das convenções; caixa "o painel lê".
- Dois gráficos novos: `dados/10.3.3-taxa-e-inflacao-japao.json` (taxa de política do BoJ e CPI cheio em 12 meses, mensal, jan/1995–set/2026, do bruto `dados/brutos/bis-politica_monetaria.csv` e `bis-cpi.csv`, REF_AREA = JP, consulta 02/11/2026; lacunas onde o BIS não registra taxa: fev/1999–jul/2000, mar/2001–fev/2006, abr/2013–ago/2016; o −0,1% de fev–ago/2016 não aparece no BIS) e `dados/10.3.3-brinquedo-preco-titulo.json` (preço do título de brinquedo). Script em scratchpad, não versionado.

### Números do painel

- BIS (consulta 02/11/2026): CPI negativo em 131 de 216 meses de 1995–2012; de abr/2013 a mar/2022, CPI ≥ 2% em 12 de 108 meses, todos entre abr/2014 e mar/2015 (imposto); CPI ≥ 2% em todos os meses de abr/2022 a dez/2025, pico de 4,35% em jan/2023; 1,3% a 1,9% de fev a ago/2026; 2,10% em set/2026; −0,94% em mar/2013, 1,55% em dez/2013, 3,67% em mai/2014, 0,69% em abr/2015; 20,9% em dez/1974. Taxa de política: 6% (1991) → 0,5% (set/1995); 1,25% desde 24/09/2026.
- Datas e taxas da saída pela nota de compilação do BIS (que cita os PDFs do BoJ k240319a, mpr240731c, mpr250124a, k251219a, k260616a, k260918a): 0–0,1% (21/03/2024), 0,25% (01/08/2024), 0,5% (27/01/2025), 0,75% (22/12/2025), 1,0% (17/06/2026), 1,25% (24/09/2026). Votos: 7–2 em mar/2024 (GAM, Nomura); 7–1 em jun/2026 com Ueda ausente por tratamento médico (CGTN, FXStreet); 7–2 em set/2026 (UPI, TradingView/MNI, dissidentes Asada e Sato); manutenção 8–1 em 30/10/2026 (Dukascopy; dissidente Takata pediu 1,5% segundo fattail.ai, não usado no texto).
- QQE: base de 138 tri (fim de 2012) → 200 tri (2013) → 270 tri (2014), ritmo de 60–70 tri/ano (BoJ, via busca); 80 tri/ano em 31/10/2014, voto 5–4. Juro negativo 29/01/2016, voto 5–4, vigência 16/02/2016, três faixas. Compras recordes de 23,69 tri em jan/2023 (Reuters). Ativo do BoJ 164 tri (mar/2013) → 714,56 tri (ano fiscal 2020).
- Fatia do BoJ: 53,34% dos JGB sem letras em mar/2023 (Nippon.com, Flow of Funds); 46,3% / 41,8% / 11,9% (BoJ / domésticos / estrangeiros, com letras, fim de 2024, MoF *JGB Newsletter* abr/2025); abaixo de 50% em 2026 (Nikkei Asia, mar/2026).
- Perda não realizada do BoJ: 45,441 tri (ano fiscal até mar/2026) contra 28,625 tri (Dow Jones via MarketScreener).
- *Shunto* (Rengo, final): 5,10% (2024), 5,25% (2025), 5,01% (2026). Salário real 2025: −1,3%, quarto ano (Jiji/Adnkronos, 09/02/2026).
- Efeito do QQE estimado pelo BoJ (Q-JEM): PIB +0,9% a 1,3%; núcleo +0,6 a 0,7 p.p. (WP 21-E-4 e *Economic Analysis and Policy* 78, 2023).
- Posição externa líquida do Japão: ≈ 561,75 tri de ienes no fim de 2025, terceira do mundo (MoF via Bloomberg/Yahoo, 25/05/2026).
- Título de dez anos: 3,12% intradia no início de out/2026, maior desde ago/1996 (Trading Economics; Admiral Markets cita fechamento oficial de 3,111% em 07/10/2026); acima de 3% pela primeira vez desde 1996 em 01/09/2026 (Jiji via Adnkronos).

### Fontes principais (todas por WebSearch; boj.or.jp, cigs.canon, gc.cuny.edu e asia.nikkei.com não abriram por WebFetch)

BoJ (comunicados de 04/04/2013, 31/10/2014, 29/01/2016, 21/09/2016, 19/03/2024 e seguintes, pela busca e pela nota do BIS; página "Price Stability Target of 2 Percent"; revisão ampla de 19/12/2024; WP 21-E-4); Ueda (discursos de 25/12/2023 e 25/12/2024, recorte do de 2023 pela busca no texto do BoJ); Krugman (1998), expressão "to be irresponsible" pela reprodução do argumento em resumos de busca; Ito e Mishkin (2006), pelo resumo do NBER; Watanabe e Watanabe (2018, AEPR 13(1): 23–41), pelo working paper e pelos slides; Watanabe (2026, CIGS WP 26-014E); Shirakawa (2021) pela resenha do FMI (F&D, dez/2021) e discurso de 30/05/2012; Borio, Erdem, Filardo e Hofmann (2015, BIS QR, quadro sobre o Japão); FMI, Artigo IV de 2026 (declaração de 13/02/2026, comunicado do Conselho de 02/04/2026, relatório 26/075); Sims (2016) pelo relato de Davies (Equitable Growth) e da Reuters.

### Lacunas (nada disso entrou como fato)

- Texto literal dos comunicados do BoJ (exceto o trecho do horizonte de dois anos) e do compromisso de ultrapassagem de 2016: parafraseados.
- Faixas do YCC de jul/2023 (0,5 como referência e compra a preço fixo a 1,0%): a busca não confirmou a data; o texto segue o calendário conhecido dos comunicados. Conferir no PDF do BoJ de 28/07/2023.
- Total comprado pelo BoJ por ano sob o YCC (a "redução furtiva"): sem número confirmado; o texto fica no qualitativo.
- Lucro do BoJ no ano fiscal de 2025 (1,93 tri) e juros pagos sobre reservas maiores que os recebidos dos títulos (2,71 × 2,52 tri): só em blog, não usados.
- Câmbio: mínima de 161,9 por dólar em jul/2024 não confirmada; o texto diz "mais de 160". Montante das intervenções de 2026 com fontes divergentes (US$ 40 bi em abril; 11,7 tri de ienes num mês): não usados.
- Fatia do BoJ em 2026 (41% a 44% conforme a medida): só o "abaixo de 50%" da Nikkei entrou.
- Juro de 10 anos negativo em 2016 e queixas do setor financeiro: retirado por falta de fonte conferida.
- Krugman (2015, "Rethinking Japan"): só citado na bibliografia, sem conteúdo.
- O FMI passou a medir a dívida bruta japonesa em valor de face consolidado no Artigo IV de 2026 (série com 227,8% → 193,1% numa tabela sem anos legíveis); a página usa os 204,8% de 2025 da 3.4 (WEO out/2026).

### Divergências

- Nenhuma de número com 3.4 (dívida 204,8% e juros líquidos 0,2% do PIB; 93,3% e 7,3% no Brasil), 3.3 (não residentes 9,9% em ago/2026), 6.3 (FBCF 16,8%, transações correntes −2,9%, poupança média 15,5%), 2.1/9.1 (ex-ante 8,73% em 23/10/2026) e 1.1.3/7.8 ("metade dos títulos"; inflação de 2% só a partir de 2022).
- 1.1.3 e 7.8 dizem que o BoJ "passou a deter cerca de metade dos títulos"; 10.3.3 precisa: 53,34% sem letras em mar/2023, 46,3% com letras no fim de 2024, abaixo de 50% em 2026. Coerente.
- 10.3 (ponte) diz que o BoJ "desmontou o arranjo e os juros negativos em março de 2024": igual.

## 10.3d

### Página entregue (02/11/2026)

- 10.3.4 Juros negativos, 1ª versão: cerca de 2.900 palavras de prosa corrida (sem parênteses de fonte, tabela, fórmulas, citações em bloco e listas dos quadros); cerca de 3.200 com citações e quadros; 4.500 pela contagem do lint, que inclui tabela e referências.
- Conteúdo: exemplo de brinquedo (banco com 1.000 de depósitos a 0%, 100 de capital, 900 de empréstimos a 3% e 200 de reservas; lucro 12 → 6,5 com reservas a −0,5%, sendo 1 de cobrança direta e 4,5 de margem; isenção de 60 reduz o custo direto a 0,7); condição $-i < c$ do papel-moeda e o ELB (Witmer e Yang 2016: Canadá ≈ −0,5%); motivos (regra de Taylor e câmbio); tabela de entrada, mínimo e saída dos cinco; gráfico; camadas (custo médio $(R-X)/R \cdot i$); efeitos (repasse, depósitos, Dinamarca, margem $\Delta\Pi \approx -\Delta E$ acima de zero e $-\Delta A$ com depósito parado, Heider et al., Eggertsson et al., Altavilla et al. 2018 e 2022, FMI 2021, câmbio); *reversal rate* (Abadi, Brunnermeier e Koby; ganho de capital único × perda de margem anual; Darracq Pariès, Kok e Rottner ≈ −1%); quadro A favor/Contra sobre a eficácia; distância do Brasil (Selic 2% de 06/08/2020 a 17/03/2021); espelho do teto prático com links para 1.5.1, 1.5.2, 1.5.3, 3.1 e 6.1; caixa "o painel lê".
- Gráfico: `dados/10.3.4-taxas-negativas.json`, mensal, jan/2010 a set/2026. Do bruto `dados/brutos/bis-politica_monetaria.csv` (REF_AREA = XM e JP, consulta 02/11/2026) mais a facilidade de depósito do BCE reconstruída pelas datas de vigência da tabela do BCE até ago/2024 (a série XM do BIS é a taxa de refinanciamento até 17/09/2024 e a facilidade de depósito depois). Conferido: em todos os meses de 2010 a ago/2024 a diferença entre a taxa de refinanciamento do BIS e a facilidade reconstruída é 0,75, 0,50, 0,40, 0,35 ou 0,25 ponto, como nas decisões do BCE. Script em scratchpad, não versionado.
- Suíça, Suécia e Dinamarca não estão no bruto do BIS (a coleta tem BR, MX, CL, CO, IN, ZA, TR, US, XM, JP, GB, RU, ID); ficaram só na tabela e no texto, como pede o cartão. Para pô-las no gráfico, acrescentar CH, SE e DK a `BIS_PAISES` em `tools/coletar.py`.

### Fontes principais (todas por WebSearch; bis.org, nber.org, fred.stlouisfed.org e data.snb.ch recusados pela rede)

BCE (comunicados de 05/06/2014 e 12/09/2019; tabela das taxas diretoras, confirmada também pela tabela do Central Bank of Ireland); SNB (decisões de 18/12/2014, 15/01/2015, jun/2022 e 22/09/2022; isenção de 20 vezes o compulsório e 25 vezes desde 01/11/2019); Riksbank (−0,10% anunciado em 12/02/2015 com vigência em 18/02; −0,25% mar/2015; −0,35% jul/2015; −0,50% fev/2016; −0,25% em jan/2019; zero decidido em 18/12/2019 com vigência em 08/01/2020; *Account of Monetary Policy 2019*); Danmarks Nationalbank (*Monetary Review* 3T/2012; comunicado de 08/09/2022: +0,65% em 09/09/2022, vindo de −0,10% desde 22/07/2022, que vinha de −0,60%; *Analysis* n. 9/2021: ≈30% dos depósitos de famílias com taxa negativa em mai/2021); Banco do Japão (via 10.3.3 e nota do BIS); Bech e Malkhozov (2016, BIS QR mar/2016, recorte do resumo pela busca); Abadi, Brunnermeier e Koby (2023, AER; recorte da definição pelo resumo reproduzido na busca); Heider, Saidi e Schepens (2019, RFS 32(10): 3728–3761, recorte do resumo); Eggertsson, Juelsrud, Summers e Wold (2019, NBER 25416; RES 2024, recorte do resumo; calibração −0,5% → +15 pb no crédito e −7 pb no produto); Eisenschmidt e Smets (2019, Banco Central do Chile); Altavilla, Boucinha e Peydró (2018); Altavilla, Burlon, Giannetti e Holton (2022); FMI (Departmental Paper 2021/003 e blog de 03/03/2021); Andersson e Jonung (2020); Flug e Honohan (2022) e a resposta do Riksbank; Darracq Pariès, Kok e Rottner (2020, BCE WP 2487); Witmer e Yang (2016); Chen, Funke e Moessner (2017, BIS WP 660); Nordea (21/11/2019); Jyske Bank (crédito imobiliário de dez anos a −0,5%, ago/2019, por CNBC e Bloomberg).

### Lacunas (nada disso entrou como fato)

- Dinamarca: data exata da volta ao negativo em 2014 (o texto diz só que, entre jan e fev/2015, foram quatro cortes de −0,05% até −0,75%); sequência de 2016 a 2021 (−0,65% em jan/2016, −0,75% em set/2019, unificação das taxas em 2021) não confirmada; o arranjo de "conta corrente a zero com limite e excedente em certificados" vem do conhecimento do painel e do resumo do BIS (três de quatro com limites), sem documento do Nationalbank aberto. Conferir no Statbank do Nationalbank.
- SNB: a vigência de 22/01/2015 está confirmada para −0,75%; a de −0,25% anunciada em 18/12/2014 não foi conferida (o texto só diz "anunciou").
- Tamanho da valorização do franco em 15/01/2015: fontes secundárias dão de 20% a 40%; o texto diz só que chegou à paridade (BIS WP 660). Estoque de notas de 1.000 francos (48,6 bi, 59% do valor em circulação no início de 2021, The Local) não usado.
- Riksbank: taxa de depósito negativa em 2009 (sem nível confirmado) fora do texto.
- Eisenschmidt e Smets (2019): só resumos; o texto se limita ao amontoamento das taxas de depósito em zero.
- FMI (2021) e Altavilla et al.: parafraseados, sem recorte.
- Bech e Malkhozov: só a primeira página (31) confirmada.
- Fuga para papel-moeda: o texto cita só a Dinamarca (*Analysis* 9/2021); nenhum número de demanda por cédulas.

### Divergências

- O cartão dá "Suécia fev/2015 −0,5%": a entrada foi −0,10% em fev/2015 e o mínimo de −0,50% veio em fev/2016. A página usa as duas datas. O cartão dá "saída da Suécia 2019": decisão em 18/12/2019, vigência em 08/01/2020.
- Saída do BCE: decisão em 21/07/2022, vigência em 27/07/2022 (cartão: jul/2022). Saída do SNB: decisão em 22/09/2022, vigência em 23/09 (cartão: set/2022). Coerentes.
- Japão: o BIS só registra −0,1% a partir de set/2016 (como em 10.3.3); a página dá a vigência de 16/02/2016 pela decisão do BoJ.
- Números brasileiros iguais às decisões de `_divergencias.md`: LFT 52,74% (ago/2026), R$ 49 bi por ponto de Selic na DPF e R$ 61,7 bi na DLSP, juros nominais de R$ 1.204,8 bi = 8,99% do PIB em 12 meses até set/2026, Selic 2% de 06/08/2020 a 17/03/2021 e 15% de 19/06/2025 a 18/03/2026 (SGS 432).

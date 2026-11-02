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

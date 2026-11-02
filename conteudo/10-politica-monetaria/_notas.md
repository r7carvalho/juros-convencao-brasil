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

# Notas da área 1, segunda metade (redator 1b: páginas 1.4 a 1.6)

Data: 02/11/2026. Não vira página. A primeira metade (1, 1.1 a 1.3) tem notas próprias em `_notas-1a.md`.

## Páginas entregues

Palavras do corpo, sem frontmatter e sem a seção "Para ler" (entre parênteses, com as referências).

| id | arquivo | palavras |
|---|---|---|
| 1.4 | 1.4-convencao.md | 3.550 (3.770) |
| 1.4.1 | 1.4.1-juro-normal.md | 2.160 (2.270) |
| 1.4.2 | 1.4.2-concurso-de-beleza.md | 1.800 (1.960) |
| 1.4.3 | 1.4.3-convencao-e-racionalidade.md | 2.410 (2.640) |
| 1.5 | 1.5-dominancia-fiscal.md | 2.600 (2.780) |
| 1.5.1 | 1.5.1-sargent-wallace.md | 1.860 (2.060) |
| 1.5.2 | 1.5.2-blanchard-favero-giavazzi.md | 2.120 (2.260) |
| 1.5.3 | 1.5.3-calvo.md | 2.050 (2.200) |
| 1.5.4 | 1.5.4-ftpl.md | 2.140 (2.470) |
| 1.5.5 | 1.5.5-equivalencia-ricardiana.md | 1.610 (1.830) |
| 1.6 | 1.6-longo-prazo-histerese.md | 3.290 (3.650) |

Total do corpo: cerca de 25.600 palavras. `python3 tools/build.py --check` passa; o único aviso nas minhas páginas é o link para 8.1, que ainda não existe.

## Gráficos (dados/)

Simulações e cálculos do painel (sem dado externo, fonte declarada como cálculo ou simulação):

- `1.4.1-perpetuidade-preco.json`: preço da perpetuidade de cupom 1 para juros de 2% a 10%.
- `1.4.1-retorno-volta-ao-normal.json`: retorno em um ano se o juro voltar a 5%.
- `1.4.1-juro-critico.json`: alta que zera um ano de cupom, r²/(1 − r), de 1% a 10%.
- `1.4.2-niveis-de-raciocinio.json`: palpites por nível de raciocínio no jogo dos 2/3.
- `1.5.1-aritmetica-desagradavel.json`: inflação sob "monetiza já" e "aperta 10 anos".
- `1.5.3-calvo-ponto-fixo.json`: probabilidade temida × probabilidade produzida (equilíbrios em 5,6% e 44,4%).
- `1.6-histerese-brinquedo.json`: tendência, recuperação completa e histerese.

Com dado:

- `1.5-primario-estabilizador.json`: cenários da Frente J (BCB, IFI).
- `1.5-juros-liquidos-paises.json`: juros líquidos 2025, FMI via Frente J. Pode duplicar gráfico da área 3 (3.4); o coordenador decide se mantém os dois.
- `1.5.2-embi-2002-2003.json`: seis pontos do EMBI+ (Frente I, Ipeadata).
- `1.5.2-ptax-2002-2003.json`: seis pontos da PTAX (Frente I, SGS 1).
- `1.5.2-selic-meta-2002-2003.json`: meta Selic no fim de cada mês, 2002–2003. Não está nos insumos (ver abaixo).
- `1.6-taxa-investimento.json`: FBCF/PIB 1996–2026 (Frente L, IBGE). Pode duplicar gráfico da área 5 (5.2).

## Números novos, não presentes nos insumos

- Meta Selic 2002–2003 (19%; 18,75% em 20/02/2002; 18,5% em mar; 18% em jul; 21% em 14/10/2002, extraordinária; 22% nov; 25% dez; 25,5% jan/2003; 26,5% fev/2003 a jun; 26% jun; 24,5% jul; 22% ago; 20% set; 19% out; 17,5% nov; 16,5% dez/2003). Lidos em cópia pública da série do BCB no GitHub (`lvbn/IC_ICV`, `data/bcb_copom_2000.csv`), porque o BCB está bloqueado. Coerentes com o juro real ex-post de 2002 (5,89%) e 2003 (12,84%) da Frente K. Conferir no histórico do Copom.
- IPCA 2002 = 12,53% e 2003 = 9,30% (IBGE). Não confirmados em fonte primária nesta sessão; coerentes com o juro real ex-post da Frente K ((1 + Selic acumulada)/(1 + IPCA) − 1). Teto da meta de 2002 = 5,5% (meta de 3,5% ± 2).

## Divergências e precisões

- Exemplo da perpetuidade (CONTEXTO: "quem crê que 5% é o normal espera perder 16%"). A conta exata: perda de capital de 20% (de 25 para 20) menos cupom de 4% em um ano = 16%. Se a volta ao normal levar cinco anos, os cupons empatam a perda. A página registra as duas coisas.
- Juro crítico de Keynes: ele escreve 0,16 p.p. a 4% e 0,04 p.p. a 2% (aproximação r²). A conta exata é r²/(1 − r): 0,167 e 0,041. A página mostra as duas.
- Frente K: o resumo fala em "R$ 62 a 69 bi por ponto" de Selic; a análise diz "R$ 61,7 bi a R$ 68,9 bi". Usei a segunda.
- McCandless e Weber: CONTEXTO diz correlação de 0,93 a 0,96; a página 1.1.2 (redator 1a) diz 0,92 a 0,96. Alinhei 1.6 com 1.1.2 (0,92 a 0,96). O coordenador deve fixar um dos dois.
- Neutro: o BCB usa 5,0% (Frente K). A estimativa de 8% "de economista de mercado" do CONTEXTO não tem autor nem data; ficou marcada [a conferir] em 1.4.1.

## O que ficou [a conferir]

- Nagel (1995): médias da primeira rodada (cerca de 37 com p = 2/3 e 27 com p = 1/2). No texto, só a descrição qualitativa (escolhas concentradas nos níveis 1 e 2), que foi conferida.
- Bank Rate de 2% de 1932 a 1951 (com alta breve em 1939), conversão do War Loan de 5% para 3,5% em 1932 e o teto de 2,5% dos títulos longos americanos em 1942–1951 (1.4.1).
- Desemprego americano de 10,8% no fim de 1982 e volta a 5%–6% no fim da década (1.6), série BLS LNS14000000.
- Composição da DPMFi por indexador em 2002 e meta de superávit primário de 2003 (1.5.2): o texto fala só em "parte relevante" atrelada à Selic e ao dólar, sem número.
- Dados bibliográficos escritos de memória e não conferidos nesta sessão (volume, número, páginas): Dequech 1999, 2003 e 2011; Orléan 1999; Wicker 1986; Garber 1982; Darby 1984; Ayres, Navarro, Nicolini e Teles 2018; Bianchi, Faccini e Melosi 2023; Ball 2014 (versão em periódico); King e Watson 1997; Lamont 2002; Hong, Kubik e Solomon 2000; Kalecki 1971 (ensaio de 1968); Loyo 1999 (mimeo); Razin e Sadka 2002 (título conforme o metadado do NBER, "A Brazilian Debt-Crisis").

## Origem dos recortes citados (todos com tradução do painel)

A rede bloqueia os sites de texto integral (hetwebsite, marxists.org, Gutenberg) e o WebFetch. O orçamento de busca web da sessão (200 buscas, compartilhado entre os redatores) se esgotou no meio desta rodada. Os trechos entre aspas foram conferidos assim:

- Keynes, *Teoria Geral*, cap. 12 (p. 152, 156, 158) e cap. 15 (p. 201, 202, 203, 204): cópias do texto em repositórios públicos do GitHub (`jundalisay/sp`, capítulos 15b e 15c; `VuAnhQuan-alh/leanblock`; `jasonacollins/behaviouraleconomics`; `uminomae/creation-space`), mais busca web que localizou as páginas escaneadas 202–204 da 1ª edição. As páginas seguem a edição Macmillan de 1936.
- Keynes, QJE 1937, p. 214–215: notas de leitura em `uminomae/creation-space` feitas sobre o PDF do hetwebsite.
- Keynes, *Tract*, 1923, cap. 3: várias cópias no GitHub; a página 80 é da 1ª edição.
- Lewis 1969 (p. 58 e 78) e Schelling 1960 (p. 57): notas de leitura em `BrettRey/Grammaticality-de-idealized-v2` e `0xferit/manuscript-decentralized-curation`.
- Resumos do NBER (Blanchard 2004; Favero e Giavazzi 2004; Woodford 1995; Ball 2014; Fatás e Summers 2016; Blanchard e Summers 1986; Blanchard, Cerutti e Summers 2015; Jordà, Singh e Taylor 2020; García-Schmidt e Woodford 2015; Garín, Lester e Sims 2016; Buiter 1998; McCallum 2003; Razin e Sadka 2002): base `ledwindra/nber` no GitHub.
- Calvo 1988 (frase das soluções) e Cerra e Saxena 2008 (descrição da replicação): busca web, resumo do IDEAS e do openICPSR.

Sem recorte entre aspas, só paráfrase com referência: Sargent e Wallace 1981, Sargent 1982, Dequech, Orléan, Barro 1974, Kalecki, Nagel 1995, Cochrane.

## Sugestões para a próxima rodada

- Conferir no SGS (432) a Selic de 2002–2003 e trazer a série diária do EMBI+ e da PTAX para os gráficos de 1.5.2, em vez dos seis pontos.
- Ler Blanchard (2004) por inteiro para citar os parâmetros estimados (elasticidade do prêmio à dívida, papel do spread americano) e a parcela da dívida em dólar em 2002.
- Acrescentar estudos brasileiros de dominância fiscal (por exemplo, Tanner e Ramos, 2003; Gadelha e Divino, 2008) e de função de reação fiscal, para dar à 1.5 evidência econométrica nacional.
- Buscar recortes textuais de Dequech e Orléan (hoje só paráfrase) e de Sargent e Wallace (o PDF está no site do Fed de Minneapolis).
- Para 1.6, trazer estimativas do produto potencial brasileiro (IFI, BCB) antes e depois de 2014, para testar a histerese com dado nacional.

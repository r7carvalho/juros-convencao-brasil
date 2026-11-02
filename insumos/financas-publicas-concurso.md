# Insumo — Finanças públicas: dívida, resultados fiscais e interfaces com a política monetária

Preparado em 02/11/2026 a partir do material de estudo para concursos fiscais guardado em disco. Uso: base de conteúdo para um site público de revisão bibliográfica. Tudo abaixo está
parafraseado. Material de curso privado entra só como **roteiro** (quais pontos a banca cobra, que erros os
cursos cometem); a sustentação de cada conceito vem da fonte oficial, citada com documento e página.

**Fonte primária de referência, com versão datada.** O BCB edita o *Manual de Estatísticas Fiscais* e o
glossário fiscal sem aviso. As páginas citadas aqui são as dos PDFs baixados em **27/09/2026**:

- BCB, *Manual de Estatísticas Fiscais*, edição de maio/2019 (a que o site servia em 27/09/2026), 49 p. —
  `https://www.bcb.gov.br/content/estatisticas/notas_metodologicas/estatisticas-fiscais/estatisticasfiscais.pdf`
- BCB, *Glossário* das estatísticas fiscais (1 p., sem data) —
  `https://www.bcb.gov.br/content/estatisticas/Documents/Estatisticas_mensais/Fiscal/glossariofiscal.pdf`
- STN, *Manual de Demonstrativos Fiscais* (MDF), 15ª ed., 1ª versão, 2025 (Portaria STN 2.057). Páginas
  citadas como "PDF p. X" (a numeração impressa é uma unidade menor).
- LC 101/2000 (LRF), LC 200/2023, CF/1988 e ADCT: texto compilado do Planalto, consulta de 27/09/2026.

Onde o material em disco **não** sustenta uma afirmação, o texto diz "fora do material em disco — conferir".

---

## 1. Mapa de conceitos

```
FINANÇAS PÚBLICAS — DÍVIDA E RESULTADOS
│
├── A. Abrangência institucional
│   ├── Setor público consolidado (base da DLSP e da NFSP)
│   │   ├── administrações diretas e indiretas das 3 esferas + previdência
│   │   ├── estatais não financeiras (exceto grupos Petrobras e Eletrobras)
│   │   └── Banco Central
│   │       └── fora: instituições financeiras públicas
│   └── Governo geral (base da DBGG e da DLGG)
│       └── 3 esferas + previdência, sem BC e sem estatais
│
├── B. Estoques (dívida)
│   ├── DLSP — líquida, setor público consolidado
│   │   ├── fórmula DLSP = M + B + E·I − A + E·F − E·R
│   │   ├── ativo real não abate (imóvel, ação de empresa)
│   │   └── Dívida Fiscal Líquida (DFL) = DLSP − ajustes patrimoniais e metodológicos
│   ├── DBGG — bruta, governo geral
│   │   ├── conceito BCB: do BC entram só as compromissadas com títulos públicos
│   │   ├── conceito "FMI": todos os títulos do Tesouro na carteira do BC
│   │   └── DBGG-estendida (GFSM 2014): + contas a pagar (restos a pagar, precatórios, FCVS)
│   ├── DPF / DPMFi / DPFe — dívida federal gerida pelo Tesouro (em mercado)
│   ├── Operações compromissadas do BC (ponte com a política monetária)
│   └── Dívida consolidada (LRF/RSF) — conceito jurídico, com precatórios e limites
│
├── C. Fluxos (resultados)
│   ├── NFSP — conceitos
│   │   ├── primário  = receitas e despesas não financeiras
│   │   ├── operacional = primário + juros reais   (série encerrada em 2009)
│   │   └── nominal   = primário + juros nominais  (= NFSP "cheia")
│   ├── Critérios de apuração
│   │   ├── abaixo da linha — BCB, variação da dívida líquida
│   │   └── acima da linha — STN/RTN e RREO, receita × despesa
│   ├── Regime: caixa (receitas e despesas) × competência (juros)
│   ├── Ajustes patrimoniais e metodológicos
│   │   ├── privatização
│   │   ├── reconhecimento de dívidas ("esqueletos") e reclassificações
│   │   ├── metodológico cambial, paridade, caixa × competência dos juros externos
│   │   └── securitização (tratamento conforme a natureza da operação)
│   └── Conciliação estoque–fluxo: ΔDLSP = primário + juros nominais + ajustes
│
├── D. Financiamento
│   ├── restrição orçamentária: emissão (M), dívida (B, I, F), venda de ativos (A, R)
│   ├── senhoriagem × imposto inflacionário
│   └── CF art. 164: BC não financia o Tesouro
│
├── E. Risco fiscal
│   ├── Anexo de Riscos Fiscais da LDO (LRF art. 4º, § 3º)
│   ├── matriz: diretas × contingentes; explícitas × implícitas
│   ├── passivos contingentes → esqueletos → ajuste patrimonial
│   └── precatórios (LRF art. 30, § 7º; ADCT 107-A; EC 136/2025)
│
├── F. Regras fiscais
│   ├── LRF: metas no AMF, limitação de empenho, limites de dívida, art. 44
│   ├── regra de ouro (CF art. 167, III; LRF art. 12, § 2º)
│   ├── teto de gastos (EC 95/2016) — revogado
│   └── Regime Fiscal Sustentável (LC 200/2023): meta de primário, banda, limite de despesa
│
└── G. Sustentabilidade
    ├── restrição intertemporal: dívida = VP dos primários futuros
    ├── dinâmica d_t = [(1+r)/(1+g)]·d_{t−1} − s_t
    └── primário estabilizador ≈ (r − g)·d
```

---

## 2. Conceito por conceito

Formato: definição (paráfrase) · fonte primária · exemplo numérico · pegadinhas registradas no material.
As pegadinhas de banca citam o certame (banca, ano, órgão) e o gabarito, tirados das listas de itens que o
material organiza; a afirmação foi reescrita.

### 2.1 Abrangência: setor público consolidado × governo geral

**Definição.** As estatísticas de dívida líquida e de NFSP cobrem o setor público não financeiro mais o
Banco Central: administrações diretas e indiretas das três esferas, previdência, fundos e estatais não
financeiras, com exclusão dos grupos Petrobras (desde maio/2009) e Eletrobras (desde novembro/2010). As
instituições financeiras públicas ficam de fora, ainda que controladas pelo governo, porque o objetivo é medir
o impacto do setor público sobre a demanda agregada pela ótica do financiamento, e a intermediação financeira
distorceria essa leitura. O governo geral é mais restrito: as três esferas com a previdência, sem BC e sem
estatais.

**Fonte.** BCB, *Manual*, pp. 8-10.

**Exemplo.** Uma estatal incluída no setor público paga 10 de dividendos ao ente controlador. A dívida líquida
da estatal sobe 10 (perdeu caixa), a do ente cai 10 (ganhou caixa); no consolidado, efeito zero. Se os mesmos
10 forem pagos a acionistas privados, a DLSP sobe 10 (*Manual*, pp. 9-10).

**Pegadinhas.**
- "A DBGG não considera estados e municípios" — errado (Cebraspe 2017, SE-DF, E).
- "A DBGG abrange as estatais federais" — errado (Cebraspe 2016, TCE-PA, E).
- Setor público = não financeiro + BC — certo (Cebraspe 2014, TJ-SE, C).
- Um curso de 2026 excluiu do setor público só a Petrobras; o manual exclui Petrobras e Eletrobras (errata
  registrada no material, *Manual*, p. 8).

### 2.2 Dívida Líquida do Setor Público (DLSP)

**Definição.** Saldo entre passivos e ativos financeiros do setor público consolidado perante o sistema
financeiro (público e privado), o setor privado não financeiro e o resto do mundo. Entra no passivo a base
monetária (passivo do BC), e saem como ativos as reservas internacionais e os créditos do governo. Ativos reais,
como imóveis e participações acionárias, não abatem.

$$\text{DLSP} = M + B + E\,I - A + E\,F - E\,R$$

M = base monetária; B = dívida interna em reais; I = dívida interna indexada ao câmbio; F = dívida externa;
A = ativos financeiros internos; R = reservas; E = taxa de câmbio.

**Fonte.** BCB, *Manual*, p. 12 (fórmula e sua diferencial); glossário fiscal.

**Exemplo.** Base 400, títulos internos 6.000, dívida indexada ao câmbio US$ 10, dívida externa US$ 50,
ativos internos 1.500, reservas US$ 350, câmbio 5. DLSP = 400 + 6.000 + 50 − 1.500 + 250 − 1.750 = 3.450.
Como R > I + F, o setor público é **credor externo líquido**: uma depreciação do real (E sobe) **reduz** a DLSP.

**Pegadinhas.**
- "A desvalorização cambial aumenta a DLSP" — errado no caso brasileiro de credor externo líquido (Cebraspe
  2015, MPOG, E). O efeito vai para ajuste metodológico e **não** passa pela NFSP.
- "A DLSP é o conceito mais amplo de dívida" — certo pela abrangência institucional (Cebraspe 2014, TJ-SE, C).
- "Bruta" não quer dizer "mais ampla": a DBGG é mais restrita que a DLSP em abrangência.

### 2.3 Dívida Bruta do Governo Geral (DBGG) — conceito BCB × conceito FMI

**Definição (BCB).** Total dos débitos do governo federal, estaduais e municipais junto ao setor privado, ao
setor público financeiro e ao resto do mundo, sem deduzir ativos. Estatais ficam fora. Do Banco Central entram
**apenas as operações compromissadas com títulos públicos**, porque têm relação estreita com a dívida do
Tesouro. Estrutura: dívida mobiliária em mercado (descontadas as aplicações da previdência, de fundos federais e
de estados e municípios em títulos), compromissadas, dívida bancária, dívida assumida pela União (Lei
8.727/1993) e dívida externa das três esferas. Débito externo convertido pelo câmbio de fim de período.

**Fonte.** BCB, *Manual*, p. 10 (nota 2) e pp. 24-25.

**Conceito FMI.** O FMI conta como dívida do governo geral **todos** os títulos do Tesouro na carteira do BC,
não só os que lastreiam compromissadas. Por isso a DBGG "critério FMI" fica acima da DBGG do BCB; o material
registra 78,7% × 93,4% do PIB em dezembro/2025, números que um curso atribui às Estatísticas Fiscais do BCB.
**Fora do material em disco — conferir** a definição exata e o nome da série na Nota de Estatísticas Fiscais do
BCB (a série costuma vir rotulada como DBGG pela metodologia usada até 2007) antes de publicar os números.

**DBGG-estendida (GFSM 2014).** O manual do BCB mostra que o GFSM 2014 inclui na dívida bruta instrumentos que a
DBGG do BCB não inclui: "outras contas a pagar" (restos a pagar, precatórios, FCVS) e regimes de seguros,
pensões e garantias padronizadas. O BCB divulga o Patrimônio Financeiro Líquido do Governo Geral (PFLGG), anual,
e, para fins didáticos, nomeia "DLGG-estendida" e "DBGG-estendida". Os passivos atuariais dos regimes próprios
ficaram de fora.

**Fonte.** BCB, *Manual*, pp. 45-48 (quadro de indicadores na p. 48).

**Exemplo.** Títulos do Tesouro: 7.000 em mercado e 2.000 na carteira do BC, dos quais 1.500 lastreiam
compromissadas. DBGG-BCB (só essa parcela) = 7.000 + 1.500 = 8.500; critério FMI = 7.000 + 2.000 = 9.000
(números ilustrativos; os demais componentes foram omitidos).

**Pegadinhas.**
- "A DBGG exclui o BC, logo exclui as compromissadas" — errado: as compromissadas entram.
- Item certo: as compromissadas entram na DBGG, que abrange a dívida mobiliária federal em mercado
  (Cebraspe 2025, SEFAZ-RJ, C, registrado no material).
- Um curso de 2026 definiu a DBGG como débitos "junto ao BC" também; a versão vigente só leva as
  compromissadas (errata V1 do material, *Manual*, p. 24).
- A LC 200/2023 ancora a sustentabilidade na **DBGG**, não na DLSP (art. 2º, § 1º). Um card do material cobra
  exatamente isso (FCC 2018, TCE-RS, E para quem trocou).

### 2.4 Dívida Pública Federal (DPF, DPMFi, DPFe)

**Definição.** Conceito operacional do Tesouro Nacional: estoque da dívida federal **em mercado**, interna
(DPMFi, títulos) e externa (DPFe). Não inclui estados e municípios nem a carteira do BC. É o objeto do Plano
Anual de Financiamento (PAF) e dos relatórios mensal (RMD) e anual (RAD).

**Fonte.** STN (PAF, RMD, RAD). **Fora do material em disco — conferir** definições e números no Tesouro
Transparente. O *Manual* do BCB (p. 24) dá a distinção posição de carteira × posição de custódia:
custódia = carteira + recompras − revendas do BC.

**Exemplo (dados que um curso atribui ao RMD de dez/2025; conferir na fonte).** DPF de R$ 7,3 tri para R$ 8,6
tri em 2025; cerca de dois terços da alta vieram de juros apropriados e um terço de emissões líquidas;
composição: Selic ≈ 48%, IPCA ≈ 26%, prefixados ≈ 22%, câmbio ≈ 4%; prazo médio 4,0 anos.

**Pegadinhas.**
- DPF ≠ DBGG: a DBGG soma estados, municípios, dívida bancária e compromissadas.
- "O maior credor da dívida brasileira é o FMI" — errado; a dívida é majoritariamente interna, detida por
  instituições financeiras, previdência e fundos (FCC 2019, AFAP, alternativa errada).
- O BC não emite título próprio desde 2002 (LRF, art. 34): o Tesouro emite, o BC opera no mercado secundário.

### 2.5 NFSP: primário, operacional e nominal

**Definição.**
- **Primário:** componente não financeiro do resultado — receitas e despesas não financeiras, correntes e de
  capital. No BCB, sai do nominal pela exclusão dos juros nominais apropriados por competência.
- **Nominal:** variação da dívida líquida, descontados os ajustes patrimoniais e metodológicos; contém o
  primário, os juros reais e a atualização monetária da dívida. É a NFSP "cheia".
- **Operacional:** nominal menos a atualização monetária da dívida interna, ou primário mais juros reais. É o
  resultado que se teria com inflação zero; relevante em inflação alta, quando o juro nominal carrega reposição
  de valor. O BCB só divulga a série até dezembro/2009.
- **Sinal:** NFSP positiva = déficit.

$$P = RN - JN \qquad RO = RN - CM = P + J_{\text{reais}} \qquad JN = J_{\text{reais}} + CM$$

**Fonte.** BCB, *Manual*, pp. 13-14 e 33-34.

**Exemplo.** Receitas primárias 1.000; despesas primárias 980; juros nominais 120, dos quais 70 de correção
monetária. Primário = superávit 20 (NFSP primária −20). Nominal = −20 + 120 = 100 de déficit. Operacional =
100 − 70 = 30 de déficit.

**Pegadinhas.**
- "Nominal − primário = juros reais" — errado, é o juro nominal (Cebraspe 2018, EBSERH, E).
- "O operacional é o conceito mais amplo" — errado, o mais amplo é o nominal (Cebraspe 2016, FUNPRESP, E).
- "Com inflação elevada, o nominal informa mais que o operacional" — errado (Cebraspe 2014, TJ-SE, E).
- "O primário de 2014-15 piorou por causa dos juros da política monetária" — errado: Selic mexe no nominal,
  não no primário (Cebraspe 2016, TCE-PA, e 2017, SE-DF, E).
- Pagamento de benefício do INSS afeta o primário e a dívida (Cebraspe 2015, MPOG).
- Esquemas de curso escrevem "nominal = operacional + **inflação**". O que se soma é a **atualização monetária
  da dívida**, que é parte dos juros nominais; a inflação em si não é parcela do resultado.
- Um curso de 2026 chamou a correção monetária da dívida de "imposto inflacionário". Imposto inflacionário é a
  perda de quem detém moeda; a correção é componente do juro nominal (errata E1; *Manual*, pp. 14, 32-33).

### 2.6 Acima × abaixo da linha

**Definição.** **Abaixo da linha** mede o resultado pela variação do endividamento líquido, isto é, pelo
financiamento que o sistema financeiro e os setores privado e externo concederam ao setor público. É o critério
do BCB, para o setor público consolidado e suas divisões. Diz quanto foi o déficit, mas não por quê. **Acima
da linha** parte das receitas e despesas, rubrica por rubrica, e revela os fatores. A STN publica por esse
critério o resultado do **governo central** (Tesouro, Previdência e BC) no *Resultado do Tesouro Nacional*
(RTN). Em princípio os dois chegam ao mesmo número; a diferença, por abrangência ou período, chama-se
discrepância estatística.

**Fonte.** BCB, *Manual*, pp. 13 e 15. Para estados e municípios (RREO, Anexo 6), o MDF manda apurar o
primário acima da linha e o nominal abaixo da linha, pela variação da dívida consolidada líquida, porque o
cálculo acima da linha não captura obrigações em atraso incluídas na dívida consolidada (STN, MDF 15ª ed.,
PDF pp. 265-267).

**Exemplo.** Acima: receitas 360, despesas não financeiras 400 → déficit primário de 40. Abaixo: a DLSP subiu
40 + juros, e o BCB, sem olhar rubricas, deduz o primário retirando os juros apropriados.

**Pegadinhas.**
- "O Tesouro apura pelo abaixo da linha" — errado (Cebraspe 2016, TCE-PA, E).
- "Abaixo da linha apura receita e despesa orçamentária" — errado (Cebraspe 2015, TCE-RN e MPOG, E).
- "O BC apura a NFSP acima da linha" — errado (Cebraspe 2014, TJ-SE, E).
- Sinais opostos: NFSP positiva é déficit; no RTN, resultado negativo é déficit.
- **Quem verifica a meta da LC 200 é o BCB**, não o RTN: o resultado primário do governo central e a razão
  DBGG/PIB são apurados pelo Banco Central (LC 200, art. 2º, § 4º, e art. 5º, § 3º).
- Um esquema de curso diz que o abaixo da linha é "utilizado para a União". O BCB apura o setor público
  consolidado, com as três esferas e estatais.

### 2.7 Regime de apuração: caixa × competência

**Definição.** Nas NFSP do BCB, receitas e despesas entram pelo **caixa** (despesa conta quando paga, receita
quando entra no caixa); os **juros** entram por **competência**, apropriados *pro rata* ("curva do papel"),
para casar com a apuração da dívida. Período mensal; exercício = ano civil. O MDF segue a mesma lógica para o
RREO: receitas e despesas primárias por caixa, juros por competência (PDF pp. 267-268). O GFSM 2014, ao
contrário, é um sistema de competência integral.

**Fonte.** BCB, *Manual*, pp. 13-15 e 46.

**Exceção registrada pelo próprio manual.** Desde dezembro/2015, por determinação do TCU (Acórdãos
825/2015 e 3.297/2015 — o caso das "pedaladas"), as equalizações agrícolas no Banco do Brasil, as do PSI no
Finame e os pagamentos do FGTS ligados ao Minha Casa Minha Vida passaram a ser computados pelo registro mensal
das entidades credoras, que seguem competência (*Manual*, p. 15, nota 4).

**Exemplo.** Despesa empenhada e liquidada em dezembro, paga em janeiro: entra no resultado de janeiro. Juro
de um título que vence em julho: apropriado mês a mês desde a emissão.

**Pegadinhas.**
- "Despesa no fato gerador e juros quando pagos" — errado (Cebraspe 2014, TJ-SE, E).
- "No Brasil, o resultado fiscal é apurado por competência para receitas e despesas" — errado (Cebraspe 2025,
  registrado no material).
- Um card do material associa "caixa" ao acima da linha e "competência" ao abaixo da linha. Mistura método
  com regime: dentro da própria NFSP do BCB, que é abaixo da linha, receitas e despesas são caixa.

### 2.8 RTN do Tesouro × estatísticas do BCB × IBGE

**Definição.** Três produtores, três recortes. A **STN** publica mensalmente o primário do governo central
acima da linha (RTN) e, pela LRF, dívida e resultados de estados e municípios, com precatórios e restos a pagar
na dívida e só estatais dependentes na abrangência, em periodicidade quadrimestral. O **BCB** publica
mensalmente DLSP, DBGG e NFSP do setor público consolidado, abaixo da linha, sem vínculo com critérios
contábeis ou legais. O **IBGE** publica, nas contas nacionais, a conta corrente e a conta de capital das
administrações públicas, anual e sem estatais.

**Fonte.** BCB, *Manual*, pp. 13 e 15.

**Pegadinhas.** O manual faz questão de dizer que as estatísticas do BCB não estão vinculadas a critério
contábil ou legal. Questão que cobre "dívida consolidada" (LRF) com a definição da DLSP, ou o inverso, troca
um conceito jurídico por um estatístico.

### 2.9 Ajustes patrimoniais e metodológicos

**Definição.** Valores que mudam o estoque da DLSP sem representar esforço fiscal do período, e que por isso
saem dos fluxos:
- **metodológico (câmbio):** efeito da variação cambial sobre a dívida externa líquida e a interna indexada
  ao dólar; o impacto sobre a demanda tende a ser neutro;
- **paridade:** variação das moedas da cesta da dívida externa contra o dólar;
- **caixa × competência dos juros externos:** a dívida segue caixa, os juros externos seguem competência;
- **privatização:** a receita de venda de estatal abate a dívida líquida, mas não melhora primário nem nominal;
- **reconhecimento de dívidas ("esqueletos"):** dívida gerada no passado afeta só o saldo, nunca o fluxo do
  mês; o valor é excluído do nominal e do primário;
- **reclassificação de contas** entre esferas.

Conciliação: $\Delta \text{DLSP} = \text{primário} + \text{juros nominais} + \text{ajustes}$ (*Manual*, p. 39), e
a tabela de "fatores condicionantes" da DLSP abre cada item nessas colunas (p. 40).

**Dívida Fiscal Líquida.** DLSP descontados os ajustes patrimoniais e metodológicos; a variação da DFL é a
NFSP nominal (glossário fiscal; o material registra a série a partir de 2001).

**Securitização.** O manual trata por natureza econômica. Cessão definitiva de crédito, a preço de mercado,
sem garantia nem obrigação subsidiária, para unidade fora do setor público: venda de ativo, baixa do crédito e
entrada de caixa, sem efeito no primário. Cessão com garantia, ou de fluxo futuro de receita: financiamento,
registra-se dívida. Em todos os casos, o uso dos recursos em gasto primário aumenta a DLSP e gera déficit; o uso
para abater dívida é neutro. A capacidade de arrecadar tributos futuros não é ativo securitizável
(*Manual*, pp. 27-31).

**Fonte.** BCB, *Manual*, pp. 13, 27-31 e 37-40.

**Exemplo.** No mês: primário −15 (déficit), juros 60, reconhecimento de esqueleto 25, privatização 10.
NFSP nominal = 15 + 60 = 75. ΔDLSP = 75 + 25 − 10 = 90.

**Pegadinhas.**
- Um curso de 2026 listou "os valores das privatizações" entre os ativos excluídos da DLSP. A privatização não
  é ativo excluído: é ajuste nos fluxos, que reduz a dívida líquida e não altera o resultado (errata E2;
  *Manual*, pp. 37-38).
- Um quadro de curso grafa NFSP = ΔDLSP + (ajustes − privatização) com os sinais trocados; o próprio material
  anotou que a forma correta, conferida em gabarito da FGV, é NFSP = ΔDLSP + privatização − outros ajustes.
- Câmbio: muda a DLSP, não muda a NFSP (Cebraspe 2015, MPOG).

### 2.10 Receita de privatização

Ver o padrão de erro 3.1, que trata o tema por inteiro. Resumo: pelo critério abaixo da linha do BCB, a venda
de estatal **reduz a DLSP e não altera primário nem nominal** (*Manual*, p. 38). Pelo critério acima da linha da
STN, a receita de alienação é receita de capital, mas não é receita primária; no RREO, entra entre os ajustes
metodológicos do nominal abaixo da linha (MDF, PDF pp. 266-267). A LRF ainda veda aplicar receita de alienação
de bens em despesa corrente, salvo destinação legal à previdência (art. 44).

### 2.11 Financiamento do déficit

**Definição.** A restrição orçamentária do setor público mostra as fontes: emissão monetária (M), aumento da
dívida interna (B), interna indexada ao câmbio (I) e externa (F), ou redução de ativos internos (A) e externos
(R). Sinal positivo da fonte financia déficit; negativo acompanha superávit. **Senhoriagem** é a receita do
emissor de moeda; **imposto inflacionário** é a perda de quem detém moeda num ambiente de inflação. A CF veda
ao BC emprestar ao Tesouro, mas permite comprar e vender títulos do Tesouro para regular moeda ou juros.

**Fonte.** BCB, *Manual*, p. 32; CF, art. 164, §§ 1º e 2º; LRF, art. 39, § 2º (compra direta pelo BC só para
rolar título vencendo na própria carteira).

**Exemplo.** Déficit nominal de 100 coberto por 20 de base monetária e 80 de títulos. A DLSP sobe 100, porque a
base também é passivo do setor público consolidado.

**Pegadinhas.**
- Senhoriagem financiou o déficit e baixou a DLSP/PIB em 1990-94 — certo (Cebraspe 2017, SE-DF, C).
- "Dívida/PIB estável na primeira metade dos anos 80 graças à senhoriagem" — errado (Cebraspe 2016, TCE-SC, E).
- Efeitos da inflação sobre o déficit: Olivera-Tanzi (a inflação corrói a receita entre fato gerador e
  recolhimento, o déficit sobe) × Patinkin (corrói a despesa fixada em valor nominal, o déficit cai). No Brasil
  dos anos 80 e 90, com tributo indexado e gasto não, prevaleceu Patinkin, e a NFSP operacional de 1990-94 caiu
  (Cebraspe 2017, SE-DF; 2018, EBSERH e ABIN). Este ponto o material sustenta só em curso e em gabaritos, sem
  livro-texto em disco.

### 2.12 Risco fiscal

**Definição.** A LDO traz um **Anexo de Riscos Fiscais** que avalia passivos contingentes e outros riscos
capazes de afetar as contas e informa as providências caso se concretizem (LRF, art. 4º, § 3º). A reserva de
contingência da LOA serve a esses eventos (LRF, art. 5º, III, "b"). O MDF define risco fiscal como a
possibilidade de evento que impacte negativamente as contas, e **contingência passiva** como obrigação possível
cuja existência depende de evento futuro fora do controle da entidade, ou obrigação presente não reconhecida
por improvável ou por não mensurável. Risco que se repete com sazonalidade conhecida (seca, dengue) deixa de
ser risco e vai para o planejamento da LDO e da LOA. O manual organiza as obrigações numa matriz de duas
entradas: **diretas** (certas) × **contingentes** (dependem de evento) e **explícitas** (lei ou contrato) ×
**implícitas** (expectativa do público, pressão política).

**Fonte.** LRF, arts. 4º, § 3º, e 5º, III; STN, MDF 15ª ed., Parte I, PDF pp. 58-60 (conceitos e Tabela 1, matriz
para a União).

**Precatórios.** Precatório não pago no exercício em que foi incluído no orçamento integra a dívida consolidada
para fins de limite (LRF, art. 30, § 7º). No RREO, a variação do saldo de precatórios na dívida consolidada é um
dos ajustes metodológicos do nominal abaixo da linha (MDF, PDF p. 266). O ADCT, art. 107-A (EC 114/2021, redação
da EC 126/2022), fixou limite anual para alocação de precatórios até 2026. O texto compilado em disco traz, no
art. 165 da CF, §§ 18 a 21 incluídos pela EC 136/2025: precatórios e RPV saem do limite individualizado do
Executivo a partir de 2026 e passam a ser incorporados gradualmente à meta de primário a partir de 2027, no
mínimo 10% ao ano, de forma cumulativa. **Conferir no Planalto** a localização desses parágrafos antes de citar.

**Exemplo.** Garantia da União a um empréstimo de estado (passivo contingente explícito). Se o estado não paga
e a União honra 50, há despesa no momento do pagamento. Uma dívida antiga reconhecida por lei (esqueleto) de
50 entra na DLSP como ajuste patrimonial, sem passar pelo primário do mês.

**Pegadinhas.**
- Um curso de 2026 explica a queda da DBGG/PIB entre 2020 e 2023 por efeito denominador (inflação alta
  inflando o PIB nominal), pelo teto de precatórios (que adiou despesa) e pelo pagamento posterior fora das
  regras fiscais. Vale como ilustração de risco fiscal empurrado no tempo; os detalhes jurídicos da decisão de
  2023 estão **fora do material em disco — conferir**.

### 2.13 Regras fiscais

**LRF (LC 101/2000).**
- Anexo de Metas Fiscais com metas de receita, despesa, primário, nominal e dívida para o exercício e os **dois**
  seguintes (art. 4º, § 1º). Para a **União**, depois da LC 200, metas de primário para o exercício e os **três**
  seguintes, marco fiscal de médio prazo, efeito em 10 anos sobre a trajetória da DBGG/PIB e banda de
  tolerância de ±0,25 p.p. do PIB (art. 4º, § 5º).
- Limitação de empenho em 30 dias se, no bimestre, a receita não comportar as metas (art. 9º).
- Definições do art. 29: dívida consolidada (obrigações com amortização em prazo superior a 12 meses),
  mobiliária, operação de crédito, concessão de garantia, refinanciamento. Equipara-se a operação de crédito a
  assunção, reconhecimento ou confissão de dívida (§ 1º).
- Limites de dívida consolidada propostos ao Senado (art. 30); recondução em três quadrimestres, cortando ao
  menos 25% do excesso no primeiro (art. 31).
- Receita de alienação de bens não financia despesa corrente, salvo previdência (art. 44).

**Regra de ouro.** A CF veda operações de crédito acima das despesas de capital, ressalvadas as autorizadas por
créditos suplementares ou especiais com finalidade precisa aprovados por maioria absoluta (art. 167, III). A
LRF repete o comando na fase de elaboração do orçamento (art. 12, § 2º).

**Teto de gastos (EC 95/2016).** Limitou por 20 exercícios a despesa primária de cada Poder ao limite do ano
anterior corrigido pelo IPCA (ADCT, arts. 106 a 114). Os arts. 106 a 112 já não constam do texto compilado em
disco; a EC 126/2022 determinou a lei complementar do novo regime (art. 6º), e a LC 200/2023 é essa lei.
**Conferir** o dispositivo exato de revogação (EC 126/2022, art. 9º) antes de citar.

**Regime Fiscal Sustentável (LC 200/2023).**
- Meta de primário do governo central na LDO, compatível com a estabilização da DBGG/PIB (art. 2º).
- Limite de despesa primária por Poder e órgão, corrigido pelo IPCA de 12 meses até junho do ano anterior
  (art. 4º) mais um crescimento real igual a **70%** do crescimento real da receita primária, se a meta do ano
  anterior foi cumprida, ou **50%**, se não foi, com piso de **0,6%** e teto de **2,5%** ao ano (art. 5º).
  A receita de referência exclui concessões, dividendos, exploração de recursos naturais, receitas
  extraordinárias de programas de recuperação fiscal e repartições (art. 5º, § 2º).
- Meta cumprida se o primário apurado pelo BCB ficar acima do limite inferior da banda (art. 5º, § 3º).
- Descumprimento: vedações do art. 167-A da CF, parciais no primeiro ano e totais no segundo consecutivo
  (art. 6º). Desde a LC 211/2024, déficit primário veda novos benefícios tributários e limita a expansão de
  pessoal até haver superávit (art. 6º-A).
- Não há infração à LRF se o gestor contingenciou e respeitou as vedações; mínimo de 75% das discricionárias
  preservado (art. 7º).
- Despesa obrigatória acima de 95% da primária total aciona as vedações (art. 8º).
- Excesso de primário acima da banda: até 70% do excedente pode ir a investimentos, limitado a 0,25 p.p. do PIB
  (art. 9º). Investimento mínimo de 0,6% do PIB na LOA (art. 10).

**Fonte.** LRF (`0_ACERVO\LEIS\BR\LRF.md`, texto do Planalto); LC 200/2023 (Planalto, 27/09/2026); CF,
arts. 164, 165 e 167; ADCT, arts. 107-A e 113.

**Exemplo (LC 200, art. 5º).** Receita primária ajustada cresceu 3% reais; meta cumprida → despesa pode crescer
0,7 × 3% = 2,1% reais. Se a receita crescesse 5%, os 3,5% esbarrariam no teto de 2,5%. Se a receita caísse,
valeria o piso de 0,6%.

**Pegadinhas.**
- "O arcabouço limita o crescimento real da despesa a 2,5%" (frase de curso) é incompleta: 2,5% é teto da
  banda; a regra é 70% ou 50% da receita, com piso de 0,6%.
- Um card de material afirma que é erro dizer que a regra de ouro está na LRF. A regra está na CF, mas a LRF a
  repete para o projeto de LOA (art. 12, § 2º). O item certo depende de como a banca formula.
- Metas gerais (LRF): exercício + 2. Metas de primário da União (LC 200): exercício + 3.
- DLSP não é a âncora da LC 200; a âncora é a DBGG.

### 2.14 Sustentabilidade da dívida

**Definição.** A **restrição orçamentária intertemporal** exige que o valor presente esperado dos superávits
primários futuros seja igual ao estoque atual da dívida: o governo não pode pagar indefinidamente dívida velha
com dívida nova. Em proporção do PIB, com $d$ = dívida/PIB, $r$ = juro real, $g$ = crescimento real e $s$ =
primário/PIB:

$$d_t = \frac{1+r}{1+g}\,d_{t-1} - s_t \qquad s^{*} = \frac{r-g}{1+g}\,d \approx (r-g)\,d$$

Se $r > g$, a razão cresce sozinha e só um fluxo contínuo de superávits a segura. Exigem primário maior: dívida
mais alta, juro real mais alto, crescimento mais baixo. O BCB usa a razão dívida/PIB como parâmetro de solvência
e comparação internacional, com PIB corrente acumulado em 12 meses e estimativa mensal própria.

**Fonte.** BCB, *Manual*, p. 36; LC 200, art. 1º, § 2º (sustentabilidade intertemporal como objetivo) e art.
2º, § 1º; espelho oficial da discursiva FCC/SEFAZ-CE 2026, estudo de caso 1 (restrição intertemporal e
condição $r > g$).

**Exemplo.** $d$ = 0,78, $r$ = 6%, $g$ = 2%: $s^{*}$ = 0,04/1,02 × 0,78 ≈ 3,1% do PIB. Com primário zero, a
razão vai a 0,78 × 1,06/1,02 ≈ 0,81 no ano seguinte. Um curso cita estimativa da IFI de primário estabilizador
de 2,1% do PIB para o Brasil; o número depende das hipóteses e deve ser conferido no Relatório de
Acompanhamento Fiscal da IFI.

**Pegadinhas.**
- Crescimento menor pede superávit maior (Cebraspe 2015, TCU, C).
- Superávits recorrentes não asseguram sustentabilidade (Cebraspe 2016, TCE-PA, C): se os juros superam o
  superávit, a dívida cresce.
- Quanto mais endividado, maior o primário requerido (Cebraspe 2018, EBSERH, C).
- "A DLSP caiu porque desconsidera os juros" — o que caiu foi a razão, com o PIB crescendo (Cebraspe 2018,
  EBSERH, E).
- "Orçamento equilibrado impede déficit no fim do ano" — errado (Cebraspe 2014, TJ-SE, E).
- Venda de ativo não resolve sustentabilidade: reduz o estoque uma vez, mas a trajetória depende do fluxo.

### 2.15 Interfaces com a política monetária

- **Compromissadas e Conta Única.** Quando o caixa do Tesouro no BC sobe, o BC retira liquidez do mercado
  com menos títulos devolvidos — as compromissadas caem; quando o Tesouro gasta, a liquidez volta e as
  compromissadas sobem. Por isso o manual mostra cessões de crédito da União **reduzindo a DBGG** no ato do
  recolhimento à Conta Única e **aumentando-a** quando o recurso sai para gasto primário (*Manual*, pp. 29-30).
  O mesmo mecanismo vale, por analogia, para o caixa de uma privatização federal (inferência a partir do manual).
- **Compromissadas como instrumento.** A operação compromissada é venda (ou compra) de título com compromisso
  de recompra (ou revenda); quando o BC vende com recompra, enxuga liquidez e o passivo conta na DBGG (FCC 2020,
  ALAP, registrado no material). No agregado monetário, as compromissadas lastreadas em títulos públicos e
  privados entram no M3 (BCB, Nota Técnica 48, nov/2018, conforme errata V2 do material).
- **Base monetária na DLSP.** A base é passivo do BC e entra na DLSP (M). Senhoriagem troca dívida que paga
  juros por moeda.
- **Selic e dívida.** Quase metade da DPF indexada à Selic (dado de curso a conferir no RMD) faz cada alta de
  juros encarecer imediatamente o estoque — a conta de juros nominais da NFSP sobe sem mexer no primário. É o
  canal da chamada dominância fiscal.
- **Resultado do BC.** Na metodologia do BCB, a transferência do resultado do BC ao Tesouro não afeta o
  resultado fiscal, porque o BC está dentro do setor público. A convergência plena ao GFSM 2014 poria o BC entre
  as corporações financeiras e faria essa transferência afetar o primário do governo geral (*Manual*, p. 47).
- **Autonomia (LC 179/2021).** Objetivo fundamental: estabilidade de preços; o CMN fixa as metas, o BC conduz
  a política para cumpri-las.
- **Depósitos voluntários remunerados** como alternativa às compromissadas: **fora do material em disco**.

---

## 3. Padrões de erro documentados

### 3.1 Resultado nominal × NFSP com receita de privatização

**O caso.** Discursiva FCC, SEFAZ-CE 2026, estudo de caso 1 (dados parafraseados): receita tributária 1.200;
pessoal e custeio 700; investimento 300; transferências assistenciais 150; juros nominais 120; e a dívida
líquida "impactada" por 40 de receitas de privatização. Pedia-se primário e nominal (NFSP), a restrição
intertemporal e a sustentabilidade com $r > g$.

**O erro registrado.** Primário e nominal saíram certos (+50 e −70), mas a resposta seguiu: "para obter a NFSP,
o déficit de 70 deve ser ajustado pelas privatizações: NFSP = 70 − 40 = 30". O mesmo tropeço já tinha
aparecido numa questão objetiva do mesmo concurso (Q75, texto não guardado em disco).

**Por que está errado — critério abaixo da linha do BCB.**

1. *O que a NFSP mede.* O resultado nominal é a variação da DLSP **descontados os ajustes patrimoniais e
   metodológicos** (*Manual*, p. 33). O desconto existe para isolar o esforço fiscal do período.
2. *O que a privatização faz com a DLSP.* O governo troca uma participação acionária, que **não entra** na DLSP
   (ativo real não abate, *Manual*, p. 12), por caixa, que **entra** como ativo financeiro. A DLSP cai 40 sem que
   nenhuma receita ou despesa não financeira do período tenha mudado. Se a NFSP fosse a variação bruta da
   dívida, a venda apareceria como "superávit".
3. *O que o BCB faz.* Registra um **ajuste de privatização** nos fluxos, que neutraliza o efeito: o valor
   depositado é abatido para que o Estado não obtenha melhora nos resultados nominal e primário. A receita de
   privatização diminui a dívida líquida, mas não altera os resultados fiscais (*Manual*, p. 38, em paráfrase
   fiel).
4. *Na identidade.* $\Delta \text{DLSP} = \text{NFSP}_{\text{nominal}} + \text{ajustes}$. Com os números do caso:
   NFSP nominal = 120 − 50 = **70 de déficit**; ajuste de privatização = −40; **ΔDLSP = 70 − 40 = +30**. O número
   30 existe, mas é a variação do **estoque**, não o **fluxo** NFSP. O erro foi chamar de NFSP a variação da
   dívida.
5. *Do lado do financiamento.* A NFSP é a necessidade (70); a privatização é uma das fontes que a cobre
   ("redução de ativos" na restrição orçamentária, *Manual*, p. 32). Os 70 foram financiados por 40 de venda
   de ativo e 30 de dívida nova. Abater a fonte de financiamento da própria necessidade confunde as duas
   colunas da restrição.

**Pelo critério acima da linha (STN).** A receita de privatização é receita de capital (alienação de bens),
mas não é receita primária: as receitas primárias excluem as de natureza financeira e as de alienação de
investimentos (MDF, PDF p. 267). No RREO, a "receita de alienação de investimentos permanentes" aparece entre
os ajustes metodológicos do nominal abaixo da linha (MDF, PDF p. 266). Primário e nominal ficam iguais pelos
dois critérios.

**O que acontece com a dívida.** A DLSP cai 40 de uma vez, e a DFL não se mexe. Na DBGG federal, o caixa que
entra na Conta Única tende a reduzir as compromissadas enquanto não é gasto (mecanismo descrito no *Manual*,
pp. 29-30, para cessões de crédito). Para a sustentabilidade, a razão dívida/PIB baixa um degrau e o primário
estabilizador $(r-g)\,d$ diminui um pouco, mas a trajetória continua dada pelo fluxo de primários. A venda é
finita e não recorrente.

**Regra de bolso para a prova.** A operação mexe na DLSP? Se sim, é esforço fiscal do período (receita ou
despesa não financeira, ou juro)? Se não, é ajuste e fica fora da NFSP.

### 3.2 Inconsistências do glossário fiscal do BCB

- **Versão anterior (anotada pelo autor do material em 10/08/2026):** o glossário definia a DFL como DLSP menos
  ajustes patrimoniais **e** metodológicos e a NFSP nominal como a variação mensal da DFL, enquanto o verbete
  "resultado nominal" descontava **só** os ajustes metodológicos. Lido ao pé da letra, o verbete deixaria a
  privatização dentro do resultado nominal, contra o próprio glossário e contra o manual (p. 38).
- **Versão de 27/09/2026:** o verbete "resultado nominal" e a definição de DFL sumiram, mas a NFSP nominal
  continua "calculada a partir da variação mensal da DFL", que o documento não define. O verbete "ajuste
  patrimonial" inclui, como terceiro item, o ajuste metodológico da dívida externa por conversão cambial,
  enquanto o manual separa ajustes **patrimoniais** de **metodológicos** (pp. 33 e 37). O documento não tem data
  nem número de versão, e foi editado sem aviso entre as duas consultas.
- **Primário no glossário × no manual:** o glossário diz que o primário é o nominal "excluídas" as despesas de
  juros sobre a DLSP e "incluídas" as receitas de juros das reservas internacionais. A redação admite a leitura
  de que os juros das reservas ficam no primário, o que destoa da fórmula do manual, $P = RN - JN$, com juros
  nominais líquidos sobre toda a dívida (p. 33). O material registra que a FGV já cobrou essa nuance.

**Recomendação para o site:** citar sempre o PDF datado e preferir o manual ao glossário quando divergirem.

### 3.3 O espelho da banca contra o manual

O espelho oficial do mesmo estudo de caso calcula a NFSP corretamente (−70) no item "a", mas no item "c" afirma
que as privatizações, como ajuste patrimonial, "reduzem a NFSP no curto prazo". Pelo manual do BCB (p. 38), a
privatização reduz a dívida líquida e **não** a NFSP. O resto do item "c" está certo: receita não recorrente, a
sustentabilidade vem do fluxo de superávits. Lição: espelho de banca também erra, e o recurso se apoia na fonte
primária.

### 3.4 Erros de material de curso conferidos na fonte

Registrados no arquivo de erratas do material (código · erro · fonte que corrige):

| Código | O material de curso diz | A fonte primária diz |
|---|---|---|
| E1 | correção monetária da dívida = "imposto inflacionário" | atualização monetária é componente do juro nominal (*Manual*, pp. 14 e 33) |
| E2 | privatizações estão entre os ativos excluídos da DLSP | privatização é ajuste nos fluxos (*Manual*, pp. 37-38) |
| L1 | só a Petrobras fica fora do setor público | Petrobras e Eletrobras (*Manual*, p. 8) |
| V1 | DBGG inclui débitos junto ao BC | do BC entram só as compromissadas (*Manual*, p. 24) |
| V2 | M2 com depósitos especiais; M4 com "títulos de alta liquidez" | NT 48/2018 reformulou M1–M4 (cooperativas no M1, compromissadas com lastro público e privado no M3, títulos federais definitivos no M4) |

Outros, achados em esquemas de curso transcritos no material: "nominal = operacional + inflação" (2.5); sinal
trocado na fórmula NFSP × ΔDLSP (2.9); abaixo da linha "para a União" (2.6); regime de caixa atribuído ao
acima da linha e competência ao abaixo da linha (2.7); "arcabouço limita a despesa a 2,5%" (2.13).

### 3.5 Pares que a banca troca

- fluxo (déficit, NFSP) × estoque (dívida)
- juros nominais × juros reais
- primário × nominal ao avaliar efeito da Selic
- DLSP (líquida, consolidado) × DBGG (bruta, governo geral) × DPF (federal, em mercado) × dívida consolidada
  (LRF, jurídica)
- BCB abaixo da linha × STN acima da linha
- caixa (receitas e despesas) × competência (juros)
- ajuste patrimonial (muda estoque) × resultado (muda fluxo)
- regra de ouro (CF, e repetida na LRF) × teto (EC 95, revogado) × Regime Fiscal Sustentável (LC 200)

---

## 4. Figuras e quadros de fonte oficial para reproduzir com atribuição

Conferir os termos de uso de cada portal antes de publicar. Páginas dos documentos do BCB e da STN conferidas
nos PDFs de 27/09/2026; os demais itens não estão em disco e têm a página marcada "a conferir".

| # | Figura ou quadro | Documento | Página | Link |
|---|---|---|---|---|
| 1 | Fórmula da DLSP e sua diferencial | BCB, *Manual de Estatísticas Fiscais*, maio/2019 | pp. 12-13 | bcb.gov.br/content/estatisticas/notas_metodologicas/estatisticas-fiscais/estatisticasfiscais.pdf |
| 2 | Restrição orçamentária do setor público (fontes M, B, I, F, A, R) | idem | p. 32 | idem |
| 3 | Resultado nominal = ΔDLSP − ajustes; P = RN − JN; juros e correção monetária | idem | pp. 33-34 | idem |
| 4 | Estrutura da DBGG (itens a–e) | idem | p. 24 | idem |
| 5 | Impactos da securitização sobre DLSP, DBGG e NFSP | idem | pp. 27-31 | idem |
| 6 | Conciliação estoque–fluxo e quadro "DLSP — fatores condicionantes" (colunas primário, juros, ajustes metodológicos, paridade, caixa × competência, reconhecimento de dívidas, privatizações) | idem | pp. 39-40 | idem |
| 7 | Quadro de indicadores do GFSM 2014: PLTGG, PFLGG, DLGG/DBGG BCB × estendida | idem | p. 48 | idem |
| 8 | Glossário fiscal (DLSP, ajuste patrimonial, NFSP nominal e primária) | BCB, glossário das estatísticas fiscais | p. 1 | bcb.gov.br/content/estatisticas/Documents/Estatisticas_mensais/Fiscal/glossariofiscal.pdf |
| 9 | Tabelas mensais de DLSP, DBGG, NFSP e fatores condicionantes | BCB, Nota de Estatísticas Fiscais (mensal) | a conferir | bcb.gov.br/estatisticas/estatisticasfiscais |
| 10 | Matriz de obrigações fiscais (diretas × contingentes; explícitas × implícitas), União | STN, *Manual de Demonstrativos Fiscais*, 15ª ed. | PDF pp. 59-60 (Tabela 1) | tesouro.gov.br — publicação do MDF 15ª ed. (Portaria STN 2.057) |
| 11 | Demonstrativo de Riscos Fiscais e Providências (modelo) | idem, Parte I | a partir do PDF p. 62 | idem |
| 12 | Demonstrativo dos Resultados Primário e Nominal, acima e abaixo da linha (RREO, Anexo 6) | idem, Parte III | PDF pp. 265-268 e tabela seguinte | idem |
| 13 | Demonstrativo das receitas de operações de crédito e despesas de capital (regra de ouro) | idem | PDF ≈ pp. 373-375 | idem |
| 14 | Gráficos de composição da DPF por indexador, prazo médio e detentores | STN, *Relatório Mensal da Dívida* (RMD) | a conferir | tesourotransparente.gov.br/publicacoes/relatorio-mensal-da-divida-rmd |
| 15 | Bandas e metas de composição da DPF | STN, *Plano Anual de Financiamento* (PAF) | a conferir | tesourotransparente.gov.br/publicacoes/plano-anual-de-financiamento-paf |
| 16 | Resultado primário do governo central acima da linha e discrepância com o BCB | STN, *Resultado do Tesouro Nacional* (RTN) | a conferir | tesourotransparente.gov.br/publicacoes/boletim-resultado-do-tesouro-nacional-rtn |
| 17 | Projeções de DBGG e primário estabilizador | Senado, IFI, *Relatório de Acompanhamento Fiscal* | a conferir | www12.senado.leg.br/ifi/publicacoes-ifi |
| 18 | Conta das administrações públicas no SCN | IBGE, Notas metodológicas do SCN ref. 2010, nota 12 (Governo) | a conferir | ftp.ibge.gov.br/Contas_Nacionais/Sistema_de_Contas_Nacionais/Notas_Metodologicas_2010/12_governo.pdf |
| 19 | Quadro integrado de estoques e fluxos do GFS | FMI, *Government Finance Statistics Manual 2014* | capítulo 4, a conferir | imf.org/external/Pubs/FT/GFS/Manual/2014/gfsfinal.pdf |

**Esquemas de curso que valem redesenho do zero** (não reproduzir o original; a estrutura abaixo é descrição):

- **Escada dos três resultados.** Três degraus empilhados: primário na base; acima, juros reais formam o
  operacional; acima, a atualização monetária completa o nominal. Ao lado, um atalho direto do primário ao
  nominal rotulado "juros nominais = juros reais + atualização monetária". Corrigir o rótulo que alguns cursos
  usam ("+ inflação").
- **Fluxo de conversões de ida e volta.** Uma linha com setas da esquerda para a direita (primário → operacional
  → nominal, somando componentes) e outra da direita para a esquerda, subtraindo.
- **Quadro de duas colunas DLSP × DBGG.** Linhas: abrangência; BC; estatais; ativos deduzidos ou não;
  compromissadas; âncora da LC 200. Destacar a exceção das compromissadas.
- **Organograma do setor público.** Raiz "setor público" com dois ramos: governo geral (União, estados,
  municípios, previdência) e atividades empresariais (não financeiras, exceto Petrobras e Eletrobras;
  financeiras, com o BC dentro e as demais fora).
- **Quadro acima × abaixo da linha.** Quem apura, base (fluxo × estoque), o que revela, vantagem (detalhe ×
  precisão), desvantagem.
- **Árvore de decisão "a operação entra na NFSP?"** Muda a DLSP? → é esforço fiscal do período? → primário ou
  juros; senão, ajuste (privatização, esqueleto, câmbio). Esta árvore é do próprio material de estudo e pode
  ser usada como está.

---

## 5. Origem do material

Material de estudo próprio do autor (especificações de flashcards, arquivo de erratas, transcrição de prova
discursiva e de espelho publicados pela banca) e documentos oficiais: BCB, *Manual de Estatísticas Fiscais*
(maio/2019) e glossário fiscal; STN, *Manual de Demonstrativos Fiscais*, 15ª ed.; LC 101/2000, LC 200/2023 e
CF/1988 (Planalto). Material de cursinho privado serviu só de roteiro; nenhum trecho, figura ou tabela dele
foi reproduzido.

**Não encontrado no material:** GFSM 2014 e RTN; Resolução do Senado 40/2001; livro-texto de finanças
públicas. Os itens 11.x do `PLANO.md` devem buscar esses documentos na fonte.

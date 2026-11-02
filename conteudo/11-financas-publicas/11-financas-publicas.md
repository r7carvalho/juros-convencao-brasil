---
id: 11
titulo: Finanças públicas: os conceitos
pai: 0
ordem: 9
resumo: Mapa dos conceitos fiscais que o painel usa e de como eles se ligam: dívida é estoque, resultado é fluxo, e a variação da dívida líquida é o déficit nominal mais os ajustes que não são esforço fiscal. Um município de brinquedo mostra primário e nominal, caixa e competência, bruto e líquido; os números de 2026 (dívida bruta de 82,9% do PIB e líquida de 70,0% em setembro; juros de 8,99% e déficit primário de 0,52% em 12 meses) mostram que quase todo o déficit nominal brasileiro é juro. O ramo diz qual dívida e qual juro pesam para a tese da convenção e para a da dominância fiscal, e apresenta as oito páginas que detalham cada conceito.
estado: revisada
---

O debate sobre juros cita números fiscais que parecem brigar entre si. A dívida é de 70% do PIB ou de 95%? O déficit é de meio ponto do PIB ou de quase dez? Todos podem estar certos ao mesmo tempo, porque medem coisas diferentes: estoque ou fluxo, governo geral ou setor público inteiro, dívida antes ou depois de descontar ativos, resultado com ou sem juros.

O ramo define esses conceitos pelas fontes que os criaram, sobretudo o *Manual de Estatísticas Fiscais* do Banco Central (maio de 2019).

## Um município de brinquedo

Estoque é o que existe numa data, como o saldo da dívida em 31 de dezembro; fluxo é o que acontece num período, como a receita e o juro do ano. Numa caixa d'água, o nível é estoque e a vazão da torneira é fluxo.

:::exemplo Um ano das contas de um município
No início do ano, o município deve 1.000 a um banco, a juro de 10% ao ano, e tem 200 em caixa. A inflação do ano é de 4%.

Durante o ano, recebe 900 de tributos e transferências. Contrata e recebe serviços no valor de 880, mas paga só 850; os outros 30 ficam para janeiro, como restos a pagar. O empréstimo gera 100 de juros (10% de 1.000), dos quais o município paga 60 em dinheiro; os 40 restantes se somam ao saldo devedor.

| Estoques | Início do ano | Fim do ano |
|---|---|---|
| Dívida bruta (empréstimo) | 1.000 | 1.040 |
| Caixa | 200 | 190 |
| Dívida líquida (bruta menos caixa) | 800 | 850 |

| Fluxos do ano | Conta | Valor |
|---|---|---|
| Resultado primário (régua de caixa) | 900 − 850 | superávit de 50 |
| Juros nominais (por competência) | 10% × 1.000 | 100 |
| Resultado nominal | 50 − 100 | déficit de 50 |
| Atualização monetária da dívida | 4% × 1.000 | 40 |
| Juros reais | 100 − 40 | 60 |
| Resultado operacional | 50 − 60 | déficit de 10 |
:::

O primário compara receitas e despesas não financeiras, o esforço fiscal que o governo controla; o nominal soma os juros. O município teve superávit primário de 50 e déficit nominal de 50. Entre os dois fica o operacional, que conta só o juro real e foi publicado até 2009 (BCB, *Manual*, pp. 13-14 e 33-34).

Pela competência, o município teria gasto 880 e o primário seria de 20; nas estatísticas do Banco Central, receitas e despesas entram quando o dinheiro se move, e os 30 de restos a pagar ficam para janeiro. Os juros seguem a regra oposta: entram por competência, mês a mês, pelos 100 que a dívida acumulou, e não pelos 60 pagos (BCB, *Manual*, pp. 13-15). Esse é um dos motivos pelos quais os juros "pagos" pela União no orçamento e os juros "apropriados" pelo Banco Central dão números muito diferentes; os outros são a abrangência e o desconto dos juros recebidos ([11.2](pagina:11.2)).

A dívida bruta subiu 40 e a líquida 50, porque o município também gastou 10 do caixa: a variação da dívida líquida é o déficit nominal. Os 30 devidos aos fornecedores não aparecem em nenhuma das duas, porque a dívida do Banco Central deixa de fora as contas a pagar que o manual do FMI inclui (BCB, *Manual*, pp. 45-48; [11.8](pagina:11.8)).

Falta o ajuste patrimonial. Suponha que, no último dia do ano, o município venda por 30 as ações da empresa municipal de ônibus. O caixa vai a 220 e a dívida líquida termina em 820 sem esforço fiscal nenhum, porque participação acionária não abate a dívida líquida e o dinheiro abate (BCB, *Manual*, p. 12). O Banco Central registra os 30 como ajuste de privatização, e o resultado nominal continua sendo um déficit de 50 (*Manual*, p. 38).

## O mapa dos conceitos

A ligação entre estoque e fluxo está no *Manual* (p. 39):

$$\Delta \text{DLSP} = \text{NFSP}_{\text{primária}} + \text{juros nominais} + \text{ajustes}$$

A NFSP (necessidade de financiamento do setor público) é o resultado com o sinal trocado: positiva é déficit. No município, com a venda das ações: NFSP primária de $-50$ (superávit), juros de 100 e ajuste de $-30$ somam $-50 + 100 - 30 = 20$, a alta da dívida líquida de 800 para 820. A Dívida Fiscal Líquida (DFL) é a DLSP sem os ajustes patrimoniais e metodológicos acumulados, de modo que sua variação é a NFSP nominal (BCB, *Manual*, pp. 33 e 37-40; o glossário fiscal vigente cita a DFL sem defini-la, ver [11.4](pagina:11.4)); no exemplo, a DFL sobe 50.

| Tipo | Conceito | O que mede | Série |
|---|---|---|---|
| Abrangência | Setor público consolidado | governo geral, BC e estatais não financeiras (sem Petrobras e Eletrobras) | |
| Abrangência | Governo geral | União, estados, municípios e previdência | |
| Estoque | DBGG, conceito BCB | dívida do governo geral sem descontar ativos, com as compromissadas do BC | SGS 13762 |
| Estoque | DBGG, conceito FMI | idem, com todos os títulos do Tesouro na carteira do BC e sem as compromissadas | BCB, Divggnp |
| Estoque | DLSP | passivos menos ativos financeiros do setor público consolidado | SGS 4513 |
| Estoque | DFL | DLSP sem os ajustes acumulados | BCB |
| Estoque | DPF e DPMFi | dívida do Tesouro em mercado | Tesouro, RMD |
| Fluxo | NFSP primária | receitas menos despesas não financeiras | SGS 5793 |
| Fluxo | NFSP nominal | primário mais juros nominais | SGS 5727 |
| Fluxo | NFSP operacional | primário mais juros reais | BCB, até 2009 |
| Critério | Abaixo e acima da linha | resultado pela variação da dívida (BCB) ou rubrica por rubrica (Tesouro, RTN) | |
| Ponte | Ajustes | câmbio, privatização, reconhecimento de dívidas: mudam a dívida sem ser resultado | |

Fonte: BCB, *Manual*, pp. 8-15, 24-25 e 33-40; quadro do painel.

## Os números de 2026

Em agosto de 2026, a dívida bruta do governo geral estava em 82,87% do PIB, 94,5% no conceito do FMI, e a dívida líquida do setor público em 69,27% (BCB, SGS 13762 e 4513, coleta de 02/11/2026; tabela especial Divggnp, consulta em 28/10/2026). A distância de 13,6 pontos entre bruta e líquida vem sobretudo das reservas internacionais, que valiam 14,5% do PIB no mesmo mês ([11.1](pagina:11.1)). Em setembro, 82,93% e 69,98%.

```grafico
dados/3-divida-conceitos.json
```

No fluxo, a NFSP nominal dos 12 meses até setembro foi de 9,51% do PIB, com déficit primário de 0,52%. A diferença, 8,99% do PIB ou R$ 1.204,8 bilhões, são os juros nominais apropriados (BCB, SGS 5727, 5793 e 4382, coleta de 02/11/2026). De 2002 a 2013 o setor público teve superávit primário todos os anos e déficit nominal mesmo assim, porque os juros ficaram sempre entre 4,4% e 8,4% do PIB.

```grafico
dados/11-primario-juros-nominal.json
```

## Qual dívida e qual juro importam para o painel

Cada tese que o painel testa olha para um termo diferente da mesma identidade. A tese da convenção pergunta quanto custa o juro que a convenção sustenta e para quem ele vai. O conceito certo é o fluxo de juros apropriados, separado em juro real e reposição de inflação. O estoque que importa é aquele sobre o qual a Selic incide sem defasagem: a LFT, 52,74% da DPF em agosto de 2026 (Tesouro, RMD), e as compromissadas, que estão na DBGG e pagam a taxa básica ([10.2.2](pagina:10.2.2)). A Selic entra no resultado pela linha de juros, nunca pelo primário.

A tese da dominância fiscal pergunta se a dívida cresce a ponto de o credor exigir prêmio e de uma alta do juro piorar a inflação em vez de melhorá-la ([1.5.2](pagina:1.5.2), [6.1](pagina:6.1)). Aqui pesam a DBGG, âncora do Regime Fiscal Sustentável (LC 200/2023, art. 2º, § 1º); o primário, que o governo controla; e a distância entre o juro implícito da dívida e o crescimento ([3.1](pagina:3.1)). A DLSP entra pelo câmbio: em 2002, elo do mecanismo de Blanchard (2004), a depreciação aumentava a dívida; hoje o setor público tem mais ativos do que dívidas em moeda estrangeira, e a depreciação reduz a DLSP ([11.1](pagina:11.1)).

:::painel
O painel lê a identidade como neutra entre as duas teses: ela diz quanto da alta da dívida veio de juro e quanto de déficit, e não diz por que o juro está onde está ([3.2](pagina:3.2)). Chamar de "rombo" o déficit nominal de 9,51% do PIB esconde que 8,99 pontos são juros. Dizer que o problema é só o juro esconde que, com o juro atual, um primário próximo de zero deixa a dívida subindo, e que o superávit que a estabilizaria está longe do observado ([3.1](pagina:3.1)).
:::

## As oito páginas do ramo

[11.1 Dívida bruta e líquida](pagina:11.1) detalha os estoques, concilia a bruta com a líquida e diz qual medida responde a qual pergunta. [11.2 Resultados fiscais](pagina:11.2) trata dos fluxos, da regra de caixa e competência e da divisão do juro entre correção monetária e juro real. [11.3 Acima e abaixo da linha](pagina:11.3) compara o resultado do Tesouro com o do Banco Central, explica a discrepância estatística e por que a meta da LC 200 é verificada pelo Banco Central (art. 5º, § 3º). [11.4 Armadilhas conceituais](pagina:11.4) reúne as confusões mais frequentes.

[11.5 Risco fiscal](pagina:11.5) separa o sentido legal, o Anexo de Riscos Fiscais da LDO (LRF, art. 4º, § 3º), do sentido de mercado, o prêmio na curva de juros. [11.6 Regras fiscais](pagina:11.6) compara desenho e desempenho da LRF, da regra de ouro, do teto de gastos e do Regime Fiscal Sustentável. [11.7 Sustentabilidade](pagina:11.7) parte da restrição intertemporal e de $r - g$, passa pelo teste de Bohn e explica por que não há "limite seguro" único de dívida. [11.8 Estatística fiscal internacional](pagina:11.8) mostra por que comparar a dívida de países exige saber qual conceito cada um publica.

## Para ler

- Banco Central do Brasil. *Manual de Estatísticas Fiscais*. Brasília, maio de 2019. [bcb.gov.br](https://www.bcb.gov.br/content/estatisticas/notas_metodologicas/estatisticas-fiscais/estatisticasfiscais.pdf).
- Tesouro Nacional. Relatório Mensal da Dívida Pública Federal, agosto de 2026. [tesourotransparente.gov.br](https://www.tesourotransparente.gov.br/publicacoes/relatorio-mensal-da-divida-rmd/2026/8).
- Brasil. Lei Complementar nº 101, de 4 de maio de 2000 (Lei de Responsabilidade Fiscal). [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm).
- Brasil. Lei Complementar nº 200, de 30 de agosto de 2023 (Regime Fiscal Sustentável). [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp200.htm).
- Blanchard, O. (2004). Fiscal dominance and inflation targeting: lessons from Brazil. NBER Working Paper 10389. [nber.org/papers/w10389](https://www.nber.org/papers/w10389).

---
id: 11
titulo: Finanças públicas: os conceitos
pai: 0
ordem: 9
resumo: Mapa dos conceitos fiscais que o painel usa e de como eles se ligam: dívida é estoque, resultado é fluxo, e a variação da dívida líquida é o déficit nominal mais os ajustes que não são esforço fiscal. Um município de brinquedo mostra primário e nominal, caixa e competência, bruto e líquido; os números de setembro de 2026 (dívida bruta de 82,9% do PIB, líquida de 70,0%, juros de 8,99% e déficit primário de 0,52% em 12 meses) mostram que quase todo o déficit nominal brasileiro é juro. O ramo diz qual dívida e qual juro pesam para a tese da convenção e para a da dominância fiscal, e apresenta as oito páginas que detalham cada conceito.
estado: 1ª versão
---

O debate sobre juros no Brasil cita números fiscais que parecem brigar entre si. A dívida é de 70% do PIB ou de 95%? O déficit é de meio ponto do PIB ou de quase dez? Todos esses números podem estar certos ao mesmo tempo, porque medem coisas diferentes: um estoque ou um fluxo, o governo geral ou o setor público inteiro, a dívida antes ou depois de descontar os ativos, o resultado com ou sem os juros. Quem troca um pelo outro chega a conclusões opostas a partir dos mesmos dados.

O ramo 11 define esses conceitos pelas fontes que os criaram, sobretudo o *Manual de Estatísticas Fiscais* do Banco Central (maio de 2019) e as leis fiscais, e mostra como um se liga ao outro. Os ramos de [dívida pública](pagina:3) e de [política monetária](pagina:10) já os usam.

## Um município de brinquedo

A distinção de base é entre estoque e fluxo. Estoque é o que existe numa data: o saldo da dívida em 31 de dezembro. Fluxo é o que acontece num período: a receita, a despesa e o juro do ano. Numa caixa d'água, o nível é estoque e a vazão da torneira é fluxo; o nível no fim do dia é o nível do começo mais o que entrou menos o que saiu.

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

O resultado primário compara receitas e despesas não financeiras; é o esforço fiscal que o governo controla. O nominal soma os juros. O município teve, no mesmo ano, superávit primário de 50 e déficit nominal de 50. Entre os dois fica o operacional, que conta só o juro real; o Banco Central publicou essa série até dezembro de 2009 (BCB, *Manual*, pp. 13-14 e 33-34).

Se a despesa fosse contada pela competência, o município teria gasto 880 e o primário seria de 20. Nas estatísticas do Banco Central, receitas e despesas entram quando o dinheiro se move, e por isso o primário é de 50; os 30 de restos a pagar entram no resultado de janeiro. Os juros seguem a regra oposta: entram por competência, mês a mês, pelos 100 que a dívida acumulou, e não pelos 60 pagos (BCB, *Manual*, pp. 13-15). É por isso que os juros "pagos" pela União no orçamento e os juros "apropriados" pelo Banco Central dão números muito diferentes ([Método](pagina:9.1)).

A dívida bruta subiu 40 e a líquida subiu 50, porque o município também gastou 10 do caixa. A variação da dívida líquida é igual ao déficit nominal: um déficit de 50 precisa ser financiado, com dívida nova ou com ativo vendido. Os 30 devidos aos fornecedores não aparecem em nenhuma das duas: a dívida bruta do Banco Central deixa de fora restos a pagar e outras contas a pagar, que o manual do FMI inclui (BCB, *Manual*, pp. 45-48; [11.8](pagina:11.8)).

Falta o ajuste patrimonial. Suponha que, no último dia do ano, o município venda por 30 as ações da empresa municipal de ônibus. O caixa vai a 220 e a dívida líquida termina em 820, 30 abaixo do que seria sem a venda, sem esforço fiscal nenhum: as ações não abatiam a dívida líquida, porque ativo real e participação acionária não entram na conta, e o dinheiro abate (BCB, *Manual*, p. 12). O Banco Central registra os 30 como ajuste de privatização, e o resultado nominal continua sendo um déficit de 50 (*Manual*, p. 38).

## O mapa dos conceitos

A ligação entre estoque e fluxo vale para o setor público inteiro e está no próprio manual do Banco Central (p. 39):

$$\Delta \text{DLSP} = \text{NFSP}_{\text{primária}} + \text{juros nominais} + \text{ajustes}$$

A NFSP (necessidade de financiamento do setor público) é o resultado com o sinal trocado: positiva é déficit. No município, com a venda das ações: NFSP primária de $-50$ (superávit), juros de 100 e ajuste de $-30$ somam $-50 + 100 - 30 = 20$, a alta da dívida líquida de 800 para 820. A Dívida Fiscal Líquida (DFL) é a DLSP sem os ajustes patrimoniais e metodológicos acumulados, de modo que sua variação é a NFSP nominal (BCB, glossário das estatísticas fiscais); no exemplo, a DFL sobe 50.

| Tipo | Conceito | O que mede | Série |
|---|---|---|---|
| Abrangência | Setor público consolidado | União, estados, municípios, previdência, estatais não financeiras (sem Petrobras e Eletrobras) e BC; base da DLSP e da NFSP | |
| Abrangência | Governo geral | União, estados, municípios e previdência, sem BC e estatais; base da DBGG | |
| Estoque | DBGG, conceito BCB | dívida do governo geral sem descontar ativos, com as compromissadas do BC | SGS 13762 |
| Estoque | DBGG, conceito FMI | idem, com todos os títulos do Tesouro na carteira do BC e sem as compromissadas | BCB, Divggnp |
| Estoque | DLSP | passivos menos ativos financeiros do setor público consolidado | SGS 4513 |
| Estoque | DFL | DLSP sem os ajustes acumulados | BCB |
| Estoque | DPF e DPMFi | dívida do Tesouro em mercado; a DPMFi é a parte interna em títulos | Tesouro, RMD |
| Fluxo | NFSP primária | receitas menos despesas não financeiras | SGS 5793 |
| Fluxo | NFSP nominal | primário mais juros nominais | SGS 5727 |
| Fluxo | NFSP operacional | primário mais juros reais | BCB, até 2009 |
| Critério | Abaixo da linha | resultado pela variação da dívida (BCB) | |
| Critério | Acima da linha | resultado rubrica por rubrica, governo central (Tesouro, RTN) | |
| Ponte | Ajustes | câmbio, privatização, reconhecimento de dívidas: mudam a dívida sem ser resultado | |

Fontes: BCB, *Manual de Estatísticas Fiscais*, pp. 8-15, 24-25, 33-40; Tesouro Nacional, Relatório Mensal da Dívida; quadro do painel.

## Os números de 2026

Em setembro de 2026, a dívida bruta do governo geral estava em 82,93% do PIB e a dívida líquida do setor público em 69,98% (BCB, SGS 13762 e 4513, coleta de 02/11/2026). No conceito do FMI, a bruta era de 94,5% em agosto (BCB, tabela especial Divggnp, consulta em 28/10/2026). A distância entre bruta e líquida, de quase 13 pontos, vem sobretudo das reservas internacionais, que valiam 14,5% do PIB em agosto ([3.1](pagina:3.1)).

```grafico
dados/11-dbgg-dlsp.json
```

No fluxo, a NFSP nominal dos 12 meses até setembro foi de 9,51% do PIB, com déficit primário de 0,52%. A diferença, 8,99% do PIB, são os juros nominais apropriados: R$ 1.204,8 bilhões sobre um PIB de 12 meses de R$ 13.402 bilhões (BCB, SGS 5727, 5793 e 4382, coleta de 02/11/2026). De 2002 a 2013 o setor público teve superávit primário todos os anos e déficit nominal mesmo assim, porque os juros ficaram sempre entre 4,4% e 8,4% do PIB.

```grafico
dados/11-primario-juros-nominal.json
```

## Qual dívida e qual juro importam para o painel

Cada tese que o painel testa olha para um termo diferente da mesma identidade.

A tese da convenção pergunta quanto custa o juro que a convenção sustenta e para quem ele vai. O conceito certo é o fluxo de juros nominais apropriados, separado em juro real e reposição de inflação, porque só o juro real é renda líquida do credor. O estoque que importa é aquele sobre o qual a Selic incide sem defasagem: a LFT, 52,74% da DPF em agosto de 2026 (Tesouro, RMD), e as compromissadas, que estão na DBGG e pagam a taxa básica ([10.2.2](pagina:10.2.2)). A Selic entra no resultado pela linha de juros, nunca pelo primário.

A tese da dominância fiscal pergunta se a dívida cresce a ponto de o credor exigir prêmio e de uma alta do juro piorar a inflação em vez de melhorá-la ([1.5.2](pagina:1.5.2), [6.1](pagina:6.1)). Aqui pesam a DBGG, âncora do Regime Fiscal Sustentável (LC 200/2023, art. 2º, § 1º) e medida que agências de risco e o FMI acompanham; o primário, que o governo controla; e a distância entre o juro implícito da dívida e o crescimento ([3.1](pagina:3.1)). A DLSP entra pelo câmbio. No mecanismo de Blanchard (2004), um dos elos era a dívida atrelada ao dólar: em 2002, a depreciação aumentava a dívida em reais. Hoje o setor público tem mais ativos do que dívidas em moeda estrangeira, e a depreciação reduz a DLSP ([3.1](pagina:3.1)).

| Pergunta | Conceito | Número | Onde se discute |
|---|---|---|---|
| Quanto custa o juro? | juros nominais apropriados | 8,99% do PIB, 12 meses até set/2026 | [3.3](pagina:3.3), [11.2](pagina:11.2) |
| Quanto disso é renda real? | juros reais (nominais menos atualização monetária) | cerca de 5,5% do PIB em 2025, estimativa do painel | [3.3](pagina:3.3), [5.4.3](pagina:5.4.3) |
| O governo faz esforço fiscal? | NFSP primária | déficit de 0,52% do PIB, 12 meses até set/2026 | [11.2](pagina:11.2), [3.2](pagina:3.2) |
| Quanto o governo tem de rolar? | DBGG, conceito BCB | 82,93% do PIB, set/2026 | [11.1](pagina:11.1) |
| Como o Brasil se compara? | DBGG, conceito FMI | 94,5% do PIB, ago/2026 | [3.4](pagina:3.4), [11.8](pagina:11.8) |
| Qual a posição patrimonial? | DLSP | 69,98% do PIB, set/2026 | [11.1](pagina:11.1) |
| Quão rápido a Selic chega à dívida? | LFT na DPF e compromissadas | 52,74% da DPF, ago/2026 | [2.4](pagina:2.4), [10.2.2](pagina:10.2.2) |

:::painel
O painel lê a identidade como neutra entre as duas teses: ela diz quanto da alta da dívida veio de juro e quanto de déficit, e não diz por que o juro está onde está ([3.2](pagina:3.2)). Os dois usos errados mais comuns são simétricos. Chamar de "rombo" o déficit nominal de 9,51% do PIB esconde que 8,99 pontos são juros. Dizer que o problema é só o juro esconde que, com o juro atual, um primário próximo de zero deixa a dívida subindo, e que o superávit que a estabilizaria está longe do observado ([3.1](pagina:3.1)).
:::

## As oito páginas do ramo

[11.1 Dívida bruta e líquida](pagina:11.1) detalha os estoques: a DBGG nos conceitos do Banco Central e do FMI, a DLSP com sua fórmula, a DPF e a DPMFi do Tesouro, o lugar das compromissadas e os ativos que a dívida líquida desconta, como reservas e créditos ao BNDES.

[11.2 Resultados fiscais](pagina:11.2) trata dos fluxos: primário, nominal e operacional, a NFSP e o sinal trocado, a regra de caixa para receitas e despesas e de competência para os juros, e a escada que leva do primário ao nominal pelos juros reais e pela atualização monetária.

[11.3 Acima e abaixo da linha](pagina:11.3) compara as duas formas de medir o mesmo resultado. O Tesouro soma receitas e despesas do governo central no Resultado do Tesouro Nacional; o Banco Central mede a variação da dívida do setor público consolidado. Explica a discrepância estatística entre os dois e por que a meta da LC 200 é verificada pelo número do Banco Central (art. 5º, § 3º).

[11.4 Armadilhas conceituais](pagina:11.4) reúne as confusões mais frequentes: abater a receita de privatização do déficit, tratar ajuste patrimonial como resultado, chamar a atualização monetária da dívida de imposto inflacionário, esperar que a desvalorização aumente a dívida líquida de um país credor em dólar. Cada uma se resolve com o manual do Banco Central e um exemplo.

[11.5 Risco fiscal](pagina:11.5) separa dois sentidos da expressão. O legal é o Anexo de Riscos Fiscais da LDO (LRF, art. 4º, § 3º), com passivos contingentes, precatórios e decisões judiciais. O de mercado é o prêmio cobrado na curva de juros e no CDS. Mostra também como um passivo reconhecido vira ajuste na dívida sem passar pelo primário do mês.

[11.6 Regras fiscais](pagina:11.6) percorre a LRF, a regra de ouro (Constituição, art. 167, III), o teto de gastos da EC 95/2016 e o Regime Fiscal Sustentável da LC 200/2023, com a fórmula do limite de despesa e a banda da meta, e compara desenho e desempenho com as regras de outros países.

[11.7 Sustentabilidade](pagina:11.7) parte da restrição intertemporal e da condição $r > g$, passa pelo teste de Bohn e pela análise de sustentabilidade do FMI, e explica por que não existe um "limite seguro" de dívida que valha como número único para todo país e toda época.

[11.8 Estatística fiscal internacional](pagina:11.8) mostra o que o GFSM 2014 mede e o Banco Central ainda não mede (contas a pagar, competência integral, Banco Central fora do governo geral) e por que comparar a dívida de países diferentes exige saber qual conceito cada um publica.

## Para ler

- Banco Central do Brasil. *Manual de Estatísticas Fiscais*. Brasília, maio de 2019. [bcb.gov.br](https://www.bcb.gov.br/content/estatisticas/notas_metodologicas/estatisticas-fiscais/estatisticasfiscais.pdf).
- Banco Central do Brasil. Glossário das estatísticas fiscais. [bcb.gov.br](https://www.bcb.gov.br/content/estatisticas/Documents/Estatisticas_mensais/Fiscal/glossariofiscal.pdf).
- Banco Central do Brasil. Estatísticas Fiscais (nota mensal e tabelas especiais). [bcb.gov.br/estatisticas/estatisticasfiscais](https://www.bcb.gov.br/estatisticas/estatisticasfiscais).
- Secretaria do Tesouro Nacional. *Manual de Demonstrativos Fiscais*, 15ª edição, 1ª versão, 2025 (Portaria STN nº 2.057). Brasília: STN.
- Tesouro Nacional. Relatório Mensal da Dívida Pública Federal, agosto de 2026. [tesourotransparente.gov.br](https://www.tesourotransparente.gov.br/publicacoes/relatorio-mensal-da-divida-rmd/2026/8).
- Brasil. Lei Complementar nº 101, de 4 de maio de 2000 (Lei de Responsabilidade Fiscal). [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm).
- Brasil. Lei Complementar nº 200, de 30 de agosto de 2023 (Regime Fiscal Sustentável). [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp200.htm).
- Fundo Monetário Internacional. *Government Finance Statistics Manual 2014*. Washington, 2014. [imf.org](https://www.imf.org/external/Pubs/FT/GFS/Manual/2014/gfsfinal.pdf).
- Blanchard, O. (2004). Fiscal dominance and inflation targeting: lessons from Brazil. NBER Working Paper 10389. [nber.org/papers/w10389](https://www.nber.org/papers/w10389).

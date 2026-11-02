# Notas da área 2 (Juros no Brasil), primeira rodada, 02/11/2026

## Páginas entregues (palavras do corpo, sem frontmatter; entre parênteses, sem a seção "Para ler")

| Id | Arquivo | Palavras | Gráficos |
|---|---|---|---|
| 2 | 2-juros-no-brasil.md | 1.210 (1.100) | nenhum |
| 2.1 | 2.1-quao-altos.md | 2.970 (2.840) | 2.1-juro-real-1995-2026, 2.1-juro-real-brasil-pares, 2.1-media-por-decada, 2.1-ranking-ex-ante-2026 |
| 2.2 | 2.2-explicacoes-concorrentes.md | 4.310 (3.970) | 2.2-diferencial-e-primario |
| 2.3 | 2.3-juro-neutro-e-meta.md | 3.100 (2.910) | 2.3-estimativas-neutro, 2.3-juro-real-ex-ante-ex-post |
| 2.4 | 2.4-transmissao.md | 2.810 (2.640) | 2.4-credito-direcionado, 2.4-spread, 2.4-lft-na-dpf, 2.4-detentores-dpmfi |
| 2.4.1 | 2.4.1-focus.md (neta nova) | 1.630 (1.500) | nenhum |
| 2.5 | 2.5-convencao-no-brasil.md | 3.950 (3.590) | nenhum (usa tabela de previsões × dados) |

Total: cerca de 20.000 palavras, 11 arquivos de dados em `dados/2.*.json`. `python3 tools/build.py --check` sem erros na área; os únicos avisos são links para páginas ainda não escritas (1, 6, 8, 7.9, 1.5.3, 1.5.4).

Ordem da página macro: `ordem: 2` entre os filhos de 0 (as áreas seguem a numeração).

## Cálculos próprios do painel (reproduzíveis com os insumos)

- Diferencial Brasil − média simples de México, Chile, Colômbia, Índia e África do Sul (painel BIS da Frente K): 6,6 p.p. (2000–2009), 3,1 (2010–2019), 3,5 (2020–ago/2026); 4,5 em 2006–2013; mínimo de −1,6 em 2021; 7,0 em 2026 (jan–ago).
- Correlação anual 2006–2025 entre o diferencial e o resultado primário do governo geral (sinal invertido do fator 3 da tabela de fatores condicionantes, Frente J): +0,39; sem 2020–2021, +0,26. Com a DBGG conceito FMI (Frente J): −0,38. Teste rudimentar, com ressalva de causalidade reversa declarada no texto.
- Juro real ex-post 1995–1999: Selic acumulada no ano de 53,08%, 27,41%, 24,77%, 28,79% e 25,59% (tabelas públicas da Selic mensal, cotejadas em numerando.com.br, meujurisbox e indicadoreseconomicoshoje porque o SGS estava bloqueado) e IPCA de 22,41%, 9,56%, 5,22%, 1,65% e 8,94% (mesmos valores de `dados/9.4-selic-ipca-longo.json`). Resultado: 25,06%, 16,29%, 18,58%, 26,70%, 15,28%. [a conferir no SGS 4390/4189 e SIDRA 1737]
- Juro real ex-ante em 23/10/2026: 1,1375 / 1,0453 − 1 = 8,82% (a Frente K, com Selic efetiva, dá 8,72%).
- Regra de Taylor ilustrativa com IPCA de 4,58%, meta de 3% e hiato de 0,4%: 10,57% com neutro de 5%; 13,57% com neutro de 8%.

## Divergências com os insumos e entre fontes

| Número | Versão A | Versão B | Decisão |
|---|---|---|---|
| Custo dos juros em 12 meses | CONTEXTO.md: cerca de R$ 1,2 tri até set/2026 (~9% do PIB) | Frente K: R$ 1.182 bi (8,86% do PIB) em 12 meses até ago/2026 (SGS 5727 − 5793) | Usado o da Frente K, com mês de referência agosto |
| Detentores da DPMFi, ago/2026 | CONTEXTO.md: bancos 31,8%, previdência 22,5%, fundos 22%, não residentes 10% | Frente K (RMD ago/2026): instituições financeiras 31,22%, previdência 22,63%, fundos 22,52%, não residentes 9,91% | Usado o da Frente K |
| DI jan/2029 depois do 2º turno (26/10/2026) | Frente K (citando Frente B): 15,25% | TMC: jan/2029 a 15,03% e jan/2031 a 15,25%, ambos de 12,64% | Texto usa "de cerca de 12,6% para cerca de 15%" |
| Participantes do Focus | Galípolo, jul/2026: 165 (32 bancos, 72 gestoras, 61 outros) | Cobertura do Focus de 26/10/2026: cerca de 172 | Texto dá os dois, com datas |
| Direcionado 2015 e 2019 | BCB, RI mar/2020: 49,2% e 42,1% | Série SGS da Frente K (dezembro): 49,1% e 42,2% | Diferença de arredondamento/mês; texto cita o RI quando cita o RI |
| Juro real Brasil 2025 | BIS (média anual): 9,09% | Selic acumulada / IPCA dez: 9,66% | Diferença de método, explicada em 2.1 |
| Superávit para estabilizar a dívida (IFI) | Frente J: 2,1% do PIB (RAF 113) | IFI RAF 117 (29/10/2026): 2,1% com neutro de 5%, 2,9% com neutro de 6,1% | Texto usa o RAF 117; área 3 deve atualizar |
| Juro neutro do BC em 2026 | Frente K: BC trabalha com 5,0% | Blog Saggo Investimentos atribui 5,00% ao RPM de jun/2026 | Compatíveis; o RPM não foi aberto nesta sessão |
| Páginas de Bresser-Pereira e Nakano (2002) | REP 22(3), jul.-set./2002, p. 533–563 (uma listagem) | "21(2)" ou "21(3)", p. 146–177 (outras citações) | Citado como 22(3), jul.-set. 2002, sem páginas [a conferir] |

## Recortes citados (origem do texto entre aspas)

Nenhuma fonte primária pôde ser aberta (SciELO, Valor, sites de autores e do BCB bloqueados nesta sessão; só a busca web funcionou). Os trechos entre aspas vêm de reproduções exibidas nos resultados de busca:

- Bresser-Pereira e Nakano (2002), "uma elevação da taxa interna de juros...": reproduzido em "Taxa de juros e prêmio de risco" (*Revista de Economia Contemporânea*, SciELO).
- Bresser-Pereira e Nakano (2002), "A diretriz básica em relação à taxa de juros...": trecho do artigo na REP exibido na busca.
- Bresser-Pereira e Nakano, *Folha*, fev/2002, "equilíbrio perverso da taxa de juros": reproduzido em artigo acadêmico sobre convenções financeiras (atribuído no texto a Seabra e Dequech, 2013) [a conferir a fonte exata da reprodução].
- Erber (2011), dois trechos: exibidos a partir do texto da REP 31(1) no SciELO; página exata [a conferir].
- Lara Resende (2017), "A hipótese neo-fisheriana...": exibido a partir de reprodução do artigo do *Valor* (Jornal GGN / PDF no blog de F. Nogueira da Costa).
- Bresser-Pereira (2024), "Os rentistas e financistas...": exibido a partir da reprodução do IHU Unisinos.
- Campos Neto (2023), "meia-entrada": B3 Bora Investir.
- Segura-Ubiergo (2012), resumo em inglês: IDEAS/RePEc.
- Keynes (1936, cap. 15, p. 203): texto canônico, reproduzido de memória e conferível na edição Macmillan e em marxists.org.

## Pendências [a conferir]

1. Mediana do juro neutro no Questionário Pré-Copom de 2026 (pergunta existe no QPC 275).
2. Teste de viés do Focus: mediana 12 meses à frente × IPCA realizado, 2001–2026 (séries do Sistema de Expectativas do BCB).
3. Expectativa de inflação dos consumidores (Sondagem do Consumidor FGV) em 2025–2026, comparada à mediana Focus no mesmo mês; dados da Firmus.
4. Número exato do CDS de 5 anos em dez/2024 (205 pontos vem de uma única fonte, Guia do Investidor) e o CDS depois de 26/10/2026.
5. Data exata da entrevista de Fábio Kanczuk ao InfoMoney (2026) e do boletim do FGV IBRE (7,5% veio da chamada de notícia de 01/10/2026, não do PDF).
6. Título exato de Oreiro (2002) na REP 22(3); autoria completa do artigo de *Economia e Sociedade* (2018) sobre o primeiro governo Dilma (arquivo "07Nader.pdf" na Unicamp; o texto menciona "Nader (2018)").
7. Ano e número do texto de Erber "Convenções de desenvolvimento no Brasil contemporâneo" (CEPAL; citado como 2008 conforme o pedido).
8. Referência do texto de Persio Arida de 2005 sobre o efeito da dívida indexada (citado pela Frente K, não localizado).
9. Metas de 3% de Chile, México e Colômbia: conhecimento consolidado, não reconferido nos sites dos bancos centrais nesta sessão.
10. Juro real 1995–1999: conferir Selic acumulada no SGS.

## Limites da sessão

O orçamento de buscas web do turno acabou antes de duas buscas planejadas: o boxe do BCB sobre determinantes do prêmio de risco (RPM jun/2025), cuja conclusão (maiores oscilações acompanham as taxas americanas) foi citada a partir do resumo do resultado de busca, e estudos sobre viés sistemático do Focus.

## Sugestões para a próxima rodada

- Um teste melhor que a correlação simples: regressão do diferencial de juro real sobre primário, dívida, inflação passada e juro americano, com defasagens, 2000–2026, e comparação com países de risco fiscal parecido e histórico inflacionário diferente (sugestão registrada no painel de 2.5).
- Série do swap DI 360 (SGS 7806) para o ex-ante no padrão de mercado.
- Estimar o efeito-riqueza invertido: renda adicional de LFT e compromissadas por setor institucional (CEI do IBGE, área 5.4.3) × propensão a consumir.
- Conferir no RPM de setembro de 2026 se o BC revisou o neutro.

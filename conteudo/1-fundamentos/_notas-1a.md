# Notas da área 1, primeira metade (redator 1a)

Data: 02/11/2026. Não vira página.

## Páginas entregues (palavras aproximadas do corpo, contando números e fórmulas)

| id | arquivo | palavras |
|---|---|---|
| 1 | 1-fundamentos.md (macro do ramo, resume 1.1 a 1.6) | 1.400 |
| 1.1 | 1.1-moeda.md | 2.170 |
| 1.1.1 | 1.1.1-identidade.md | 1.600 |
| 1.1.2 | 1.1.2-longo-prazo-cagan.md | 2.000 |
| 1.1.3 | 1.1.3-reservas-qe.md | 1.880 |
| 1.1.4 | 1.1.4-moeda-endogena.md | 1.950 |
| 1.2 | 1.2-inercia-real.md | 2.400 |
| 1.2.1 | 1.2.1-teoria-inercia.md | 1.690 |
| 1.2.2 | 1.2.2-pai-fse-urv-real.md | 1.820 |
| 1.2.3 | 1.2.3-ancoras.md | 1.660 |
| 1.2.4 | 1.2.4-cruzado.md | 1.570 |
| 1.3 | 1.3-expectativas.md | 3.190 |

## Gráficos (dados/)

- `1.1-eua-base-m2-precos.json`: base, M2 e CPI dos EUA, índice dez/2007 = 100, mensal 2007–2015.
- `1.1.1-eua-velocidade-m2.json`: velocidade de M2 (M2V), trimestral 1990–2021.
- `1.1.3-eua-base-m2-bilhoes.json`: base e M2 em US$ bi, mensal 2007–2016.
- `1.1.3-eua-inflacao.json`: CPI e núcleo do PCE em 12 meses, 2007–2016, com linha da meta de 2%.
- `1.2-ipca-mensal-1993-1995.json`: IPCA mensal 1993–1995.
- `1.2.3-selic-1994-1999.json`: Selic SGS 4189 (anualizada base 252), jul/1994–dez/1999.
- `1.2.3-cambio-1994-1999.json`: dólar média mensal SGS 3698, jul/1994–dez/1999.
- `1.2.4-ipca-cruzado.json`: IPCA mensal 1985–1987.
- `1.3-brinquedo-expectativas.json`: simulação de brinquedo (sem dado real), declarada como tal na fonte.

## Proveniência dos dados (ler antes de publicar)

FRED, API do BCB e Ipeadata estavam bloqueados na rede da sessão (WebFetch e curl). Os valores foram lidos
de cópias públicas das mesmas séries em repositórios do GitHub, via raw.githubusercontent.com:

- FRED (BOGMBASE, M2SL, CPIAUCSL, PCEPILFE): repositório `Gariyuuu/forecast-graveyard`, `data/raw/`, vintage até jul/2026. Valores conferem com o que se conhece da série (base de US$ 847,6 bi em ago/2008 e 4.075 bi em ago/2014).
- FRED M2V: repositório `mak8427/MonetarySupply`, série até 2021-T4.
- IPCA mensal (SGS 433): duas cópias independentes e idênticas (`viniclerigo/monitor-indicadores`, `GiovanniManiezzo/companies_indicators_br`) e uma terceira para 1994–1996 (`marcusos/modern-ml`). Totais anuais batem com o IBGE (1993: 2.477,15%; 1995: 22,41%).
- Selic SGS 4189: cópia da série Ipeadata GM366_TJOVER366 em `luisfantozzialvarez/Econometria-III`.
- Dólar SGS 3698: painel `MatmJr/PainelEconomiaBR` (catálogo confirma o código 3698).

Cada JSON diz isso na `nota`. Recomendo reextrair das fontes primárias quando a rede permitir e conferir.

## Números que divergem dos insumos ou do CONTEXTO

- McCandless e Weber (1995): CONTEXTO diz correlação de 0,93 a 0,96. O resumo de Walsh (2010, cap. 1) diz 0,92 a 0,96. Usei 0,92 a 0,96. A diferença provavelmente vem de arredondar 0,925 (M0). Conferir a tabela 1 do artigo original.
- Inflação dos EUA em jun/2022: a cópia do CPI com ajuste sazonal dá 8,98% em 12 meses; o insumo K cita 9,1% (índice sem ajuste, número divulgado pelo BLS). Usei 9,1% citando o insumo K.
- Balanço do Fed (insumo K): "de US$ 0,9 tri para US$ 4,5 tri" é o ativo total (WALCL). Usei a base monetária (BOGMBASE: 847,6 bi em ago/2008, 4.075 bi em ago/2014). São conceitos diferentes, não divergência; quem citar os dois deve dizer qual é qual.
- IPCA de 1983: o IPCA foi 164,0% (cálculo a partir do mensal; IBGE). O número de 211% que às vezes circula é do IGP-DI. Cuidado em outras áreas.
- IPCA de 1994: o cálculo a partir do mensal dá 916,43%; o oficial é 916,46% (arredondamento). Usei 916%.

## [a conferir]

- Resultado primário do setor público 1995–1998 (BCB) e balanço de pagamentos 1994–1998: citados qualitativamente em 1.2.2 e 1.2.3 com marca [a conferir].
- Base monetária e M1 de 1994–1995 (remonetização depois do Real): citada sem número em 1.2.2.
- Declaração de Galípolo sobre os 165 participantes do Focus (32 bancos, 72 gestoras, 61 outros): veio do CONTEXTO; falta a fonte primária.
- Carvalho e Minella (2012): citei o escopo do artigo, não os resultados específicos; detalhar em 2.4.
- Regra da mediana do Focus calculada sobre projeções dos últimos 30 dias: conferir na metodologia do BCB.
- Lista dos sete episódios de Cagan (1956): citei Alemanha, Áustria, Hungria (duas), Polônia, Grécia e Rússia de memória da literatura; a busca não confirmou a lista.
- Referências que não consegui confirmar por busca: Lopes (1984), "Só um choque heterodoxo pode derrubar a inflação", *Economia em Perspectiva*; Lara Resende (1984/1985), "A moeda indexada", republicação na REP 5(2); Pastore (1997), "Passividade monetária e inércia", RBE 51(1); Bacha (1994), REP 14(1); Pollin (1991), JPKE 13(3); Kaldor (1970), *Lloyds Bank Review* 97. Todas aparecem só em "Para ler" ou com paráfrase, sem recorte.
- Anedota do Natal atribuída a Kaldor: apresentada como "o exemplo que ficou associado a ele".

## Recortes citados (só os que tenho o texto)

- McCandless e Weber (1995), reproduzido em Cooper e John, *Economics: Theory Through Applications*, cap. 26 (texto conferido no repositório público `saylordotorg`).
- McLeay, Radia e Thomas (2014), p. 14, frase confirmada por busca.

Outros autores (Muth, Lucas, Friedman, Lopes, Arida e Lara Resende, Kaldor) estão parafraseados. A cota de buscas web da sessão acabou no meio do trabalho, o que impediu conferir trechos para recorte em português de Lopes e de Arida e Lara Resende. Sugiro, na próxima rodada, abrir os PDFs da SciELO (REP 4(1) e 5(2)) e acrescentar recortes curtos com página.

## Sugestões para a próxima rodada

- Reextrair FRED e SGS das fontes primárias e acrescentar à 1.1.3 as reservas excedentes (EXCSRESNS) e a taxa de juros sobre reservas (IOER).
- Acrescentar em 1.2.2 um gráfico de base monetária 1994–1996 (SGS) para mostrar a remonetização.
- Acrescentar em 1.2.3 a série de reservas internacionais e de conta corrente 1994–1999.
- Ajustar o resumo de 1.6 na página macro quando a página existir (escrita antes de 1.6 estar pronta; resumo feito pela topologia e pelo CONTEXTO).

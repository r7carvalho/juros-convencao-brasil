# Plano item a item

**Isto supera a forma de trabalho do `BRIEF.md` (subagentes por macroárea em paralelo).** O
conteúdo, as fontes e o estilo continuam valendo como está no briefing.

Regra de execução: pegue o **primeiro item não marcado**, faça só ele até o critério de pronto,
rode o build, faça commit e push com a mensagem `item <id>: <título>`, marque `[x]` aqui no mesmo
commit e só então comece o próximo. Um item por vez. Se um item for grande demais para uma sessão,
divida-o aqui mesmo em subitens (`5.1a`, `5.1b`) antes de começar. Ao terminar a sessão, deixe uma
linha em `RELATORIO.md` dizendo qual foi o último item feito.

Para cada item de texto, use um subagente Opus para a pesquisa (fontes, recortes, dados) e escreva
você mesmo a página a partir do que ele trouxe; ao fim de cada macroárea, um subagente revisor que
não escreveu nada audita as páginas dela contra `ESTILO.md` e as regras do briefing.

Critério de pronto de uma página: resumo no topo; texto extenso e didático (1.500 a 4.000
palavras); exemplo de brinquedo antes do dado real; recortes citados com autor, ano e página ou
link; todo número com fonte e data; quadro "A favor / Contra" quando houver disputa; "Para ler" no
fim; publicada em `docs/` sem erro de build.

## Infraestrutura

- [ ] 00.1 Motor do site: build Markdown + frontmatter → HTML em `docs/`, árvore lateral, breadcrumb, anterior/próxima, tema claro/escuro, celular sem rolagem horizontal
- [ ] 00.2 Componente de gráfico SVG (linha, barra, faixa de governo, tooltip, tabela de valores) lendo `dados/*.json`
- [ ] 00.3 Componentes de texto: recorte citado, quadro A favor/Contra, fórmula KaTeX, caixa de exemplo numérico
- [ ] 00.4 Página inicial com o mapa completo da topologia e o estado de cada página

## 1. Fundamentos teóricos

- [ ] 1.0 Página macro: o que cada teoria diz sobre juro e inflação, em mapa
- [ ] 1.1a Identidade M·V = P·Y e teoria quantitativa, com exemplo de brinquedo
- [ ] 1.1b Evidência: McCandless e Weber (1995), Cagan (1956), limites (causalidade reversa, crítica de Lucas)
- [ ] 1.1c Moeda endógena: Kaldor, pós-keynesianos, Banco da Inglaterra (2014)
- [ ] 1.1d O QE de 2008 e de 2020: base, reservas remuneradas, velocidade, o que aconteceu com a inflação
- [ ] 1.2a Inflação inercial: Lopes (1984), Arida e Lara Resende (1984), regra de bolso
- [ ] 1.2b Do Cruzado ao Real: PAI, FSE, URV, troca da moeda, âncoras (com cronologia e dados)
- [ ] 1.3a Expectativas adaptativas e racionais (Friedman, Lucas, Sargent)
- [ ] 1.3b Neo-fisherianos (Cochrane 2016) e as críticas (García-Schmidt e Woodford)
- [ ] 1.4a Convenção: definição (Lewis), ponto focal (Schelling), incerteza radical (Keynes 1937)
- [ ] 1.4b O juro "altamente convencional" (Teoria Geral, cap. 15) com o exemplo da perpetuidade
- [ ] 1.4c Concurso de beleza (cap. 12) e o experimento de Nagel (1995)
- [ ] 1.4d Dequech (1999, 2003, 2011) e Orléan (2011): convenção, racionalidade, autoridade
- [ ] 1.5a Aritmética da dívida e primário estabilizador, com exemplos
- [ ] 1.5b Sargent e Wallace (1981), Calvo (1988), FTPL
- [ ] 1.5c Blanchard (2004) e Favero e Giavazzi (2004): o caso Brasil 2002–2003
- [ ] 1.5d Equivalência ricardiana (Barro): o que é e por que não é dominância fiscal
- [ ] 1.6 Longo prazo, neutralidade e histerese (Keynes 1923, Blanchard e Summers 1986)
- [ ] 1.R Revisão independente da macroárea 1

## 2. Juros no Brasil

- [ ] 2.0 Página macro
- [ ] 2.1a Série do juro real ex-post e ex-ante, 1995–2026 (BCB), com gráfico
- [ ] 2.1b Comparação internacional (BIS, ranking de juro real), com gráfico
- [ ] 2.2a Incerteza jurisdicional: Arida, Bacha e Lara Resende (2005) e as críticas
- [ ] 2.2b Crédito direcionado e poupança baixa como explicações
- [ ] 2.2c Prêmio de risco fiscal como explicação
- [ ] 2.2d Rentismo: Bresser-Pereira e o novo-desenvolvimentismo
- [ ] 2.3 Juro neutro e meta: estimativas (BC, mercado, academia), o que se observa e o que se convenciona
- [ ] 2.4a Canais de transmissão no Brasil (crédito, câmbio, riqueza, expectativas) com estudos do BC
- [ ] 2.4b LFT e o efeito riqueza invertido
- [ ] 2.4c Focus: composição, viés, comparação com expectativas de empresas e consumidores
- [ ] 2.5a Bresser e Nakano (2002): o juro alto como convenção e armadilha
- [ ] 2.5b Erber: convenção de desenvolvimento e convenção de estabilidade
- [ ] 2.5c Lara Resende (2017): juros, moeda e ortodoxia
- [ ] 2.R Revisão independente da macroárea 2

## 3. Dívida pública

- [ ] 3.0 Página macro
- [ ] 3.1 Aritmética aplicada ao Brasil (r, g, d, s atuais e cenários)
- [ ] 3.2 Decomposição da alta pelos fatores condicionantes do BCB (insumo `frente-J.json`)
- [ ] 3.3a Detentores da DPF (Tesouro) e evolução
- [ ] 3.3b Contas Econômicas Integradas (IBGE): juros pagos e recebidos por setor institucional
- [ ] 3.4 Comparação internacional de nível e de custo
- [ ] 3.5 Auditoria Cidadã da Dívida: o que afirma, a resposta do Tesouro e as críticas metodológicas
- [ ] 3.R Revisão independente da macroárea 3

## 4. Inflação: de onde vem

- [ ] 4.0 Página macro
- [ ] 4.1a IPCA 2003–2026: livres × administrados, com gráfico
- [ ] 4.1b Alimentos, serviços e industriais; câmbio e commodities
- [ ] 4.1c Decomposições do próprio BC (boxes dos relatórios: inércia, expectativas, câmbio, hiato)
- [ ] 4.2 Pandemia 2020–2022: choques, Selic a 2% e a alta até 13,75%
- [ ] 4.3a 2011–2013: cortes de juros, Nova Matriz, inflação (com a correção do teto em 2013)
- [ ] 4.3b 2014–2016: recessão, crise fiscal, crise política, Lava Jato e investimento
- [ ] 4.4 2023–2026: Selic a 15%, desinflação de 2025 e expectativas
- [ ] 4.5 Teste da tese "sem demanda nem oferta, só choque externo": veredito com dados
- [ ] 4.R Revisão independente da macroárea 4

## 5. Investimento refém do juro

- [ ] 5.0 Página macro
- [ ] 5.1a Juro real × ROE/ROIC de empresas não financeiras (séries públicas)
- [ ] 5.1b Juro real × taxa de lucro macro (IBGE)
- [ ] 5.2 FBCF, capital por trabalhador e relação capital-produto (insumo `frente-L.json`)
- [ ] 5.3 CDI como referência: fundos, metas atuariais, TLP, custo de oportunidade
- [ ] 5.4a Tabela de Recursos e Usos simplificada do ano mais recente
- [ ] 5.4b Valor adicionado por atividade e o peso das atividades financeiras ao longo do tempo
- [ ] 5.R Revisão independente da macroárea 5

## 6. Contrapontos ortodoxos

- [ ] 6.0 Página macro
- [ ] 6.1 Prêmio fiscal e dominância (Blanchard, Favero e Giavazzi, Lisboa e Pessôa)
- [ ] 6.2 Política monetária funciona (Holland e Padovani, estudos do BC, 2025)
- [ ] 6.3 Poupança baixa e juro neutro alto
- [ ] 6.4 Autonomia do BC e credibilidade (lei de 2021, evidência)
- [ ] 6.R Revisão independente da macroárea 6 (inclui conferir que tem a extensão das áreas 2 a 5)

## 7. Caminhos de política

- [ ] 7.0 Página macro com a matriz premissa → política
- [ ] 7.1 Meta de inflação maior
- [ ] 7.2 Desindexação da dívida (menos LFT) e alongamento
- [ ] 7.3 Mudança de referência (CDI) e indexação dos contratos
- [ ] 7.4 Tributação da renda de juros
- [ ] 7.5 Renegociação e calote (por que a dívida em reais muda a análise; casos internacionais)
- [ ] 7.6 Coordenação fiscal-monetária
- [ ] 7.7 Crédito direcionado e bancos públicos
- [ ] 7.R Revisão independente da macroárea 7

## 8–9. Conclusão e apoio

- [ ] 8.1 Matriz tese × evidência × força, item por item
- [ ] 8.2 Direção de conclusão, com o grau de confiança declarado
- [ ] 9.1 Glossário
- [ ] 9.2 Linha do tempo 1980–2026 (planos, regimes, Selic, inflação, crises)
- [ ] 9.3 Bibliografia completa e método
- [ ] 9.R Revisão final do site inteiro e `RELATORIO.md`

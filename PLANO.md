# Plano item a item

**Isto supera a forma de trabalho do `BRIEF.md` (subagentes por macroárea em paralelo).** O
conteúdo, as fontes e o estilo continuam valendo como está no briefing.

**Ordem de execução dos blocos:** 00 → 1 → 10 → 11 → 2 → 3 → 4 → 5 → 6 → 7 → 12 → 8–9. A base
teórica (1, 10 e 11) vem antes das páginas aplicadas ao Brasil, e as vozes do debate (12) vêm
depois, porque se apoiam em tudo o que foi escrito antes.

Regra de execução: pegue o **primeiro item não marcado na ordem acima**, faça só ele até o critério de pronto,
rode o build, faça commit e push com a mensagem `item <id>: <título>`, marque `[x]` aqui no mesmo
commit e só então comece o próximo. Um item por vez. Se um item for grande demais para uma sessão,
divida-o aqui mesmo em subitens (`5.1a`, `5.1b`) antes de começar. Ao terminar a sessão, deixe uma
linha em `RELATORIO.md` dizendo qual foi o último item feito.

**Cada item é uma chamada nova** (atualizado em 02/11/2026). O coordenador não pesquisa nem escreve
página: ele monta o cartão do item, abre um subagente Opus **novo** para executá-lo, confere o
resultado pelo checklist, roda o build, faz o commit e marca o item. O subagente não herda a
conversa do coordenador, então o cartão tem de ser autocontido:

```
ITEM <id> — <título>
Leia antes: BRIEF.md (regras), ESTILO.md, CONTEXTO.md e as páginas já publicadas que este item cita.
Escopo: <o que entra e o que fica para outro item>
Perguntas que a página responde: <3 a 8>
Fontes obrigatórias: <lista>; procure outras.
Insumos: <arquivos de insumos/ e dados/ que servem>
Saída: conteudo/<area>/<arquivo>.md (frontmatter: título, pai, ordem, resumo) + dados/<arquivo>.json se houver gráfico
Pronto quando: critério de pronto abaixo + <específico do item>
```

O subagente devolve só um resumo curto (o que escreveu, fontes principais, lacunas), para que o
contexto do coordenador não encha. Ao fim de cada macroárea, um subagente revisor que não escreveu
nada audita as páginas dela contra `ESTILO.md` e as regras do briefing.

**Imagens e prints.** Entram gráficos e quadros de fonte oficial (BCB, Tesouro, IBGE, IFI, FMI, BIS,
Fed, BCE, BoJ) com atribuição e link, recortados no trecho que interessa, e gráficos refeitos em SVG a
partir dos dados. Fala pública de economista ou influenciador entra como citação textual curta com
link e data; captura de tela de post público só quando o texto sozinho perder o sentido. Não entra
reprodução de material de curso privado (Estratégia, Gran, Direção etc.): o esquema bom de curso se
redesenha do zero com a fonte primária.

Critério de pronto de uma página: resumo no topo; texto extenso e didático (1.500 a 4.000
palavras); exemplo de brinquedo antes do dado real; recortes citados com autor, ano e página ou
link; todo número com fonte e data; quadro "A favor / Contra" quando houver disputa; "Para ler" no
fim; publicada em `docs/` sem erro de build.

## Infraestrutura

- [x] 00.1 Motor do site: build Markdown + frontmatter → HTML em `docs/`, árvore lateral, breadcrumb, anterior/próxima, tema claro/escuro, celular sem rolagem horizontal
- [x] 00.2 Componente de gráfico SVG (linha, barra, faixa de governo, tooltip, tabela de valores) lendo `dados/*.json`
- [x] 00.3 Componentes de texto: recorte citado, quadro A favor/Contra, fórmula KaTeX, caixa de exemplo numérico
- [x] 00.4 Página inicial com o mapa completo da topologia e o estado de cada página

## 1. Fundamentos teóricos

- [x] 1.0 Página macro: o que cada teoria diz sobre juro e inflação, em mapa
- [x] 1.1a Identidade M·V = P·Y e teoria quantitativa, com exemplo de brinquedo
- [x] 1.1b Evidência: McCandless e Weber (1995), Cagan (1956), limites (causalidade reversa, crítica de Lucas)
- [x] 1.1c Moeda endógena: Kaldor, pós-keynesianos, Banco da Inglaterra (2014)
- [x] 1.1d O QE de 2008 e de 2020: base, reservas remuneradas, velocidade, o que aconteceu com a inflação
- [x] 1.2a Inflação inercial: Lopes (1984), Arida e Lara Resende (1984), regra de bolso
- [x] 1.2b Do Cruzado ao Real: PAI, FSE, URV, troca da moeda, âncoras (com cronologia e dados)
- [x] 1.3a Expectativas adaptativas e racionais (Friedman, Lucas, Sargent)
- [x] 1.3b Neo-fisherianos (Cochrane 2016) e as críticas (García-Schmidt e Woodford)
- [x] 1.4a Convenção: definição (Lewis), ponto focal (Schelling), incerteza radical (Keynes 1937)
- [x] 1.4b O juro "altamente convencional" (Teoria Geral, cap. 15) com o exemplo da perpetuidade
- [x] 1.4c Concurso de beleza (cap. 12) e o experimento de Nagel (1995)
- [x] 1.4d Dequech (1999, 2003, 2011) e Orléan (2011): convenção, racionalidade, autoridade
- [x] 1.5a Aritmética da dívida e primário estabilizador, com exemplos
- [x] 1.5b Sargent e Wallace (1981), Calvo (1988), FTPL
- [x] 1.5c Blanchard (2004) e Favero e Giavazzi (2004): o caso Brasil 2002–2003
- [x] 1.5d Equivalência ricardiana (Barro): o que é e por que não é dominância fiscal
- [x] 1.6 Longo prazo, neutralidade e histerese (Keynes 1923, Blanchard e Summers 1986)
- [x] 1.R Revisão independente da macroárea 1

## 2. Juros no Brasil

- [x] 2.0 Página macro
- [x] 2.1a Série do juro real ex-post e ex-ante, 1995–2026 (BCB), com gráfico
- [x] 2.1b Comparação internacional (BIS, ranking de juro real), com gráfico
- [x] 2.2a Incerteza jurisdicional: Arida, Bacha e Lara Resende (2005) e as críticas
- [x] 2.2b Crédito direcionado e poupança baixa como explicações
- [x] 2.2c Prêmio de risco fiscal como explicação
- [x] 2.2d Rentismo: Bresser-Pereira e o novo-desenvolvimentismo
- [x] 2.3 Juro neutro e meta: estimativas (BC, mercado, academia), o que se observa e o que se convenciona
- [x] 2.4a Canais de transmissão no Brasil (crédito, câmbio, riqueza, expectativas) com estudos do BC
- [x] 2.4b LFT e o efeito riqueza invertido
- [x] 2.4c Focus: composição, viés, comparação com expectativas de empresas e consumidores
- [x] 2.5a Bresser e Nakano (2002): o juro alto como convenção e armadilha
- [x] 2.5b Erber: convenção de desenvolvimento e convenção de estabilidade
- [x] 2.5c Lara Resende (2017): juros, moeda e ortodoxia
- [x] 2.R Revisão independente da macroárea 2

## 3. Dívida pública

- [x] 3.0 Página macro
- [x] 3.1 Aritmética aplicada ao Brasil (r, g, d, s atuais e cenários)
- [x] 3.2 Decomposição da alta pelos fatores condicionantes do BCB (insumo `frente-J.json`)
- [x] 3.3a Detentores da DPF (Tesouro) e evolução
- [x] 3.3b Contas Econômicas Integradas (IBGE): juros pagos e recebidos por setor institucional
- [x] 3.4 Comparação internacional de nível e de custo
- [x] 3.5 Auditoria Cidadã da Dívida: o que afirma, a resposta do Tesouro e as críticas metodológicas
- [x] 3.R Revisão independente da macroárea 3

## 4. Inflação: de onde vem

- [x] 4.0 Página macro
- [x] 4.1a IPCA 2003–2026: livres × administrados, com gráfico
- [x] 4.1b Alimentos, serviços e industriais; câmbio e commodities
- [x] 4.1c Decomposições do próprio BC (boxes dos relatórios: inércia, expectativas, câmbio, hiato)
- [x] 4.2 Pandemia 2020–2022: choques, Selic a 2% e a alta até 13,75%
- [x] 4.3a 2011–2013: cortes de juros, Nova Matriz, inflação (com a correção do teto em 2013)
- [x] 4.3b 2014–2016: recessão, crise fiscal, crise política, Lava Jato e investimento
- [x] 4.4 2023–2026: Selic a 15%, desinflação de 2025 e expectativas
- [x] 4.5 Teste da tese "sem demanda nem oferta, só choque externo": veredito com dados
- [x] 4.R Revisão independente da macroárea 4

## 5. Investimento refém do juro

- [x] 5.0 Página macro
- [x] 5.1a Juro real × ROE/ROIC de empresas não financeiras (séries públicas)
- [x] 5.1b Juro real × taxa de lucro macro (IBGE)
- [x] 5.2 FBCF, capital por trabalhador e relação capital-produto (insumo `frente-L.json`)
- [x] 5.3 CDI como referência: fundos, metas atuariais, TLP, custo de oportunidade
- [x] 5.4a Tabela de Recursos e Usos simplificada do ano mais recente
- [x] 5.4b Valor adicionado por atividade e o peso das atividades financeiras ao longo do tempo
- [x] 5.R Revisão independente da macroárea 5

## 6. Contrapontos ortodoxos

- [x] 6.0 Página macro
- [x] 6.1 Prêmio fiscal e dominância (Blanchard, Favero e Giavazzi, Lisboa e Pessôa)
- [x] 6.2 Política monetária funciona (Holland e Padovani, estudos do BC, 2025)
- [x] 6.3 Poupança baixa e juro neutro alto
- [x] 6.4 Autonomia do BC e credibilidade (lei de 2021, evidência)
- [x] 6.R Revisão independente da macroárea 6 (inclui conferir que tem a extensão das áreas 2 a 5)

## 7. Caminhos de política

- [x] 7.0 Página macro com a matriz premissa → política
- [x] 7.1 Meta de inflação maior
- [x] 7.2 Desindexação da dívida (menos LFT) e alongamento
- [x] 7.3 Mudança de referência (CDI) e indexação dos contratos
- [x] 7.4 Tributação da renda de juros
- [x] 7.5 Renegociação e calote (por que a dívida em reais muda a análise; casos internacionais)
- [x] 7.6 Coordenação fiscal-monetária
- [x] 7.7 Crédito direcionado e bancos públicos
- [x] 7.R Revisão independente da macroárea 7

## 10. Política monetária: instrumentos convencionais e não convencionais

Fontes de base para todo o bloco: Banco Central do Brasil (Relatório de Política Monetária e boxes,
Relatório de Inflação anterior a 2025, atas e comunicados do Copom, "Sistema de Metas para a
Inflação", página de instrumentos de política monetária, Trabalhos para Discussão, Relatório de
Estabilidade Financeira, Lei Complementar 179/2021, Lei 14.185/2021, EC 106/2020); Blanchard
(manual *Macroeconomics*, caps. de política monetária e de armadilha de liquidez; Blanchard,
Dell'Ariccia e Mauro, "Rethinking Macroeconomic Policy", 2010; Blanchard, "Public Debt and Low
Interest Rates", AER 2019; *Fiscal Policy under Low Interest Rates*, 2023); Bernanke ("The New Tools
of Monetary Policy", AER 2020; discurso de 2002 sobre deflação); Woodford (2003); Svensson; Mishkin
(*Economics of Money, Banking and Financial Markets*, caps. de instrumentos); Walsh; Borio e
Disyatat (2009, "Unconventional monetary policies: an appraisal", BIS); Gagnon et al. (2011);
Krishnamurthy e Vissing-Jorgensen (2011); Campbell, Evans, Fisher e Justiniano (2012); Brunnermeier
e Koby ("reversal rate"); Kuroda e documentos do BoJ; BCE (APP, PEPP, TLTRO); BoE (APF, FLS);
Turner (2015), Galí (2020) e Bernanke (2003) sobre financiamento monetário; Kelton e Wray (MMT) e as
críticas a ela.

- [x] 10.0 Página macro: mapa de instrumentos (convencionais × não convencionais), canais e regimes; o que cada um faz no balanço do banco central, com um balanço de brinquedo
- [x] 10.1a Regimes monetários: metas monetárias, câmbio fixo, metas de inflação; o caso brasileiro de 1999, a meta contínua de 2025, o mandato do BC na LC 179/2021
- [x] 10.1b Por que meta de 3%: a literatura sobre o nível ótimo da meta (Blanchard et al. 2010 e a proposta de 4%, Ball, críticas), metas de países emergentes comparadas
- [x] 10.2a Taxa básica e corredor: Selic meta × Selic over, operações compromissadas, depósitos voluntários remunerados (Lei 14.185/2021), como o BC faz a taxa "acontecer" no mercado
- [x] 10.2b Operações de mercado aberto: definitivas × compromissadas; por que o BC não emite título próprio desde a LRF (2002); a carteira do BC e a DBGG
- [x] 10.2c Redesconto e assistência de liquidez: emprestador de última instância (Bagehot), modalidades no Brasil, uso em crises (2008, 2020)
- [x] 10.2d Recolhimento compulsório: história no Brasil, uso anticíclico e macroprudencial (2008, 2020), comparação internacional
- [x] 10.2e Regra de Taylor e modelos do BC (semiestrutural, projeções condicionais), com exemplo numérico da regra
- [x] 10.2f Comunicação convencional: atas, comunicados, balanço de riscos, o "Copom dependente de dados"
- [x] 10.3a Forward guidance: Delphic × Odyssean (Campbell et al. 2012), Fed 2011–2013, o BCB em 2020, quando funciona e quando vira armadilha
- [x] 10.3b Quantitative easing: Fed (QE1–QE3, 2020), BoE, BCE (APP, PEPP); canais (portfolio balance, sinalização, liquidez); estimativas de efeito (Gagnon, Krishnamurthy e Vissing-Jorgensen); o que aconteceu com inflação e dívida
- [x] 10.3c Japão: QQE (2013), controle da curva de juros (2016–2024), Abenomics, saída em 2024; o que ensina
- [x] 10.3d Juros negativos: BCE, BoJ, Suíça, Suécia, Dinamarca; efeitos sobre bancos; o "reversal rate"
- [x] 10.3e Credit easing e linhas dirigidas: TLTRO, Funding for Lending, facilities do Fed em 2020
- [x] 10.3f Câmbio como instrumento: swaps cambiais e reservas do BCB, intervenções, quando substituem juro
- [x] 10.3g Brasil 2020: EC 106 (compra de títulos no secundário), linhas do BCB; o que foi usado e o que ficou no papel
- [x] 10.3h Financiamento monetário, "dinheiro de helicóptero" e MMT: Bernanke (2003), Turner (2015), Galí (2020), Kelton; o debate com os críticos; o que vale para moeda não reserva
- [x] 10.4 Blanchard por inteiro: da dominância fiscal de 2004 ao "dívida com juro baixo" de 2019 e ao livro de 2023; onde as posições dele mudaram e o que dizem sobre o Brasil
- [x] 10.5 O que as não convencionais ensinam ao Brasil: moeda não reserva, repasse cambial, dívida indexada à Selic, crédito direcionado; o que é transponível e o que não é
- [x] 10.R Revisão independente do bloco 10

## 11. Finanças públicas: os conceitos

Insumo obrigatório: `insumos/financas-publicas-concurso.md` (extraído do material de concurso do
usuário). Fontes de base: Manual de Estatísticas Fiscais do BCB, notas de estatísticas fiscais do
BCB, Resultado do Tesouro Nacional (RTN), Relatório Mensal e Anual da Dívida, PAF, Manual Técnico de
Orçamento, LRF (LC 101/2000), Constituição (art. 167, III), EC 95/2016, LC 200/2023, Anexo de Riscos
Fiscais da LDO, IFI (RAF), FMI (GFSM 2014, Fiscal Monitor, DSA).

- [x] 11.0 Página macro: mapa dos conceitos fiscais e como eles se ligam (estoque × fluxo)
- [x] 11.1 Dívida bruta e líquida: DBGG conceito BCB × FMI, DLSP, DPF, DPMFi, compromissadas, ativos (reservas, créditos ao BNDES)
- [x] 11.2 Resultados fiscais: primário, nominal e operacional; NFSP; competência × caixa; com um orçamento de brinquedo
- [x] 11.3 Acima e abaixo da linha: RTN do Tesouro × estatísticas do BCB, a "discrepância estatística" e por que os números divergem
- [x] 11.4 Armadilhas conceituais: receita de privatização e NFSP, ajuste patrimonial, juros nominais × reais, efeito câmbio na DLSP (inclui o padrão de erro documentado no insumo)
- [x] 11.5 Risco fiscal: o Anexo de Riscos Fiscais da LDO, passivos contingentes, precatórios, judicialização; e o "risco fiscal" no sentido do mercado (prêmio, CDS, curva)
- [x] 11.6 Regras fiscais: LRF, regra de ouro, teto (EC 95), arcabouço (LC 200/2023); desenho, desempenho e comparação internacional
- [x] 11.7 Sustentabilidade: r − g, teste de Bohn, DSA do FMI, "limite seguro" de dívida e por que ele não existe como número único
- [x] 11.8 Estatística fiscal internacional: GFSM 2014 e por que comparar dívida entre países exige cuidado
- [x] 11.R Revisão independente do bloco 11

## 12. Vozes do debate: influenciadores, mídia, mercado e jargões

Regras próprias do bloco, além do briefing:
- Só fala pública, com link e data (vídeo com minutagem, coluna, post, entrevista, relatório).
  Nada de vida privada, nada de ataque pessoal.
- Princípio da caridade: apresente o argumento da pessoa na sua forma mais forte antes de avaliá-lo.
- Classifique cada argumento: **procede**, **procede em parte**, **não procede**, **falta evidência**,
  com a base teórica e a evidência ao lado. Concordar quando procede é parte do método.
- Agrupe argumentos repetidos entre pessoas numa página de jargão (bloco 12.4) e, na página da
  pessoa, remeta a ela.
- Identidades a confirmar antes de escrever (o pedido veio por voz): "Investidor Sardinha" (Raul
  Sena), "Primo Rico" (Thiago Nigro), Bruno Perini ("Você Mais Rico"), Samuel Pessôa (FGV IBRE e
  Folha), "Márcio … do INPE" (provavelmente Marcos Lisboa, do Insper). Se a identidade não se
  confirmar, registre a dúvida em `RELATORIO.md` e pule a página.
- Para o painel não ficar de um lado só, as vozes heterodoxas (12.5) recebem o mesmo tratamento.

- [x] 12.0 Página macro: método, matriz pessoa × argumento × classificação, mapa dos jargões
- [x] 12.1a Influenciador: Investidor Sardinha (Raul Sena)
- [x] 12.1b Influenciador: Primo Rico (Thiago Nigro)
- [x] 12.1c Influenciador: Bruno Perini
- [x] 12.1d1 Influenciador: Economista Sincero (Charles Mendlowicz)
- [x] 12.1d2 Influenciador: Ricardo Amorim
- [x] 12.1d3 Nathalia Arcuri: verificada; poucas falas sobre os temas do painel, sem página
- [x] 12.1d4 Influenciador: Tiago Reis (Suno)
- [ ] 12.1d5 Influenciador: Eduardo Moreira (ICL)
- [x] 12.2a Mídia e academia: Samuel Pessôa
- [x] 12.2b Mídia e academia: Marcos Lisboa (confirmar identidade)
- [x] 12.2c1 Mídia e academia: Mansueto Almeida
- [ ] 12.2c2 Mídia e academia: Felipe Salto
- [ ] 12.2c3 Mídia e academia: Armínio Fraga
- [ ] 12.2c4 Mídia e academia: Zeina Latif
- [ ] 12.2c5 Mídia e academia: Alexandre Schwartsman
- [ ] 12.2c6 Mídia e academia: Marcos Mendes
- [ ] 12.2c7 Mídia e academia: Fabio Giambiagi
- [x] 12.3a Economistas-chefes de bancos e gestoras: o que projetam, com que histórico de acerto (comparar projeções do Focus e de relatórios com o realizado)
- [x] 12.3b O Focus como instituição: composição, viés, acerto histórico
- [ ] 12.4a Jargão: "o Brasil vai quebrar" / "a dívida é impagável"
- [ ] 12.4b Jargão: "gastança", "o Estado gasta demais", "o governo é como uma família"
- [ ] 12.4c Jargão: "o mercado está nervoso", "o mercado está precificando", "risco fiscal"
- [ ] 12.4d Jargão: "dominância fiscal" usado como explicação de tudo
- [ ] 12.4e Jargão: "desancoragem das expectativas", "juro neutro subiu"
- [ ] 12.4f Jargão: "imprimir dinheiro gera inflação"
- [ ] 12.4g Jargão: "o juro é alto por culpa do governo" / "o BC é técnico e independente"
- [ ] 12.4h Jargão: "o Brasil vai virar Argentina/Venezuela"
- [ ] 12.4i Jargão: "não existe almoço grátis", "o arcabouço não para em pé"
- [ ] 12.4j Jargões do outro lado: "metade do orçamento vai para juros" (Auditoria Cidadã), "o BC trabalha para os bancos", "inflação é só choque externo"; mesmo rigor
- [ ] 12.5a Ramo e André Lara Resende
- [ ] 12.5b Luiz Gonzaga Belluzzo
- [ ] 12.5c Paulo Nogueira Batista Jr.
- [ ] 12.5d Laura Carvalho
- [ ] 12.5e André Roncaglia
- [ ] 12.5f Eduardo Moreira (ICL)
- [ ] 12.5g José Luis Oreiro
- [ ] 12.5h Luiz Carlos Bresser-Pereira
- [ ] 12.R Revisão independente do bloco 12, com atenção a citação fiel, data e link de cada fala

## 8–9. Conclusão e apoio

A conclusão (8.1 e 8.2) só se escreve depois dos blocos 10, 11 e 12, porque a matriz final incorpora
os argumentos deles.

- [x] 8.1 Matriz tese × evidência × força, item por item (1ª versão em 02/11/2026; refazer depois dos blocos 10 a 12)
- [x] 8.2 Direção de conclusão, com o grau de confiança declarado
- [x] 9.1 Glossário
- [x] 9.2 Linha do tempo 1980–2026 (planos, regimes, Selic, inflação, crises)
- [x] 9.3 Bibliografia completa e método (9.2 gerada por tools/analises/9.2_bibliografia.py; regenerar ao fim)
- [x] 9.R Revisão final do site inteiro e `RELATORIO.md`

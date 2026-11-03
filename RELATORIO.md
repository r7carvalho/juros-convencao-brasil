# Relatório do coordenador

Estado em 03/11/2026. Site: https://r7carvalho.github.io/juros-convencao-brasil/ (GitHub Pages, `main:/docs`).
Este relatório é atualizado a cada rodada; a seção "Último item feito" no fim diz onde parar e retomar.

## O que está pronto

**155 páginas publicadas, cerca de 628 mil palavras (contagem do build) e 172 gráficos**, em todas as
macroáreas da topologia original (0 a 9) e nos três blocos acrescentados pelo `PLANO.md` (10 política
monetária, 11 finanças públicas, 12 vozes do debate). Todos os itens do `PLANO.md` estão marcados.

| Área | Páginas | Palavras (aprox.) | Estado |
|---|---|---|---|
| 0 Início e "como ler" | 2 | 5.400 | 2ª versão (revisão independente em curso) |
| 1 Fundamentos teóricos | 23 | 55.600 | revisadas |
| 2 Juros no Brasil | 7 | 25.000 | revisadas |
| 3 Dívida pública | 6 | 19.800 | revisadas |
| 4 Inflação | 6 | 21.400 | revisadas |
| 5 Investimento | 8 | 20.700 | revisadas |
| 6 Contrapontos ortodoxos | 14 | 33.000 | revisadas |
| 7 Caminhos de política | 10 | 28.900 | revisadas |
| 8 Conclusão e matriz | 2 | 14.800 | 2ª versão, refeita com os blocos 10 a 12 (revisão independente em curso) |
| 9 Método, fontes, glossário, linha do tempo | 5 | 48.700 | revisadas; 9.2 gerada por script |
| 10 Política monetária | 22 | 82.900 | revisadas |
| 11 Finanças públicas | 9 | 33.900 | revisadas |
| 12 Vozes do debate | 41 | 164.700 | revisadas (23 pessoas, 10 jargões, 2 páginas do mercado, ramos e conclusão do bloco) |

O contraponto ortodoxo (área 6, mais as linhas O1 a O6 da matriz e os ramos ortodoxos do bloco 12)
tem extensão comparável à da tese em teste, como o briefing pede.

**Revisão independente.** Cada área de 1 a 7, a 9, a 10, a 11 e o bloco 12 (em três partes) foi lida
por um revisor que não escreveu nada. Os relatórios estão em `conteudo/_revisao/`: cerca de 1.130
achados nas áreas 1 a 9 e 256 no bloco 12. Corretores aplicaram os achados, e o topo de cada relatório
registra o que não foi aplicado e por quê. Uma passada de consistência entre áreas alinhou os números
às decisões de `conteudo/_divergencias.md`. Nenhuma pessoa privada é citada; as alusões à conversa de
origem, as fontes internas e as marcas de produção ("Frente X", "insumo", "[a conferir]", "nesta
rede") saíram do texto público, e `tools/lint.py` as veta.

**Bloco 12 (vozes do debate).** 23 pessoas públicas (influenciadores, mídia e academia, heterodoxos),
com só fala pública com link e data, princípio da caridade e a mesma régua para os dois lados. A
revisão encontrou réguas desiguais entre escolas, insinuações comerciais e trechos de vida privada;
tudo isso foi corrigido, e as regras ficaram no método da página 12 (perguntas e títulos não viram
"não procede"; falas de risco não são previsão; intenção e contrafactual não medido ficam em "falta
evidência"; relação comercial só em "Quem é"). Balanço depois da revisão: 387 proposições de pessoas =
153 procedem / 162 em parte / 22 não procedem / 50 falta evidência. Lado crítico 10,1% de "não
procede", demais 2,9%; 17 dos 22 "não procede" são previsões ou leituras de conjuntura.

**Dados primários.** A rede da sessão de nuvem bloqueia os sites oficiais. A solução foi um coletor
(`tools/coletar.py`) que roda no GitHub Actions (`.github/workflows/coletar-dados.yml`, toda segunda
e sob demanda) e grava em `dados/brutos/` o bruto das APIs: 132 arquivos, entre eles séries do SGS do
BCB, o Focus pela API Olinda, tabelas do SIDRA, o BIS, o Tesouro (CKAN), o Ipeadata e o SCN 2022 do
FTP do IBGE. As análises reprodutíveis estão em `tools/analises/`.

**Direção de conclusão (página 8, confiança moderada no conjunto).** O juro real brasileiro é alto por
uma soma de causas: um prêmio fiscal e político que move a curva e responde à dívida e à própria Selic,
sobre uma dívida que o primário de hoje não estabiliza (confiança alta); uma estrutura de LFT, crédito
direcionado e reservas que encarece cada ponto de Selic (confiança moderada no mecanismo, baixa no
tamanho); e um resíduo de 2 a 4,5 pontos que nenhuma explicação medida fecha e que o painel não chama
de convenção (confiança baixa de que a convenção responda por parte relevante). A tese em teste acerta
nos fatos e no círculo entre juro e dívida e erra nas formas absolutas (Selic sem eficácia, inflação
sem demanda, Focus inflado, dominância ativa); a leitura ortodoxa acerta no curto prazo e na trajetória
da dívida e não explica o nível.

**Achados que a evidência impôs ao painel** (detalhe na matriz 8.1, 27 linhas):
- Diferencial de juro real para os pares de 6,6 p.p. em 2000–2009, 3,1 em 2010–2019 e 5,5 em
  2023–2026 (BIS); quase sumiu em 2018–2021.
- O Focus subestimou a inflação (1,0 p.p., 2002–2025) e não tem viés fixo de Selic; o realizado ficou
  fora de toda a faixa das projeções em 16 de 24 anos (Selic): erro comum grande.
- Os juros explicam cerca de 90% da alta da dívida bruta desde 2022 (10,1 de 11,2 p.p.); r − g de
  +3,5 em 2023–2025; o primário deixou de responder à dívida depois de 2013 (teste de Bohn).
- O risco fiscal legal caiu enquanto o prêmio subiu; estudos do BCB e da IFI acham a dívida e a
  própria Selic no prêmio.
- Custo de carregamento das reservas de 1,41% do PIB em 12 meses (set/2026), líquido de R$ 66 bi em
  2012–2025 com o ganho cambial.
- Resíduo de 2 a 4,5 p.p. no juro que nenhuma explicação medida fecha.

## O que ficou raso ou sem fonte

- **Textos integrais não abertos.** Literatura, relatórios do BC e parte das falas do bloco 12 estão
  em paráfrase com link quando o texto não abriu (SciELO, BCB, NBER, YouTube, X, sites de jornal com
  paywall). Aspas só onde o texto foi visto. Listas em `conteudo/<área>/_notas.md`, seções
  "Pendências após a revisão".
- **Contas nacionais.** A CEI com juros (D.41) por setor institucional não está no FTP do SCN 2022/2023
  do IBGE; a 5.4.3 usa o SCN 2020 e diz isso.
- **FRED** dá timeout no runner do GitHub Actions; as séries americanas vêm de outras fontes citadas.
- **Hiato do produto do BC** não está nos brutos; a 10.2.5 usa filtro HP no IBC-Br, declarado como
  aproximação.
- **Séries longas anteriores a 1999** (Selic antes do Copom, base monetária antes de 2001) faltam nos
  gráficos.
- **Extensão.** As páginas de pessoa do bloco 12 passam do limite do cartão (4.000 a 4.700 palavras
  contra 3.500), e as de jargão também (3.200 a 4.400 contra 2.800); o que sobra são tabelas e testes.
  A coluna "jargão" das tabelas de pessoa está preenchida em 162 de 387 proposições.
- **Bloco 12, pontos abertos:** posts sem link localizado (fora das tabelas), datas aproximadas de
  vídeos e entrevistas, um vídeo citado pelo título e não assistido (classificado "falta evidência").

## Identidades deduzidas

- Item 12.2b: o pedido por voz citava "Márcio … do INPE". A página 12.2.2 trata de **Marcos Lisboa**
  (ex-presidente do Insper, ex-secretário de Política Econômica da Fazenda, colunista da Folha), com
  confiança moderada: "Marcos" ≈ "Márcio", "Insper" ≈ "INPE", presença alta no debate de 2023–2026 e
  coautoria com Samuel Pessôa e Mansueto Almeida de textos do ajuste fiscal. Alternativa: Marcio
  Pochmann (ex-presidente do Ipea, presidente do IBGE desde 2023), nome exato e "Ipea" ≈ "INPE", sem
  fala recente localizada sobre Selic e dívida; se for ele, a página cabe no ramo 12.5. **Decisão para
  o dono do painel.** A página não expõe a origem do pedido. Detalhes em `conteudo/12-vozes/_notas.md`,
  seção 12.2b.

## O que fazer na próxima rodada

1. Aplicar a revisão independente da conclusão e da página inicial (`conteudo/_revisao/8.md`) e
   passar 0, 0.1, 8 e 8.1 a "revisada".
2. Confirmar a identidade do item 12.2b (Lisboa ou Pochmann).
3. Fechar as pendências de texto integral quando a rede permitir: liberar no ambiente os domínios
   oficiais e de imprensa (bcb.gov.br, ibge.gov.br, tesourotransparente.gov.br, IFI, BIS, FMI, SciELO,
   YouTube) e trocar paráfrases por aspas conferidas.
4. Encurtar as páginas de pessoa e de jargão do bloco 12 até os limites do cartão e completar a coluna
   "jargão" das tabelas.
5. Coleta: rodar de novo o workflow em grupos menores (o grupo inteiro estoura 75 min); localizar a CEI;
   SIDRA 1621, novas M1 e M2, EMBI e TJLP já estão no coletor.
6. Recolocar na 7.8 a reação de Marcos Mendes à proposta de Lara Resende (BPMoney e Terra, 01 e
   02/11/2026), em paráfrase com link.

## Como reproduzir

```bash
python3 tools/build.py            # gera docs/
python3 tools/build.py --check    # valida links, âncoras e frontmatter
python3 tools/lint.py             # vícios de estilo e resíduos de produção
python3 tools/analises/9.2_bibliografia.py --relatorio   # regenera a 9.2
python3 tools/coletar.py sgs      # coleta (precisa de rede aberta; ou rode o workflow no GitHub)
```

## Último item feito

Bloco 12 revisado e corrigido (12.R) e concluído na página 12 (12.C); conclusão 8 e 8.1 e página
inicial refeitas em 2ª versão com os blocos 10 a 12; 9.2 regenerada. Em curso: revisão independente
de 8, 8.1, 0 e 0.1.

# Convenções de produção (valem para todos os subagentes)

Leia antes: `BRIEF.md`, `CONTEXTO.md`, `ESTILO.md`, `TOPOLOGIA.md` e os JSON de `insumos/`. O
briefing manda sobre qualquer dúvida. Data de referência: 02/11/2026.

## Árvore de páginas (ids fixos)

O id é o número da topologia. Use exatamente estes ids; uma área pode acrescentar netas dentro do
próprio ramo (por exemplo `2.4.1`), nunca fora dele.

```
0      Início (escrito no fim)                          conteudo/0-inicio/
0.1    A tese em teste e como ler o painel (no fim)
1      Fundamentos teóricos                             conteudo/1-fundamentos/
1.1    Moeda: teoria quantitativa, moeda endógena e o QE de 2008
1.1.1  M·V = P·Y como identidade
1.1.2  Moeda e inflação no longo prazo: McCandless e Weber, Cagan
1.1.3  Juros sobre reservas e o QE de 2008
1.1.4  Moeda endógena: Kaldor, pós-keynesianos e Banco da Inglaterra (2014)
1.2    Inflação inercial, URV e o Real
1.2.1  A teoria da inércia: Lopes, Arida e Lara Resende
1.2.2  PAI, FSE, URV e Real: a sequência
1.2.3  As âncoras de 1994–1999: câmbio e juros
1.2.4  O que o Cruzado errou
1.3    Expectativas: adaptativas, racionais, regra de bolso e neo-fisherianos
1.4    Convenção: Keynes, Dequech, Orléan, Lewis e Schelling
1.4.1  O juro "normal" (Teoria Geral, cap. 15) e o exemplo da perpetuidade
1.4.2  O concurso de beleza
1.4.3  Convenção e racionalidade
1.5    Dominância fiscal e aritmética da dívida
1.5.1  Sargent e Wallace (1981)
1.5.2  Blanchard (2004) e Favero e Giavazzi (2004)
1.5.3  Calvo (1988)
1.5.4  Teoria fiscal do nível de preços (FTPL)
1.5.5  Equivalência ricardiana: o que é e o que não é
1.6    Longo prazo, neutralidade e histerese
2      Juros no Brasil                                  conteudo/2-juros/
2.1    Quão altos: juro real Brasil × mundo, 1995–2026
2.2    Explicações concorrentes
2.3    O juro neutro e a meta: o que se observa e o que se convenciona
2.4    Transmissão: crédito direcionado, LFT, câmbio, expectativas e Focus
2.5    A tese da convenção aplicada ao Brasil
3      Dívida pública                                   conteudo/3-divida/
3.1    Aritmética da dívida, com exemplos
3.2    Decomposição da alta: fatores condicionantes do BCB
3.3    Quem detém e quem recebe
3.4    Comparação internacional
3.5    Auditoria Cidadã da Dívida: o que afirma e as críticas
4      Inflação: de onde vem                            conteudo/4-inflacao/
4.1    Decomposição do IPCA, 2003–2026
4.2    Pandemia, 2020–2022: choque de oferta e a resposta da Selic
4.3    2011–2016: cortes, Nova Matriz, crise política, Lava Jato e o investimento
4.4    2023–2026: Selic a 15% e o que ela fez
4.5    Teste da tese "sem demanda nem oferta, só choque externo"
5      Investimento refém do juro                       conteudo/5-investimento/
5.1    Juro real × retorno do capital
5.2    FBCF, capital por trabalhador e relação capital-produto
5.3    Indexação das decisões: CDI, metas atuariais, TLP
5.4    Contas nacionais: o que a TRU, o valor adicionado e a CEI mostram
5.4.1  A Tabela de Recursos e Usos simplificada
5.4.2  Valor adicionado por atividade e o peso das atividades financeiras
5.4.3  Contas Econômicas Integradas: juros pagos e recebidos por setor
6      Contrapontos ortodoxos                           conteudo/6-contrapontos/
6.1    Prêmio fiscal e dominância
6.2    A política monetária funciona
6.3    Poupança baixa e juro neutro alto
6.4    Autonomia do Banco Central e credibilidade
       (netas 6.x.y à escolha da área, para chegar à extensão das áreas 2 a 5)
7      Caminhos de política                             conteudo/7-politica/
7.1    Meta de inflação maior
7.2    Desindexação da dívida: menos LFT
7.3    Alongamento da dívida
7.4    Mudança de referência: o CDI
7.5    Tributação da renda de juros
7.6    Renegociação
7.7    Calote, e por que a dívida em reais muda a análise
7.8    Coordenação fiscal-monetária
7.9    Crédito direcionado
10     Política monetária: instrumentos convencionais e não convencionais   conteudo/10-politica-monetaria/
10.1   Regimes e a meta
10.1.1 Regimes monetários e o caso brasileiro
10.1.2 O nível ótimo da meta
10.2   Instrumentos convencionais
10.2.1 Taxa básica e corredor: Selic meta, Selic over, compromissadas e depósitos remunerados
10.2.2 Operações de mercado aberto e a carteira do BC
10.2.3 Redesconto e assistência de liquidez
10.2.4 Recolhimento compulsório
10.2.5 Regra de Taylor e os modelos do BC
10.2.6 Comunicação convencional
10.3   Instrumentos não convencionais
10.3.1 Forward guidance
10.3.2 Quantitative easing
10.3.3 Japão: QQE e controle da curva de juros
10.3.4 Juros negativos
10.3.5 Credit easing e linhas dirigidas
10.3.6 Câmbio como instrumento: swaps e reservas
10.3.7 Brasil 2020: EC 106 e as linhas do BCB
10.3.8 Financiamento monetário, dinheiro de helicóptero e MMT
10.4   Blanchard por inteiro
10.5   O que é transponível ao Brasil
11     Finanças públicas: os conceitos                   conteudo/11-financas-publicas/
11.1   Dívida bruta e líquida
11.2   Resultados fiscais: primário, nominal, operacional e NFSP
11.3   Acima e abaixo da linha
11.4   Armadilhas conceituais
11.5   Risco fiscal
11.6   Regras fiscais
11.7   Sustentabilidade da dívida
11.8   Estatística fiscal internacional
12     Vozes do debate                                   conteudo/12-vozes/
12.1   Influenciadores digitais (12.1.x, uma página por pessoa)
12.2   Mídia e academia (12.2.x, uma página por pessoa)
12.3   Economistas de mercado e o Focus (12.3.1, 12.3.2)
12.4   Jargões (12.4.x, uma página por jargão ou grupo)
12.5   Vozes heterodoxas (12.5.x, uma página por pessoa)
8      Conclusão (escrita no fim)                       conteudo/8-conclusao/
8.1    Matriz tese × evidência × força (no fim)
9      Método, fontes, glossário e linha do tempo       conteudo/9-metodo/
9.1    Método e regras de evidência
9.2    Fontes e bibliografia (no fim)
9.3    Glossário
9.4    Linha do tempo, 1964–2026
```

Fronteiras entre áreas: a área 1 trata de teoria e literatura, com exemplos internacionais e a
história do Real. As áreas 2 a 5 trazem a evidência brasileira. A área 6 traz o melhor argumento
ortodoxo **com** a evidência brasileira que o apoia. A área 7 trata de política. Quando um tema é de
outra área, faça um parágrafo curto e ponha um link interno em vez de repetir.

## Arquivo de página

Um arquivo por página: `conteudo/<pasta-da-area>/<id>-<slug>.md`, por exemplo
`conteudo/1-fundamentos/1.4.1-juro-normal.md`. A página macro da área tem o id da área
(`conteudo/2-juros/2-juros-no-brasil.md`). Frontmatter no topo, exatamente assim:

```
---
id: 1.4.1
titulo: O juro "normal" e o exemplo da perpetuidade
pai: 1.4
ordem: 1
resumo: Três a cinco linhas numa única linha de texto, dizendo o que a página mostra e a que conclusão chega.
---
```

`pai` da página macro é `0`. `ordem` é a posição entre irmãs (1, 2, 3...). Não escreva o título de
novo no corpo (o build gera o `<h1>`); o corpo começa direto no texto.

## Markdown aceito pelo build (`tools/build.py`)

- Seções com `##` e subseções com `###`. Não use `#`.
- Parágrafos, `**negrito**` (raro), `*itálico*`, `` `código` ``, listas com `-` ou `1.`.
- Links externos `[texto](https://...)`. Links internos `[texto](pagina:4.2)`.
- Tabelas no formato pipe do GitHub (`| a | b |` com linha `|---|---|`). Tabela larga rola sozinha.
- Fórmulas: `$...$` na linha e `$$...$$` em bloco próprio (KaTeX no navegador; sem KaTeX o texto
  aparece em fonte monoespaçada, então escreva TeX legível).
- Citação de obra (recorte): bloco `>` com o trecho entre aspas e, na última linha, a referência
  entre parênteses:

  ```
  > "trecho de até ~40 palavras"
  > (Keynes, 1936, *Teoria Geral*, cap. 15, p. 203)
  ```

  Tradução livre: diga "(tradução do painel)". Trecho que você não leu na fonte não entra entre
  aspas; parafraseie e cite a obra.
- Caixas (abrem com `:::tipo` e fecham com `:::` sozinho na linha; podem ter título após o tipo):
  - `:::exemplo Título` para o exemplo de brinquedo com números redondos.
  - `:::painel` para "o painel lê": interpretação própria, separada do fato e do autor.
  - `:::afavor` e `:::contra` em sequência, para o quadro "A favor / Contra" (o build põe lado a
    lado). Dentro, lista curta de evidências com fonte.
  - `:::nota` para ressalva metodológica.
- Gráfico: bloco cercado com a palavra `grafico` e o caminho do JSON de dados:

  ````
  ```grafico
  dados/4.1-ipca-livres-administrados.json
  ```
  ````

## Arquivo de dados (um JSON por gráfico, em `dados/`)

Nome `dados/<id-da-página>-<nome>.json`. Formato:

```json
{
  "titulo": "Juro real ex-post, Brasil e pares (% a.a.)",
  "tipo": "linha",
  "unidade": "% a.a.",
  "fonte": "BIS, policy rates e CPI; cálculo do painel",
  "url": "https://data.bis.org/...",
  "consulta": "2026-11-02",
  "nota": "opcional: método, quebra de série, o que é projeção",
  "governos": true,
  "ref": [{"v": 4.5, "rotulo": "teto da meta"}],
  "series": [
    {"nome": "Brasil", "pontos": [{"t": "2000", "v": 9.7}, {"t": "2001", "v": 8.1}]},
    {"nome": "México", "pontos": [{"t": "2000", "v": 6.4}]}
  ]
}
```

Tipos: `linha` (eixo de tempo; `t` em `AAAA`, `AAAA-MM`, `AAAA-MM-DD` ou `AAAA-T1..T4`),
`barras` (categorias no eixo x; várias séries ficam lado a lado), `empilhadas` (categorias no eixo
x, séries empilhadas com sinal, útil para decomposições e contribuições) e `barrash` (barras
horizontais de uma série, útil para rankings). `governos: true` desenha as faixas de mandato
presidencial (só em `linha`). `ref` desenha linhas horizontais de referência. Valores só numéricos
(use `null` para ausente). Todo gráfico tem `fonte` e `consulta`; sem isso o build recusa.

## Fontes e rede nesta sessão

O acesso direto às APIs e sites de IBGE, BCB, Tesouro, IFI, BIS e FMI está **bloqueado** pela rede
da sessão (tanto `curl` quanto WebFetch). Funciona a **busca web** (WebSearch, use modo `extended`
para dado numérico fino) e o GitHub. Então:

1. Os JSON de `insumos/` já trazem séries conferidas na fonte primária (SGS do BCB, SIDRA, BIS, PWT,
   Ipea, Tesouro), com URL e data. Use-os como base e cite a fonte primária que eles citam.
2. Para dado novo, busque na web até achar o número atribuído a uma fonte primária (página do IBGE,
   relatório do BCB, nota do Tesouro, PDF da IFI, texto para discussão), e cite a URL primária e a
   data de consulta. Se só achou o número na imprensa, cite a matéria e diga de qual fonte primária
   ela tira o número.
3. Número que você não conseguiu confirmar não entra no texto como fato. Escreva o argumento sem
   ele ou marque `[a conferir: ...]` e registre em `_notas.md` da área.
4. Literatura: cite edição e página quando souber. Não invente página, ano ou trecho. Recorte entre
   aspas só se você tem o texto (busca, PDF aberto, citação reproduzida em fonte confiável que você
   cita junto); caso contrário, parafraseie.

## Dados primários já coletados (`dados/brutos/`)

Desde 02/11/2026 o workflow `.github/workflows/coletar-dados.yml` roda `tools/coletar.py` no GitHub
Actions e grava o bruto das APIs oficiais em `dados/brutos/` (cada arquivo traz `fonte`, `url_api`,
`coleta` e `dados`). Há 39 séries do SGS do BCB (`sgs-<código>.json`: Selic meta e over, CDI, IPCA
cheio, 12 meses, livres, monitorados, alimentação, serviços, comercializáveis, núcleos, IGP-M,
câmbio, reservas, DBGG, DLSP, NFSP, PIB 12 meses, crédito livre e direcionado, spread, base
monetária, depósitos voluntários, desocupação), o Focus pela API Olinda (`focus-*.json`), o SIDRA
(`sidra-*.json`: PIB trimestral pelas óticas, IPCA por grupo 2012–2026, PNAD), o BIS (taxas de
política e CPI de 13 países, `bis-*.csv`) e arquivos do IBGE (`scn/`). Antes de buscar um número na
web, procure aqui e cite a fonte primária (por exemplo "BCB, SGS 13522, consulta em 02/11/2026").
`dados/brutos/_coleta.json` lista o que veio. Descrição marcada "(conferir)" no arquivo indica que
o nome da série ainda deve ser confirmado pelo comportamento dos dados.

## Notas da área

Cada área grava também `conteudo/<pasta>/_notas.md` (não vira página) com: lista de páginas
entregues e contagem aproximada de palavras; números usados que divergem dos insumos ou de outra
fonte (com as duas versões e a fonte de cada); o que ficou `[a conferir]`; e sugestões para a
próxima rodada.

## Regras que não se negociam

- Nenhum nome de pessoa privada. Pessoas públicas (economistas, autoridades, políticos, autores,
  comentaristas com obra publicada) podem ser citadas pelo que publicaram.
- Separe fato, interpretação do autor citado e interpretação do painel (`:::painel` ou "o painel lê").
- Não atribua a autor o que ele não disse (Lara Resende fala em "conservadorismo intelectual"; a tese
  do poder dos rentistas é de Bresser-Pereira).
- A tese do usuário é testada, não presumida. Onde os dados não a sustentam, o texto diz, com dados.
- Exemplo de brinquedo antes do dado real. Fórmula seguida de exemplo resolvido.
- Extensão: página filha de 1.500 a 4.000 palavras; neta de 1.000 a 2.500; página macro de 800 a
  1.500 palavras (apresenta o ramo, resume cada filha em um parágrafo com link, e diz o que o ramo
  conclui). Cada página termina com `## Para ler` (referências completas, com link quando houver).
- Siga `ESTILO.md` à risca, em especial: sem "não é X, é Y", sem fecho de efeito, sem travessão como
  conector, sem negrito decorativo, sem vocabulário de IA ("crucial", "robusto", "cenário",
  "fundamental", "vale destacar", "nesse sentido").
- Não rode `git`. Não edite arquivos fora da sua pasta de conteúdo e dos seus `dados/<id>-*.json`.
  Para checar o formato, rode `python3 tools/build.py --check` se o script existir.

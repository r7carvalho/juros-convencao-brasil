# Briefing do coordenador: painel "Juros, convenção e dívida no Brasil"

> **Atualização de 02/11/2026: a execução segue `PLANO.md`, item a item, um por vez, com commit a
> cada item.** Isso supera a seção "Organização do trabalho" abaixo no que diz respeito a abrir
> todas as macroáreas em paralelo. Conteúdo, fontes e estilo continuam como estão aqui.

Você é o **coordenador** de uma pesquisa extensa que vira um site estático publicado no GitHub Pages
deste repositório. Leia, nesta ordem, antes de qualquer coisa: este arquivo, `CONTEXTO.md`,
`TOPOLOGIA.md`, `ESTILO.md` e os insumos em `insumos/`. Data de referência: novembro de 2026. Os
créditos de nuvem do usuário vencem em 05/11/2026, então priorize terminar uma versão publicada
completa até lá e refinar depois.

## O que o usuário quer

Um painel com **revisão bibliográfica, evidência empírica com fonte e uma direção de conclusão**
sobre por que os juros reais brasileiros são dos mais altos do mundo. O painel deve **contrapor a
visão que parece consensual no Brasil**: a de que o problema é fiscal, o juro é consequência e a
expectativa é âncora técnica. A hipótese do usuário, que o painel testa (não presume):

> O convencionalismo brasileiro tirou a eficácia da política monetária. As decisões de
> investimento ficaram indexadas a um patamar de juros que virou convenção social; investimentos
> que seriam razoáveis em qualquer economia comparável não fecham a conta aqui, o investimento real
> cai e se forma um círculo: a dominância fiscal ganha peso, os agentes que lucram com o juro
> aproveitam, a dívida sobe, o juro não cai, e consolida-se uma convenção com verniz técnico. Isso
> induz na sociedade um alarmismo inflacionário sem componente de demanda nem de oferta que o
> justifique; o que houve de inflação veio sobretudo de choques externos.

O painel apresenta essa tese com o melhor argumento possível, **e** o contraponto ortodoxo com
extensão e rigor equivalentes, **e** a evidência que favorece e a que contraria cada parte. A
conclusão é uma direção sustentada pela evidência, com o grau de confiança declarado. Onde a
evidência não sustenta uma parte da tese (por exemplo, "sem nenhum componente de demanda"), o
painel diz isso com dados.

## Organização do trabalho (coordenador + subagentes)

- Use subagentes **Opus** (`model: opus`), um por macroárea da `TOPOLOGIA.md` (cerca de 10). Cada
  subagente recebe a área, os arquivos de estilo e contexto, e grava sua produção em
  `conteudo/<area>/` no formato definido abaixo. Rode-os em paralelo.
- O coordenador não reescreve o que o subagente já escreveu; revisa por checklist, cruza números
  entre áreas, registra divergência em `conteudo/_divergencias.md` e decide.
- Depois do primeiro ciclo, um subagente **revisor independente** (que não escreveu nada) lê o site
  inteiro procurando: número sem fonte, afirmação além da fonte, contraponto mais curto que a tese,
  vícios de `ESTILO.md`, e nome de pessoa privada. Corrija o que ele apontar.
- Commits frequentes e pequenos na branch padrão, com mensagem em português.

## Exigências de conteúdo

1. **Fonte em tudo.** Número sem fonte e data não entra. Preferência por fonte primária: IBGE (SIDRA,
   Contas Nacionais: Tabela de Recursos e Usos, valor adicionado por atividade, Contas Econômicas
   Integradas com renda de propriedade por setor institucional), Banco Central (SGS, Relatório de
   Política Monetária, Focus, Estatísticas Fiscais, fatores condicionantes da dívida, Trabalhos para
   Discussão), Tesouro (Relatório Mensal da Dívida, PAF, detentores), IFI, Ipea, FGV IBRE, BIS, FMI.
   Crítica: Auditoria Cidadã da Dívida, apresentada com o que ela afirma **e** as críticas
   metodológicas que recebe (por exemplo, somar rolagem/refinanciamento ao gasto com juros).
2. **Recortes das fontes.** Cada tese traz trechos curtos citados da obra (até ~40 palavras por
   citação, entre aspas, com autor, ano, página ou link), seguidos da explicação.
3. **Literatura mínima** (amplie): Keynes (Teoria Geral caps. 12, 15 e 17; QJE 1937; Tract 1923),
   Dequech (1999, 2003, 2011), Orléan (2011), Lewis (1969), Schelling, Bresser-Pereira e Nakano
   (2002), Bresser-Pereira (rentismo, novo-desenvolvimentismo), Erber (convenção de desenvolvimento,
   2008/2011), Lara Resende (2017, *Juros, moeda e ortodoxia*; "Juros e conservadorismo
   intelectual"), Arida e Lara Resende (inércia, 1984), Lopes (1984), Arida, Bacha e Lara Resende
   (2005), Blanchard (2004), Favero e Giavazzi (2004), Sargent e Wallace (1981), Sargent (1982),
   Calvo (1988), Cochrane (FTPL e neo-fisherianos, 2016), García-Schmidt e Woodford, Blanchard e
   Summers (1986), Kaldor e moeda endógena, Banco da Inglaterra (2014), McCandless e Weber (1995),
   Cagan (1956), Holland e Padovani, Lisboa e Pessôa, Barbosa Filho (2017), Serrano e Summa,
   Carvalho (Laura) e outros sobre 2011–2016. Cite edição e página quando possível.
4. **Contas nacionais como evidência.** Monte, a partir do IBGE, ao menos: (a) TRU simplificada do
   ano mais recente; (b) valor adicionado por atividade, com a participação das atividades
   financeiras ao longo do tempo; (c) CEI: juros pagos e recebidos por setor institucional
   (governo, empresas não financeiras, financeiras, famílias) e a transferência líquida que isso
   revela; (d) FBCF e taxa de investimento longas.
5. **Teste explícito da tese da inflação.** Decomponha o IPCA (livres × administrados, alimentos,
   serviços, industriais; contribuição de câmbio e commodities; decomposições do próprio BC nos
   relatórios) para 2003–2026, com foco em 2015, 2020–2022 e 2024–2026. Mostre onde há choque
   externo, onde há componente de demanda (hiato, mercado de trabalho, serviços) e onde há inércia.
6. **Juro real × retorno do capital.** Compare a Selic real e o CDI com a rentabilidade de empresas
   não financeiras (ROE/ROIC de séries públicas, Ipea, CEMEC/FIPE, BC) e com a taxa de lucro
   macro (IBGE). Esse é o centro empírico da tese do investimento refém.
7. **Episódios** com dados conferidos: o Real (PAI, FSE, URV, âncoras); 2002–2003; 2011–2016 (com a
   correção: o teto de 6,5% foi rompido em 2013, não em 2012; FBCF com pico no 2º tri de 2013);
   pandemia (Selic 2% de ago/2020 a mar/2021, até 13,75% em ago/2022; IPCA 10,06% em 2021 e 5,79% em
   2022); 2023–2026 (Selic a 15%, LFT em 52,7% da DPF).
8. **Opções de política**, cada uma com a premissa de que depende, quem ganha, quem perde, risco e
   evidência internacional: meta maior, desindexação da dívida (menos LFT), alongamento, mudança de
   referência (CDI), tributação de renda de juros, renegociação, calote (e por que a dívida em
   reais muda a análise), coordenação fiscal-monetária, crédito direcionado.

## Forma do site

- **Topologia hierárquica**: página macro, páginas filhas e netas, como em `TOPOLOGIA.md`. Árvore
  de navegação lateral (que vira menu no celular), trilha de navegação (breadcrumb), links "anterior
  / próxima" e página inicial com o mapa completo.
- Cada página: resumo de 3–5 linhas no topo, texto extenso e didático com exemplos simples (números
  de brinquedo antes dos números reais), recortes citados, gráficos SVG com fonte e data, quadro
  "A favor / Contra" quando houver disputa, e "Para ler" no fim.
- Conteúdo em Markdown por página (`conteudo/<area>/<pagina>.md` com frontmatter: título, pai,
  ordem, resumo) e dados em JSON (`dados/*.json`); um script de build sem dependências pesadas gera o
  HTML em `docs/` para o Pages. Tema claro e escuro, leitura confortável no celular (sem rolagem
  horizontal; tabela larga rola dentro do próprio bloco), sem biblioteca externa obrigatória.
- Referência visual e de motor gráfico: o site do repositório público `r7carvalho/alarmismo-x-fatos`
  (`assets/app.js` desenha gráficos SVG com faixas de governo e tooltip). Pode reaproveitar.
- Publique em GitHub Pages servindo de `docs/` na branch padrão. Se não conseguir ativar o Pages
  pela sessão, deixe tudo pronto e registre no README o comando:
  `gh api -X POST repos/r7carvalho/juros-convencao-brasil/pages -f "source[branch]=main" -f "source[path]=/docs"`.

## Extensão e tom

O usuário pediu explicitamente: **extenso, didático, intuitivo, com exemplos simples; se for pecar,
que seja pelo excesso de explicação e de evidência**, nunca pelo texto curto de IA. Cada página
filha tende a ter de 1.500 a 4.000 palavras. A escrita segue `ESTILO.md`.

## Regras que não se negociam

- Nenhum nome de pessoa privada. A conversa que originou o painel (resumida em `CONTEXTO.md`)
  envolve um interlocutor privado: ele não aparece.
- Separe fato, interpretação do autor citado e interpretação do painel. Escreva "o painel lê" quando
  for interpretação própria.
- Não atribua a autor o que ele não disse. Exemplo já corrigido: Lara Resende fala em
  "conservadorismo intelectual", não em captura por rentistas; a tese do poder dos rentistas é de
  Bresser-Pereira.
- Dados de 2025–2026 podem ter sido revistos; cite a data da consulta.

## Entrega

1. Site publicado (ou pronto para publicar) com todas as páginas da topologia.
2. `conteudo/_divergencias.md` com as divergências de número e como foram resolvidas.
3. `RELATORIO.md`: o que ficou pronto, o que ficou raso ou sem fonte, e o que fazer na próxima
   rodada.

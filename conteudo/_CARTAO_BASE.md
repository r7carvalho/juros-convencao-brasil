# Cartão-base dos itens (vale para todo item de escrita do PLANO.md)

Repositório: /home/user/juros-convencao-brasil. Cada item é executado por um subagente novo que
recebe o cartão específico (escopo, perguntas, fontes, saída) e segue este cartão-base.

## Leia antes

BRIEF.md (regras), PLANO.md (o bloco do item e as fontes de base do bloco), ESTILO.md, CONTEXTO.md,
conteudo/_CONVENCOES.md (formato de arquivo, ids, Markdown aceito, caixas, gráficos, rede e a seção
"Dados primários já coletados"), conteudo/_divergencias.md (números já decididos para todo o painel)
e as páginas já escritas que o cartão citar. Antes de escrever sobre um tema, procure com `grep -ril`
em conteudo/ se outra página já o trata; se sim, faça um parágrafo curto e ponha link interno
`[texto](pagina:ID)` em vez de repetir.

## Regras de fonte

- Primeiro `dados/brutos/` (SGS do BCB, SIDRA, Focus, BIS, Tesouro, IBGE): cite "BCB, SGS <código>,
  consulta em <data>" ou equivalente. Depois WebSearch (modo extended para número fino; se a cota
  falhar, espere e tente de novo). WebFetch e curl não abrem sites .gov.br, bancos centrais, BIS,
  FMI, SciELO e a maioria dos sites de texto integral nesta rede.
- Nunca cite "Frente X", "insumo", "painel irmão" ou "nesta rodada" no texto público: use a fonte
  primária que o insumo cita.
- Nenhuma marca "[a conferir]" no texto público. Número não confirmado não entra: reescreva sem ele e
  registre a pendência nas notas do bloco.
- Recorte entre aspas só se você teve o texto na frente (página de busca que o reproduz, PDF, resumo
  oficial), com autor, ano e página ou link; senão, paráfrase.
- Nenhum nome de pessoa privada e nenhuma alusão à conversa que originou o painel. Diga "a tese em
  teste", nunca "a tese do usuário".

## Forma da página

Frontmatter (id, titulo, pai, ordem, resumo em uma linha de 3 a 5 linhas de texto, estado: 1ª versão).
Corpo sem título repetido e sem abertura de metadiscurso ("Esta página..."). Exemplo de brinquedo antes
do dado real; fórmula em KaTeX seguida de exemplo resolvido; recortes citados; gráficos em
dados/<id>-*.json com fonte e consulta; quadro `:::afavor` / `:::contra` onde houver disputa; caixa
`:::painel` para a leitura própria; `## Para ler` no fim com referências completas.

## Pronto quando

Extensão do cartão cumprida; `python3 tools/build.py --check` sem ERRO nos seus arquivos (avisos de
link para páginas ainda não escritas são aceitáveis); `python3 tools/lint.py <seus arquivos>` sem
travessão, "não é X, é Y", palavra vetada, "Frente", "insumo", "esta página" ou "tese do usuário";
seção do item acrescentada ao fim do `_notas.md` do bloco (palavras, fontes principais, lacunas,
números que divergem de outras páginas). Não rode git e não rode o build sem `--check`.

Devolva só um resumo curto: o que escreveu (palavras), fontes principais, lacunas, números divergentes.

# Cartão de correção (aplicar o relatório de revisão de uma área)

Repositório: /home/user/juros-convencao-brasil. Leia antes: BRIEF.md, ESTILO.md, CONTEXTO.md,
conteudo/_CONVENCOES.md (inclusive "Dados primários já coletados"), conteudo/_divergencias.md
(inclusive "Decisões ... que valem para todo o painel") e o relatório conteudo/_revisao/<área>.md.

Tarefa: aplicar as correções do relatório nas páginas da área, editando os arquivos existentes (Edit),
sem reescrever do zero o que está bom. Regras de decisão:

1. Fontes internas fora do texto público: toda menção a "Frente A/C/I/J/K/L", "insumo", "painel
   irmão", "nesta rodada", "nesta sessão" vira a fonte primária que o insumo cita (abra
   insumos/frente-*.json e use o campo fonte/url da série ou da alegação: BCB SGS com código, Tesouro
   RMD com mês, FMI com edição, BIS, IBGE), com data de consulta. Vale também para os campos
   fonte/nota dos JSON em dados/<área>*.json.
2. Marcas "[a conferir]" saem do texto público. Para cada uma: se o número estiver em dados/brutos/
   (SGS, SIDRA, Focus, BIS), confira e cite "BCB, SGS <código>, consulta em 02/11/2026"; se der para
   confirmar com WebSearch (modo standard, poucas buscas, priorize gravidade 2 e 3), confirme e cite;
   senão, reescreva sem o número ou a afirmação e registre a pendência no _notas.md da área, seção
   "Pendências após a revisão".
3. Nenhuma alusão à conversa de origem. "A tese do usuário" vira "a tese em teste".
4. Números e contas: siga conteudo/_divergencias.md e o relatório; refaça as contas indicadas.
5. Gravidade 4 e 5: interpretação vai para `:::painel` ou "o painel lê"; reforce o contraponto onde o
   relatório aponta desequilíbrio; não chame de convenção o que a evidência só mostra como resíduo
   não explicado (diga que o resíduo é compatível com convenção e com outras explicações).
6. Estilo: corte metadiscurso de abertura, reduza os contrastes ", e não X", tire fechos de efeito;
   rode `python3 tools/lint.py conteudo/<pasta>/*.md` ao fim.
7. Achados de que você discorde: não aplique e explique em uma linha no _notas.md.
8. Não edite páginas de outras áreas. Se uma correção muda um número que outra área usa, liste no
   resumo final (página, número antigo, número novo, fonte).

Ao terminar: acrescente no topo de conteudo/_revisao/<área>.md uma seção "Aplicação (data)" com
achados aplicados, não aplicados (e por quê) e pendentes; mude o `estado` das páginas revisadas para
"revisada"; `python3 tools/build.py --check` sem ERRO. Não rode git nem o build sem --check.

Devolva só um resumo curto: achados aplicados, não aplicados, pendências e números que mudaram e que
outras áreas usam.

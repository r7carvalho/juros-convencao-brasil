# Notas do bloco 11 (Finanças públicas: os conceitos)

## 11.0

Arquivo: `conteudo/11-financas-publicas/11-financas-publicas.md` (id 11, pai 0, ordem 9). Redação de 02/11/2026.

Palavras: cerca de 1.780 de prosa e 2.180 contando as três tabelas (sem o "Para ler"); o `tools/lint.py` conta 2.510 tokens, porque separa números e inclui referências. Sem travessão, sem "não é X, é Y", sem palavra vetada.

Gráficos:
- `dados/11-dbgg-dlsp.json` (linha): DBGG conceito BCB (SGS 13762, desde dez/2006) e DLSP (SGS 4513, desde dez/2001), dezembro de cada ano e set/2026. Sobrepõe-se em parte ao gráfico dono `dados/3-divida-conceitos.json` (que traz também o conceito FMI, de 2006 a ago/2026). Se o coordenador preferir um dono só, trocar pelo da área 3 e perder 2001–2005 da DLSP.
- `dados/11-primario-juros-nominal.json` (empilhadas): NFSP primária (SGS 5793) e juros nominais (SGS 5727 − 5793), 12 meses, dez/2002 a dez/2025 e set/2026. A soma é a NFSP nominal. Nenhuma outra página tem essa decomposição (a 5.4.3 só mostra os juros, desde 2010).

Fontes principais: BCB, *Manual de Estatísticas Fiscais* (maio/2019), páginas citadas conforme o PDF de 27/09/2026 (pp. 8-15, 24-25, 33-40, 45-48); glossário fiscal do BCB (DFL); LC 200/2023, arts. 2º, § 1º, e 5º, § 3º; BCB, SGS 13762, 4513, 5793, 5727 e 4382 (coleta de 02/11/2026); tabela especial Divggnp (DBGG conceito FMI, consulta de 28/10/2026, via páginas 3.1 e 10.2.2); Tesouro, RMD de agosto de 2026 (LFT 52,74% da DPF).

Números usados e mês de referência:
- DBGG 82,93% e DLSP 69,98% do PIB em set/2026 (SGS). O ramo 3 cita agosto (82,9% e 69,3%): mesma série, mês diferente.
- DBGG conceito FMI 94,5% em ago/2026 (não há setembro na tabela lida).
- NFSP nominal 9,51%, primária 0,52% (déficit), juros 8,99% do PIB = R$ 1.204,8 bi em 12 meses até set/2026 (igual a `_divergencias.md`).
- Juros reais cerca de 5,5% do PIB em 2025: cálculo do painel da página 3.3 (IPCA sobre a DLSP do fim de 2024), não série oficial.
- De 2002 a 2013, superávit primário todos os anos e juros entre 4,44% (2012) e 8,42% (2003) do PIB (SGS 5727 − 5793).

Lacunas e pendências:
- As páginas do *Manual* do BCB vêm do PDF de 27/09/2026 descrito no material de base; o PDF não foi reaberto nesta redação (sites do BCB bloqueados na rede).
- A DFL não tem série em `dados/brutos/`; a página só a define.
- O *Manual de Demonstrativos Fiscais* aparece no "Para ler" sem link, porque a URL exata da 15ª edição não foi confirmada. O link da LC 200 segue o padrão do Planalto (`lcp200.htm`) e deve ser conferido.
- Para 11.2 e 11.4: o glossário fiscal do BCB foi editado sem aviso e tem verbetes que divergem do *Manual* (DFL, resultado nominal, juros das reservas no primário); preferir o *Manual* e citar o PDF datado.
- Para 11.4: o erro de "abater a privatização da NFSP" aparece num espelho de correção de banca de 2026; decidir se a página cita a prova como documento público ou descreve o erro de modo genérico, sem alusão à origem do material.
- Links para 11.1 a 11.8 geram aviso no build até as filhas existirem.

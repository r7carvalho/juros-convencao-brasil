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

## 11.1

Arquivo: `conteudo/11-financas-publicas/11.1-divida-bruta-e-liquida.md` (id 11.1, pai 11, ordem 1). Redação de 02/11/2026.

Palavras: cerca de 3.450 contando só palavras alfabéticas fora das tabelas e do "Para ler"; o `tools/lint.py` conta 4.704 tokens (números, tabelas e referências incluídos). Sem travessão, sem "não é X, é Y", sem palavra vetada.

Gráficos:
- `dados/11.1-bruta-liquida-reservas.json` (linha): DBGG menos DLSP (SGS 13762 e 4513), reservas em % do PIB (SGS 3546 × PTAX do último dia útil, SGS 1, sobre SGS 4382) e créditos do Tesouro ao BNDES (Divggnp, via série já usada em 3.2), dez/2006 a dez/2025 e ago/2026. Não repete os gráficos donos dos três conceitos (`3-divida-conceitos.json`, `9.1-divida-tres-conceitos.json`, `11-dbgg-dlsp.json`).
- `dados/11.1-ajustes-dlsp.json` (barras): ajustes patrimoniais e metodológicos por ano, 2002–2025, calculados como variação da DLSP em reais (razão × PIB de 12 meses, dez/dez) menos a NFSP nominal do ano (SGS 5727 × PIB), sobre o PIB. Cálculo do painel; aproxima a série oficial de ajustes da tabela de fatores condicionantes da DLSP, que o painel não tem.

Fontes principais: BCB, *Manual de Estatísticas Fiscais* (maio/2019), pp. 8-15, 24-25, 33-40 e 45-48 (páginas conforme o PDF de 27/09/2026 descrito no material de base; PDF não reaberto); glossário fiscal (DFL); SGS 13762, 4513, 5727, 5793, 3546, 1788, 28964, 1 e 4382 (coleta de 02/11/2026); Divggnp.xlsx (BNDES, conta única, compromissadas, conceito FMI, consulta de 28/10/2026); Tesouro, RMD de ago/2026 (DPF R$ 9,292 tri, DPMFi R$ 8,944 tri, DPFe ≈ R$ 348 bi por diferença, LFT 52,74%, 16,39% vencendo em 12 meses) via Ministério da Fazenda e imprensa de 28/09/2026; LC 200/2023, art. 2º, § 1º; FMI CR 23/289 (como em 10.2.2).

Conciliação DBGG → DLSP de ago/2026 (% do PIB): 82,87 + base monetária 3,24 + depósitos voluntários 1,24 − reservas 14,47 − BNDES 1,75 = 71,13; DLSP 69,27; demais itens −1,86 por diferença. Memória: títulos livres na carteira do BC 11,66 e conta única 13,54 se anulam na consolidação.

Números novos e contas do painel:
- Reservas em % do PIB: 7,6 (2006), 15,8 (2012), 23,2 (2015), 14,47 (ago/2026), 14,03 (set/2026). Distância bruta − líquida: 9,0 (2006), 21,0 (2013), 29,9 (2015, máximo), 13,6 (ago/2026), 12,95 (set/2026).
- Ajustes na DLSP: 2002 +10,0; 2008 −3,4; 2015 −6,0; 2016 +3,1; 2020 −5,1; 2024 −3,3 pontos do PIB; 2011–2015 somam −12,1.
- Sensibilidade: posição líquida em dólar ≈ 11,9% do PIB (reservas 14,47 − DPFe 2,61); 10% de depreciação ≈ −1,2 p.p. na DLSP e +0,3 p.p. na DBGG (sem swaps e sem dívida externa de estados e municípios).
- LFT (≈ R$ 4,9 tri) + compromissadas (R$ 1,37 tri) ≈ R$ 6,3 tri = 47% do PIB e 57% da DBGG em ago/2026.
- DLSP de 69,98% em set/2026 é o maior valor do SGS 4513 (série iniciada em dez/2001); imprensa de 29/10/2026 diz o mesmo.

Lacunas e pendências:
- A abertura oficial da DLSP por componente (créditos do FAT, aplicações, compulsórios, dívida líquida do BC e das estatais) não estava nos dados; a conciliação fecha com uma linha "demais itens" por diferença. Sugestão: acrescentar ao coletor a tabela de DLSP por componente das Estatísticas Fiscais ou as séries SGS correspondentes.
- DFL sem série nos dados brutos; a página só a define e mostra os ajustes pelo cálculo acima.
- DPFe tomada como DPF − DPMFi (R$ 348 bi, igual ao que 3.1 e 3.4 citam como R$ 348,26 bi); o PDF do RMD não foi aberto (hosts bloqueados).
- Custo de carregamento das reservas segue sem estimativa oficial ano a ano (mesma lacuna da 3.2).

Divergências com outras páginas: nenhuma nova. A 3.1 usa ago/2026 (DLSP 69,3%); a 11.1 traz agosto e setembro com o mês dito. A 9.1 diz que as devoluções do BNDES "quase não mexem na líquida"; a 3.1 e a 11.1 mostram que entre 2018 e 2022 a líquida subiu 3,4 pontos enquanto a bruta caía 3,6 (compatível: a devolução em si é neutra; a alta da líquida veio de outros fatores). Datas das devoluções: a 11.1 diz "iniciadas em 2016" (Divggnp: 8,58% em 2015 para 6,85% em 2016); a 3.2 trata 2017–2019 como o período das devoluções. Observação de processo: um `python3 tools/build.py --help` rodou por engano o build completo e regravou `docs/`; o `git status` ficou limpo depois, de modo que a saída coincidiu com a versão já commitada.

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

## 11.2

Arquivo: `conteudo/11-financas-publicas/11.2-resultados-fiscais.md` (id 11.2, pai 11, ordem 2). Redação de 02/11/2026.

Palavras: cerca de 3.370 de prosa fora das tabelas e do "Para ler" (3.660 com as tabelas); o `tools/lint.py` conta 4.901 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada.

Exemplo de brinquedo: uma federação (Tesouro com LFT, LTN e NTN-B; banco central com compromissadas, reservas e swaps; um estado; crédito a banco de fomento), diferente do município da página 11. Mostra quatro juros: 51 pagos no orçamento, 141 apropriados na dívida do Tesouro, 164 nominais líquidos do consolidado, 119 reais.

Gráficos:
- `dados/11.2-tres-resultados.json` (linha, mensal, dez/2002 a set/2026): NFSP primária (SGS 5793), nominal (SGS 5727) e operacional calculado pelo painel.
- `dados/11.2-juros-correcao-real.json` (empilhadas, anual 2002–2025 e 12 meses até set/2026): atualização monetária estimada e juro real.
- Reusa `dados/3.5-juros-2025-medidas.json` (dono: 3.5) para as medidas de juros de 2025.
- Script: `tools/analises/11.2_resultados.py` (refaz os dois JSON; `--resumo` imprime médias por período, somas e a comparação com o SGS 5839).

Método do juro real (declarado na página): juros nominais (5727 − 5793) menos IPCA de 12 meses (SGS 13522) vezes a DLSP de 12 meses antes em reais (SGS 4513 × SGS 4382 do mês m−12), sobre o PIB de 12 meses do mês m. É o método de 3.3 e 3.5 para 2025, estendido. Operacional = primário + juro real.

Números da conta do painel: 2025 atualização 2,41% do PIB (R$ 307,0 bi; 3.5 diz "cerca de R$ 308 bi", mesma conta com arredondamento) e juro real 5,50% (R$ 700,0 bi); 12 meses até set/2026 atualização 2,76% (≈R$ 370 bi) e juro real 6,23% (≈R$ 834 bi); operacional 6,75%. Médias: 2002–2013 primário −2,91, juros 6,05 (2,63 + 3,42), operacional +0,51; 2014–2019 operacional 5,52; 2023–2025 operacional 6,05, juro real 5,01. Soma 2002–2025 em reais correntes: juros nominais R$ 8,5 tri, juro real R$ 5,0 tri (59%). Juro real negativo só em 2021 (−0,23%).

Fontes principais: BCB, *Manual de Estatísticas Fiscais* (maio/2019, pp. 13-15, 33-34, 47; páginas conforme o material de base, PDF não reaberto) e edição de março/2018 (recorte do conceito operacional, lido em resultado de busca); BCB, SGS 5793, 5727, 4513, 4382, 13522 (coleta de 02/11/2026); BCB, notas de Estatísticas Fiscais de 30/12/2024 (swap de nov/2024 e nov/2023, via resultado de busca), 30/01/2026 (2025 por esfera, via Poder360 e CNN Brasil) e 29/10/2026 (set/2026, via Agência Brasil); BNDES e FGV IBRE (decomposição de Borça Jr. e Barbosa Filho: swaps +1,0% do PIB em 2024 e −0,8% em 2025; juro real sem swaps 3,1% e 5,3%); Câmara, Estudo Técnico 16/2025 (Moura, Oliveira e Volpe); Inesc (R$ 371,7 bi) e BGU via análises secundárias (R$ 363,6 bi).

Lacunas e pendências:
- SGS 5839: o coletor a rotula "juros nominais (conferir)", mas ela não é juros nominais. Vai de dez/1999 a dez/2009 e os valores de dezembro (2002 −2,11; 2003 4,34; 2004 1,46; 2005 5,09; 2006 3,46; 2007 1,69; 2008 1,16; 2009 4,20) ficam sempre abaixo de 5727 − 5793 (7,61 a 5,13) e se movem ao contrário dos IGPs (baixos em 2002, 2004, 2007 e 2008; altos em 2005 e 2009). O padrão é compatível com os juros reais do conceito operacional oficial (deflator geral de preços sobre a dívida interna líquida), mas o nome da série não foi confirmado (sites do BCB e dadosabertos bloqueados; a busca não trouxe o rótulo). Pela numeração vizinha (5727 nominal, 5760 juros nominais e 5793 primário, totais do consolidado em blocos de 33 códigos), 5839 pode ser até uma subdivisão por esfera. Ficou fora da página e dos gráficos; a comparação está no `--resumo` do script. Sugestão: conferir o rótulo no SGS e corrigir a descrição em `tools/coletar.py`; se for o juro real oficial, acrescentar ao gráfico de 11.2 como série de 1999–2009.
- Abertura dos juros nominais por esfera (governo central, regionais, estatais, BC) não encontrada para 2025 nem para set/2026; a página dá a abertura só do primário de 2025.
- Resultado anual dos swaps em reais (2024 e 2025) não encontrado na fonte primária; a página usa as razões do PIB do BNDES/FGV IBRE.
- O recorte do conceito operacional vem da edição de 2018 do *Manual*, lida em resultado de busca, sem página. Os dois outros recortes do *Manual* (regime caixa/competência e resultado nominal) também foram lidos em resultado de busca; as páginas citadas (pp. 13-15 e 33) seguem o mapeamento do material de base.
- PDF do Estudo 16/2025 da Câmara não aberto; só a conclusão geral (competência tende a superar o orçamento) entra.

Divergências com outras páginas:
- 9.1 diz que parte da diferença entre juros pagos e apropriados vem da "rolagem (parte do juro é paga com emissão de novos títulos)". A 11.2 não repete esse item: o refinanciamento, pela LRF, paga principal e atualização monetária; a diferença que a 11.2 explica vem do tempo (juro capitalizado em LFT e LTN e pago no resgate), da classificação da correção como amortização, da abrangência (BC, estados, estatais) e de os juros do BCB serem líquidos e incluírem swaps. Sugestão para a revisão do bloco: reler o item de 9.1.
- Juro real de 2024: a conta do painel dá 5,36% do PIB (com swaps) e 4,36% (sem swaps); BNDES/FGV IBRE dá 3,1% sem swaps. A página explica que os níveis diferem pelo método e que o salto 2024–2025 (cerca de 2 pontos) aparece nas duas contas. CONTEXTO.md cita "juro real de 3,1% para 5,3% do PIB entre 2024 e 2025": é a série do BNDES/FGV IBRE, não a do painel.

## 11.3

Arquivo: `conteudo/11-financas-publicas/11.3-acima-e-abaixo-da-linha.md` (id 11.3, pai 11, ordem 3). Redação de 02/11/2026.

Palavras: cerca de 3.080 palavras alfabéticas fora das tabelas e do "Para ler" (inclui as referências entre parênteses no texto); o `tools/lint.py` conta cerca de 4.800 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada.

Exemplo de brinquedo: padaria com dois cadernos (caixa × extrato), discrepância de 3 (2 de tempo, 1 de omissão) e um passivo com o moinho que nenhum dos dois registra (análogo das pedaladas). Não repete a tabela de sinais da 11.2; usa o sinal do RTN só na fórmula e remete à 11.2.

Gráfico: `dados/11.3-primario-12m-2012-2016.json` (linha, mensal, jan/2012 a dez/2016, SGS 5793). Mostra o salto de 0,88% para 1,86% do PIB entre nov e dez/2015 (pagamento dos passivos do Acórdão 825/2015). Recorte da série que a 11.2 mostra inteira; o recorte existe para tornar visível o degrau de dezembro de 2015.

Fontes principais: BCB, *Manual de Estatísticas Fiscais* (maio/2019, pp. 8, 13-15, 33, 39; p. 15 nota 4 para o registro por competência dos subsídios desde dez/2015; páginas conforme o material de base, PDF não reaberto); BCB, nota de Estatísticas Fiscais de 08/11/2023 (PIS/Pasep, recorte lido em resultado de busca), notas de 31/01/2025 e 30/01/2026; BCB, Nota Metodológica DSTAT 2020/002 (FIES); SGS 5793 e 4382 (coleta de 02/11/2026); LC 200/2023, art. 5º, § 3º (recorte conferido no texto reproduzido pela Câmara e pela CBIC em resultado de busca); Tesouro, RTN (estrutura da tabela 1, boletim de fev/2020; tratamento semestral dos subsídios, boletim de set/2025), nota metodológica de conciliação GCO, apresentação do FIES de 18/07/2017, Relatório de Avaliação do Cumprimento das Metas Fiscais do 1º quadrimestre de 2026; Prisma Fiscal, nota especial de nov/2020; TCU, Acórdãos 825/2015, 2.461/2015 e 3.297/2015 (via notícias do TCU e imprensa), Contas do Presidente de 2025 (ficha de achados, via resultado de busca); IFI, RAF 108; Gobetti e Orair (2017), Ipea TD 2288 (só o resumo).

Números e de onde vêm:
- Governo central 2025: RTN déficit R$ 61,69 bi (0,48% do PIB); BCB déficit R$ 58,69 bi; diferença +3,0 bi. Meta: zero, banda −0,25 p.p.; TCU desconta R$ 48,7 bi de despesas excluídas e considera cumprida.
- 2024: RTN déficit R$ 43,0 bi; BCB governo central R$ 45,4 bi (CNN Brasil; consolidado R$ 47,6 bi na nota do BCB de 31/01/2025); diferença −2,4 bi.
- 2023: RTN déficit R$ 230,5 bi; BCB governo central "cerca de R$ 254,5 bi" só na cobertura do Poder360 de 07/02/2024 (não achei o número na nota do BCB); diferença ≈ −24 bi, compatível com os R$ 26,0 bi do PIS/Pasep. Confiança média; conferir na tabela do BCB.
- FIES 2016: discrepância de R$ 8,9 bi, dos quais ≈ R$ 7 bi do FIES; déficit de 2016 no RTN revisto de R$ 154,3 bi para R$ 161,3 bi (imprensa de 18/07/2017 citando a apresentação do Tesouro).
- Pedaladas: TCU estimou ≈ R$ 40 bi omitidos da dívida em 2014; pagamento de R$ 72,4 bi em dez/2015 (BNDES 30,0; FGTS 22,6; BB 18,2; Caixa 1,5), dos quais R$ 55,6 bi passivos do Acórdão 825 e R$ 16,8 bi de 2015 (nota da Fazenda via imprensa; algumas matérias dizem R$ 55,8 bi). Dez/2015: déficit primário consolidado de R$ 71,7 bi no BCB (imprensa); governo central 2015 no RTN R$ 114,9 bi. SGS 5793 dá 1,86% do PIB em dez/2015; a imprensa de jan/2016 dizia 1,88% (série revista).

Lacunas e pendências:
- Sites gov.br, cdn.tesouro.gov.br, sites.tcu.gov.br e repositorio.ipea.gov.br bloqueados (WebFetch e curl); nada de RTN em `dados/brutos/` além dos metadados do CKAN. Sem série histórica da discrepância ano a ano; sugestão: incluir no coletor a planilha "Resultado do Tesouro Nacional - Série Histórica" (linhas de ajuste metodológico e discrepância) e montar o gráfico RTN × BCB de 1997 a 2026.
- A nota metodológica do Tesouro sobre a conciliação foi lida só em resultado de busca; o texto parafraseia (sem aspas). O significado exato da linha "ajuste metodológico Itaipu" do RTN não foi confirmado e ficou fora.
- Mecanismo exato do FIES na dívida líquida (por que o BCB captava impacto primário) não confirmado; a página só diz que o BCB captava pela evolução dos saldos.
- Não achei RAF da IFI dedicado à discrepância; só o uso da linha de ajustes e discrepância no RAF 108.
- Abertura do resultado de 2015 do governo central pelo BCB não encontrada.
- A afirmação de que o BCB apura estados e municípios separadamente e estatais por esfera segue o conhecimento das tabelas das Estatísticas Fiscais, sem página do *Manual*.

Divergências com outras páginas: nenhuma nova. Os números de 2025 por esfera são os mesmos da 11.2 (governo central −58,7 no BCB). A 11 e a 11.2 chamam o critério do BCB de abaixo da linha e o do Tesouro de acima da linha, como aqui.

## 11.4

Arquivo: `conteudo/11-financas-publicas/11.4-armadilhas-conceituais.md` (id 11.4, pai 11, ordem 4). Redação de 02/11/2026.

Palavras: cerca de 3.180 de prosa fora das tabelas, das fórmulas e do "Para ler" (cerca de 3.360 com o quadro-resumo); o `tools/lint.py` conta 5.126 tokens (números, alvos de link e referências incluídos). Sem travessão, sem "não é X, é Y", sem palavra vetada. `build.py --check` sem erro; avisos só para links a 11.5, 11.7 e 11.8, ainda não escritas.

Estrutura: oito armadilhas, cada uma com a afirmação formulada como "confusão comum", por que parece certa, a regra com fonte e página, um exemplo resolvido em caixa `:::exemplo` e o lugar no debate sobre juros, com links para as páginas que usam o conceito. Abre com o teste "muda a DLSP? é receita/despesa não financeira ou juro do período? se não, é ajuste" e a identidade do *Manual*, p. 39; fecha com quadro-resumo e `:::painel`. O padrão de erro da privatização (chamar de NFSP a variação da DLSP depois de abater a venda; inverter os sinais de NFSP = ΔDLSP + privatização − outros ajustes; "a privatização reduz a NFSP no curto prazo") entra com números próprios do painel (estado com primário −30, juros 90, venda de 50), sem os números nem qualquer menção à origem do erro. As divergências entre o glossário fiscal e o *Manual* (prometidas pela 11.2) estão numa `:::nota` da primeira armadilha e numa frase da armadilha do BC.

Gráficos: nenhum JSON novo. Reusa `dados/11.1-ajustes-dlsp.json` (dono: 11.1) na armadilha do câmbio e `dados/11-primario-juros-nominal.json` (dono: 11) na do superávit.

Fontes principais: BCB, *Manual de Estatísticas Fiscais* (maio/2019), pp. 12-15, 24, 32-40, 45-48, páginas conforme o PDF de 27/09/2026 do material de base (PDF não reaberto; sites do BCB bloqueados); glossário fiscal do BCB (versão de 27/09/2026, e a redação anterior do verbete "resultado nominal", ambas conforme o material de base); STN, MDF 15ª ed., PDF pp. 266-267; LRF arts. 29 (V e § 1º) e 44 (recorte do art. 44 conferido em resultado de busca que reproduz o texto); LC 200/2023, arts. 2º, § 1º, e 5º, § 2º; SGS 1788, 13522, 4513, 13762, 5727, 5793, 4382 (coleta de 02/11/2026); Garcia (2003), *Valor*, 28/10/2003 (esqueletos de 6,1 p.p. do PIB em ago/2003, DLSP 57,7% contra 51,6% sem eles; lido em resultado de busca); Agência Brasil 29/01/2020 (cessão onerosa: R$ 69,96 bi de bônus em dez/2019, déficit do governo central de R$ 95,1 bi em 2019); Poder360 2019 (estatais de R$ 802 bi); Poder360 2023 (LCA sobre classificar encargos de precatórios como despesa financeira); JB jun/2026 (PEC 65/2023 no Senado).

Números e contas do painel:
- Imposto inflacionário nos 12 meses até set/2026 ≈ R$ 20 bi (0,15% do PIB) = base monetária de R$ 434,9 bi (SGS 1788, set/2026) × IPCA 12m de 4,58% (SGS 13522); contra atualização monetária da dívida de 2,76% do PIB (≈ R$ 370 bi, 11.2). Aproximação (a fórmula exata usa π/(1+π) e a base média): dá ≈ R$ 19 bi.
- Precatórios de dez/2023: R$ 92,4 bi ≈ 0,84 p.p. do PIB (3.2) sobre déficit primário consolidado de 2,28% do PIB em 2023 (SGS 5793) = 37%, "mais de um terço". A imprensa da época (nota do BCB de fev/2024) dava 2,29% e R$ 249,1 bi; a série foi revista. Usei o SGS.
- Alívio de uma venda de 5 p.p. do PIB com r − g = 3 p.p.: 0,15 p.p. de primário por ano (conta de brinquedo).
- Câmbio: ajustes +10,0 (2002) e −3,3 (2024) p.p. do PIB, e swaps +1,0 p.p. nos juros em 2024: números da 11.1 e da 11.2.
- BC: lucro de R$ 270,9 bi em 2024 (cambial 242,8) e R$ 325 bi ao Tesouro em 2020: números da 10.2.2.

Lacunas e pendências:
- Bônus de outorga da Eletrobras (2022): valores divergentes nas fontes (R$ 23,2 bi no PPI, R$ 25,3 bi no TCU, R$ 26,6 bi na apresentação da companhia) e sem confirmação do registro no primário; ficou fora. O exemplo de concessão usado é a cessão onerosa de 2019.
- Total de receitas de privatização dos anos 1990 (US$ 105 bi circula sem fonte localizada; o BNDES dá US$ 63,7 bi para o PND federal com outro recorte e US$ 34,7 bi para os estados em 1996–2002): não entrou. Sem série recente da linha "privatizações" dos fatores condicionantes da DLSP.
- Que o BCB registra o pagamento de precatórios como despesa primária vem da prática (dez/2023 no SGS 5793 e cobertura de imprensa) e de declaração do então presidente do BC relatada sem data clara; a classificação final dos encargos em 2023 (financeira ou primária) não foi confirmada e a página não a afirma.
- A afirmação de que o programa de 2019 era "defendido também como meio de reduzir a dívida" se apoia em coberturas de imprensa (Poder360 e outras) lidas só em resultado de busca.
- O verbete explicativo que descreve o primário como "economia para pagar juros" não foi citado com fonte; a página fala em "linguagem corrente".

Divergências com outras páginas: nenhuma nova. Déficit primário de 2023: a página usa 2,28% (SGS 5793, igual ao JSON da página 11); a cobertura de fev/2024 dizia 2,29%.

## 11.5

Arquivo: `conteudo/11-financas-publicas/11.5-risco-fiscal.md` (id 11.5, pai 11, ordem 5). Redação de 02/11/2026.

Palavras: cerca de 3.500 de prosa fora das tabelas, das fórmulas, dos parênteses de fonte e do "Para ler" (3.760 contando as referências no texto); o `tools/lint.py` conta 5.400 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada. `build.py --check` sem erro; aviso só para o link a 11.7, ainda não escrita.

Estrutura: exemplo de brinquedo (família com dívidas diretas, ação trabalhista de 60 com 30% de chance, fiança de 40 com 10%; exposição 100, perda esperada 22; o banco cobra 2 pontos pelo comportamento, não pelo parecer); sentido legal (LRF art. 4º, § 3º, citado; art. 5º, III, "b"; MDF 15ª ed. pp. 58-60, matriz direta/contingente × explícita/implícita; riscos gerais e específicos do Anexo V; fórmula da perda esperada); tamanho dos passivos contingentes (tabela de dez/2025 e gráfico); precatórios (fluxo, EC 113/114, ADIs 7.047 e 7.064, MP 1.200, EC 136, PLDO e PLOA 2027, projeção do Tesouro em gráfico); sentido de mercado (CDS, prêmio a termo, inclinação e inflação implícita com fórmula de Fisher e exemplo); medição do prêmio (BCB RI dez/2022, RPM jun/2025 e WP 637; IFI RAF 116; FMI CR 25/194) com três cuidados de método; ponte lei → preço; quadro A favor / Contra e `:::painel`. Não repete os episódios de 6.1.1 nem o registro contábil do precatório de 11.4; liga para 3.2, 6.1, 6.1.1, 6.1.2, 7.2, 7.7, 1.5.2, 2.5, 3.1, 11.4 e 11.7.

Gráficos: `dados/11.5-riscos-especificos-2025.json` (barrash, % do PIB, cinco grupos que somam 37,9%; "outros riscos primários" e "outros riscos financeiros" por diferença; garantias = 336,6 / PIB de 2025 do SGS 4382) e `dados/11.5-precatorios-fora-da-meta.json` (barras, R$ bi, projeção do Tesouro de 12/01/2026: 2026–2030 e 2035; 2031–2034 não divulgados na cobertura).

Fontes principais: LRF (texto do § 3º conferido em reproduções do dispositivo em resultado de busca); MDF 15ª ed. (páginas conforme o material de base); PLDO 2027, Anexo V, via IFI RAF 112 (21/05/2026) e Nota Técnica Conjunta das consultorias de orçamento; JOTA (abr/2026, via CNPL) para as tributárias; Agência Câmara (LDO 2026, dados de 2024) e Conjur (17/04/2024, LDO 2025); AGU (jan/2026); BGU 2025 (provisões); Tesouro, Relatório de Garantias Honradas (dez/2025 e jan/2026) e Relatório de Projeções Fiscais (12/01/2026, via CNN, Exame, Times Brasil); Insper, Mendes, Coelho, Lisboa e Barbosa (2025); IFI RAF 116 (17/09/2026; Poder360 de 19/09/2026); BCB, RI dez/2022 e RPM jun/2025 (boxes) e WP 637; FMI CR 25/194; Anbima ETTJ (28/10/2026); Focus (dados/brutos, 23/10/2026); CNN e Exame (Correios, 28/10/2026); STF (ADIs 7.047 e 7.064). Todos os sites .gov.br, senado.leg.br, camara.leg.br, tcu, insper e repec estavam bloqueados ao WebFetch; os números vêm de trechos e resumos de busca que citam o documento primário.

Números e contas do painel:
- Exposição de dez/2025: 4.828,6 (37,9%), primários 3.149,3 (24,7%), demandas judiciais 2.273,2 (17,8%), financeiros 1.679,3 (13,2%), haveres 888,8 (7,0%) (IFI RAF 112). Pico de 57,2% do PIB em 2022.
- Demandas judiciais: ≈ 3,6 tri (dados de 2023, ≈ 1 tri provável), ≈ 2,6 tri (dados de 2024; possível −18,7%, provável −45,1%), 2.273,2 bi (2025; possível de 2.101,5 para 1.740,0). Provável de 2025 ≈ 533 bi por diferença (cálculo do painel), próximo das provisões judiciais e administrativas do BGU 2025 (14,17% de R$ 3,636 tri ≈ R$ 515 bi).
- Tributárias 2025: 805,8 (provável 172,6, contra 224,7 em 2024; possível 633,2, contra 649,2).
- Garantias: estoque 336,6 bi (35,7 de estados no RRF); honradas 11,08 bi em 2025 (MG 32%), 86,5 bi desde 2016, 6,03 bi recuperados.
- Precatórios e RPV: 2026 autorizado 73,8 + 44,2; PLOA 2027 51,3 + 46,4 = 97,7; 39,4% na meta em 2027 (R$ 38,4 bi no PLOA), 56,2% em 2028, 100% em 2036; PLDO estimava R$ 57,8 bi fora em 2027; projeção do Tesouro de jan/2026 (com 10% mínimo): 57,8 / 96,1 / 98,7 / 91,3 / 85,1 (2026–2030) e 21,6 em 2035. IFI: execução média de 0,6% do PIB (2018–2022) e 0,7% (2024–2026).
- Inflação implícita de 1 ano em 28/10/2026: (1,142476 / 1,067635) − 1 = 7,01% (Anbima ETTJ, vértice 252 du), contra Focus 12 meses ≈ 4,5% em 23/10/2026 (dados/brutos/focus-inflacao_12m.json, mediana não suavizada 4,53 a 4,57).
- IFI: contribuição média da dívida bruta ao prêmio ACM de 5 anos de 3,16 p.p. nos 12 meses até ago/2026.

Lacunas e pendências:
- O total de demandas judiciais de 2,27 tri e a queda do risco possível de 2.101,5 para 1.740,0 bi vêm de trechos de busca (IFI e Anexo V); conferir na Tabela de demandas judiciais do Anexo V do PLDO 2027. O provável de 2025 (≈ 533 bi) é derivado por diferença.
- APET afirmou que o total "no fechamento de 2025" era R$ 2,607 tri segundo o anexo da LDO 2026; parece confundir o ano de referência (a LDO 2026 traz dados de 2024) e não foi usado.
- Estoque do FCVS em reconhecimento e valores de fundos e estatais no anexo: não localizados; a página cita o FCVS sem número.
- Tabela de sensibilidade da dívida do Anexo V (efeito de 1 p.p. de Selic, PIB e primário): não localizada; a página usa o R$ 61,7 bi da DLSP (decisão de divergências) e a frase do Tesouro sobre sensibilidade alta a juros curtos e baixa ao câmbio.
- RI dez/2022 e RPM jun/2025: conclusões lidas em resumos de busca, sem coeficientes; o nível do prêmio ACM de 5 anos não foi localizado. A IFI também cita choque de um desvio-padrão da dívida associado a ≈ 2,16 p.p.; não usado por falta de contexto.
- Data exata do texto da APET e do TCU sobre o PLDO 2027 não confirmada (2026 pela ordem dos fatos).
- Os R$ 12 bi de empréstimo dos Correios de dez/2025: a página não afirma que tiveram garantia da União (só o de R$ 7 bi, DOU de 28/10/2026).
- Sugestão: pôr no coletor a série histórica do Anexo de Riscos Fiscais (exposição por grupo, 2015–2025) para um gráfico de linha, e a série de despesas com sentenças judiciais (SIOP) para o fluxo anual.

Divergências com outras páginas: nenhuma nova. Precatório de dez/2023 (R$ 92,4 bi, 0,84 p.p., R$ 60,1 bi represados), superávit de 2022 (R$ 54,1 bi) e exclusões de 2025 (R$ 48,7 bi, 41,1 de precatórios) iguais a 3.2, 6.1.2 e 7.7. CDS de 110 (09/10/2026), 120→152 (26/10/2026) e 205 (fim de 2024) iguais a 6.1 e 6.1.1. O FMI (CR 25/194, um terço da depreciação de 2024 por risco doméstico) responde em parte à ressalva do `:::painel` de 6.1, que dizia faltar a comparação com outras moedas; sugerir à revisão da área 6 acrescentar o número lá.

## 11.6

Arquivo: `conteudo/11-financas-publicas/11.6-regras-fiscais.md` (id 11.6, pai 11, ordem 6). Redação de 02/11/2026.

Palavras: cerca de 3.530 de prosa fora das tabelas, das fórmulas, dos parênteses de fonte e do "Para ler" (cerca de 3.800 contando os parênteses); o `tools/lint.py` conta cerca de 6.000 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada. `build.py --check` sem erro; aviso só para o link a 11.7.

Estrutura: exemplo de brinquedo (família com renda 100, gasto 90, dívida 200 a 5%; quatro regras; ano de queda de 10% em que a regra de resultado exige corte de 11% e a de despesa deixa a dívida ir a 210,5; juro dobrado em que as regras de resultado e despesa seguem cumpridas e a dívida sobe); tipologia com tabela (FMI, Fiscal Rules Dataset) e as oito propriedades de Kopits e Symansky (1998); LRF, regra de ouro, teto e arcabouço (fórmula do limite com exemplo); desempenho com gráfico e tabela por regime; por que o Brasil trocou de regra; Chile, UE e Suíça; evidência sobre regras e spread; a ligação com o juro pelo $s^*$, com as leituras das duas teses, quadro A favor / Contra e `:::painel`. Não repete os episódios de mercado (6.1.1), os precatórios (11.5), a apuração BCB × Tesouro (11.3) nem o argumento da despesa obrigatória (6.1.2); liga para eles.

Gráficos:
- `dados/11.6-meta-resultado-governo-central.json` (barras, % do PIB, 2016–2026): piso legal da meta, resultado cheio (RTN, valores divulgados em janeiro do ano seguinte) e resultado para fins de meta (2023–2026). Conversão para % do PIB com SGS 4382 (dezembro); 2026 com o PIB implícito na meta (R$ 34,3 bi = 0,25%, ≈ R$ 13,72 tri). 2020 sem barra de meta (dispensada pelo Decreto Legislativo 6/2020).
- Reusa `dados/3.1-primario-estabilizador.json` (dono: 3.1).

Fontes principais: LRF (arts. 4º, 9º, 12, 19, 35, 42); CF art. 167, III (recorte conferido em resultado de busca que reproduz o texto); EC 95, 106, 109, 113, 114, 123, 126 e 136; LC 200/2023 e LC 211/2024 (dispositivos conforme o texto do Planalto de 27/09/2026 descrito no material de base); Tesouro, RTN (2016–2025, via imprensa) e Relatório de Avaliação de Receitas e Despesas Primárias do 4º bimestre de 2026 (24/09/2026, via Agência Brasil e CNN Brasil); IFI (nota sobre o PLDO 2026; RAF 108, 116 e 117); Blog do IBRE (31/01/2022); Bráulio Borges para a BBC (R$ 794,9 bi acima do teto em 2019–2022); Gazeta do Povo (2022); Consultoria de Orçamento da Câmara (Informativo PLDO 2027); Prisma Fiscal de outubro de 2026; FMI (Fiscal Rules Dataset; WP/25/195 de Acalin, Martinez e Roch; SDN/2025/004); Banco Mundial (PRWP 10741); Kopits e Symansky (1998); Feld et al. (2017); Heinemann, Moessinger e Yeter (2018); Paetz e Truger (2015); Dipres e CFA (Chile); Regulamento (UE) 2024/1263; BCB, SGS 5793, 5727, 13762, 4513 e 4382 (coleta de 02/11/2026). Todos os sites .gov.br, ipea, ebc e senado estavam bloqueados ao WebFetch; os números vêm de trechos de busca que citam o documento primário.

Números e contas do painel:
- Governo central (R$ bi; meta = resultado mínimo aceito): 2016 −170,5 / −154,3 (revisto depois para −161,3, ver 11.3); 2017 −159 / −124,4; 2018 −159 / −120,3; 2019 −139 / −95,1; 2020 meta dispensada / −743,1; 2021 −247,1 / −35,1; 2022 −170,5 / +54,1; 2023 −213,6 (LDO −65,9) / −230,5, −138,1 sem precatórios; 2024 piso −0,25% / −43,0, −11,0 para fins de meta; 2025 piso −0,25% / −61,7, −13,0 (exclusões de 48,7); 2026 piso 0 / projeção −80,9, −13,6 para fins de meta, contingenciamento de 13,6.
- Médias por regime (setor público consolidado, SGS 5793 e 5727, dezembro): primário +2,91 (2002–2013), −1,63 (2014–2016), −1,89 (2017–2022; −1,36 em 2017–2019), −1,04 (2023–2025; ≈ −0,8 sem os precatórios de 2023); juros 6,05 / 6,75 / 5,23 / 7,51% do PIB. DLSP 59,9 (2002) → 30,5 (2013) → 46,1 (2016) → 56,1 (2022) → 65,2 (2025) → 70,0 (set/2026); DBGG 55,5 (2006) → 51,5 → 69,8 → 71,7 → 78,6 → 82,9.
- $s^*$ de brinquedo: d = 0,80, g = 2%: 2,4% do PIB com r = 5% e 4,7% com r = 8%; 0,8 p.p. de primário por ponto de juro real.

Lacunas e pendências:
- Metas e resultados de 2001–2015 ano a ano (setor público consolidado em % do PIB e governo central) não foram montados: não havia tabela consolidada acessível; o gráfico começa em 2016. Sugestão: pôr no coletor a planilha de série histórica do RTN e os Anexos de Metas Fiscais das LDOs (ou a tabela do Blog do IBRE de 31/01/2022) e estender o gráfico a 2001.
- Autor do post do Blog do IBRE "21 anos de meta de resultado primário" não confirmado; citado sem autor.
- Valores aprovados de crédito para a regra de ouro em 2021 (PLN 9/2021: pedido de R$ 164 bi, relatório que propunha aprovar só R$ 28,5 bi), 2022, 2023 e 2024 não confirmados; a página cita 2019, 2020, a insuficiência de 2021 e o PLN 14/2025.
- Composição das deduções de 2026 (R$ 67,3 bi = 80,9 − 13,6) por item (precatórios, saúde, educação, defesa) não localizada; a página cita só o total implícito e o resultado para fins de meta.
- O resultado de 2022 aparece como R$ 54,1 bi (RTN) e R$ 54,9 bi (TCU, possivelmente BCB); a página usa o RTN.
- O total de R$ 794,9 bi acima do teto (Borges) inclui os créditos extraordinários da pandemia, que o teto já excluía; a Gazeta do Povo dá R$ 840 bi com outro recorte. A página usa Borges e diz o que inclui.
- Números da UE (1 e 0,5 ponto de redução da dívida; margem de 1,5% de déficit estrutural) e da meta chilena de 2001 vêm do conhecimento do regulamento e da literatura, confirmados só em parte pela busca (o Conselho da UE confirma a trajetória de despesa e os planos de 4 a 7 anos); conferir no Regulamento (UE) 2024/1263.
- Dívida federal suíça em % do PIB não localizada; a página diz só que caiu.
- PRWP 10741 do Banco Mundial: título e autores não confirmados (a busca sugere Islamaj, Samano e Sommers); citado pelo número.

Divergências com outras páginas:
- 7.8 diz metas de "zero em 2024 e 2025 e superávit de 0,25% em 2026" e déficit consolidado de 0,40% (2024) e 0,43% (2025) pelo SGS 5793: compatível. A 11.6 acrescenta o resultado do governo central pelo RTN (0,36% e 0,48%).
- 6.1.2 diz que o arcabouço "limita o crescimento real da despesa total entre 0,6% e 2,5%": correto como faixa; a 11.6 mostra que a regra é 70% ou 50% da receita dentro dela.
- Primário estabilizador: a 11.6 usa a faixa 2,9% (IFI, RAF 117) a 3,4% (painel, dívida de ago/2026), como `_divergencias.md`.
- Juro real ex-ante de 2025: 10,5% pela convenção única (10,52).

## 11.7

Arquivo: `conteudo/11-financas-publicas/11.7-sustentabilidade.md` (id 11.7, pai 11, ordem 7). Redação de 02/11/2026.

Palavras: cerca de 3.480 de prosa fora das tabelas, das fórmulas, dos parênteses de fonte e do "Para ler" (3.840 contando os parênteses); o `tools/lint.py` conta cerca de 5.400 tokens. Sem travessão, sem "não é X, é Y", sem palavra vetada ("projeção de referência" no lugar de "cenário-base"). `build.py --check` sem erro; aviso só para o link a 10.4, ainda não escrita.

Estrutura: exemplo de brinquedo (duas dívidas de 80% com primário zero, r − g de −2 e +4; tabela e gráfico em dez anos: 65,6% × 117,5%; s* = 3,1% para B; A aguentaria déficit de 2% e pararia em 102%); restrição intertemporal em razão do PIB com a condição de transversalidade e o caso r < g (sem refazer a derivação da 1.5 e da 3.1); solvência × liquidez com o caixa (13,5% do PIB) e o que vence em 12 meses (16,39% da DPF ≈ R$ 1,5 tri ≈ 11% do PIB); r − g do Brasil 2006–2026 (gráfico, tabela por período, exemplo de 2025 nominal e real); r − g no mundo (Blanchard 2019, Mauro et al. 2015, Mauro e Zhou 2020, Escolano et al. 2017); teste de Bohn (fórmula, limiar ρ > (r − g)/(1 + g), tabela da literatura brasileira e teste simples do painel); DSA do FMI (mapa de calor de 2013, SRDSF de 2022, Artigos IV de 2025 e 2026); limite seguro (Reinhart e Rogoff 2010 × Herndon, Ash e Pollin; moeda, detentores, prazo, histórico; Ghosh et al. 2013 e Pereira 2020; tabela Brasil × Itália × Japão); leituras das duas teses, quadro A favor / Contra e `:::painel`. Liga para 1.5, 1.5.3, 2.1, 2.5, 3.1, 3.3, 3.4, 6.1, 10.3.3, 10.4 e 11.5.

Gráficos e script:
- `tools/analises/11.7_r_menos_g.py` (com `--resumo` imprime a tabela anual, as médias por período e as regressões).
- `dados/11.7-r-menos-g.json` (linha, p.p., 2006–2026): i − g nominal e r − g real com o IPCA. i = juros apropriados sobre a DBGG (fatores condicionantes do BCB, edições de setembro de 2008 a 2026, mesma base de dados/3.1 e 3.2) × (Y_t/Y_{t−1}) ÷ DBGG de dez do ano anterior (SGS 13762); reproduz a série de dados/3.1 (12,55% em 2025). 2006 usa a taxa publicada (14,18%), porque o SGS 13762 começa em dez/2006. 2026 preliminar: juro de jan–ago (8,59%) anualizado = 13,16%; PIB de 12 meses set/2026 ÷ set/2025 = 7,01%; IPCA 12m set/2026 = 4,58%.
- `dados/11.7-brinquedo-trajetorias.json` (barras, % do PIB, anos 0 a 10).

Números e contas do painel:
- i − g por ano: 2006 +3,18; 2007 +0,51; 2008 −1,30; 2009 +3,81; 2010 −5,62; 2011 −0,01; 2012 +1,08; 2013 −0,17; 2014 +3,01; 2015 +9,98; 2016 +8,46; 2017 +5,00; 2018 +2,01; 2019 +2,27; 2020 +3,32; 2021 −10,88; 2022 −1,30; 2023 +2,73; 2024 +3,25; 2025 +4,40; 2026* +6,15.
- Médias (i, g, i − g, r com IPCA, r − g real): 2006–2013 12,1 / 11,9 / +0,2 / 6,5 / +0,2; 2014–2016 12,7 / 5,6 / +7,2 / 4,6 / +6,6; 2017–2019 8,7 / 5,6 / +3,1 / 4,9 / +3,0; 2020–2022 8,1 / 11,1 / −3,0 / 1,3 / −2,7; 2023–2025 11,6 / 8,1 / +3,5 / 6,7 / +3,3; 2026* 13,2 / 7,0 / +6,2 / 8,2 / +5,9.
- 2025: r = 7,95% (IPCA 4,26%); r − g real = 4,22 = 4,41/1,0426. Limiar de Bohn com as taxas de 2025: 0,0441/1,0814 = 0,041.
- Teste de Bohn do painel (MQO, Newey-West com 2 defasagens; s = −SGS 5793 de dezembro; controle: SGS 7326; dummy 2020): DLSP 2002–2013 ρ = +0,062 (ep 0,010); DLSP 2014–2025 −0,017 (0,022); DLSP 2002–2025 −0,047 (0,047); DBGG 2007–2025 −0,093 (0,025); DBGG 2007–2013 −0,033 (0,057, n = 7, não entrou no texto); DBGG 2014–2025 +0,009 (0,052, não entrou).

Fontes principais: BCB (fatores condicionantes da DBGG; SGS 13762, 4513, 4382, 13522, 5793, 7326, coleta de 02/11/2026); Tesouro (RMD de agosto de 2026); IFI (RAF 117); FMI (CR 25/194 e 26/191, comunicado 26/257, guias de DSA de 2013 e 2022, DataMapper); Blanchard (2019); Bohn (1998); Mauro et al. (2015); Mauro e Zhou (2020/2021); Escolano, Shabunina e Woo (2017); Mendonça, Santos e Sachsida (2009); Luporini (2015); Campos e Cysne (2019a, 2019b); Campos, Cysne e Madureira (2022); Oliveira, Nobrega e Maia (2022); Pereira (Ipea DP 250, 2020); Reinhart e Rogoff (2010); Herndon, Ash e Pollin (2014); Ghosh et al. (2013). imf.org, ipea, scielo, usp e poder360 estavam bloqueados ao WebFetch; tudo veio de resumos e trechos de busca.

Lacunas e pendências:
- Artigo IV de 2026: a classificação "moderado", o primário estabilizador de cerca de 1,5% do PIB e a "metade flutuante, um quinto rolado por ano" vêm do resumo publicado pela IndraStra (set/2026), que cita o relatório; o PDF do FMI não abriu. A página atribui à IndraStra. Uma busca chegou a sugerir risco "elevated", sem trecho que confirme; conferir na seção de DSA do CR 26/191. Também não se obteve o mapa de calor nem os resultados de cada choque do Artigo IV (o quadro novo, SRDSF, não usa mais mapa de calor); a página descreve o método e não traz números por choque.
- O diferencial de juro e crescimento projetado pelo FMI para 2026–2031 (2,8 p.p., num resumo de busca) não foi confirmado e ficou fora.
- Os limiares do mapa de calor de 2013 (70% e 85% do PIB) foram confirmados por busca no guia de 2013; os de necessidade de financiamento (15% e 20%) não, e ficaram fora.
- Coeficientes de Campos e Cysne (2019a, 2019b, 2022) e o limite numérico de Pereira (2020) não obtidos; a página usa só o sinal e a conclusão. Luporini (2015): 0,096 no resumo do artigo; uma monografia cita 0,0595 para a dívida líquida; ficou o do resumo. A amostra de Luporini aparece como 1991–2011 numa fonte e 2001–2013 noutra; a página diz "do início dos anos 1990 ao começo dos 2010".
- Ghosh et al. (2013): lista de países com e sem espaço fiscal vem do resumo da Royal Economic Society; os limites numéricos por país não foram obtidos.
- Bohn (1998): o coeficiente americano não foi confirmado; a página diz só que é positivo.
- Linha da Itália na tabela comparativa (indexação "prefixada na maior parte", BCE como comprador) é descritiva, sem número; conferir com o Tesouro italiano se a revisão pedir número.
- Páginas e número do volume de Mauro e Zhou na *IMF Economic Review* (69(1), 2021) e o número de Escolano et al. em *Fiscal Studies* (38, p. 179–217; ano 2016 ou 2017 conforme a fonte) devem ser conferidos.

Divergências com outras páginas:
- Nenhuma de número. O i − g por ano é o mesmo de dados/3.1 (reconstruído pelo script; 2007 dá 13,41 contra 13,40 por arredondamento). A 3.1 diz que o diferencial de 2006–2013 teve "média de 0,2 ponto (de −5,6 em 2010 a +3,8 em 2009)": igual.
- A 3.1 trata 2021 e 2022 como "−10,9 e −1,3": igual. O cartão do item dizia "negativo em 2020–2022": em 2020 o diferencial foi positivo (+3,3 p.p.), porque o PIB nominal cresceu só 3%; a página diz que o triênio foi negativo só na média.
- Primário estabilizador: a 11.7 cita a faixa da 11.6 (2,9% IFI a 3,4% painel) e acrescenta o FMI (≈1,5%, via resumo secundário); a diferença vem da hipótese de juro.

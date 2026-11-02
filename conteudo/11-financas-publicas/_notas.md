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

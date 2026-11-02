# Notas da área 3 (Dívida pública)

Redação: 02/11/2026. Base: insumos Frente A, J e K (dados do BCB, Tesouro, FMI, IFI consultados em 28/10/2026) e busca web em 02/11/2026. O acesso direto a sites do BCB, Tesouro, Câmara e Auditoria Cidadã ficou bloqueado nesta sessão (WebFetch: ENOTFOUND), e o limite de buscas web da rodada foi atingido antes de fechar todas as pendências.

## Páginas entregues (contagem aproximada de palavras do corpo, incluindo tabelas e referências)

| Id | Arquivo | Palavras | Gráficos |
|---|---|---|---|
| 3 | 3-divida-publica.md | ~1.250 | dados/3-divida-conceitos.json |
| 3.1 | 3.1-aritmetica-da-divida.md | ~3.600 | 3.1-primario-estabilizador.json; 3.1-juro-implicito-crescimento.json; 3-divida-conceitos.json (reuso) |
| 3.2 | 3.2-fatores-condicionantes.md | ~4.100 (prosa ~3.700) | 3.2-fatores-anuais.json; 3.2-fatores-periodos.json; 3.2-compromissadas-caixa-bndes.json |
| 3.3 | 3.3-quem-detem-quem-recebe.md | ~2.900 | 3.3-detentores-ago2026.json; 3.3-detentores-historico.json; 3.3-juros-apropriados-rs.json |
| 3.4 | 3.4-comparacao-internacional.md | ~2.900 | 3.4-divida-bruta-paises.json; 3.4-juros-liquidos-paises.json; 3.4-lft-na-dpf.json |
| 3.5 | 3.5-auditoria-cidada.md | ~3.900 | 3.5-orcamento-2025-tres-contas.json; 3.5-juros-2025-medidas.json |

Total: 6 páginas, 14 arquivos de dados (13 gráficos distintos). `python3 tools/build.py --check` passa sem aviso de formato para a área; restam só links para páginas de outras áreas ainda não escritas (1.5.1, 2, 2.5, 5, 5.4.3, 6, 7.6, 7.7, 7.8, 8).

## Resposta ao teste "juro ou déficit?" (para a matriz da área 8)

Fatores condicionantes da DBGG, p.p. do PIB (BCB; Frente J; agregação do painel):

| Período | Δ DBGG | Bola de neve (juros + efeito PIB) | Primário | Ativos | Leitura |
|---|---|---|---|---|---|
| 2006–2013 | −4,26 | +0,77 | −20,94 | +15,53 | superávit segurou; reservas e BNDES empurraram |
| 2014–2016 | +18,30 | +12,16 | +4,71 | +0,18 | bola de neve 2/3, déficit 1/4 |
| 2017–2019 | +4,60 | +6,34 | +4,26 | −6,99 | devoluções do BNDES compensaram |
| 2020–2022 | −2,76 | −6,49 | +7,40 | −4,99 | déficit (2020) domina; inflação desfaz |
| dez/2022–ago/2026 | +11,19 | +10,05 | +3,56 | −2,68 | bola de neve 90%, déficit 32% |
| 2006–ago/2026 | +27,06 | +22,80 | −1,02 | +1,04 | primário acumulado quase neutro |

## Números divergentes (registrar em conteudo/_divergencias.md)

1. Juro implícito da DBGG em 2025: resolvido pela decisão do painel (_divergencias nº 2): 12,55% (juros apropriados no ano ÷ estoque de dez/2024) em toda a área desde a revisão de 02/11/2026.
2. Primário estabilizador "com taxas de 2025": resolvido (_divergencias nº 4): 3,2% com a dívida de dez/2025 (78,6%) e 3,4% com a de ago/2026 (82,9%). IFI: RAF 117, 2,9% com neutro de 6,1%.
3. Juro real do setor público: CONTEXTO.md diz "de 3,1% para 5,3% do PIB entre 2024 e 2025". O cálculo do painel (juros nominais menos IPCA × DLSP do fim do ano anterior) dá cerca de 5,4% em 2024 e 5,5% em 2025 (R$ ~700 bi). Fonte do número do CONTEXTO não identificada; o painel usa o próprio cálculo, declarado como aproximação.
4. Detentores da DPMFi: CONTEXTO (bancos 31,8%, previdência 22,5%, fundos 22%, não residentes 10%) corresponde a junho de 2026 (Agência Brasil: 31,76 / 22,52 / 22 / 9,95). A área usa agosto de 2026 (RMD, Frente K: 31,22 / 22,63 / 22,52 / 9,91). Explicado no texto da 3.3.
5. Juros pagos pela União em 2025 (caixa): R$ 371,7 bi (Inesc, citado pela Frente K) × R$ 363,6 bi (BGU 2025, segundo análises secundárias; a ACD cita R$ 363 bi). A 3.5 usa R$ 363,6 bi na conta e cita o do Inesc.
6. Juros apropriados sobre a DPF em 2025: R$ 857,9 bi (análise secundária do BGU 2025) × R$ 879,9 bi ("incorporação de juros", Portal In, a partir do Tesouro). Marcado [a conferir no BGU 2025].
7. Dívida no conceito FMI em 2030: 104,5% (DataMapper, Frente J) × 104,8% (Artigo IV de jul/2026, Frente A). Edições diferentes; a 3.4 cita as duas.
8. Fatia da dívida no orçamento executado de 2025 segundo a ACD: 42,24% (maioria dos textos) × 42,4% (outro texto da ACD), ambos sobre R$ 2,135 tri. Usado 42,24%.
9. LOA 2025: despesa dos orçamentos fiscal e da seguridade de cerca de R$ 5,72 tri (Lei 15.121) × "R$ 5,9 tri" na imprensa (soma o orçamento de investimento das estatais, R$ 166,5 bi). Juros (R$ 480,0 bi) e amortização (R$ 393,1 bi) vêm do PLOA (nota técnica conjunta CONOF/CONORF); os valores finais da LOA não foram obtidos. A conta de 44,2% confere com os 44% da ACD (PLOA) e os 44,14% do Monitor Mercantil (LOA).
10. Juros líquidos do FMI (primário menos nominal) para México (6,1% do PIB) e Colômbia (2,3%) parecem destoar de outras medidas; o resíduo pode incluir itens além de juros. Marcado na 3.4.
11. Plebiscito da dívida de 2000: 5,1 mi (Monitor Mercantil), 5,6 mi e "mais de 6 mi" (Brasil de Fato, CADTM). A 3.5 cita a faixa.
12. Equador, recompra de 2009: desconto de 65% (ministra Elsa Viteri) × 70% (outras fontes); custo de US$ 800 mi × US$ 900 mi. A 3.5 diz "perto de 35% do valor de face".
13. DBGG de 2006 a 2014 no conceito BCB foi reconstruída somando as variações da Frente J ao nível de 2013; difere do SGS em até 0,05 p.p. (nota no JSON).
14. Reservas: US$ 372,6 bi (ago/2026, Frente J) e US$ 362,8 bi (set/2026, Frente A). Meses diferentes, não é erro; cada página diz o mês.

## Revisão independente aplicada em 02/11/2026

Achados aplicados, não aplicados e pendentes estão em `conteudo/_revisao/3.md`, seção "Aplicação". Abaixo, só o que fica para a próxima rodada.

### Achados não aplicados ou aplicados de outro modo (uma linha cada)

- 3.2 nº 9: o juro real ex-post foi recalculado com os brutos (Selic acumulada no ano pelo SGS 4189, deflacionada pelo IPCA do SGS 13522): 8,2%, 5,7% e 9,6% em 2023–2025, em vez de 8,0/5,8/9,7 propostos (diferença de método de capitalização).
- 3.2 nº 14: Segura-Ubiergo (2012) saiu do Para ler em vez de entrar no texto, porque o painel não abriu o texto para atribuir-lhe conclusões.
- 3.2 nº 16: em vez de citar o Relatório de Gestão das Reservas (não aberto), a frase ficou sem atribuição ("o custo de carregamento é o prêmio desse seguro").
- 3.4 nº 14: o gráfico de LFT saiu da 3.4 e virou link para a 2.4, que é a página dona do tema pela decisão do painel; `dados/3.4-lft-na-dpf.json` ficou sem uso (nota corrigida, sem "recorde"), à disposição da 2.4 ou para remoção pelo coordenador.
- 3.5 nº 4 e nº 17: os recortes de Fattorelli (*Extra Classe*), da ACD (2024), do Tesouro ("A dívida em vídeos") e do Aos Fatos viraram paráfrase com a fonte, porque não foi possível conferir a redação exata (domínios auditoriacidada.org.br, extraclasse.org.br, aosfatos.org e tesourotransparente.gov.br bloqueados na sessão; busca não achou o trecho de Fattorelli). A resposta da ACD à crítica da rolagem entrou como paráfrase, a partir da descrição do texto de jan/2024 em resultados de busca.
- 3.1 nº 4: a distância entre o juro ex-ante (8,5% a 8,8%) e o neutro de 5% ficou "3,5 a 3,8 pontos", conta exata, em vez de "3,5 a 4".

### Pendências após a revisão

- 3.5: relator atual da ADPF 59 (Barroso deixou o STF em out/2025; a busca não confirmou o sucessor nem a redistribuição); reabrir os quatro recortes acima e voltar às aspas se a redação conferir; abrir o Estudo nº 16/2025 da Câmara e trazer a conciliação LOA × BCB; percentuais de saúde (4,27%) e educação (3,18%) no PDF do gráfico da ACD de 2025 (retirados do texto); recomendações do relatório final da CPI da Dívida (2010) e destino do voto em separado; pareceres do TCU sobre a tese da regra de ouro; valores finais de juros e amortização na LOA 2025.
- 3.3: juros apropriados sobre a DPF em 2025 (R$ 857,9 × 879,9 bi, BGU/RAD 2025); participação de não residentes em títulos locais de outros emergentes; distribuição de aplicações financeiras por faixa de renda (Grandes Números do IRPF); LFT: a afirmação de recorde saiu (a busca só trouxe 49,32% em jun/2026 e fonte que chama 51,1% de "maior desde ago/2003"); conferir no anexo do RMD desde quando 52,74% é o maior nível.
- 3.2: custo de carregamento das reservas (diferencial Selic × rendimento das reservas) ano a ano.
- 3.4: juros do governo geral por país na tabela do Fiscal Monitor (México e Colômbia); grupo e número de "3,8% do PIB" do Fiscal Monitor de abr/2026 (retirado); data do prazo médio de 71 meses (PGPF); prazo médio dos JGB (MOF); participação das FRN na dívida americana; taxa vigente do BoJ em nov/2026; documento do Tesouro com as projeções 83,5/87,9/83,1 (citado via Newsquawk); projeções da IFI no RAF 117 para 2026–2027 (só 2036 foi obtido, via Poder360).
- 3.1 e 3.2: números do BIS para 2003–2008 e 2010–2019 vêm da decisão registrada em _divergencias (brutos do BIS, cálculo do revisor); não recalculados nesta aplicação.

## Pendências [a conferir] da redação original (superadas pela lista acima)

- 3.2: custo de carregamento das reservas (diferencial Selic × rendimento das reservas) nas notas do BCB.
- 3.3: participação de não residentes em títulos locais de outros emergentes (FMI/BIS); juros apropriados sobre a DPF em 2025 no BGU; distribuição de aplicações financeiras por faixa de renda (Grandes Números do IRPF); ano mais recente das CEI (coordenar com a página 5.4.3).
- 3.4: juros do governo geral por país na tabela estatística do Fiscal Monitor (México, Colômbia); definição do grupo "3,8% do PIB" no Fiscal Monitor de abr/2026; data do prazo médio de 71 meses do Tesouro americano (PGPF); prazo médio dos JGB (MOF do Japão); participação de FRN na dívida americana.
- 3.5: percentuais de saúde (4,27%) e educação (3,18%) no PDF do gráfico da ACD de 2025 (vieram de comentário que reproduz o gráfico); situação atual da ADPF 59; recomendações do relatório final da CPI da Dívida (2010) quanto a auditoria e destino do voto em separado; manifestações do TCU sobre a tese de violação da regra de ouro; valores finais de juros e amortização na LOA 2025 (não só no PLOA).
- Geral: despesa primária do governo central de 2025 em R$ e % do PIB (RTN dez/2025) para uma comparação adicional na 3.5; a busca não trouxe o número.

## Sugestões para a próxima rodada

- Abrir o Estudo nº 16/2025 da Consultoria de Orçamento da Câmara (Moura, Oliveira e Volpe) e trazer a tabela de conciliação entre LOA e BCB; é a melhor fonte neutra para a 3.5 e pode render um recorte citado.
- Obter a série de reservas (SGS 3546) desde 2006 para quantificar a relação compra de reservas × compromissadas na 3.2.
- Obter estimativa do custo de carregamento das reservas e do resultado dos swaps cambiais para separar, dentro dos juros apropriados, o que é custo da política cambial.
- Se a página 5.4.3 trouxer o saldo de juros das empresas não financeiras na CEI, inserir uma frase com o número na seção "O que as contas nacionais dizem" da 3.3.
- Considerar uma neta 3.2.1 sobre precatórios (EC 113/114, MP 1.200, EC 136/2025), hoje resumida em dois parágrafos.

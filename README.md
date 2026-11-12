# Citizen Assist AI — Energia Renovável em Residências

Contribuição da disciplina **Soluções em Energias Renováveis e Sustentáveis** (Global Solution 2026).

## Integrantes
- Guilherme Cedro — RM 571050
- Gabriel Gonçalves — RM 569189
- Gabriel Carvalho — RM 571381

## Público e problema
**Público:** moradores de residências em São Paulo (SP), famílias com conta de luz mensal.
**Problema:** muitas famílias querem reduzir o gasto com energia elétrica, mas não sabem quanto
consomem nem se vale a pena investir em eficiência (lâmpadas LED) ou em energia solar.
**Como ajudamos:** o assistente mostra o consumo, compara duas alternativas para o mesmo
período (10 anos) e explica custos, viabilidade, impacto ambiental e limitações.

## Funcionalidades de energia
1. Consumo da casa exemplo (potência x horas de uso).
2. Entrada dos dados do próprio usuário (consumo, tarifa, lâmpadas).
3. Comparação: **A) trocar lâmpadas por LED** x **B) energia solar fotovoltaica (renovável)**.
4. Recomendação baseada nos cálculos.
5. Limitações e referências.

## Como executar
1. Instale o Python 3 e abra a pasta no PyCharm.
2. Execute `main.py`.
3. Use o menu digitando o número da opção. Para testar: opção 3 e depois a opção 4.

## Estrutura
- `main.py`: assistente (menu).
- `dados.py`: dados, premissas e origem.
- `calculos.py`: fórmulas e comparação.
- `docs/justificativas.md`: justificativas das recomendações.
- `docs/referencias.md`: referências.
- `docs/testes_usuarios.md`: testes com usuários e ajustes.

## Dados e premissas (todos ESTIMADOS)
| Dado | Valor | Unidade | Origem / observação |
|---|---|---|---|
| Tarifa | 0,78 | R$/kWh | Conta de luz de um integrante do grupo (com impostos) |
| Período de análise | 10 | anos | Definido pelo grupo (igual para A e B) |
| Dias no mês | 30 | dias | Simplificação |
| Potência e horas dos aparelhos | ver `dados.py` | W e h/dia | Valores típicos estimados (conferir Procel/Inmetro) |
| Lâmpada fluorescente / LED | 23 / 10 | W | Estimativa |
| Preço da lâmpada LED | 12,00 | R$ | Estimativa de mercado |
| Horas de sol pleno (HSP) | 4,5 | h/dia | Estimativa; conferir CRESESB |
| Eficiência do sistema solar | 0,80 | — | Premissa comum de perdas |
| Custo do sistema solar | 4.500 | R$/kWp | Estimativa; pedir orçamentos |
| Custo de disponibilidade | 50 | kWh/mês | Valor para ligação bifásica (ANEEL) |
| Fator de emissão | 0,0385 | kg CO2/kWh | Média da rede (MCTI); conferir o ano |

## Fórmulas
- Energia (kWh/mês) = potência (W) × horas/dia × quantidade × 30 ÷ 1000
- Economia (R$/mês) = kWh economizados × tarifa
- Retorno = investimento ÷ economia mensal
- Geração solar (kWh/mês) = kWp × HSP × 30 × eficiência
- CO2 evitado = kWh economizados × meses × fator de emissão

## Resultados com os valores padrão (aproximados)
| | A) LED | B) Solar |
|---|---|---|
| Investimento | R$ 120,00 | R$ 9.000,00 (2,0 kWp) |
| Economia mensal | ~R$ 15,21 | ~R$ 129,71 |
| Saldo em 10 anos | ~R$ 1.705 | ~R$ 6.566 |
| Retorno | ~8 meses | ~5,8 anos |
| CO2 evitado em 10 anos | ~90 kg | ~768 kg |

São **estimativas, não garantias**. Veja as limitações em `docs/justificativas.md`.

## Referências, testes e justificativas
Ver a pasta `docs/`.
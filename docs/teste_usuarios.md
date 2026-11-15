# Testes com usuários

Não foram registrados nomes nem dados pessoais.

| Pessoa | Situação testada | Entendeu as orientações? | Comentários | Ajuste feito |
|---|---|---|---|---|
| Pessoa 1 | Consumo de 222 kWh/mês, tarifa R$ 0,78 e 8 lâmpadas; usou as opções 3, 1, 2, 4 e 5 do menu | Sim | Observação do grupo: após informar o consumo na opção 2, a opção 1 continuou mostrando 216,3 kWh, o que pode passar a impressão de que o dado foi ignorado | Título da opção 1 alterado para informar que a casa exemplo não muda com a opção 2 |
| Pessoa 2 | Consumo de 50 kWh/mês na opção 2, depois opção 4 | Parcialmente (disse que não entendeu muito bem) | Disse que não entendeu muito bem, mas que ficou claro que os valores são estimativas. Não achou nada confuso. Acha que as informações não seriam muito úteis para ela, mas ainda são úteis | Adicionado resumo em linguagem simples ao final da comparação, com mensagem própria para consumo baixo |
| Pessoa 3 | Digitou letras e 0 no campo de consumo (opção 2), além das opções 3 e 4 | Sim | Disse que entendeu normal e que ficou claro que os valores são estimativas. Sugeriu limpar o console para não ficar muito poluído. Achou as informações úteis ("com certeza") | Pausa com Enter antes de voltar ao menu e linhas em branco para separar as telas |

## Situações testadas
1. Valores padrão (casa exemplo, 216,3 kWh/mês, 10 lâmpadas).
2. Dados informados pelo usuário (222 kWh/mês, 8 lâmpadas).
3. Consumo baixo (50 kWh/mês).
4. Valores inválidos (letras e zero) no campo de consumo.

## Perguntas feitas aos testadores
- Você entendeu o resultado da comparação?
- Ficou claro que os valores são estimativas?
- Algo ficou confuso? O que mudaria?
- Você acha que essas informações seriam úteis para decidir sobre energia solar na sua casa?
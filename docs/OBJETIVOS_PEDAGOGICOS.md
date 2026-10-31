# Objetivos pedagógicos

**A meta é explicar o mecanismo e demonstrar o resultado.** Cada atividade exige evidência observável.

| Competência | Atividade | Evidência de aprendizagem |
| --- | --- | --- |
| Entender programa armazenado | Montar opcode e operando na memória | Identificar automodificação LD/MM no trace |
| Definir ABI | Usar posições fixas de entrada e resultado | Apontar 0300/0500/0700/0900 e explicar SC/RS |
| Distinguir byte e palavra | Consumir MSB e LSB de GD | Recuperar todos os 256 valores sem erro de sinal |
| Proteger a pilha | Limitar a 127 palavras | Demonstrar SP=0FFE vazio e SP=0F00 cheio |
| Interpretar RPN | Acumular dígitos e aplicar operadores binários | Testar ordem dos operandos, EOF, newline e erros |
| Avaliar compatibilidade | Executar assembly no modelo novo | Identificar diferenças que requerem simulador oficial |

## Sequência de estudo

1. Leia o contrato e resolva um exemplo pequeno à mão.
2. Preveja saída e estado intermediário antes de executar.
3. Confronte sua previsão com o programa.
4. Altere uma entrada de fronteira e justifique o resultado.
5. Explique o invariante violado em um teste negativo.
6. Proponha uma extensão com critério de aceitação.

## Rubrica sugerida

| Critério | Inicial | Adequado | Avançado |
| --- | --- | --- | --- |
| Explicação | Repete a saída | Explica etapas | Justifica invariante e contraexemplo |
| Verificação | Usa um exemplo | Testa fronteiras | Compara com referência independente |
| Limites | Omite hipóteses | Declara domínio | Explica falha e sua detecção |
| Reprodução | Depende do ambiente pessoal | Usa comandos e fixtures | Registra versão, origem e evidência |

Rubrica proposta nesta edição, sem estudo de eficácia pedagógica com participantes ou nota institucional.

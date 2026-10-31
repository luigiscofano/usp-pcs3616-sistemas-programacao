# RPN: scanner, operandos e execução real

```sh
python -m unittest discover -s tests -v
python scripts/executar.py "12 3 +" --trace
python scripts/executar.py "5 9 -"
```

A CLI monta e executa as palavras do assembly, sem eval. O scanner acumula dígitos; espaço/tab/CR separam; LF ou 00 encerram. Para operador binário, o primeiro pop é o direito e o segundo é o esquerdo.

**Atividade:** rastreie 5 9 − e justifique −4. Depois explique por que inverter a ordem dos pops mudaria a resposta. Compare com [o trace real de 12 3 +](../../assets/README.md).

Ao terminar deve restar exatamente um valor. Divisão por zero, falta/excesso de operandos e operador desconhecido geram erro. Aritmética é modular de 16 bits e a divisão trunca para zero. O orçamento do executor evita execução infinita, sem provar compatibilidade com o simulador oficial.

[Scanner assembly](../../asm/rpn.asm) · [Arquitetura e limites](../ARQUITETURA.md)

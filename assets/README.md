# Rastreamento real da MVN didática

[Trace JSON de 12 3 +](trace_12_3_mais.json), gerado pela execução das palavras de máquina montadas dos arquivos ASM. Cada item registra PC anterior, instrução e acumulador após o passo, em hexadecimal. O trace é limitado a 1.000 instruções por configuração padrão.

O resultado 15 fica em 0904 e status zero em 0908. Para reconstruir a execução completa: python scripts/executar.py "12 3 +" --trace. Não é um log do simulador oficial.

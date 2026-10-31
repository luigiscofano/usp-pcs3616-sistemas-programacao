# SUB_LE_BYTE e ordem dos bytes

Entrada em 0300, resultado em 0304 e argumento reservado em 0306. O dispositivo implementado é fixo: GD /300, disco zero. Cada leitura retorna dois bytes, primeiro MSB e depois LSB, usando cache e flag.

O leitor retorna palavras positivas entre zero e 255. Quando o byte alto ≥128, a palavra lida parece negativa na divisão com sinal; a rotina trata o bit alto antes de dividir e recompõe o byte. Os testes percorrem os 256 valores.

**Atividade:** preveja as quatro saídas para bytes 41 42 80 FF (hex). Explique por que interpretar a palavra 80FF como inteiro com sinal exige cuidado para extrair 80.

No protocolo RPN, 00 termina a expressão; não se distingue NUL literal do EOF preenchido com zero. Isso é contrato do modelo atual, não um protocolo universal de arquivo.

[Assembly](../../asm/le_byte.asm) · [Mapa e ABI](../ARQUITETURA.md)

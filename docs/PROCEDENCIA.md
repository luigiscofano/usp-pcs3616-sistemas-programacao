# Procedência e reconstrução

Conversas de abril de 2025 documentam le_byte.asm, pilha.asm, rpn.asm, SC/RS, endereços fixos e a região reservada do programa principal. O pacote originalmente entregue não foi recuperado. O main.asm histórico, que não deveria ser alterado, não foi modificado: não foi encontrado. O arquivo atual é um harness novo identificado como tal.

Assembly, montador e executor desta edição são reconstruções de 2026 com assistência de IA. Preservam as entradas e posições de resultados recuperadas. Nos slots 0506/0706/0906 há saltos para handlers locais; palavras de status foram acrescentadas em 0508/0708/0908. Essa convenção adicional é nova, sem comprovação de compatibilidade com o avaliador antigo.

O montador aceita o formato absoluto documentado aqui. Não implementa o linker e todos os recursos/dispositivos do ecossistema oficial. Os testes demonstram execução neste modelo; validação no simulador oficial continua sendo uma etapa distinta.

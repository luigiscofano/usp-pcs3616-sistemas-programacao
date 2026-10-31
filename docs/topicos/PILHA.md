# Pilha de 127 palavras

A região 0F00–0FFD reserva 254 bytes, equivalentes a 127 palavras alinhadas. STACK_POINTER fica em 0FFE: esse valor significa vazia; 0F00 significa cheia.

| Operação | Verificação | Alteração |
| --- | --- | --- |
| Push | SP diferente da base | Decrementa dois e grava |
| Pop | SP diferente de 0FFE | Lê e incrementa dois |

Os operandos LD/MM são automodificados para acesso indireto. As rotinas compartilham palavras de retorno e dados, portanto não são reentrantes.

**Atividade:** acompanhe dois pushes e dois pops no mapa, mostrando os endereços lidos/escritos. Em seguida explique como a verificação impede um 128º item e o pop de uma pilha vazia.

Os slots 0506/0706 desviam para handlers; status 0508/0708 são extensão da reconstrução atual. [Assembly](../../asm/pilha.asm) · [Contrato completo](../ARQUITETURA.md).

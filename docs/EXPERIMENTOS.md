# Experimentos e critérios de aceitação

## Exercício guiado

Execute os exemplos de [INSTALACAO.md](INSTALACAO.md) e anote a previsão antes de rodar. A saída só conta como evidência depois de comparada com o contrato de [ARQUITETURA.md](ARQUITETURA.md).

## Casos de fronteira e referência

Nove testes unittest: 400 expressões aleatórias com referência independente, todos os 256 bytes, limites de 127 itens, posições fixas, overflow modular, divisão negativa, entradas inválidas, timeout e desalinhamento.

Leia a suíte e escolha um caso que quebra uma solução ingênua. Explique o motivo, reduza a entrada ao menor contraexemplo e proponha uma correção sem alterar o contrato silenciosamente. Use referência independente quando disponível.

## O que não concluir

Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

Não use tempo isolado ou gráfico atraente como prova de correção. Registre ambiente, entrada, saída, versão e limitações relevantes.

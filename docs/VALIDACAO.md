# Validação

## Evidência local — 31/10/2026

Nove testes unittest: 400 expressões aleatórias com referência independente, todos os 256 bytes, limites de 127 itens, posições fixas, overflow modular, divisão negativa, entradas inválidas, timeout e desalinhamento.

## Limites da conclusão

Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

Um workflow configurado ou PR aberto não demonstra aprovação. A evidência remota e o commit testado serão registrados após conclusão do GitHub Actions.

O [registro local estruturado](validacao-local.json) preserva o comando e o log efetivamente obtidos.

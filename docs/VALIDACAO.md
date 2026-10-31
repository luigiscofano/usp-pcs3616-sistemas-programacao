# Validação

## Evidência local — 31/10/2026

Nove testes unittest: 400 expressões aleatórias com referência independente, todos os 256 bytes, limites de 127 itens, posições fixas, overflow modular, divisão negativa, entradas inválidas, timeout e desalinhamento.

## Limites da conclusão

Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

Um workflow configurado ou PR aberto não demonstra aprovação. A evidência remota e o commit testado serão registrados após conclusão do GitHub Actions.

O [registro local estruturado](validacao-local.json) preserva o comando e o log efetivamente obtidos.

## Evidência remota confirmada

[Execução 41227782882](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/runs/41227782882) aprovada no commit `5714b03563da0413904f375f5c9163f3b0ece820`.

- **testes (macos-15)**: success.
- **testes (windows-latest)**: success.
- **testes (ubuntu-24.04)**: success.

Os artefatos podem exigir login no GitHub e têm prazo de retenção; os fontes permanecem no repositório.

- [evidencia-macos-15](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/runs/41227782882/artifacts/13053025204) — retenção até 2027-01-29T18:06:47Z.
- [evidencia-windows-latest](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/runs/41227782882/artifacts/13052641376) — retenção até 2027-01-29T18:06:47Z.
- [evidencia-ubuntu-24.04](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/runs/41227782882/artifacts/13052506712) — retenção até 2027-01-29T18:06:47Z.

O commit acima identifica exatamente a versão testada. Atualizações documentais posteriores não ampliam a conclusão funcional.

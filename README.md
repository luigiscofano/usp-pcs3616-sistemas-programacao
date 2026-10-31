<p align="center"><img src="assets/capa.svg" alt="PCS3616 · Sistemas de Programação" width="100%"></p>

# PCS3616 · Sistemas de Programação

**Uma expressão RPN percorre bytes, memória, subrotinas e pilha.**

[![Verificação](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/workflows/verificacao.yml)

Portfólio de **Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334**. Organização e complementos de 2026 com assistência de IA, distinguindo acervo recuperado e implementações novas. [Procedência](docs/PROCEDENCIA.md).

## Objetivos pedagógicos em destaque

- **Entender programa armazenado** — Montar opcode e operando na memória.
- **Definir ABI** — Usar posições fixas de entrada e resultado.
- **Distinguir byte e palavra** — Consumir MSB e LSB de GD.
- **Proteger a pilha** — Limitar a 127 palavras.
- **Interpretar RPN** — Acumular dígitos e aplicar operadores binários.
- **Avaliar compatibilidade** — Executar assembly no modelo novo.

**[Atividades, evidências e rubrica →](docs/OBJETIVOS_PEDAGOGICOS.md)**

## Execute e experimente

```sh
python -m unittest discover -s tests -v
python scripts/executar.py "12 3 +" --trace
python scripts/executar.py "5 9 -"
```

Ambiente: **Assembly MVN e Python 3.12**. [Instalação detalhada](docs/INSTALACAO.md).

## Encontre cada parte

**[Guias por assunto](docs/topicos/README.md) · [Mapa de branches](docs/BRANCHES.md) · [PRs e entregas](docs/PUBLICACAO.md)**

| Diretório | Conteúdo |
| --- | --- |
| [asm/](asm/README.md) | Leitor de bytes, pilha, RPN e harness novo. |
| [mvn/](mvn/README.md) | Montador absoluto e executor didático do subconjunto utilizado. |
| [tests/](tests/README.md) | Testes do mapa, limites, operações e todos os valores de byte. |
| [scripts/](scripts/README.md) | CLI que monta e executa os arquivos assembly, sem eval. |
| [examples/](examples/README.md) | Expressões sintéticas de reprodução. |
| [assets/](assets/README.md) | Rastreamento da execução e mapa de memória. |
| [docs/](docs/README.md) | Arquitetura, objetivos, reprodução, apresentação e evidência |

## Verificação e limites

Nove testes unittest: 400 expressões aleatórias com referência independente, todos os 256 bytes, limites de 127 itens, posições fixas, overflow modular, divisão negativa, entradas inválidas, timeout e desalinhamento.

Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

**[Validação →](docs/VALIDACAO.md)** · **[Arquitetura e decisões →](docs/ARQUITETURA.md)**

Use o [roteiro de apresentação](docs/APRESENTACAO.md) e confira os [PRs reais](docs/PUBLICACAO.md). As branches representam organização atual, sem datas retroativas ou revisões fictícias.

[Contribuir](CONTRIBUTING.md) · [Direitos e créditos](DIREITOS_E_CREDITOS.md) · [Referências](docs/REFERENCIAS.md) · [Mudanças](CHANGELOG.md)

**CI confirmada:** [testes aprovados](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/runs/41227782882). Consulte o registro de [validação remota](docs/validacao-remota.json).

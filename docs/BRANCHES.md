# Branches e entregas

Use `main` para clonar e executar a versão consolidada. As branches abaixo preservam o ponto de entrega de cada assunto; depois da integração, podem estar atrás de `main`.

Cada branch está ligada a uma alteração concreta. A organização foi feita nesta edição: os nomes não indicam trabalho em datas antigas nem revisão de outras pessoas.

| Branch | Finalidade | Acesso |
| --- | --- | --- |
| `main` | Código e documentação consolidados | [Abrir](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/tree/main) |
| `docs/evidencia-da-ci` | Registrar validacao remota e artefatos reproduziveis | [PR #5](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pull/5) |
| `docs/objetivos-e-arquitetura` | Documentar objetivos pedagogicos, arquitetura e procedencia | [PR #4](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pull/4) |
| `feat/aplicacoes-e-acervo` | Adicionar calculadora RPN em Assembly e harness | [PR #2](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pull/2) |
| `feat/fundamentos` | Implementar leitor de bytes, pilha e executor MVN didatico | [PR #1](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pull/1) |
| `test/verificacao-automatica` | Adicionar testes executaveis e GitHub Actions | [PR #3](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pull/3) |
| `docs/leitor-de-bytes` | Guia de SUB_LE_BYTE e representação de palavras | [Guia](../docs/topicos/LEITURA_BYTES.md) · [Branch](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/tree/docs/leitor-de-bytes) |
| `docs/pilha-e-memoria` | Guia da pilha limitada e do mapa de memória | [Guia](../docs/topicos/PILHA.md) · [Branch](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/tree/docs/pilha-e-memoria) |
| `docs/rpn-e-rastreamento` | Guia da calculadora RPN e de seus traces | [Guia](../docs/topicos/RPN.md) · [Branch](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/tree/docs/rpn-e-rastreamento) |

## Como continuar

Parta da versão atual de `main`, crie uma branch para uma mudança delimitada e abra um PR explicando comportamento, motivo e validação. Não use branches antigas como base para novos assuntos sem atualizar a base.

```sh
git switch main
git pull --ff-only
git switch -c docs/nova-atividade
```

[Guias por assunto](topicos/README.md) · [Registro de publicação](PUBLICACAO.md) · [Todos os PRs](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/pulls?q=is%3Apr)

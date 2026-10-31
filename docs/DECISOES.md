# Decisões de engenharia

| Decisão | Motivo | Consequência |
| --- | --- | --- |
| Separar acervo e código novo | Preservar procedência | Não corrigir silenciosamente o passado |
| Testes com entradas fixas ou sementes declaradas | Reproduzir falhas | Não usar resultado aleatório como evidência sem repetir |
| Scripts sem caminhos pessoais | Facilitar reprodução | Ferramentas precisam estar instaladas ou indicadas por ambiente |
| Contratos e erros explícitos | Evitar saídas plausíveis para entradas inválidas | Casos negativos fazem parte da suíte |
| PRs por entregas verificáveis | Facilitar revisão | Datas refletem organização atual |

Decisões específicas e diferenças em relação ao histórico estão em [ARQUITETURA.md](ARQUITETURA.md) e [PROCEDENCIA.md](PROCEDENCIA.md). Limites: Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

# Roteiro de apresentação · PCS3616 · Sistemas de Programação

## Problema e contexto · 1 minuto

Uma expressão RPN percorre bytes, memória, subrotinas e pilha. Apresente a procedência e identifique o que é recuperado e novo.

## Mecanismo · 3 minutos

Abra [ARQUITETURA.md](ARQUITETURA.md). Explique entradas, estado intermediário e saída em um exemplo pequeno. Relacione diagrama e arquivos reais.

## Demonstração · 3 minutos

Execute [os comandos](INSTALACAO.md), prevendo o resultado antes. Repita com entrada inválida. Explique um teste com referência independente ou invariante.

## Aprendizagem · 2 minutos

Escolha duas competências de [OBJETIVOS_PEDAGOGICOS.md](OBJETIVOS_PEDAGOGICOS.md). Mostre atividade, evidência exigida e uma pergunta que requer entender o mecanismo.

## Evidência e limites · 1 minuto

Mostre [VALIDACAO.md](VALIDACAO.md) e os PRs reais. Limites: Executor e montador próprios; sem certificação no simulador oficial; apenas disco 0; PD e OS não implementados; rotinas não reentrantes; diferenças da ABI de erro documentadas.

Perguntas: qual hipótese permite a decisão central? Que entrada quebra a versão ingênua? Como separar bug e limite do modelo? Que evidência permitiria ampliar a conclusão?

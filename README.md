# PCS3616 · Assembly MVN, pilha e calculadora RPN

> Calculadora de notação pós-fixa em Assembly MVN, com leitor de bytes, pilha limitada, montador e executor didáticos em Python, testes e rastreamento de instruções.

![Visão geral de PCS3616 · Assembly MVN, pilha e calculadora RPN](assets/capa.svg)

[![Verificação](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/actions/workflows/verificacao.yml)

[O que faz](#o-que-este-projeto-faz) · [Módulos](#funcionalidades-e-módulos) · [Executar](#como-executar) · [Aprendizagem](#o-que-desenvolvi-e-aprendi) · [Estado atual](#estado-atual) · [Documentação](#documentação-e-navegação)

## O que este projeto faz

Monta e executa rotinas Assembly para uma Máquina de Von Neumann didática. A demonstração recebe uma expressão como `12 3 +`, executa as palavras do programa e devolve 15. Não usa `eval` para calcular a expressão: o resultado é produzido pelo código montado e executado na máquina.

## Qual problema resolve

Em notação pós-fixa, o operador vem depois dos operandos. Uma pilha permite processar a expressão sem parênteses: empilha 12, empilha 3 e, ao ler `+`, desempilha os dois e empilha 15. O projeto torna visíveis os mecanismos que uma linguagem de alto nível costuma esconder: leitura de bytes, endereços, chamadas de subrotina, pilha e aritmética de tamanho fixo.

## Funcionalidades e módulos

As partes abaixo formam um caminho integrado. Leitor, pilha e montador podem ser estudados isoladamente, mas não representam aplicativos finais independentes.

| Camada | Responsabilidade | Arquivo / pasta |
| --- | --- | --- |
| Montador | Resolve rótulos e transforma instruções em palavras | [mvn/](mvn/README.md) |
| Executor | Mantém memória, registradores, dispositivo de entrada e trace | [mvn/maquina.py](mvn/maquina.py) |
| Leitor | Entrega um byte por chamada a partir das palavras lidas | [le_byte.asm](asm/le_byte.asm) |
| Pilha | Push/pop com detecção de cheio e vazio | [pilha.asm](asm/pilha.asm) |
| Calculadora | Scanner, operadores e resultado/status | [rpn.asm](asm/rpn.asm) |
| Demonstração | Monta os fontes e apresenta saída JSON | [executar.py](scripts/executar.py) |

### 1. Leitor de bytes

O dispositivo fornece dois bytes por palavra, primeiro o mais significativo. `SUB_LE_BYTE` usa cache e flag para alternar alto/baixo, tratando palavras que parecem negativas na interpretação com sinal. Cada byte retornado fica entre 0 e 255. O dispositivo implementado é fixo; a rotina não escolhe outros periféricos.

### 2. Pilha limitada

A região 0F00–0FFD reserva 254 bytes, ou **127 palavras**. O ponteiro em 0FFE identifica pilha vazia e desce a cada push. O código usa instruções automodificadas para acesso indireto; as rotinas compartilham dados e retorno, portanto não são reentrantes.

### 3. Scanner e operações RPN

Aceita inteiros decimais não negativos, operadores `+ - * /` e separadores. No operador, o primeiro pop é o operando direito: `5 9 -` resulta em −4. Ao terminar deve restar exatamente um valor. Divisão por zero, operador desconhecido e falta/excesso de operandos geram status de erro.

A aritmética é **modular de 16 bits**: `32767 1 +` resulta −32768. A divisão trunca para zero. LF ou byte 00 encerram a expressão; o modelo não distingue um NUL literal do EOF preenchido com zero.

### 4. Montador, execução e trace

O montador de duas passagens entende origem, constantes, rótulos e instruções do subconjunto fornecido. O executor registra o caminho real de instruções e impõe orçamento de até 200.000 instruções por chamada. Ele não implementa todo o ecossistema, linker ou dispositivos da MVN oficial.

## Como executar

**Requisitos:** Python 3.12 e Git. O executor e os testes usam a biblioteca padrão; não há pacote externo para instalar. Não é necessário instalar um simulador MVN separado para a demonstração incluída.

```sh
git clone https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao.git
cd usp-pcs3616-sistemas-programacao
```

```sh
python -m unittest discover -s tests -v
python scripts/executar.py "12 3 +" --trace
python scripts/executar.py "5 9 -"
```

Os resultados esperados são `{"status": 0, "resultado": 15}` e `{"status": 0, "resultado": -4}`. O primeiro comando de execução cria `build/trace.json`, com o rastreamento. Leia esse arquivo para acompanhar memória, operandos e saltos.

### Experimentar limites e erros

```sh
python scripts/executar.py "32767 1 +"
python scripts/executar.py "1 0 /"
```

O primeiro mostra o wrap de 16 bits. O segundo termina com status não zero e código de saída 2; nesse caso o campo de resultado não deve ser interpretado como uma resposta válida. Use apenas texto ASCII na expressão.

Para mudar as rotinas, edite os fontes em `asm/`, execute novamente a suíte e inspecione o trace. O [mapa de memória e ABI](docs/ARQUITETURA.md) informa os endereços compartilhados antes de qualquer alteração.

## O que desenvolvi e aprendi

As rotinas e o ambiente desta edição exercitam representação binária, endianidade, chamadas SC/RS, pilha, código automodificável, montagem e tratamento de erro. As posições recuperadas de argumentos e resultados foram preservadas; extensões de status estão identificadas na [procedência](docs/PROCEDENCIA.md).

**Objetivos pedagógicos:** extrair o byte 0x80 de uma palavra com sinal, explicar por que o 128º push falha e rastrear a ordem dos pops de uma subtração. [Atividades e rubrica](docs/OBJETIVOS_PEDAGOGICOS.md).

## Estado atual

| Disponível | Limite / evolução |
| --- | --- |
| Montador, executor, leitor, pilha e RPN | Modelo didático próprio, sem certificação de compatibilidade oficial |
| Status, erros e rastreamento | Aritmética de 16 bits, entrada ASCII e orçamento finito |
| Nove testes e CI multiplataforma | Sem todos os dispositivos, objetos relocáveis ou ligação externa |
| Contratos e memória documentados | Novas rotinas exigem respeitar a ABI e as regiões reservadas |

## Validação e limites

A suíte percorre os 256 bytes, limites da pilha, expressões de referência e 400 expressões aleatórias. Ela executa o Assembly montado, mas não prova comportamento em um simulador oficial diferente. Os comandos e a evidência estão em [VALIDACAO.md](docs/VALIDACAO.md).

## Documentação e navegação

[Assembly](asm/README.md) · [Montador e máquina](mvn/README.md) · [Scripts](scripts/README.md) · [Testes](tests/README.md) · [Exemplos e trace](assets/README.md) · [Guias por assunto](docs/topicos/README.md) · [Documentação](docs/README.md) · [Branches](docs/BRANCHES.md) · [PRs](docs/PUBLICACAO.md)


## Autoria, referências e licença

**Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334.** Fontes recuperados, componentes de terceiros e trabalhos em grupo mantêm os créditos indicados nos arquivos e na documentação.

[Direitos e créditos](DIREITOS_E_CREDITOS.md) · [Procedência](docs/PROCEDENCIA.md) · [Como contribuir](CONTRIBUTING.md) · [Mudanças](CHANGELOG.md)

## Tópicos do repositório

`assembly` · `virtual-machine` · `assembler` · `stack-machine` · `reverse-polish-notation` · `python` · `computer-architecture` · `systems-programming` · `usp` · `educational`

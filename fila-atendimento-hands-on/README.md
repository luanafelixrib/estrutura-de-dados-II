# Fila de Atendimento — Hands-on

Sistema Inteligente de Atendimento que simula três formas de organizar clientes
em uma central de atendimento: Fila Clássica (FIFO), Fila Circular e Fila de
Prioridade.

## Integrantes

-Luana Felix Ribeiro

## Resumo das implementações

**Fila Clássica**: FIFO usando `collections.deque`. `enqueue` insere no
final, `dequeue` remove do início. Teste com 10 clientes comprova que a
ordem de atendimento é igual à ordem de chegada.

**Fila Circular**: array fixo de capacidade 5, com índices `front` e `rear`
que avançam circularmente (`% capacidade`). Um contador `tamanho` separado
evita a ambiguidade de `front == rear` significar tanto vazia quanto cheia.
Teste demonstra reaproveitamento de posições liberadas após remoção.

**Fila de Prioridade**: usa `heapq` com tuplas `(prioridade, contador,
cliente)`. O `contador` (via `itertools.count()`) evita comparar objetos
`Cliente` diretamente e preserva a ordem de chegada em caso de empate de
prioridade.

**main.py**: gera 20 clientes com prioridades aleatórias, roda as três
simulações e compara, posição a posição, a ordem de saída da fila clássica
com a da fila de prioridade.

## Evidências dos testes

### Fila Clássica (`fila_classica.py`)

```
=== Ordem de chegada (dentro da fila) ===
Cliente1 (senha S001, prioridade 3)
Cliente2 (senha S002, prioridade 3)
Cliente3 (senha S003, prioridade 3)
...
Cliente10 (senha S010, prioridade 3)

=== Ordem de atendimento (dequeue) ===
Cliente1 (senha S001, prioridade 3)
Cliente2 (senha S002, prioridade 3)
Cliente3 (senha S003, prioridade 3)
...
Cliente10 (senha S010, prioridade 3)
```

A ordem de atendimento é idêntica à ordem de chegada, como esperado no FIFO.

### Fila Circular (`fila_circular.py`)

```
=== Inserindo 5 clientes (fila vai ficar cheia) ===
front=0, rear=0, tamanho=5
[Cliente1, Cliente2, Cliente3, Cliente4, Cliente5]

=== Removendo 2 clientes ===
Cliente atendido: Cliente1 (senha S001, prioridade 3)
Cliente atendido: Cliente2 (senha S002, prioridade 3)
front=2, rear=0, tamanho=3
[None, None, Cliente3, Cliente4, Cliente5]

=== Inserindo mais 2 clientes novos ===
Cliente inserido: Cliente6 (senha S006, prioridade 3)
Cliente inserido: Cliente7 (senha S007, prioridade 3)
front=2, rear=2, tamanho=5
[Cliente6, Cliente7, Cliente3, Cliente4, Cliente5]
```

Depois de remover Cliente1 e Cliente2 (posições 0 e 1, que ficaram `None`),
Cliente6 e Cliente7 foram inseridos exatamente nessas posições reaproveitadas
— comprovando o comportamento circular.

### Fila de Prioridade (`fila_prioridade.py`)

```
=== Ordem de atendimento (dequeue) ===
Cliente2 (senha S002, prioridade 1)
Cliente4 (senha S004, prioridade 1)
Cliente3 (senha S003, prioridade 2)
Cliente1 (senha S001, prioridade 3)
Cliente5 (senha S005, prioridade 3)
```

Cliente2 e Cliente4 têm a mesma prioridade (1); Cliente2 chegou primeiro e
foi atendido primeiro, comprovando o desempate por ordem de chegada.

### Desafio Final (`main.py`)

Trecho da comparação final entre a Fila Clássica e a Fila de Prioridade
(20 clientes gerados com prioridades aleatórias):

```
=== Comparação dos resultados ===
Posição 1: Fila Clássica = Cliente2 (prioridade 2) | Fila de Prioridade = Cliente4 (prioridade 1)
Posição 2: Fila Clássica = Cliente3 (prioridade 2) | Fila de Prioridade = Cliente7 (prioridade 1)
Posição 3: Fila Clássica = Cliente4 (prioridade 1) | Fila de Prioridade = Cliente8 (prioridade 1)
...
Total de posições comparadas: 20
Total de posições diferentes entre as duas ordens: 14
```

De 20 clientes, 14 saíram em posição diferente entre as duas estruturas —
os clientes de prioridade 1 (emergência) "furaram fila" na Fila de
Prioridade, saindo bem antes do que sairiam na ordem pura de chegada.

## Relatório

**Por que a ordem da fila de prioridade pode ser diferente da fila
clássica?**

Pois a Fila de Prioridade, como o próprio nome diz, ordena a saída pela prioridade de cada cliente, e só usa a ordem de chegada para desempatar quando dois clientes têm a mesma prioridade. Já a Fila Clássica segue o modelo FIFO, onde o que entra primeiro é o primeiro que sai, sem considerar prioridade nenhuma. Por isso, um cliente com prioridade alta que chegou depois pode ser atendido antes de clientes que chegaram muito antes dele — coisa que nunca aconteceria na Fila Clássica.

**Em quais situações reais uma fila de prioridade seria mais adequada?**

Em qualquer contexto onde a urgência do atendimento importa mais do que o
momento em que a pessoa chegou. Exemplos:
- Pronto-socorro hospitalar (triagem): pacientes em estado grave são atendidos antes de casos leves, independentemente da ordem de chegada.
- Suporte técnico com SLA diferenciado: chamados críticos (sistema fora do ar) são priorizados sobre dúvidas simples.

**Vantagens e limitações da fila circular?**

Vantagens:
- Melhor uso de memória: o espaço é alocado uma única vez, com tamanho fixo, sem precisar crescer dinamicamente.
- Reaproveitamento de posições: 
- Operações de inserção e remoção com custo constante (O(1)).

Limitações:
- Capacidade fixa: uma vez definida, não é possível inserir além do limite
- Maior complexidade de implementação em comparação a uma fila simples, já que é preciso controlar cuidadosamente os índices `front`, `rear` e o tamanho para não confundir fila cheia com fila vazia.

**O que acontece ao tentar inserir um elemento em uma fila circular cheia?**
A implementação não ocorre,pois para poder inserir um elemento tem que haver espaço na fila por isso que fizemos a remoção ou a análise de espaços vazios na fila. Ao tentar inserir em uma fila circular cheia, o método enqueue() detecta que tamanho == capacidade, imprime a mensagem "Fila circular cheia! Não foi possível inserir." e retorna False, sem alterar o array. O cliente não entra na fila — antes de conseguir inserir, é preciso remover algum cliente com dequeue() para abrir espaço.
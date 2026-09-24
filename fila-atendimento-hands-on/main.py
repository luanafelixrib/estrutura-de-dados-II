import random  
from fila_classica import Cliente, Fila 
from fila_circular import FilaCircular  
from fila_prioridade import FilaPrioridade  


clientes = []  # lista que vai guardar os 20 clientes gerados
for i in range(1, 21):  # repete 20 vezes, i vai de 1 até 20
    cliente = Cliente(f"Cliente{i}", f"S{i:03d}", random.randint(1, 3))  # cria cliente com prioridade aleatória
    clientes.append(cliente)  # adiciona o cliente criado na lista


print("=== Clientes na ordem de chegada ===")  # cabeçalho da primeira demonstração
for cliente in clientes:  # percorre a lista de clientes na ordem em que foram gerados
    print(cliente)  # imprime cada cliente


ordem_fila_classica = []  # lista que vai guardar a ordem de saída da fila clássica
print("\n=== Simulação: Fila Clássica (FIFO) ===")
fila = Fila()
for cliente in clientes:
    fila.enqueue(cliente)
for i in range(fila.size()):
    cliente = fila.dequeue()
    print(cliente)
    ordem_fila_classica.append(cliente)  # guarda o cliente atendido, na ordem em que saiu


print("\n=== Simulação: Fila Circular ===")  # cabeçalho da terceira demonstração
fila_circ = FilaCircular(capacidade=5)  # cria a fila circular com capacidade 5

for cliente in clientes:  # percorre os 20 clientes, um de cada vez
    if fila_circ.tamanho == fila_circ.capacidade:  # verifica se a fila circular está cheia
        atendido = fila_circ.dequeue()  # remove um cliente para abrir espaço
        print(f"Cliente atendido: {atendido}")  # imprime quem foi atendido/removido
    fila_circ.enqueue(cliente)  # insere o cliente atual, já com espaço garantido

print("\nEsvaziando o que sobrou na fila circular:")  # cabeçalho da parte final da fila circular
while fila_circ.tamanho > 0:  # repete enquanto ainda houver clientes na fila circular
    atendido = fila_circ.dequeue()  # remove o próximo cliente
    print(f"Cliente atendido: {atendido}")  # imprime quem foi atendido/removido


ordem_fila_prioridade = []  # lista que vai guardar a ordem de saída da fila de prioridade
print("\n=== Simulação: Fila de Prioridade ===")
fila_prio = FilaPrioridade()
for cliente in clientes:
    fila_prio.enqueue(cliente)

print("\nEsvaziando o que sobrou na fila de prioridade:")
while not fila_prio.empty():
    atendido = fila_prio.dequeue()
    print(f"Cliente atendido: {atendido}")
    ordem_fila_prioridade.append(atendido)  # guarda o cliente atendido, na ordem em que saiu

print("\n=== Comparação dos resultados ===")  # cabeçalho da comparação final
furos = 0  # contador de quantas posições tiveram clientes diferentes entre as duas ordens

for posicao, (classico, prioridade) in enumerate(zip(ordem_fila_classica, ordem_fila_prioridade)):  # percorre as duas listas juntas, com o índice da posição
    if classico != prioridade:  # verifica se o cliente da fila clássica é diferente do cliente da fila de prioridade nessa posição
        print(f"Posição {posicao}: Fila Clássica = {classico} | Fila de Prioridade = {prioridade}")  # mostra a diferença encontrada
        furos += 1  # incrementa o contador de diferenças

print(f"\nTotal de posições diferentes entre as duas ordens: {furos}")  # mostra o total de "furos de fila" encontrados
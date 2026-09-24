import heapq  # módulo que implementa a estrutura de heap (fila de prioridade)
import itertools  # usado para gerar um contador incremental (desempate)
from fila_classica import Cliente  # importa a classe Cliente já criada no outro arquivo

class FilaPrioridade:  # classe que implementa a fila de prioridade usando heapq
    def __init__(self):  # construtor
        self.heap = []  # lista que o heapq vai usar internamente como estrutura de heap
        self.contador = itertools.count()  # gerador de números incrementais (0, 1, 2, ...)

    def enqueue(self, cliente):  # insere um cliente na fila de prioridade
        item = (cliente.prioridade, next(self.contador), cliente)  # monta a tupla (prioridade, contador, cliente)
        heapq.heappush(self.heap, item)  # insere a tupla no heap, mantendo a ordem de prioridade

    def dequeue(self):  # remove e retorna o cliente de maior prioridade (menor número)
        if len(self.heap) == 0:  # verifica se o heap está vazio
            print("A lista está vazia")  # avisa que não há cliente para atender
            return None  # não há cliente para retornar
        item_removido = heapq.heappop(self.heap)  # remove a menor tupla (maior prioridade) do heap
        return item_removido[2]  # retorna só o cliente, que está na posição 2 da tupla

    def empty(self):  # verifica se a fila está vazia
        if len(self.heap) == 0:  # checa se o heap não tem nenhum item
            return True  # confirma que está vazia
        else:
            return False  # indica que ainda há clientes na fila


if __name__ == "__main__":  # só executa esse bloco quando o arquivo roda diretamente
    fila_p = FilaPrioridade()  # cria a fila de prioridade

    print("=== Inserindo clientes com prioridades variadas ===")  # cabeçalho da demonstração
    fila_p.enqueue(Cliente("Cliente1", "S001", 3))  # normal, chega primeiro
    fila_p.enqueue(Cliente("Cliente2", "S002", 1))  # emergência, chega em segundo
    fila_p.enqueue(Cliente("Cliente3", "S003", 2))  # prioritário, chega em terceiro
    fila_p.enqueue(Cliente("Cliente4", "S004", 1))  # emergência, chega em quarto (empate com Cliente2)
    fila_p.enqueue(Cliente("Cliente5", "S005", 3))  # normal, chega em quinto

    print("\n=== Ordem de atendimento (dequeue) ===")  # cabeçalho da segunda demonstração
    while not fila_p.empty():  # repete enquanto ainda houver clientes na fila
        cliente = fila_p.dequeue()  # remove o cliente de maior prioridade
        print(cliente)  # imprime o cliente que acabou de ser atendido
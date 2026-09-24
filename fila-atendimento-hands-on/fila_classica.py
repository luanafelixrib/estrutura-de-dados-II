from collections import deque  

class Cliente:  # classe que representa um cliente da central de atendimento
    def __init__(self, nome, senha, prioridade):  # construtor: recebe os dados do cliente
        self.nome = nome  # guarda o nome do cliente
        self.senha = senha  # guarda a senha do cliente
        self.prioridade = prioridade  # guarda a prioridade (1, 2 ou 3)

    def __repr__(self):  # define como o cliente aparece quando impresso
        return f"{self.nome} (senha {self.senha}, prioridade {self.prioridade})"  # string formatada com os dados


class Fila:  # classe que implementa a fila clássica FIFO
    def __init__(self):  # construtor da fila
        self.itens = deque()  # cria a estrutura interna vazia que vai guardar os clientes

    def enqueue(self, cliente):  # método para inserir um cliente na fila
        self.itens.append(cliente)  # adiciona o cliente no final da fila

    def dequeue(self):  # método para atender/remover o próximo cliente
        if self.empty():  # verifica se a fila está vazia
            print("Fila vazia, não há cliente para atender.")  # avisa que não há o que remover
            return None  # não há cliente para retornar
        return self.itens.popleft()  # remove e retorna o cliente do início da fila

    def head(self):  # método para consultar o próximo cliente sem remover
        if self.empty():  # verifica se a fila está vazia
            print("Fila vazia, não há próximo cliente.")  # avisa que não há cliente a consultar
            return None  # não há cliente para retornar
        return self.itens[0]  # retorna o cliente do início sem removê-lo

    def size(self):  # método para informar quantos clientes há na fila
        return len(self.itens)  # retorna a quantidade de itens armazenados

    def empty(self):  # método para verificar se a fila está vazia
        return len(self.itens) == 0  # retorna True se não houver itens, False caso contrário


if __name__ == "__main__":  # só executa esse bloco quando o arquivo roda diretamente
    fila = Fila()  # cria a fila clássica

    for i in range(0, 10):  # repete 10 vezes, i vai de 1 até 10
        cliente = Cliente(f"Cliente{i}", f"S{i:03d}", 3)  # cria o cliente i com prioridade fixa 3
        fila.enqueue(cliente)  # insere esse cliente na fila

    print("=== Ordem de chegada (dentro da fila) ===")  # cabeçalho da primeira demonstração
    for cliente in fila.itens:  # percorre os clientes na ordem em que estão guardados
        print(cliente)  # imprime cada cliente sem removê-lo

    print("\n=== Ordem de atendimento (dequeue) ===")  # cabeçalho da segunda demonstração
    for i in range(fila.size()):  # repete uma vez para cada cliente presente na fila
        cliente = fila.dequeue()  # remove o próximo cliente da fila (o do início)
        print(cliente)  # imprime o cliente que acabou de ser atendido
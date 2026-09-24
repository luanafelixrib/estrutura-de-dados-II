from fila_classica import Cliente  # importa a classe Cliente já criada no outro arquivo

class FilaCircular:  # classe que implementa uma fila circular de capacidade fixa
    def __init__(self, capacidade=5):  # construtor, capacidade padrão de 5
        self.capacidade = capacidade  # guarda o tamanho máximo da fila
        self.itens = [None] * capacidade  # cria um array fixo, todas posições vazias (None)
        self.front = 0  # índice de onde o próximo cliente será atendido
        self.rear = 0  # índice de onde o próximo cliente será inserido
        self.tamanho = 0  # quantidade de clientes atualmente na fila

    def enqueue(self, cliente):  # insere um cliente na fila
        if self.tamanho == self.capacidade:  # verifica se a fila está cheia
            print("Fila circular cheia! Não foi possível inserir.")  # avisa que não deu pra inserir
            return False  # indica falha na inserção
        self.itens[self.rear] = cliente  # coloca o cliente na posição rear
        self.rear = (self.rear + 1) % self.capacidade  # avança rear circularmente
        self.tamanho += 1  # incrementa a quantidade de clientes na fila
        return True  # indica sucesso na inserção

    def dequeue(self):  # remove e retorna o cliente do início da fila
        if self.tamanho == 0:  # verifica se a fila está vazia
            print("Fila circular vazia!")  # avisa que não há cliente para atender
            return None  # não há cliente para retornar
        cliente_atendido = self.itens[self.front]  # guarda o cliente que está na posição front
        self.itens[self.front] = None  # limpa essa posição, marcando como livre
        self.front = (self.front + 1) % self.capacidade  # avança front circularmente
        self.tamanho -= 1  # decrementa a quantidade de clientes na fila
        return cliente_atendido  # retorna o cliente removido

    def estado(self):  # mostra o estado interno da fila (para debug/demonstração)
        print(f"front={self.front}, rear={self.rear}, tamanho={self.tamanho}")  # mostra os índices e o tamanho atual
        print(self.itens)  # mostra o conteúdo bruto do array, incluindo posições None


if __name__ == "__main__":  # só executa esse bloco quando o arquivo roda diretamente
    fila_c = FilaCircular(capacidade=5)  # cria a fila circular com capacidade 5

    print("=== Inserindo 5 clientes (fila vai ficar cheia) ===")  # cabeçalho da primeira demonstração
    for i in range(1, 6):  # repete 5 vezes, i vai de 1 até 5
        cliente = Cliente(f"Cliente{i}", f"S{i:03d}", 3)  # cria o cliente i com prioridade fixa 3
        fila_c.enqueue(cliente)  # insere esse cliente na fila circular
    fila_c.estado()  # mostra front, rear e o array depois de encher a fila

    print("\n=== Removendo 2 clientes ===")  # cabeçalho da segunda demonstração
    for i in range(2):  # repete 2 vezes
        atendido = fila_c.dequeue()  # remove o cliente do início da fila
        print(f"Cliente atendido: {atendido}")  # imprime quem foi atendido/removido
    fila_c.estado()  # mostra front, rear e o array depois de remover 2 clientes

    print("\n=== Inserindo mais 2 clientes novos ===")  # cabeçalho da terceira demonstração
    for i in range(6, 8):  # repete 2 vezes, i vai de 6 até 7 (continuando a numeração)
        cliente = Cliente(f"Cliente{i}", f"S{i:03d}", 3)  # cria o cliente i com prioridade fixa 3
        fila_c.enqueue(cliente)  # insere esse cliente, reutilizando posições liberadas
        print(f"Cliente inserido: {cliente}")  # imprime o cliente que acabou de entrar
    fila_c.estado()  # mostra front, rear e o array — repare que ocupou as posições que estavam None
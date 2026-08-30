import random

def gerar_lista(tamanho):  # cria uma lista vazia que vai receber os números aleatórios
    lista = []
    for i in range(tamanho):     # repete "tamanho" vezes (ex: 10, 20, 1000)

        numero = random.randint(1, 1000)  # sorteia um número entre 1 e 1000
        lista.append(numero)              # adiciona o número na lista
    return lista                         # devolve a lista pronta
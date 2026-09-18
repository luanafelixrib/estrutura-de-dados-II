def insertion_sort(vetor):
    comparacoes = 0     # conta toda comparação feita no while
    movimentacoes = 0   # conta toda vez que um elemento é deslocado

    n = len(vetor)
    for i in range(1, n):          # percorre do 2º elemento até o último (a chave a ser inserida)
        chave = vetor[i]           # elemento que será inserido na parte já ordenada
        j = i - 1                  # começa comparando com o último da parte ordenada

        while j >= 0 and vetor[j] > chave:  # enquanto não chegar ao início e o elemento for maior que a chave
            comparacoes += 1
            movimentacoes += 1
            vetor[j+1] = vetor[j]  # desloca o elemento maior uma posição pra direita
            j -= 1                 # continua comparando com o próximo à esquerda

        vetor[j + 1] = chave       # insere a chave no espaço aberto (posição correta)

    return comparacoes, movimentacoes
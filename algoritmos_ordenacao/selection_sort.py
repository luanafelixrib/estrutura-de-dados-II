def selection_sort(vetor):
    n = len(vetor)
    comparacoes = 0     # conta toda comparação feita no loop interno
    trocas = 0           # conta só quando realmente troca de posição

    for i in range(n - 1):             # controla o início do trecho ainda não ordenado
        menor = i                      # assume que o primeiro do trecho é o menor

        for j in range(i + 1, n):      # percorre o resto do trecho procurando um menor
            comparacoes += 1
            if vetor[j] < vetor[menor]:
                menor = j               # atualiza o índice do menor encontrado

        if menor != i:                 # só troca se o menor não estiver já na posição certa
            temp = vetor[menor]
            vetor[menor] = vetor[i]
            vetor[i] = temp
            trocas += 1

    return comparacoes, trocas
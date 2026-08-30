def bubble_sort(array):
    n = len(array)
    contador = 0  # conta comparações
    trocas = 0    # conta trocas

    for i in range(0, n):               # controla quantas passadas serão feitas
        for j in range(0, n - i - 1):   # percorre os pares vizinhos (limite diminui a cada passada)
            contador += 1                # toda comparação é contada, mesmo se não trocar
            if array[j] > array[j+1]:    # testa se estão fora de ordem
                # troca os dois de posição
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                trocas += 1               # só conta quando realmente troca

    return contador, trocas  # devolve os dois totais
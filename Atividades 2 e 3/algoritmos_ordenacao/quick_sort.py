# variáveis globais: acumulam o total entre todas as chamadas recursivas
comparacoes = 0
mvmaior = 0
mvmenor = 0
mvtotal = 0

def quicksort(n):
    global comparacoes, mvmaior, mvmenor, mvtotal

    if len(n) <= 1:
        return n  # caso base: lista com 0 ou 1 elemento já está ordenada

    else:
        menores = []
        maiores = []
        pivo = n[-1]  # escolhe o último elemento como pivô

        for elemento in n[:-1]:  # percorre tudo, menos o pivô
            comparacoes += 1      # conta toda comparação feita
            if elemento < pivo:
                menores.append(elemento)  # vai pro lado dos menores
                mvmenor += 1
            else:
                maiores.append(elemento)  # vai pro lado dos maiores
                mvmaior += 1

        mvtotal = mvmenor + mvmaior  # soma o total de movimentações

    # ordena recursivamente cada lado e junta tudo: menores + pivô + maiores
    return quicksort(menores) + [pivo] + quicksort(maiores)
import random
# Função principal de busca sequencial em matriz
def busca_matriz(matriz, valor):
    comparacao = 0
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            comparacao += 1
            if matriz[i][j] == valor:
                return True, i, j, comparacao

    return False, None, None, comparacao


# Função interativa: usuário digita um valor e busca na matriz 10x10
def busca_interativa():
    valor_procurado = int(input("Digite o valor que você deseja encontrar: "))
    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_10x10, valor_procurado)

    if achou == True:
        print(f"O número procurado está na linha {linha} e na coluna {coluna}")
    else:
        print("Valor não encontrado na matriz")

    print(f"Comparações realizadas: {qtd_comparacao}")


# ---------- Geração das matrizes de teste ----------

# Matriz 2x2 (fixa, escrita na mão)
matriz_2x2 = [
    [1, 2],
    [3, 4]
]

# Matriz 10x10 (gerada automaticamente, números de 1 a 100)
matriz_10x10 = []
n_atual = 1
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(n_atual)
        n_atual += 1
    matriz_10x10.append(linha)

# Matriz 100x100 (gerada automaticamente, números de 1 a 10000)
matriz_100x100 = []
n_atual = 1
for i in range(100):
    linha = []
    for j in range(100):
        linha.append(n_atual)
        n_atual += 1
    matriz_100x100.append(linha)


# ---------- Testes automáticos (para gerar a tabela da atividade) ----------

if __name__ == "__main__":
    # TESTE MATRIZ 2X2
    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_2x2, 1)
    print(f"Busca no início (2x2): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_2x2, 4)
    print(f"Busca no final (2x2): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_2x2, 28)
    print(f"Busca inexistente (2x2): {qtd_comparacao} comparações.\n")

    # TESTE MATRIZ 10X10
    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_10x10, 1)
    print(f"Busca no início (10x10): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_10x10, 100)
    print(f"Busca no final (10x10): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_10x10, 256)
    print(f"Busca inexistente (10x10): {qtd_comparacao} comparações.\n")

    # TESTE MATRIZ 100X100
    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_100x100, 1)
    print(f"Busca no início (100x100): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_100x100, 10000)
    print(f"Busca no final (100x100): {qtd_comparacao} comparações.")

    achou, linha, coluna, qtd_comparacao = busca_matriz(matriz_100x100, 920345)
    print(f"Busca inexistente (100x100): {qtd_comparacao} comparações.")
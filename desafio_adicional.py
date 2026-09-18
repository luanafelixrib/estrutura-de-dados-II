import sys
sys.setrecursionlimit(3000)
import gerar_dados
from algoritmos_ordenacao import bubble_sort
from algoritmos_ordenacao import quick_sort
from algoritmos_ordenacao import insertion_sort
from algoritmos_ordenacao import selection_sort


def rodar_desafio():
    tipos = ["aleatorio", "ordenado", "invertido"]
    tamanhos = [10, 20, 1000]

    for tipo in tipos:
        print(f"\n===== Tipo de vetor: {tipo} =====")

        for tamanho in tamanhos:
            # gera o vetor original de acordo com o tipo escolhido
            if tipo == "aleatorio":
                vetor_original = gerar_dados.gerar_lista(tamanho)
            elif tipo == "ordenado":
                vetor_original = sorted(gerar_dados.gerar_lista(tamanho))
            elif tipo == "invertido":
                vetor_original = sorted(gerar_dados.gerar_lista(tamanho))[::-1]

            # faz as 4 cópias independentes
            lista_bs = vetor_original.copy()
            lista_qs = vetor_original.copy()
            lista_is = vetor_original.copy()
            lista_ss = vetor_original.copy()

            # roda os 4 algoritmos
            comparacoes_bs, trocas_bs = bubble_sort.bubble_sort(lista_bs)
            comparacoes_is, trocas_is = insertion_sort.insertion_sort(lista_is)
            comparacoes_ss, trocas_ss = selection_sort.selection_sort(lista_ss)

            quick_sort.comparacoes = 0
            quick_sort.mvmenor = 0
            quick_sort.mvmaior = 0
            quick_sort.mvtotal = 0
            quick_sort.quicksort(lista_qs)
            comparacoes_qs = quick_sort.comparacoes
            mvtotal_qs = quick_sort.mvtotal

            # mostra os resultados
            print(f"--- Tamanho: {tamanho} ---")
            print(f"Bubble Sort  -> Comparações: {comparacoes_bs} | Trocas: {trocas_bs}")
            print(f"Quick Sort   -> Comparações: {comparacoes_qs} | Movimentações: {mvtotal_qs}")
            print(f"Insert Sort  -> Comparações: {comparacoes_is} | Trocas: {trocas_is}")
            print(f"Select Sort  -> Comparações: {comparacoes_ss} | Trocas: {trocas_ss}")
            print()


# roda automaticamente se você executar ESTE arquivo diretamente
if __name__ == "__main__":
    rodar_desafio()
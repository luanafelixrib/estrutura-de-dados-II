import gerar_dados
from algoritmos_ordenacao import bubble_sort
from algoritmos_ordenacao import quick_sort
from algoritmos_ordenacao import selection_sort
from algoritmos_ordenacao import insertion_sort
import busca_matriz
import array_temperaturas
import matriz_sensores


continuar = True  # controla se o menu continua aparecendo

while continuar:  # repete até o usuário escolher sair
    print("\n===== MENU =====")
    print("1 - Comparar Bubble Sort e Quick Sort")
    print("2 - Busca em matriz")
    print("3 - Analisar temperaturas")
    print("4 - Analisar sensores")
    print("5 - Sair")

    escolha = int(input("Digite a opção desejada: "))  # converte pra número, pra comparar certo

    if escolha == 1:
        tamanhos = [10, 20, 1000]  # os 3 tamanhos que a atividade pede

        for tamanho in tamanhos:
            # gera os dados e faz 2 cópias independentes (uma pra cada algoritmo)
            minha_lista = gerar_dados.gerar_lista(tamanho)
            lista_bs = minha_lista.copy()
            lista_qs = minha_lista.copy()
            lista_is = minha_lista.copy()
            lista_ss = minha_lista.copy()

            # roda o Bubble Sort e recebe os contadores de volta
            comparacoes_bs, trocas_bs = bubble_sort.bubble_sort(lista_bs)
            comparacoes_is, trocas_is = insertion_sort.insertion_sort(lista_is)
            comparacoes_ss, trocas_ss = selection_sort.selection_sort(lista_ss)

            # zera os contadores globais do Quick Sort antes de rodar de novo
            quick_sort.comparacoes = 0
            quick_sort.mvmenor = 0
            quick_sort.mvmaior = 0
            quick_sort.mvtotal = 0

            # roda o Quick Sort (ele mexe direto nas variáveis globais do módulo)
            quick_sort.quicksort(lista_qs)
            comparacoes_qs = quick_sort.comparacoes
            mvtotal_qs = quick_sort.mvtotal

            # mostra os resultados desse tamanho
            print(f"--- Tamanho: {tamanho} ---")
            print(f"Bubble Sort  -> Comparações: {comparacoes_bs} | Trocas: {trocas_bs}")
            print(f"Quick Sort   -> Comparações: {comparacoes_qs} | Movimentações: {mvtotal_qs}")
            print(f"Insert Sort  -> Comparações: {comparacoes_is} | Trocas: {trocas_is}")
            print(f"Select Sort  -> Comparações: {comparacoes_ss} | Trocas: {trocas_ss}")
            print()

    elif escolha == 2:
        busca_matriz.busca_interativa()  # pede o valor e busca na matriz 10x10

    elif escolha == 3:
        array_temperaturas.analisar_temperaturas()  # pede 10 temperaturas e mostra a análise

    elif escolha == 4:
        # gera a matriz de sensores e guarda numa variável
        sensores = matriz_sensores.gerar_sensores()
        # usa essa mesma matriz nas 4 análises seguintes
        matriz_sensores.media_por_sensor(sensores)
        matriz_sensores.maior_temperatura(sensores)
        matriz_sensores.media_geral(sensores)
        matriz_sensores.leituras_acima_limite(sensores)

    elif escolha == 5:
        print("Encerrando o programa...")
        continuar = False  # faz o while parar de repetir

    else:
        print("Opção inválida. Tente novamente.")  # protege contra número fora de 1-5
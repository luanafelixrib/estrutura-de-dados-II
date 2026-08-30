def analisar_temperaturas():
    temperaturas = []

    for i in range(0, 10):
        temperatura = float(input("Digite a temperatura: "))
        temperaturas.append(temperatura)

    print(f"As temperaturas digitadas foram: {temperaturas}")
        # Mostra a tabela de índice x temperatura
    print("\nÍndice:     ", end="")
    for i in range(len(temperaturas)):
        print(f"{i:>8}", end="")
    print()

    print("Temperatura:", end="")
    for temp in temperaturas:
        print(f"{temp:>8}", end="")
    print()

    media = sum(temperaturas) / len(temperaturas)
    print(f"A média das temperaturam foi: {media}")

    maior = temperaturas[0]
    indice_maior = 0
    for i in range(0, len(temperaturas)):
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            indice_maior = i

    menor = temperaturas[0]
    indice_menor = 0
    for i in range(0, len(temperaturas)):
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            indice_menor = i

    acima_media = []
    for temperatura in temperaturas:
        if temperatura > media:
            acima_media.append(temperatura)

    print(f"As temperaturas que estão acima da média são: ", acima_media)
    print(f"A quantidade de temperaturas acima da media foi: ", len(acima_media))
    print(f"Maior temperatura: {maior} (índice {indice_maior})")
    print(f"Menor temperatura: {menor} (índice {indice_menor})")

if __name__ == "__main__":
    analisar_temperaturas()
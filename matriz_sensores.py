import random

# 1. Gera a matriz de sensores com valores aleatórios
def gerar_sensores():
    sensores = []
    for i in range(5):
        linha = []
        for j in range(24):
            temperatura = round(random.uniform(15, 35), 2)
            linha.append(temperatura)
        sensores.append(linha)
    return sensores


# 2. Calcula e mostra a média de cada sensor
def media_por_sensor(sensores):
    for indice, linha in enumerate(sensores):
        media_sensor = round(sum(linha) / len(linha), 2)
        print(f"A media do sensor {indice + 1} é: {media_sensor}")


# 3. Acha a maior temperatura, o sensor e o horário
def maior_temperatura(sensores):
    maior = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0

    for i in range(len(sensores)):
        for j in range(len(sensores[0])):
            if sensores[i][j] >= maior:
                maior = sensores[i][j]
                sensor_maior = i
                horario_maior = j

    print(f"A maior temperatura registrada foi: {maior}, que se encontra no sensor {sensor_maior + 1} e no horário {horario_maior}")


# Função auxiliar: "achata" a matriz numa lista única (usada pelas próximas duas funções)
def achatar_matriz(sensores):
    todas_medicoes = []
    for linha in sensores:
        todas_medicoes.extend(linha)
    return todas_medicoes


# 4. Calcula a média geral (todas as 120 medições)
def media_geral(sensores):
    todas_medicoes = achatar_matriz(sensores)
    media = round(sum(todas_medicoes) / len(todas_medicoes), 2)
    print(f"A média geral de todas as temperaturas é: {media}")


# 5. Pede um limite ao usuário e mostra quantas/quais medições estão acima dele
def leituras_acima_limite(sensores):
    limite = float(input("Digite o valor para comparação: "))
    todas_medicoes = achatar_matriz(sensores)

    acima_limite = []
    for valor in todas_medicoes:
        if valor > limite:
            acima_limite.append(valor)

    print(f"A quantidade de valores acima do solicitado são: {len(acima_limite)} e são eles {acima_limite}")


# Bloco de teste (só roda se você executar ESTE arquivo diretamente)
if __name__ == "__main__":
    sensores = gerar_sensores()
    print(sensores)
    media_por_sensor(sensores)
    maior_temperatura(sensores)
    media_geral(sensores)
    leituras_acima_limite(sensores)
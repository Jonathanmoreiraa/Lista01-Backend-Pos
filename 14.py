import random

matriz = [[0 for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        matriz[i][j] = random.randint(1,10)

matrizT = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        matrizT[j][i] = matriz[i][j]

for i in range(len(matrizT)):
    print(matrizT[i])
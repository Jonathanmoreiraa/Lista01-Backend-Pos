import random
matriz = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i == j:
            matriz[i][j] = 1
        elif i < j:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 2

for i in range(10):
    print(matriz[i])

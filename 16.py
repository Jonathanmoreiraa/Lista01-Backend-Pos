matriz = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Informe o elemnto da linha {i+1} e coluna {j+1}: "))

det = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1]) - (matriz[2][0] * matriz[1][1] * matriz[0][2]) - (matriz[2][1] * matriz[1][2] * matriz[0][0]) - (matriz[2][2] * matriz[1][0] * matriz[0][1])

for i in range(3):
    print(matriz[i])

print(det)
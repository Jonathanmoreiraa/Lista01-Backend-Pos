def primo(num):
    m = 0
    for i in range(2, num):
        if num % i == 0:
            m += 1
    if m == 0:
        return True
    else:
        return False
matriz = []

matriz = [[0 for _ in range(10)] for _ in range(10)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j != len(matriz[i]) - 1:
            matriz[i][j] = int(f"{i}{j+1}")
        else:
            matriz[i][j] = int(f"{i}{j}")+1

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        ver = primo(matriz[i][j])
        if ver ==  True and matriz[i][j] > 1:
            matriz[i][j] = "*"
for i in range(10):
    print(matriz[i])



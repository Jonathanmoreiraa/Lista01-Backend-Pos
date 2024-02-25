def crescente(vetor):
    for i in range(10):
        for j in range(0, 10-i-1):
           if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

def decrescente(vetor):
    for i in range(10):
        for j in range(0, 10-i-1):
           if vetor[j] < vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

vetores = []
for i in range(10):
    valor = int(input(f"Informe um número inteiro: "))
    vetores.append(valor)

print(crescente(vetores))
print(decrescente(vetores))
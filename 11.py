vetor = []

while len(vetor) < 10:
    num = int(input("Informe o número: "))
    vetor.append(num)

par = 0
somaImpar = []

for vet in vetor:
    if vet % 2 == 0:
        par += vet
    else:
        somaImpar.append(vet)

print(f"A soma é {par}")
media = sum(somaImpar) / len(somaImpar)
print(f"Média impar é {media}")
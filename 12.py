import random
vetor = []
maiores = []

while len(vetor) < 1000:
    numero = random.randint(1, 1000)

    if numero >= 700:
        maiores.append(numero)

    vetor.append(numero)
porcentagem = (len(maiores) / len(vetor)) * 100
print(f"A porcentagem de números maiores ou iguais a 700 existentes no vetor é {porcentagem}")
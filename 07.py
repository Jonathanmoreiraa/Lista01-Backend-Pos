import random

def recebeNumero():
    num = int(input("Informe um número inteiro: "))
    if num >= 0 and num <= 9:
        return num
    else:
        print("O número deve ser entre 0 e 9!")
        num = recebeNumero()
        return num

aleatorio = random.randint(0, 9)
num = recebeNumero()

if num == aleatorio:
    print("Você acertou número o {num} (sorteado) em 1 tentativa".format(num = aleatorio))
else:
    cont = 1
    while num != aleatorio:
        cont += 1
        num = recebeNumero()
    print("Você acertou número o {num} (sorteado) em {c} tentativas".format(num = aleatorio, c = cont))

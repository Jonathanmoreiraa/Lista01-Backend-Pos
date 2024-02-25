def recebeNumero():
    num = int(input("Informe um número inteiro: "))
    if num > 1:
        return num
    else:
        print("O número deve ser inteiro e maior que 1!")
        num = recebeNumero(num)
        return num
    
num = recebeNumero()
m = 0
for i in range(2, num):
    if num % i == 0:
        m += 1
if m == 0:
    print("Esse número é primo!")
else:
    print("Esse número não é primo!")
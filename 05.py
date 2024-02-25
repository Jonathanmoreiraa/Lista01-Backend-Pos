def recebeNumero(num1):
    num2 = int(input("Informe o segundo número: "))
    if num2 != num1 or num2 > 0:
        return num2
    else:
        print("O segundo número deve ser maior que zero e diferente do primeiro!")
        num2 = recebeNumero(num1)
        return num2
    

num1 = int(input("Informe o primeiro número: "))
num2 = recebeNumero(num1)
j = num1
while j >= num1 and j <= num2:
    for i in range(1,11,1):
        valor = j * i
        print("{um} * {dois} = {r}".format(um = j, dois = i, r = valor))
    print("\n")
    j +=1
def conta(num1, num2):
    if acao == "1":
        soma = num1 + num2
        print("A soma é: {soma}".format(soma = soma))
    elif acao == "2":
        sub = num1 - num2
        print("A subtração é: {sub}".format(sub = sub))
    elif acao == "3":
        mult = num1 * num2
        print("A multilicação é: {mult}".format(mult = mult))
    elif acao == "4":
        divisao = num1 / num2
        print("A divisão é: {div}".format(div = divisao))
    else:
        print("Número incorreto!")
        conta(num1, num2)
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
acao = input("Informe o número que represente a ação escolhida: \n1 - Somar\n2- Subtrair\n3 - Multiplicar\n4- Dividir\n")
conta(num1, num2)
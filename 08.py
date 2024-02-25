def validador():
    cpf = str(input("Digite um CPF para ser validado ao lado: "))

    #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
    if len(cpf) > 11:
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
    elif len(cpf) == 11:
        numeros = [int(digito) for digito in cpf]
    qtd = False
    validacao1 = False
    validacao2 = False

    if len(numeros) == 11:
        qtd = True
    
        soma = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
        digito = (soma * 10 % 11) % 10
        if numeros[9] == digito:
            validacao1 = True

        soma1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
        digito1 = (soma1 *10 % 11) % 10
        if numeros[10] == digito1:
            validacao2 = True

        if qtd == True and validacao1 == True and validacao2 == True:
            print(f"O CPF {cpf} é válido.")
        else:
            print(f"O CPF {cpf} não é válido.")
    else:
        print(print(f"O CPF {cpf} não é válido."))

validador()
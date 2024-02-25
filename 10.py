def fazer_login(login, senha, n):
    if login == "IFSP" and senha == "PosWEB":
        print("Login efetuado com sucesso!")
    else:
        n -= 1
        if n == 0:
            print("Acesso negado!")
        else:
            if n == 1:
                print(f"Você tem mais {n} tentativa!")
            else:
                print(f"Você tem mais {n} tentativas!")

            login = input("Informe o login: ")
            senha = input("Informe a senha: ")
            fazer_login(login, senha, n)

login = input("Informe o login: ")
senha = input("Informe a senha: ")
fazer_login(login, senha, 3)
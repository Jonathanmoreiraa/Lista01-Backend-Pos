def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Informe um número para o cálculo: "))    
valor = fatorial(n)
print(f"O resultado é {valor}")
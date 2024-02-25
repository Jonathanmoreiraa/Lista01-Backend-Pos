def informePeso():
    peso = input("Informe seu peso: ")
    if peso != "":
        return float(peso)
    else:
        print("Erro ao acessar o peso!")
        peso = informePeso()
        return float(peso)
    
def informeAltura():
    altura = input("Informe sua altura: ")
    if altura != "":
        return float(altura)
    else:
        print("Erro ao acessar a altura!")
        altura = informeAltura()
        return float(altura)

peso = informePeso()
altura = informeAltura()
imc = peso / (altura * altura)

if imc <= 16.5:
    print("Desnutrição")
elif imc > 16.5 and imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("Peso normal") 
elif imc > 25 and imc <= 29.9:
    print("Sobrepeso") 
else:
    print("Obesidade")
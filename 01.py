nome = input("Informe o nome: ")
endereco = input("Informe o endereço: ")
valor = input("Informe o valor: ")
data = input("Informe a data: ")

aviso = "\n\t\t\tAVISO\t"
frase = "Caro cliente Sr(a) {nome}, os produtos da sua compra no valor de R$ {valor} serão entregues no endereço abaixo:".format(nome = nome, valor = valor)
frase_endereco = "Rua {endereco}".format(endereco = endereco)
entrega = "Data de entrega: {data}".format(data = data)
agradecimento = "******************** Obrigado pela Preferência! **********************"
print(aviso)
print(frase)
print(frase_endereco)
print(entrega)
print(agradecimento)
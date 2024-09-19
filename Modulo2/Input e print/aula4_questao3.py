# 3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é
# calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o
# preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
# Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
# A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas
# casas decimais).
# Entrada:
# Digite o nome do produto 1: calça
# Digite o preço unitário do produto 1: 199.90
# Digite a quantidade do produto 1: 3
# Digite o nome do produto 2: camisa
# Digite o preço unitário do produto 2: 49.95
# Digite a quantidade do produto 2: 10
# Digite o nome do produto 3: cinto
# Digite o preço unitário do produto 3: 25
# Digite a quantidade do produto 3: 3

# Saída:
# Total: R$1,174.20

#################### PRODUTO 1 ####################
# Leitura do nome do pruduto 1
nome_produto1= input("Digite o nome do produto 1:")

#Leitura do preço unitario do produto 1 
preco_unitario1= float(input("Digite o preço unitario do produto 1:"))

# Leitura da quantidade do produto 1
quantidade1= int(input("Digite a quantidade do produto 1:"))

#################### PRODUTO 2 ####################
# Leitura do nome do pruduto 2
nome_produto2= input("Digite o nome do produto 2:")

#Leitura do preço unitario do produto 2
preco_unitario2= float(input("Digite o preço unitario do produto 2:"))

# Leitura da quantidade do produto 2
quantidade2= int(input("Digite a quantidade do produto 2:"))

#################### PRODUTO 3 ####################
# Leitura do nome do pruduto 3
nome_produto3= input("Digite o nome do produto 3:")

#Leitura do preço unitario do produto 3
preco_unitario3= float(input("Digite o preço unitario do produto 3:"))

# Leitura da quantidade do produto 3
quantidade3= int(input("Digite a quantidade do produto 3:"))

# Calculo do preço total do produto 1
total_produto1= preco_unitario1*quantidade1

# Calculo do preço total do produto 2
total_produto2= preco_unitario2*quantidade2

# Calculo do preço total do produto 3
total_produto3= preco_unitario3*quantidade3

# Total da compra
preco_total= total_produto1+total_produto2+total_produto3

#Resultado
print(f"Total: R${preco_total:,.2f}")
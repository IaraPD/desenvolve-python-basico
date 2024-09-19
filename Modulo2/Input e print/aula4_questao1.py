# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado
# da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.
# O terreno possui 250m2 e custa R$512,490.50
# Comente na linha acima de cada instrução uma breve descrição da instrução.
# Fórmulas:
# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

# Leitura do comprimento do terreno
comprimento= int(input("Digite o comprimento do terreno (em metros):"))

#Leitura da largura do terreno
largura= int(input("Digite a largura do terreno (em metros):"))

#Leitura do preço
preco_m2= float("Digite o preço por metro quadrado (em reais):")

#Calculo da area do terreno em metros quadrados
area_m2= comprimento*largura

#Calculo do preço
preco_total= preco_m2*area_m2

#Resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
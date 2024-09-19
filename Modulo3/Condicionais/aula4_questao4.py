# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do
# pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve
# calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg


# Recebendo a distância e o peso do pacote dp usuário
distancia= float(input("Insira a distância da entrega em quilômetros:"))
peso= float(input("Insita o peso do pacote em quilogramas:"))

# Calculando o valor do frete de aordo com as regras estabelecidas
if distancia <=100:
    valor_frete= peso*1
elif 1001 <= distancia <=300:
    valor_frete= peso*1.50
else:
    valor_frete= peso*2

# Acrescentando taxa para pacotes com peso superior a 10 kg
if peso >10:
    valor_frete+=10
    print("O valor do frete é de r$ {valor_frete:.2f}")
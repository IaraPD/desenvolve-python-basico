# 2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir,
# converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

# 86 graus Fahrenheit são 30 graus Celsius.


# Leitura do valor de temperaturaem graus Fahrenheit
Fahrenheit= int(input("Digite a temperatura em graus Fahrenheit: "))

# Conversão da temperatura
celsius= (Fahrenheit-32)/(5/9)

# Conversão de celsius para um inteiro
celsius_inteiro= int(celsius)

#Resultado
print(f"{Fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")
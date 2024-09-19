# Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses
# dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado
# para duas casas decimais.
#	Exemplo de interação:
# Digite o primeiro número: 3.1415
# Digite o segundo número: 1.4142
# A diferença absoluta entre os números é: 1.73

def diferenca_absoluta():
    num1= float(input("Digite o primeiro número:"))
    num2= float(input("Digite o segundo número: "))
    
    diferenca= abs(num1-num2)
    diferenca_arredondada= round(diferenca, 2)

    print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")

    diferenca_arredondada()
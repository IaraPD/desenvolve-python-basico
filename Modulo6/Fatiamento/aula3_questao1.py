# 1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os
# armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )

# Solicitar ao usuário uma quantidade indefinida de números inteiros
numeros = input("Digite pelo menos 4 números inteiros, separados por espaço: ").split()
numeros = [int(n) for n in numeros]

# Garantir que há pelo menos 4 números
if len(numeros) < 4:
    print("Por favor, insira pelo menos 4 números.")
else:
    # A lista original
    print("Lista original:", numeros)
    # Os 3 primeiros elementos
    print("Os 3 primeiros elementos:", numeros[:3])
    # Os 2 últimos elementos
    print("Os 2 últimos elementos:", numeros[-2:])
    # A lista invertida
    print("A lista invertida:", numeros[::-1])
    # Os elementos de índice par
    print("Os elementos de índice par:", numeros[::2])
    # Os elementos de índice ímpar
    print("Os elementos de índice ímpar:", numeros[1::2])
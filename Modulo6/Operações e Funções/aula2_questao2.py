# 2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida
# gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos.
# Em seguida imprima:
# A lista elementos
# A soma dos valores da lista
# A média dos valores da lista


import random
# Gerar um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Soma dos valores da lista
soma_valores = sum(elementos)

# Média dos valores da lista
media_valores = soma_valores / len(elementos)

# Imprimir os resultados
print("Lista elementos:", elementos)
print("Soma dos valores:", soma_valores)
print("Média dos valores:", media_valores)
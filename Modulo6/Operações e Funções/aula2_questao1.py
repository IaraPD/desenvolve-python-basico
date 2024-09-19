# 1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima
# na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista


import random

# Gerar 20 valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Lista ordenada sem modificar a original
lista_ordenada = sorted(lista)

# Índice do maior valor da lista
indice_maior_valor = lista.index(max(lista))

# Índice do menor valor da lista
indice_menor_valor = lista.index(min(lista))

# Imprimir os resultados
print("Lista original:", lista)
print("Lista ordenada:", lista_ordenada)
print("Índice do maior valor:", indice_maior_valor)
print("Índice do menor valor:", indice_menor_valor)
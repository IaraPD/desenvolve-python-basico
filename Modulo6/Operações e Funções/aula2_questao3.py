# 3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista chamada
# interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista
# Atenção, a lista de intersecções não pode ter duplicatas. Segue um exemplo da saída esperada.
# lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
# lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
# Interseccao - [10, 11, 20]
# Contagem
# 10: (lista1=4, lista2=1)
# 11: (lista1=1, lista2=2)
# 20: (lista1=1, lista2=1)


import random
# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a intersecção sem duplicatas
interseccao = list(set(lista1) & set(lista2))

# Contar as ocorrências em ambas as listas
contagem_lista1 = {x: lista1.count(x) for x in interseccao}
contagem_lista2 = {x: lista2.count(x) for x in interseccao}

# Imprimir os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao ordenada:", sorted(interseccao))
print("Contagem de ocorrências:")
for valor in sorted(interseccao):
    print(f"{valor} (lista1={contagem_lista1[valor]}, lista2={contagem_lista2[valor]})")
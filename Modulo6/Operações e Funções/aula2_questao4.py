# 4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de
# valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o
# final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
# Exemplo de interação via terminal (entradas em negrito):
# Digite a quantidade de elementos da lista 1: 4
# Digite os 4 elementos da lista 1:
# 1
# 2
# 3
# 4Digite a quantidade de elementos da lista 2: 6
# Digite os 6 elementos da lista 2:
# 5
# 6
# 7
# 8
# 9
# 10Lista intercalada: 1 5 2 6 3 7 4 8 9 10


def intercalar_listas(lista1, lista2):
    # Inicializa a lista intercalada
    lista_intercalada = []
    # Pega o tamanho das listas
    tamanho1, tamanho2 = len(lista1), len(lista2)
    # Intercala os elementos das duas listas
    for i in range(min(tamanho1, tamanho2)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    # Adiciona os elementos restantes da maior lista
    if tamanho1 > tamanho2:
        lista_intercalada.extend(lista1[tamanho2:])
    else:
        lista_intercalada.extend(lista2[tamanho1:])
    return lista_intercalada

# Receber entrada do usuário para a lista 1
num_elementos_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {num_elementos_lista1} elementos da lista 1:")
for _ in range(num_elementos_lista1):
    elemento = int(input())
    lista1.append(elemento)

# Receber entrada do usuário para a lista 2
num_elementos_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {num_elementos_lista2} elementos da lista 2:")
for _ in range(num_elementos_lista2):
    elemento = int(input())
    lista2.append(elemento)

# Intercalar as listas
lista_intercalada = intercalar_listas(lista1, lista2)

# Imprimir a lista intercalada
print("Lista intercalada:", lista_intercalada)
# 3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior
# quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]


import random

# Criar lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontrar o intervalo com mais números negativos
max_negativos = 0
melhor_intervalo = (0, 0)

for i in range(len(lista)):
    for j in range(i, len(lista)):
        negativos = sum(1 for x in lista[i:j+1] if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            melhor_intervalo = (i, j)

# Deletar o intervalo
del lista[melhor_intervalo[0]:melhor_intervalo[1]+1]

print("Editada:", lista)
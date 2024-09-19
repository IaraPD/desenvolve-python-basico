# Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário
# o valor de n
# Biblioteca random: Função randint()
# Biblioteca math: Função sqrt()

import random
import math

def raiz_quadrada_soma():
    n= int(input("Digite o valor de n:"))
    soma= sum(random.randint(0, 100) for _ in range(n))
    raiz_quadrada= math.sqrt(soma)

    print(f"A raiz quadrada da soma dos valores é {raiz_quadrada}")
    raiz_quadrada()
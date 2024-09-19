# Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para
# adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o
# usuário acertar o palpite.
# Exemplo de interação:
# Adivinhe o número entre 1 e 10: 5
# Muito alto, tente novamente!
# Adivinhe o número entre 1 e 10: 3
# Correto! O número é 3.

import random

def adivinhe_numero():
    numero_aleatorio= random.randint(1, 10)
    palpite= None

    while palpite != numero_aleatorio:
        palpite= int(input("Adivinhe o número entre 1 e 10:"))

        if palpite < numero_aleatorio:
            print("Muito abaixo, tente novamente")
        elif palpite> numero_aleatorio:
            print("Muito alyto, tente novamente")
        else:
            print(f"Correto! O número é {palpite}.")

            adivinhe_numero()
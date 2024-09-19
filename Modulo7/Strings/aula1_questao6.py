from collections import Counter

def encontrar_anagramas(frase, palavra):
    palavra_contador = Counter(palavra)
    anagramas = []
    palavras_frase = frase.split()

    for palavra_frase in palavras_frase:
        if Counter(palavra_frase) == palavra_contador:
            anagramas.append(palavra_frase)

    return anagramas

# Teste da função
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {anagramas}")
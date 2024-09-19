def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    indices_vogais = [i for i, letra in enumerate(frase) if letra in vogais]
    num_vogais = len(indices_vogais)
    return num_vogais, indices_vogais

# Teste da função
frase = input("Digite uma frase: ")
num_vogais, indices_vogais = contar_vogais(frase)
print(f"{num_vogais} vogais")
print(f"Indices {indices_vogais}")
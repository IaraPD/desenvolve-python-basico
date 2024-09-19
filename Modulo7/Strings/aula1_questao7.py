import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ''.join(
            chr((ord(letra) - 33 + chave) % 94 + 33) for letra in nome)
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave

# Teste da função
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
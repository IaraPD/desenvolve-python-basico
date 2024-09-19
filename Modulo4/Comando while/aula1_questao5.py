# Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia
# um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das
# idades.
# (idade1 + idade2 + idade3 + … + idade_n)/N



# Lê a quantidade de respondentes
N= int(input("Digite a quantidade de respondentes:"))

# Inicializar a soma das idades 
soma_idades= 0

# Lê as idades e soma
for i in range(N):
    idade= int(input("Digite a idade do respondente {i+1}:"))
soma_idades += idade

# Calcule a média das idades
medias_idades= soma_idades / N

# Imprime a média das idades
print(f"A médias das idades dos respondentes é: {medias_idades:.2f}")
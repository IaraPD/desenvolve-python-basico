# 6) Exercício de maratona: https://www.beecrowd.com.br/judge/pt/problems/view/1094

# Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram
# utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos,
# ratos e coelhos. 

# Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um
# inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia
# (S:Sapo, R:Rato ou C:Coelho).

# Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de
# cobaias utilizadas

# EXEMPLO DE ENTRADA
# 10        # 5 C       # 8 S
# 10 C      # 14 R      # 5 C
# 6 R       # 9 C       # 14 R
# 15 S      # 6 R

# EXEMPLO DE SAIDA
# Total: 92 cobaias
# Total de coelhos: 29
# Total de ratos: 40
# Total de sapos: 23
# Percentual de coelhos: 31.52%
# Percentual de ratos: 43.48%
# Percentual de sapos: 25.00%




# Ler o número de experimentos
N= int(input())

# Inicializar contadores
total_cobaias= 0
total_coelhos= 0
total_ratos= 0
total_sapos= 0

# Ler os experimentos e contar os tipos de cobaias
for _ in range(N):
    entrada= input().split()
    quantia= int(entrada[0])
    tipo= entrada[1]

    total_cobaias+= quantia

    if tipo== 'C':
        total_coelhos+= quantia
    elif tipo== 'R':
        total_ratos+= quantia
    elif tipo== 'S':
        total_sapos+= quantia


# Calcular percentuais
percentual_coelho= (total_coelhos/total_cobaias)*100
percentual_rato= (total_ratos/total_cobaias)*100
percentual_sapo= (total_sapos/total_cobaias)*100

# Exibir os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelho:.2f} %")
print(f"Percentual de ratos: {percentual_rato:.2f} %")
print(f"Percentual de sapos: {percentual_sapo:.2f} %")
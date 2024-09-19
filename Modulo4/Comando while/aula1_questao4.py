# 4) Transforme em código o fluxograma a seguir

# Leia n
n= int(input("Digite o valor de n"))
maior= 0

while n >0:
    x= int(input("Digite um número:"))
    if x > maior:
        maior= x
        n-=1
        print("O maior número é:", maior)
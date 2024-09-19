# 3) Transforme em código o fluxograma a seguir

# Leia n1, n2, n3
n1= float(input("Digite a nota 1: "))
n2= float(input("Digite a nota 2:"))
n3= float(input("Digite a nota 3:"))

# Calcule a média
m= (n1+n2+n3) / 3

#Verifique a média e imprima o resultaado
if m >= 60:
    print("Aptovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

    print("Fim")
def ajustar_numero():
    numero = input("Digite o número: ")
    if len(numero) == 8 and numero.isdigit():
        numero_completo = '9' + numero
        print(f"Número completo: {numero_completo}")
    else:
        print("Número inválido! Verifique se tem 8 dígitos.")

ajustar_numero()
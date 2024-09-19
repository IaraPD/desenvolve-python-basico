def calcular_digito_verificador(cpf, pos):
    if pos == 1:
        multiplicadores = list(range(10, 1, -1))
        numeros = cpf[:9]
    else:
        multiplicadores = list(range(11, 1, -1))
        numeros = cpf[:10]
    
    soma = sum(int(n) * m for n, m in zip(numeros, multiplicadores))
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    # Remove caracteres especiais
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Calcula os dígitos verificadores
    digito1 = calcular_digito_verificador(cpf, 1)
    digito2 = calcular_digito_verificador(cpf, 2)
    
    # Verifica se os dígitos calculados coincidem com os fornecidos
    return cpf[-2:] == f"{digito1}{digito2}"

# Teste da função
cpf_input = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")

if validar_cpf(cpf_input):
    print("Válido")
else:
    print("Inválido")
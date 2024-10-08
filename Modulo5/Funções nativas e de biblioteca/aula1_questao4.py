# Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a
# seguir:
# Data: 15/03/2023 
# Hora: 14:05

# Você pode consultar esse tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras de resolver essa questão.
# Uma sugestão é:

# Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute

# Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos precedidos por
# zero se necessário.


from datetime import datetime

def exibir_data_hora():
    agora= datetime.now()

    data_formatada= f" {agora.day:02d}/{agora.month:02d}/{agora.year}"
    hora_formatada= f"{agora.hour:02d}:{agora.minute:02d}"

    print(f"Data: {data_formatada}")
    print(f"Hora: {hora_formatada}")
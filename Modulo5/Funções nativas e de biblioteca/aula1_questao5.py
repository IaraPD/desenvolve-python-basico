# Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas.
# Faça:
# No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip
# $ pip install emoji

# Conheça a função emoji.emojize()
# Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. Em seguida,
# solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).

# A seguir um exemplo de interação, com uma lista de emojis sugeridos. Você pode consultar o texto que codifica outros emojis indo
# nessa página e passando o mouse por cima do emoji desejado. 

# Emojis disponíveis:
# ❤️ - :red_heart:
# 👍 - :thumbs_up:
# 🤔 - :thinking_face:
# 🥳 - :partying_face:

# Digite uma frase e ela será emojizada:
# Olá mundo! :red_heart:
# Frase emojizada:
# Olá mundo! ❤️    


import emoji

# Lista de emojis disponíveis
emojis = {
    "♥": ":red heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe a lista de emojis disponíveis
print("Emojis disponíveis:")
for symbol, description in emojis.items():
    print(f"{symbol} {description}")

# Solicita uma frase codificada ao usuário
user_input = input("Digite uma frase e ela será emojizada:\n")

# Decodifica a frase usando emojis
emojized_message = emoji.emojize(user_input, use_aliases=True)

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(emojized_message)
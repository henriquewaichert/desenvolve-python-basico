# 3) Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

# Digite uma frase (digite "fim" para encerrar): Radar
# "Radar" é palíndromo
# Digite uma frase (digite "fim" para encerrar): Bom dia!
# "Bom dia!" não é palíndromo
# Digite uma frase (digite "fim" para encerrar): Ame o poema
# "Ame o poema" é palíndromo
# Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
# "A Daniela ama a lei? Nada!" é palíndromo
# Digite uma frase (digite "fim" para encerrar): fim

import re

def verifique_palindromo(n):
    frase_normal = re.sub(r'[^a-zA-Z0-9]', '', n).lower()
    return frase_normal == frase_normal[::-1]

while True:
    n = input('Digite uma frase (digite "fim" para encerrar): ')
    if n.lower() == "fim":
        break
    if verifique_palindromo(n):
        print(f'"{n}" é palíndromo')
    else:
        print(f'"{n}" não é palíndromo')
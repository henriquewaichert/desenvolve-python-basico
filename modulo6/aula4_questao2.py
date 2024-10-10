# 2) Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

frase = input("Digite uma frase: ")

vogal = "aeiouAEIOU"

vogais_ordenadas = sorted([l for l in frase if l in vogal])

consoantes = [l for l in frase if l.isalpha() and l not in vogal]

print("Vogais:", vogais_ordenadas)
print("Consoantes:", consoantes)
# 2) Solicite uma frase do usuário e usando compreensão de listas imprima:

# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase

# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

frase = input("Digite uma frase: ")

vogais = [letra.lower() for letra in frase if letra.lower() in 'aeiou']
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']

vogais_ordenadas = sorted(vogais)
consoantes_ordenadas = sorted(consoantes)

print("Vogais:", vogais_ordenadas)
print("Consoantes:", consoantes_ordenadas)

# 2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

frase = input("Digite uma frase: ")
vogal = "aeiouAEIOU"

frase_modificada = ''.join(['*' if char in vogal else char for char in frase])

print(f"Frase modificada: {frase_modificada}")
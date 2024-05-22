# 2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'

frase_modificada = ''

for vogal in frase:
    if vogal in vogais:
        frase_modificada += '*'
    else:
        frase_modificada += vogal

print(f"Frase modificada: {frase_modificada}")

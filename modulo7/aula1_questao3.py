# Escreva um script que dado uma frase conta os espaços em branco.
# Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
# Espaços em branco: 11

def espacos_branco(frase):
    return frase.count(' ')

frase = input("Digite a frase: ")

contar_espacos = espacos_branco(frase)

print(f"Espaços em branco: {contar_espacos}")
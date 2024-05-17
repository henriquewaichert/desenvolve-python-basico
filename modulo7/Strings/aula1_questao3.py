# Escreva um script que dado uma frase conta os espaços em branco.

# Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
# Espaços em branco: 11

def contar_espacos(frase):
    espacos = 0
    for caractere in frase:
        if caractere == ' ':
            espacos += 1
    return espacos

frase = input("Digite a frase: ")
print("Espaços em branco:", contar_espacos(frase))

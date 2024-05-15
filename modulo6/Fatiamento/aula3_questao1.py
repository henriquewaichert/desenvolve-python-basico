# 1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:

# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )

numeros = []  
quantidade_minima = 4  

while True :
    entrada = input("Digite um número inteiro ou 'Fim' para finalizar: ")
    if entrada.isdigit():  
        numero = int(entrada)
        numeros.append(numero)
    elif len(numeros) < quantidade_minima:
        print("Insira mais de 4 números pelo menos na lista")
        continue
    elif entrada == 'Fim':
        break  

print(" ")
print("A lista original:", numeros)
print(" ")
print("Os 3 primeiros elementos:", numeros[0:3])
print(" ")
print("Os 2 últimos elementos:", numeros[-2:])
print(" ")
print("A lista invertida (do fim para o começo)", numeros[::-1])
print(" ")
print("Os elementos de índice par (0, 2, 4 … )", numeros[::2])
print(" ")
print("Os elementos de índice ímpar (1, 3, 5, … )", numeros[1::2])
print(" ")
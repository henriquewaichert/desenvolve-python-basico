# 1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )

quatros_numeros = []

while len(quatros_numeros) < 4:
    numero = int(input("Digite um número inteiro (pelo menos 4 valores são necessários: "))
    quatros_numeros.append(numero)

print("Lista original:", quatros_numeros)

print("Os 3 primeiros elementos:", quatros_numeros[:3])

print("Os 2 últimos elementos:", quatros_numeros[-2:])

print("Lista invertida:", quatros_numeros[::-1])

print("Elementos de índice par:", quatros_numeros[::2])

print("Elementos de índice ímpar:", quatros_numeros[1::2])
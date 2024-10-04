# 1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random

lista_original = [random.randint(-100 , 100) for i in range(20)]

lista_ordenada = sorted(lista_original)

maior_indice = lista_original.index(max(lista_original))
menor_indice = lista_original.index(min(lista_original))

print("A lista ORDENADA, sem modificar a lista original:", lista_ordenada)
print("A lista ORIGINAL:", lista_original)
print(f"O índice do MAIOR valor da lista ({max(lista_original)}) é:" , maior_indice)
print(f"O índice do MENOR valor da lista ({min(lista_original)}) é:" , menor_indice)
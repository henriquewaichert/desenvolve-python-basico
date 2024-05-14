# 1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista
import random

valores = []

for n in range(20):
    valores.append(random.randint(-100, 100))

valores_ordenados = sorted(valores)
valor_maior = max(valores)
valor_menor = min(valores)

print(" ")
print("A lista ordenada, sem modificar a lista original:", valores_ordenados)
print(" ")
print("A lista original:", valores)
print(" ")
print("O índice do maior valor da lista:", valor_maior)
print(" ")
print("O índice do menor valor da lista", valor_menor)
print(" ")
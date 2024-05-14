# 4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

# Exemplo de interação via terminal (entradas em negrito):

# Digite a quantidade de elementos da lista 1: 4

# Digite os 4 elementos da lista 1:
# 1
# 2
# 3
# 4 

#Digite a quantidade de elementos da lista 2: 6

# Digite os 6 elementos da lista 2:
# 5
# 6
# 7
# 8
# 9
# 10

#Lista intercalada: 1 5 2 6 3 7 4 8 9 10

lista1 = []
lista2 = []

n1 = int(input("Digite a quantidade de elementos da lista 1: "))

print(f"Digite os {n1} elementos da lista 1: ")

for n in range(n1):
    elemento = int(input(f"Elemento {n+1}: "))
    lista1.append(elemento)

n2 = int(input("Digite a quantidade de elementos da lista 2: "))

print(f"Digite os {n2} elementos da lista 2: ")

for n in range(n2):
    elemento = int(input(f"Elemento {n+1}: "))
    lista2.append(elemento)

lista_intercalada = []

for elemento1, elemento2 in zip(lista1, lista2):
    lista_intercalada.append(elemento1)
    lista_intercalada.append(elemento2)

lista_intercalada.extend(lista1[len(lista2):])
lista_intercalada.extend(lista2[len(lista1):])

print(" ")
print("Lista 1:", lista1)
print(" ")
print("Lista 2:", lista2)
print(" ")
print("Lista intercalada:", lista_intercalada)
print(" ")

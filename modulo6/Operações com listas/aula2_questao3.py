# 3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:

# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista

# Atenção, a lista de intersecções não pode ter duplicatas. Segue um exemplo da saída esperada.

# lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
# lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
# Interseccao - [10, 11, 20]
# Contagem
# 10: (lista1=4, lista2=1)
# 11: (lista1=1, lista2=2)
# 20: (lista1=1, lista2=1)

import random

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(random.randint(0, 50))

for i in range(20):
    lista2.append(random.randint(0, 50))

lista1.sort()
lista2.sort()

for n in lista1:
    if n in lista2 and n not in interseccao:
        interseccao.append(n)

# quantidades_lista = {x: lista1.count(x) for x in interseccao} and {x: lista2.count(x) for x in interseccao}
quantidades = {x: (lista1.count(x), lista2.count(x)) for x in interseccao}


print(" ")
print("Essa é a primeira lista:", lista1)
print(" ")
print("Essa é a segunda lista:", lista2)
print(" ")
print("Essa é a lista intersecção ordenada:", interseccao)
print(" ")
print("Contagem:")
print(" ")
for elemento, (quantidade_lista1, quantidade_lista2) in quantidades.items():
    print(f"    {elemento}: {quantidade_lista1} na Lista 1, {quantidade_lista2} na Lista 2")
    print(" ")

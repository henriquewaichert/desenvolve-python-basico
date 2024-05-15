# 3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

# import random

# lista = []

# num_aleaatorios = random.randint(0, 20)

# for i in range(num_aleaatorios):
#     lista.append(random.randint(-10, 10))

# print("Original:",lista)

# maior_contagem = 0
# inicio_intervalo = 0

# for i, num in enumerate(lista):
#     if num < 0:
#         contagem_atual = sum(1 for x in lista[i:] if x < 0)
#         if contagem_atual > maior_contagem:
#             maior_contagem = contagem_atual
#             inicio_intervalo = i

# del lista[inicio_intervalo:inicio_intervalo + maior_contagem]

# print("Editada:", lista)

import random

lista = []

num_aleatorios = random.randint(0,20)

for i in range(num_aleatorios):
    lista.append(random.randint(-10, 10))

print("Original:", lista)

inicio_intervalo = 0
fim_intervalo = 0
contador_atual_negativos = 0
contador_max_negativos = 0

for i, num in enumerate(lista):
    if num < 0:
        contador_atual_negativos += 1
    else:
        if contador_atual_negativos > contador_max_negativos:
            contador_max_negativos = contador_atual_negativos
            inicio_intervalo = i - contador_atual_negativos
            fim_intervalo = i
        contador_atual_negativos = 0

if contador_atual_negativos > contador_max_negativos:
    contador_max_negativos = contador_atual_negativos
    inicio_intervalo = len(lista) - contador_atual_negativos
    fim_intervalo = len(lista)

del lista[inicio_intervalo:fim_intervalo]

print("Editada:", lista)

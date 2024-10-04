# 3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random

lista_elementos = [random.randint(-10, 10) for i in range(20)]

print("Original:", lista_elementos)

inicio_maior_intervalo = 0
fim_maior_intervalo = 0
maximos_negativos = 0

for i in range(len(lista_elementos)):
    if lista_elementos[i] < 0:
        inicio_intervalo = i
        cont_negativos = 0
        while i < len(lista_elementos) and lista_elementos[i] < 0:
            cont_negativos += 1
            i += 1
        fim_intervalo = i
        if cont_negativos > maximos_negativos:
            maximos_negativos = cont_negativos
            inicio_maior_intervalo = inicio_intervalo
            fim_maior_intervalo = fim_intervalo

del lista_elementos[inicio_maior_intervalo:fim_maior_intervalo]

print("Editada:", lista_elementos)

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

lista1 = [random.randint(0 , 50) for i in range(20)]
lista2 = [random.randint(0 , 50) for i in range(20)]

interseccao = sorted(set(lista1).intersection(lista2))

def ocorrencias(lista,valor):
    return lista.count(valor)

print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)
print("Contagem")
for valor in interseccao:
    contagem_lista1 = ocorrencias(lista1, valor)
    contagem_lista2 = ocorrencias(lista2, valor)
    print(f"{valor}: (lista1={contagem_lista1}, lista2={contagem_lista2})")
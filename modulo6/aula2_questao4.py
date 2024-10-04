# 4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
    # Exemplo de interação via terminal (entradas em negrito):
    # Digite a quantidade de elementos da lista 1: 4
    # Digite os 4 elementos da lista 1:
    # 1
    # 2
    # 3
    # 4Digite a quantidade de elementos da lista 2: 6
    # Digite os 6 elementos da lista 2:
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10Lista intercalada: 1 5 2 6 3 7 4 8 9 10

def juntar_listas(primeira_lista, segunda_lista):
    lista_intercalada = []
    quantidade1, quantidade2 = len(primeira_lista), len(segunda_lista)

    for i in range(min(quantidade1, quantidade2)):
        lista_intercalada.append(primeira_lista[i])
        lista_intercalada.append(segunda_lista[i])

        if quantidade1 > quantidade2:
            lista_intercalada.extend(primeira_lista[quantidade2:])
        else:
            lista_intercalada.extend(segunda_lista[quantidade1:])

    return lista_intercalada
    
quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quantidade_lista1} elementos da lista 1:")
lista1 = [int(input()) for i in range(quantidade_lista1)]

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quantidade_lista2} elementos da lista 2:")
lista2 = [int(input()) for i in range(quantidade_lista2)]

lista_intercalada = juntar_listas(lista1,lista2)

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
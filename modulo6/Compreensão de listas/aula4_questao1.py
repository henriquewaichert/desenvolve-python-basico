# 1) Escreva um script python que use compreensão de listas para criar as seguintes listas:

# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
# Todos os números entre 1 e 100 que sejam divisíveis por 7
# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 

lista_1 = [i for i in range(20,51)]
lista_pares = [i for i in lista_1 if i % 2 == 0]

lista_2 = [1,2,3,4,5,6,7,8,9]
lista_quadrado = [n**2 for n in lista_2]

lista_3 = [i for i in range(1, 101)]
lista_divisivel = [i for i in lista_3 if i % 7 == 0]

lista_4 = [i for i in range(0,30,3)]
lista_par_impar = ['par' if i % 2 == 0 else 'ímpar' for i in lista_4]

print(' ')
print("Todos os números pares entre 20 e 50:", lista_pares)
print(' ')
print("Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]:", lista_quadrado)
print(' ')
print("Todos os números entre 1 e 100 que sejam divisíveis por 7", lista_divisivel)
print(' ')
print("Para todos os valores em range(0,30,3), escreva 'par' ou 'ímpar' dependendo da paridade do elemento:", lista_par_impar )
print(' ')

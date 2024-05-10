#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n
# Biblioteca random: Função randint()
# Biblioteca math: Função sqrt()

import random
import math
soma = 0

n = int(input("Digite um valor de n: "))

for i in range(n):
    valores_aleatorios = random.randint(0, 100)
    print(valores_aleatorios)

soma += valores_aleatorios
raiz_quadrada_soma = math.sqrt(soma)
print(f"A raíz quadrada da soma dos valores é: {raiz_quadrada_soma:.2f}")
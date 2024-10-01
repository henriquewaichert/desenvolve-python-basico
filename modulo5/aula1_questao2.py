import random
import math

valor_n = int(input("Digite a quantidade de valores inteiros aleatórios (n): "))

valores_somados = 0
for i in range (valor_n):
    valor = random.randint(0,100)
    valores_somados += valor

raiz_quadrada = math.sqrt(valores_somados)

print(f"A soma dos {valor_n} valores é: {valores_somados}")
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}")
# 2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

# 86 graus Fahrenheit são 30 graus Celsius.

temperatura_F = int(input("Digite a temperatura em Fahrenheit: "))
temperatura_C = int((temperatura_F - 32) * (5 / 9))

print(f"{temperatura_F} graus Fahrenheit são {temperatura_C} graus Celsius")
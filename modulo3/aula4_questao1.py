# Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

somando = numero1 + numero2

if somando % 2 == 0:
    print(f"A soma {somando} é par!")
else:
    print(f"A soma {somando} é ímpar!")
# 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

# Entrada:
# 576

# Saída:
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

valor_reais = int(input("Digite o valor em reais: "))

notas_de_100 = valor_reais // 100
valor_reais = valor_reais % 100

notas_de_50 = valor_reais // 50
valor_reais = valor_reais % 50

notas_de_20 = valor_reais // 20
valor_reais = valor_reais % 20

notas_de_10 = valor_reais // 10
valor_reais = valor_reais % 10

notas_de_5 = valor_reais // 5
valor_reais = valor_reais % 5

notas_de_2 = valor_reais // 2
valor_reais = valor_reais % 2

notas_de_1 = valor_reais 

print(f"{notas_de_100} nota(s) de R$100,00")
print(f"{notas_de_50} nota(s) de R$50,00")
print(f"{notas_de_20} nota(s) de R$20,00")
print(f"{notas_de_10} nota(s) de R$10,00")
print(f"{notas_de_5} nota(s) de R$5,00")
print(f"{notas_de_2} nota(s) de R$2,00")
print(f"{notas_de_1} nota(s) de R$1,00")
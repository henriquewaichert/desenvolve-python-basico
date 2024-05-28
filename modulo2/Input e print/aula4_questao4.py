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

valor = int(input('INSIRA UM VALOR INTEIRO: '))
print(f"{valor // 100} nota(s) de R$100,00")
valor = valor % 100
print(f"{valor // 50} nota(s) de R$50,00")
valor = valor % 50
print(f"{valor // 20} nota(s) de R$20,00")
valor = valor % 20
print(f"{valor // 10} nota(s) de R$10,00")
valor = valor % 10
print(f"{valor // 5} nota(s) de R$5,00")
valor = valor % 5
print(f"{valor // 2} nota(s) de R$2,00")
valor = valor % 2
print(f"{valor // 1} nota(s) de R$1,00")

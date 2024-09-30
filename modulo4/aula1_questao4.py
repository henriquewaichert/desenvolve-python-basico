n = int(input("Digite o valor de n: "))

maior = 0

while n > 0:
    x = int(input("Digite um valor para x: "))

    if x > maior:
        maior = x
    else:
        n = n - 1
    print ("O maior valor é:", maior)
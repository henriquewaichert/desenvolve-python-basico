
n = int(input("Digite o valor de n: "))


maior = 0


while n > 0:
    
    x = float(input("Digite um valor para x: "))
    
    
    if x > maior:
        maior = x
        n = n - 1
    print("Maior valor encontrado até agora:", maior)

n = int(input("Insira a quantidades de experimentos: "))
cont = 0
soma_sapo , soma_rato , soma_coelho = 0, 0, 0

while cont < n:
    print(cont, n)
    
    quantia = int(input("Diga a quantidade de cobaia: "))
    tipo = input("Diga o tipo de cobaia(S:Sapo, R:Rato ou C:Coelho): ")

    if tipo == 'S' :
        soma_sapo += quantia
    elif tipo == 'R' :
        soma_rato += quantia
    elif tipo == 'C' :
        soma_coelho += quantia

    cont += 1
    print("Total de cobaias: ", soma_sapo + soma_rato + soma_coelho)
    print("Total de sapos: ", soma_sapo)
    print("Total de ratos: ", soma_rato)
    print("Total de coelhos: ", soma_coelho)
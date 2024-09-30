qntd_experimentos = int(input("Dê o número de experimentos registrados: "))

cobaias_totais = 0
sapos_totais = 0
ratos_totais = 0
coelhos_totais = 0

for i in range(qntd_experimentos):
    dados = input(f"{i+1}- ").split()
    quantia = int(dados[0])
    especie = dados[1]

    cobaias_totais = cobaias_totais + quantia
    if especie == "S":
        sapos_totais = sapos_totais + quantia
    elif especie == "R":
        ratos_totais = ratos_totais + quantia
    elif especie == "C":
        coelhos_totais = coelhos_totais + quantia

print(f"Total: {cobaias_totais} cobaias")
print(f"Total de coelhos: {coelhos_totais}")
print(f"Total de ratos: {ratos_totais}")
print(f"Total de sapos: {sapos_totais}")

coelhos_porcentagem = (coelhos_totais / cobaias_totais) * 100
ratos_porcentagem = (ratos_totais / cobaias_totais) * 100
sapos_porcentagem = (sapos_totais / cobaias_totais) * 100

print(f"Percentual de coelhos: {coelhos_porcentagem:.2f} %")
print(f"Percentual de ratos: {ratos_porcentagem:.2f} %")
print(f"Percentual de sapos: {sapos_porcentagem:.2f} %")

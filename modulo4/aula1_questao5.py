N = int(input("Digite a quantidade de respondentes: "))

idades_soma = 0

for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    idades_soma = idades_soma + idade

idade_media = idades_soma / N

print(f"A média das idades é: {idade_media:.0f}")
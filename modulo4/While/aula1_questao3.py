
n1 = 0
n2 = 0
n3 = 0
m = 0


while n1 == 0 or n2 == 0 or n3 == 0:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))


m = (n1 + n2 + n3) / 3


if m >= 60:
    print(f"Sua nota final foi {m:.0f} e você esta: Aprovado")
elif m >= 40:
    print(f"Sua nota final foi {m:.0f} e você esta: Recuperação")
else:
    print(f"Sua nota final foi {m:.0f} e você esta: Reprovado")

print("Fim")
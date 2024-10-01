primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

calculo_diferenca = abs(primeiro_numero - segundo_numero)

diferenca_arrendondada = round(calculo_diferenca, 2)

print(f"A diferença absoluta entre os números é: {diferenca_arrendondada}")
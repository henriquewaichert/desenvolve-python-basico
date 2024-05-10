# Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

#Exemplo de interação:
# Digite o primeiro número: 3.1415
# Digite o segundo número: 1.4142
# A diferença absoluta entre os números é: 1.73


numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

diferenca_absoluta = abs(numero1 - numero2)

diferenca_absoluta_arredondada = round(diferenca_absoluta, 2)

print("A diferença absoluta entre os números é:", diferenca_absoluta_arredondada)
# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

    # O terreno possui 250m2 e custa R$512,490.50

    # Comente na linha acima de cada instrução uma breve descrição da   instrução.

    # Fórmulas:
    # area_m2 = comprimento * largura
    # preco_total = preco_m2 * area_m2

#Pegando as dimensoes do terreno
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))

#Pegando o preco do m2
preco_m2 = float(input("Digite o preço do metro quadrado: "))

#Calculando a área por m2
area_m2 = comprimento * largura

#Calculando o valor total do terreno
preco_total = preco_m2 * area_m2

#Imprimindo o resultado final
print(f"Em metros quadrados o terreno possui {area_m2} e custa R${preco_total:.2f}.")
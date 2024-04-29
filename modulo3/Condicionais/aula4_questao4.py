# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int(input("Insira a distância da entrega em quilômetros: "))
peso = int(input("Insira o peso do pacote em quilogramas: "))

if distancia <= 100:
    preco_1 = 1
    frete1 = (peso * preco_1)
    print("O valor do Frete é:", frete1 if (peso <= 10) else frete1 + 10)
    
if distancia >= 101 and distancia <= 300 :
    preco_1_50 = 1.50
    frete2 = (peso * preco_1_50)
    print("O valor do Frete é:", frete2 if (peso <= 10) else frete2 + 10)

if distancia > 300 :
    preco_2 = 2
    frete3 = (peso * preco_2)
    print("O valor do Frete é:", frete3 if (peso <= 10) else frete3 + 10)
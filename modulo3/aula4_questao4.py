# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

entrega_distancia = float(input("Digita a distância da entrega em km?: "))
pacote_peso = float(input("Digita o peso do pacote em kg?: "))
valor_frete = 0

if entrega_distancia <= 100:
    valor_frete = 1 * pacote_peso
elif 101 <= entrega_distancia <= 300:
    valor_frete = 1.50 * pacote_peso
else:
    valor_frete = 2 * pacote_peso

if pacote_peso > 10:
    valor_frete += 10

print(f"O valor do frete é de: R${valor_frete:.2f}")
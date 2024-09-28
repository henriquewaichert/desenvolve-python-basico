# 3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
        # Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
        # A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
    # Entrada:
    # Digite o nome do produto 1: calça
    # Digite o preço unitário do produto 1: 199.90
    # Digite a quantidade do produto 1: 3
    # Digite o nome do produto 2: camisa
    # Digite o preço unitário do produto 2: 49.95
    # Digite a quantidade do produto 2: 10
    # Digite o nome do produto 3: cinto
    # Digite o preço unitário do produto 3: 25
    # Digite a quantidade do produto 3: 3
    
    # Saída:
    # Total: R$1,174.20

produto1_nome = input("Digite o nome do produto 1: ")
produto1_preco = float(input("Digite o preço unitário do produto 1: "))
produto1_quant = int(input("Digite a quantidade do produto 1: "))

produto2_nome = input("Digite o nome do produto 2: ")
produto2_preco = float(input("Digite o preço unitário do produto 2: "))
produto2_quant = int(input("Digite a quantidade do produto 2: "))

produto3_nome = input("Digite o nome do produto 3: ")
produto3_preco = float(input("Digite o preço unitário do produto 3: "))
produto3_quant = int(input("Digite a quantidade do produto 3: "))

total_produto1 = produto1_preco * produto1_quant
total_produto2 = produto2_preco * produto2_quant
total_produto3 = produto3_preco * produto3_quant

total_preco = total_produto1 + total_produto2 + total_produto3

print(f"Total: R${total_preco:,.2f}")
# 3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:

# tiver entre 16 e 18 anos
# já tiver jogado pelo menos 3 jogos
# já ter vencido pelo menos 1 jogo,

# Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em negrito e as impressões de seu código em itálico (apenas para facilitar sua visualização).

# Digite sua idade: 17
# Já jogou pelo menos 3 jogos de tabuleiro? True
# Quantos jogos já venceu? 2
# Apto para ingressar no clube de jogos de tabuleiro: True

# Entrada de dados

idade = int(input("Digite sua idade: "))
qntd_jogos = input("Ja jogou pelo menos 3 jogos de tabuleiro? (Se 'SIM' resposta deve ser 'True', se 'NÃO' resposta deve ser 'False'): ")
jogos_ganho = int(input("Quantos jogos já venceu? : "))

# Processamento

idade_apto = idade >= 16 or idade <= 18
qntd_jogos_apto = qntd_jogos == 'True'
jogos_ganho_apto = jogos_ganho >= 1

apto = idade_apto and qntd_jogos_apto and jogos_ganho_apto

# Saída

print("Apto para ingressar no clube de jogos de tabuleiro: " , apto)
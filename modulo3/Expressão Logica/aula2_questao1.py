# 1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

# entrada de dados
# idade de juliana
# idade de cris

idade_juliana = int(input())
idade_cris = int(input())

# processamento
# True se ambos forem maior de idade
# False em qualquer outro caso

pode_entrar = idade_juliana >= 18 and idade_cris >= 18

# saída

print(pode_entrar)
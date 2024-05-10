# Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

# Exemplo de interação:
# Adivinhe o número entre 1 e 10: 5
# Muito alto, tente novamente!
# Adivinhe o número entre 1 e 10: 3
# Correto! O número é 3.

import random

numero_sorteado = random.randint(1, 10)

while True:
    n = int(input("Adivinhe o número entre 1 e 10: "))
       
    if numero_sorteado == n :
        print("Você acertou!!")
        break
    else:
        if n < numero_sorteado:
            print("O número sorteado é maior.")
        if n > numero_sorteado:
            print("O número sorteado é menor.")
# 4) Vamos fazer o jogo da forca! Antes de programar crie e salve os seguintes arquivos na mesma pasta onde você vai programar a solução: 

# Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
# Baixe o arquivo "gabarito_enforcado.txt": https://github.com/camilalaranjeira/python-basico-exercicios/blob/main/modulo7/gabarito_enforcado.txt

# Escreva um programa em Python para executar o jogo, de acordo com as definições:

# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
# No início exiba o número de letras da palavra sorteada como underscores;
# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).

import random

def imprime_enforcado(tentativas):
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.readlines()
    print(estagios[tentativas].strip())

def main():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().strip().split("\n")
    
    palavra = random.choice(palavras).upper()
    letras_adivinhadas = set()
    tentativas = 6
    progresso = ["_" for _ in palavra]

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra: " + " ".join(progresso))

    while tentativas > 0 and "_" in progresso:
        letra = input("Digite uma letra: ").upper()
        
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.add(letra)

        if letra in palavra:
            for index, char in enumerate(palavra):
                if char == letra:
                    progresso[index] = letra
            print("Bom trabalho! Progresso: " + " ".join(progresso))
        else:
            tentativas -= 1
            imprime_enforcado(6 - tentativas)
            print(f"Letra incorreta! Você ainda tem {tentativas} tentativas.")

    if "_" not in progresso:
        print("Parabéns! Você adivinhou a palavra: " + palavra)
    else:
        print("Você perdeu! A palavra era: " + palavra)

if __name__ == "__main__":
    main()
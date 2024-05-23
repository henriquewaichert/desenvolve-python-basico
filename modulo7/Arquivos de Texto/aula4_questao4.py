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

def escolher_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
        return random.choice(palavras)

def criar_lista_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        return arquivo.read().splitlines()

def imprime_progresso(palavra, letras_corretas):
    progresso = ""
    for letra in palavra:
        if letra in letras_corretas:
            progresso += letra + " "
        else:
            progresso += "_ "
    print(progresso)

def imprime_enforcado(erros, lista_enforcado):
    for i in range(erros):
        print(lista_enforcado[i])

def jogar_forca():
    palavra = escolher_palavra().lower()
    lista_enforcado = criar_lista_enforcado()
    letras_corretas = set()
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    imprime_progresso(palavra, letras_corretas)

    while erros < 6:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            letras_corretas.add(letra)
            imprime_progresso(palavra, letras_corretas)
        else:
            erros += 1
            imprime_enforcado(erros, lista_enforcado)
            print("Letra incorreta! Tente novamente.")

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns, você ganhou!")
            break
    else:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_forca()

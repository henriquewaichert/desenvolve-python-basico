# 2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
# Ex:
# Bom
# dia
# meu
# nome
# é
# Davi

import os
import re

with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

frase_limpa = re.sub(r'[^a-zA-Z\s]', '', frase)
palavras = frase_limpa.split()

with open("palavras.txt", "w") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + '\n')

with open("palavras.txt", "r") as arquivo_palavras:
    conteudo = arquivo_palavras.read()
    print(conteudo)
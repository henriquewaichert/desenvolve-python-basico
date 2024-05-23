# 2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

# Ex:
# Bom
# dia
# meu
# nome
# é
# Davi

import re

nome_arquivo_entrada = "frase.txt"
nome_arquivo_saida = "palavras.txt"

with open(nome_arquivo_entrada, "r") as arquivo_entrada:
    conteudo = arquivo_entrada.read()

palavras = re.findall(r'\b\w+\b', conteudo)

with open(nome_arquivo_saida, "w") as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + "\n")

with open(nome_arquivo_saida, 'r') as arquivo_saida:
    conteudo_palavras = arquivo_saida.read()
    print(conteudo_palavras)
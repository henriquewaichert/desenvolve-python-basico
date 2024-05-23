# 3) Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import re

nome_arquivo = "estomago.txt"

def contar_ocorrencias(texto, nome):
    return len(re.findall(fr'\b{nome}\b', texto, re.IGNORECASE))

with open(nome_arquivo, "r", encoding="utf-8", errors="ignore") as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas do arquivo:")
for linha in linhas[:25]:
    print(linha.strip())

numero_de_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {numero_de_linhas}")

linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa.strip()}")

conteudo = ''.join(linhas)
contagem_nonato = contar_ocorrencias(conteudo, "Nonato")
contagem_iria = contar_ocorrencias(conteudo, "Íria")

print(f"\nNúmero de menções ao personagem 'Nonato': {contagem_nonato}")
print(f"Número de menções ao personagem 'Íria': {contagem_iria}")

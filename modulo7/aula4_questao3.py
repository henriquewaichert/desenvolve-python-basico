# 3) Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import re

with open("estomago.txt", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

numero_linhas = len(linhas)
print(f"\nNúmero total de linhas: {numero_linhas}")

linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres: {linha_maior.strip()}")

contador_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
contador_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

print(f"\nNúmero de menções a 'Nonato': {contador_nonato}")
print(f"Número de menções a 'Íria': {contador_iria}")

# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
# nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
# chave_aleatoria = 5
# nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random

def encrypt(lista_nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in lista_nomes:
        nome_criptografado = ''
        for char in nome:
            novo_char = chr((ord(char) + chave - 33) % 94 + 33)
            nome_criptografado += novo_char
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
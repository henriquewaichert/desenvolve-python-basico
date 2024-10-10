# 1) Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
# Ex: 
# Digite uma frase: Bom dia, meu nome é Davi.
# Frase salva em /Users/laranjeira/python-basico/frase.txt

import os

frase_usuario = input("Digite uma frase: ")

nome_arquivo = "frase.txt"

with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase_usuario)

caminho = os.path.abspath(nome_arquivo)
print(f"Frase salva em {caminho}")
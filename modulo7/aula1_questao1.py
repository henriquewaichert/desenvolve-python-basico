# Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
# Digite seu nome: Fulano
# F
# Fu
# Ful
# Fula
# Fulan
# Fulano

nome_usuario = input("Digite seu nome: ")

for n in range(1, len(nome_usuario) + 1):
    print(nome_usuario[:n])
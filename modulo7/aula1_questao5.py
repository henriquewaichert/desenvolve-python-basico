# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# 19 vogais
# Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

def contando_vogal(frase):
    vogais = "aeiouAEIOU" 
    indices = []
    contagem = 0
    
    for n, letra in enumerate(frase):
        if letra in vogais:
            indices.append(n)
            contagem += 1
            
    return contagem, indices

frase = input("Digite uma frase: ")

quantidade_de_vogais, lista_indices = contando_vogal(frase)

print(f"{quantidade_de_vogais} vogais")
print(f"Índices {lista_indices}")
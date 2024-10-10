# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor
# Anagramas: ["amor", "mora", "ramo", "Roma"] 

from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    frase = frase.lower().replace(",", "").replace(".", "").replace("e", " ").replace("  ", " ")
    palavras = frase.split()
    
    contagem_palavra = Counter(palavra_objetivo)
    
    anagramas = []
    
    for palavra in palavras:
        if Counter(palavra) == contagem_palavra:
            anagramas.append(palavra)
    
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

resultado_anagramas = encontrar_anagramas(frase, palavra_objetivo)

print(f"Anagramas: {resultado_anagramas}")
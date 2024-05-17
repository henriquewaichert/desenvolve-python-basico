# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor
# Anagramas: ["amor", "mora", "ramo", "Roma"] 

def encontrar_anagramas(frase, objetivo):
    frase = frase.lower()
    objetivo = objetivo.lower()
    palavras = frase.split()
    anagramas = []
    objetivo_ordenado = sorted(objetivo)
    
    for palavra in palavras:
        if len(palavra) == len(objetivo):
            palavra_ordenada = sorted(palavra)
            if palavra_ordenada == objetivo_ordenado:
                anagramas.append(palavra)
    return anagramas

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

resultado = encontrar_anagramas(frase, objetivo)
print("Anagramas:", resultado)
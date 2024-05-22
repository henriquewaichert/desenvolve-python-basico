# 4) Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:

# Pelo menos 8 caracteres de comprimento.
# Contém pelo menos uma letra maiúscula e uma letra minúscula.
# Contém pelo menos um número.
# Contém pelo menos um caractere especial (por exemplo, @, #, $).
# Complete o seguinte código:
# def validador_senha(senha):
#     #### Escreva a função

# # Exemplo de uso:
# senha1 = "Senha123@"
# senha2 = "senhafraca"
# senha3 = "Senha_fraca"
# print(validador_senha(senha1))  # Saída esperada: True
# print(validador_senha(senha2))  # Saída esperada: False
# print(validador_senha(senha3))  # Saída esperada: False


def tem_letra_maiuscula(senha):
    for n in senha:
        if n.isupper():
            return True
    return False

def tem_letra_minuscula(senha):
    for n in senha:
        if n.islower():
            return True
    return False

def tem_numero(senha):
    for n in senha:
        if n.isdigit():
            return True
    return False

def tem_caractere_especial(senha):
    caracteres_especiais = set("@#$%^&+=!")
    for n in senha:
        if n in caracteres_especiais:
            return True
    return False

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not tem_letra_maiuscula(senha):
        return False
    if not tem_letra_minuscula(senha):
        return False
    if not tem_numero(senha):
        return False
    if not tem_caractere_especial(senha):
        return False
    return True

senha1 = input("Insira a primeira senha: ")
senha2 = input("Insira a segunda senha: ")
senha3 = input("Insira a terceira senha: ")


print(validador_senha(senha1)) 
print(validador_senha(senha2)) 
print(validador_senha(senha3)) 
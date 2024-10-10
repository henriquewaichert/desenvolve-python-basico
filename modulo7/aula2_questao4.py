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

def validar_senha(senha):
    if len(senha) < 8:
        return False
    
    possui_maiscula = any(char.isupper() for char in senha)
    possui_minuscula = any(char.islower() for char in senha)
    possui_numero = any(char.isdigit() for char in senha)
    possui_caractere_especial = any(char in "@#$%&*!" for char in senha)

    return possui_maiscula and possui_minuscula and possui_numero and possui_caractere_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validar_senha(senha1)) 
print(validar_senha(senha2)) 
print(validar_senha(senha3))
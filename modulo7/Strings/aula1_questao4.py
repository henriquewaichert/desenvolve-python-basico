# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

# Digite o número: 97651234
# Número completo: 99765-1234
# Digite o número: 980876543
# Número completo: 98087-6543 

def formatar_numero(numero):
    numero = numero.replace(" ", "").replace("-", "")
    
    if len(numero) == 8:
        numero = "9" + numero
    
    elif len(numero) == 9 and numero[0] != "9":
        numero = numero[:1] + "-" + numero[1:]
    
    numero_formatado = numero[:5] + "-" + numero[5:]
    
    return numero_formatado

while True:
    telefone = input("Digite o número: ")
    if telefone.isdigit():
        telefone_formatado = formatar_numero(telefone)
        print("Número completo:", telefone_formatado)
        break
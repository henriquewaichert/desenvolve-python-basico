# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
# Digite o número: 97651234
# Número completo: 99765-1234
# Digite o número: 980876543
# Número completo: 98087-6543 

def formatar_numero (num):
    num = str(num).strip()

    if len(num) == 8:
        num = '9' + num
    elif len(num) == 9:
        if num[0] != '9':
            print("Número inválido. O primeiro dígito deve ser '9' para um número com 9 dígitos.")
            return None
    else:
        print("Número inválido. Deve ter 8 ou 9 dígitos.")
        return None
    
    num_formatado = f"{num[:5]}-{num[:5]}"
    return num_formatado

num = input("Digite o número: ")

num_completo = formatar_numero(num)

if num_completo:
    print(f"Número completo: {num_completo}")
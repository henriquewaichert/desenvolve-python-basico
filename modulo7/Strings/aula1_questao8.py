# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        return True
    else:
        return False

def main():
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
    if validar_cpf(cpf):
        print("CPF Válido")
    else:
        print("CPF Inválido")

if __name__ == "__main__":
    main()
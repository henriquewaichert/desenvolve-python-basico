def calcular_digito_verificador(cpf, peso_inicial):
    soma = 0
    for i, digito in enumerate(cpf):
        soma += int(digito) * (peso_inicial - i)
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    primeiros_nove_digitos = cpf[:9]
    primeiro_digito = calcular_digito_verificador(primeiros_nove_digitos, 10)
    segundo_digito = calcular_digito_verificador(primeiros_nove_digitos + str(primeiro_digito), 11)
    if cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito):
        return "Válido"
    else:
        return "Inválido"

cpf_input = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf_input)
print(resultado)
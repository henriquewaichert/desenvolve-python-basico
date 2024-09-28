# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

seu_genero = input("Digite seu gênero (M ou F): ").upper()
sua_idade = int(input("Digite sua idade: "))
seu_tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

if seu_genero == "F":
    aprovado_aposentar = sua_idade > 60 or seu_tempo_servico >= 30 or (sua_idade >= 60 and seu_tempo_servico >= 25)
elif seu_genero == "M":
    aprovado_aposentar = sua_idade > 65 or seu_tempo_servico >= 30 or (sua_idade >= 60 and seu_tempo_servico >= 25)
else:
    aprovado_aposentar = False

print(f"Pode se aposentar: {aprovado_aposentar}")
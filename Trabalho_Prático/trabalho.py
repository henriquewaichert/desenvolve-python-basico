import csv

# Função para carregar dados de um arquivo CSV
def carregar_dados(nome_arquivo):
    dados = []
    with open(nome_arquivo, mode='r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            dados.append(linha)
    return dados

# Função para salvar dados em um arquivo CSV
def salvar_dados(nome_arquivo, dados, campos):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

# Funções CRUD para Usuários
def criar_usuario(dados, id, nome, senha, cargo, permissoes):
    dados.append({'id': id, 'nome': nome, 'senha': senha, 'cargo': cargo, 'permissoes': permissoes})
    print(f"Usuário {nome} criado com sucesso.")

def listar_usuarios(dados):
    for usuario in dados:
        print(f"{usuario['id']}: {usuario['nome']} - {usuario['cargo']}")

def atualizar_usuario(dados, id, campo, novo_valor):
    for usuario in dados:
        if usuario['id'] == id:
            usuario[campo] = novo_valor
            print(f"Usuário {id} atualizado.")
            return
    print(f"Usuário com id {id} não encontrado.")

def deletar_usuario(dados, id):
    for usuario in dados:
        if usuario['id'] == id:
            dados.remove(usuario)
            print(f"Usuário {id} removido com sucesso.")
            return
    print(f"Usuário com id {id} não encontrado.")

# Funções CRUD para Serviços
def criar_servico(dados, codigo, nome, descricao, preco):
    dados.append({'codigo': codigo, 'nome': nome, 'descricao': descricao, 'preco': preco})
    print(f"Serviço {nome} adicionado.")

def listar_servicos(dados):
    for servico in dados:
        print(f"{servico['codigo']}: {servico['nome']} - {servico['descricao']} - Preço: R${servico['preco']}")

def buscar_servico_por_nome(dados, nome):
    for servico in dados:
        if servico['nome'].lower() == nome.lower():
            print(f"Serviço encontrado: {servico['nome']} - Preço: R${servico['preco']}")
            return
    print(f"Serviço {nome} não encontrado.")

def atualizar_servico(dados, codigo, campo, novo_valor):
    for servico in dados:
        if servico['codigo'] == codigo:
            servico[campo] = novo_valor
            print(f"Serviço {codigo} atualizado.")
            return
    print(f"Serviço com código {codigo} não encontrado.")

def deletar_servico(dados, codigo):
    for servico in dados:
        if servico['codigo'] == codigo:
            dados.remove(servico)
            print(f"Serviço {codigo} removido.")
            return
    print(f"Serviço com código {codigo} não encontrado.")

# Testando as funcionalidades
usuarios = carregar_dados('usuarios.csv')
servicos = carregar_dados('servicos.csv')

# Exemplo de uso:
criar_usuario(usuarios, 4, 'Ricely', 'suporte', 'cliente', 'viwe_only')
listar_usuarios(usuarios)
salvar_dados('usuarios.csv', usuarios, ['id', 'nome', 'senha', 'cargo', 'permissoes'])

criar_servico(servicos, 104, 'SEO para Sites', 'Serviço de otimização para mecanismos de busca', 2000)
listar_servicos(servicos)
salvar_dados('servicos.csv', servicos, ['codigo', 'nome', 'descricao', 'preco'])
# LOJA = TechStore 

# Introdução: 
# A "TechStore" é uma loja de eletrônicos que oferece uma ampla variedade de produtos eletrônicos, desde smartphones e laptops até acessórios como fones de ouvido e carregadores. O sistema de gerenciamento foi desenvolvido para permitir o controle de acesso de diferentes tipos de usuários, como gerentes, funcionários e clientes, e para facilitar o gerenciamento dos produtos oferecidos pela loja.

import csv
import os

# Função para carregar usuários do arquivo CSV para um dicionário
def carregar_usuarios(filename):
    usuarios = {}
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            username, password, tipo, permissions = row
            usuarios[username] = [password, tipo, permissions.split(';')]
    return usuarios

# Função para salvar usuários do dicionário para o arquivo CSV
def salvar_usuarios(filename, usuarios):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Password', 'Type', 'Permissions'])
        for username, data in usuarios.items():
            password, tipo, permissions = data
            writer.writerow([username, password, tipo, ';'.join(permissions)])

# Função para carregar produtos do arquivo CSV para uma lista de dicionários
def carregar_produtos(filename):
    produtos = []
    if not os.path.exists(filename):
        return produtos  # Retorna lista vazia se o arquivo não existir
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append(row)
    return produtos

# Função para salvar produtos da lista de dicionários para o arquivo CSV
def salvar_produtos(filename, produtos):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Price', 'Quantity', 'Category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função para criar o arquivo 'usuarios.csv' com dados de exemplo
def criar_arquivo_usuarios(filename):
    dados_usuarios = [
        ['Username', 'Password', 'Type', 'Permissions'],
        ['joao123', 'senha123', 'gerente', 'C;R;U;D'],
        ['maria456', 'senha456', 'funcionario', 'C;R'],
        ['carlos789', 'senha789', 'estagiario', 'R']
    ]
    with open(filename, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(dados_usuarios)

# Função principal
def main():
    usuarios_csv = 'usuarios.csv'
    produtos_csv = 'produtos.csv'

    # Criar arquivo usuarios.csv se não existir
    if not os.path.exists(usuarios_csv):
        criar_arquivo_usuarios(usuarios_csv)

    # Criar arquivo produtos.csv se não existir
    if not os.path.exists(produtos_csv):
        # Você pode adicionar dados de exemplo aqui se desejar
        with open(produtos_csv, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Name', 'Price', 'Quantity', 'Category'])

    # Carregar dados de usuários e produtos
    usuarios = carregar_usuarios(usuarios_csv)
    produtos = carregar_produtos(produtos_csv)

    # Restante do seu código...

if __name__ == "__main__":
    main()

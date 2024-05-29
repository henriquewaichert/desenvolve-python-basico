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
        writer.writerows(produtos)

# Função para criar o arquivo 'produtos.csv' com dados de exemplo
def criar_arquivo_produtos(filename):
    dados_produtos = [
        {'Name': 'Smartphone XYZ', 'Price': 999.99, 'Quantity': 10, 'Category': 'Smartphones'},
        {'Name': 'Laptop ABC', 'Price': 1299.99, 'Quantity': 5, 'Category': 'Laptops'},
        {'Name': 'Headphones XYZ', 'Price': 99.99, 'Quantity': 20, 'Category': 'Acessórios'}
    ]
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dados_produtos[0].keys())
        writer.writeheader()
        writer.writerows(dados_produtos)

# Função principal
def main():
    usuarios_csv = 'usuarios.csv'
    produtos_csv = 'produtos.csv'

    # Criar arquivo produtos.csv se não existir
    if not os.path.exists(produtos_csv):
        criar_arquivo_produtos(produtos_csv)

    # Carregar dados de usuários e produtos
    usuarios = carregar_usuarios(usuarios_csv)
    produtos = carregar_produtos(produtos_csv)

    # Restante do seu código...

if __name__ == "__main__":
    main()

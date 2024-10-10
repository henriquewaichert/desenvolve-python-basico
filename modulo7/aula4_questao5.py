# 5) A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.

# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
# Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
# Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
# Seu arquivo deve ser aberto como uma planilha parecida com a imagem anexada neste exercício.

livros = [
    {"Título": "Orgulho e Preconceito", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 368},
    {"Título": "A Metamorfose", "Autor": "Franz Kafka", "Ano de publicação": 1915, "Número de páginas": 120},
    {"Título": "Fahrenheit 451", "Autor": "Ray Bradbury", "Ano de publicação": 1953, "Número de páginas": 158},
    {"Título": "O Morro dos Ventos Uivantes", "Autor": "Emily Brontë", "Ano de publicação": 1847, "Número de páginas": 416},
    {"Título": "A Casa dos Espíritos", "Autor": "Isabel Allende", "Ano de publicação": 1982, "Número de páginas": 368},
    {"Título": "O Grande Gatsby", "Autor": "F. Scott Fitzgerald", "Ano de publicação": 1925, "Número de páginas": 180},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "O Senhor dos Anéis: A Sociedade do Anel", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 423},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417},
    {"Título": "A Cidade do Sol", "Autor": "Khaled Hosseini", "Ano de publicação": 2007, "Número de páginas": 384},
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo.write(linha)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

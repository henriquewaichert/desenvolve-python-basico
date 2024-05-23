# 5) A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
# Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
# Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
# Seu arquivo deve ser aberto como uma planilha parecida com a imagem anexada neste exercício.


livros = [
    {"Título": "Dom Quixote", "Autor": "Miguel de Cervantes", "Ano de publicação": 1605, "Número de páginas": 863},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 152},
    {"Título": "O Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1209},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "Harry Potter e a Câmara Secreta", "Autor": "J.K. Rowling", "Ano de publicação": 1998, "Número de páginas": 251},
    {"Título": "Harry Potter e o Prisioneiro de Azkaban", "Autor": "J.K. Rowling", "Ano de publicação": 1999, "Número de páginas": 317}
]

with open("meus_livros.csv", "w", newline="", encoding="utf-8") as arquivo:

    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for livro in livros:
        titulo = livro["Título"]
        autor = livro["Autor"]
        ano = str(livro["Ano de publicação"])
        paginas = str(livro["Número de páginas"])
        linha = f"{titulo},{autor},{ano},{paginas}\n"
        arquivo.write(linha)

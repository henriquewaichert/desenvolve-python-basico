# 6) Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos!
# Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá! (http://kaggle.com/)
# Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
# No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas
# Ao abrir o arquivo, defina o parâmetro encoding='latin-1'  na função open
# Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.
# O arquivo está estruturado da seguinte forma: cada linha representa uma música e contém as seguintes informações separadas por vírgula (CSV):

# track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists

# Usaremos apenas informações das colunas:
# track_name: Nome da música
# artist(s)_name: Nome do artista
# artist_count: Número de artistas listados em artist(s)_name
# released_year: Ano de lançamento
# streams: Número de vezes que a música foi tocada no Spotify
# Você deve criar um script Python para processar esse arquivo e gerar uma lista com 10 elementos, cada qual representando a música mais tocada de cada ano no intervalo de 2012 a 2022. Considere somente músicas dentro do intervalo solicitado. Cada elemento da lista produzida deve conter as seguintes informações:

# [track_name, artist(s)_name, released_year, streams]

# Essa atividade tem alguns desafios. Assim como as colunas da tabela são separadas por vírgulas, músicas com mais de um artista (artist_count>1) terá o campo artist(s)_name entre aspas com o nome dos artistas separado por vírgulas. 

# Ex: Seven (feat. Latto) (Explicit Ver.),"Latto, Jung Kook",2,2023, …

# Há também nomes de músicas entre aspas por conter caracteres especiais como vírgulas ou aspas. 

# Ex: "Peso Pluma: Bzrp Music Sessions,Vol.55","Bizarrap,Peso Pluma",2,2023,

# Você deve ignorar essas linhas, e terá portanto que propor uma verificação para identificá-las.

# Ao final imprima a lista produzida. Ex:
# [ ['When I Was Your Man', 'Bruno Mars', 2012, 1661187319],
#  ['I Wanna Be Yours', 'Arctic Monkeys', 2013, 1297026226],
#  ...,
#  ['As It Was', 'Harry Styles', 2022, 2513188493] ]

import csv

def obter_musicas_mais_tocadas(arquivo):
    musicas_por_ano = {}

    with open(arquivo, 'r', encoding='latin-1') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)

        for linha in leitor:
            if len(linha) < 10:
                continue
            
            track_name = linha[0]
            artist_name = linha[1]
            released_year = int(linha[3])
            streams_str = linha[8]

            if '"' in track_name or len(artist_name.split(',')) > 1:
                continue

            try:
                streams = int(streams_str)
            except ValueError:
                continue

            if 2012 <= released_year <= 2022:
                if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                    musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    lista_musicas = [musicas_por_ano[ano] for ano in range(2012, 2023) if ano in musicas_por_ano]

    return lista_musicas

arquivo = 'spotify-2023.csv'
musicas_mais_tocadas = obter_musicas_mais_tocadas(arquivo)

print(musicas_mais_tocadas)

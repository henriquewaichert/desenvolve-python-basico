# 2) Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.

# URLs: ["www.google.com&quot;, "www.gmail.com&quot;, "www.github.com&quot;, "www.reddit.com&quot;, "www.yahoo.com&quot;]
# dominios:  ["google", "gmail", "github", "reddit", "yahoo"]

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

nomes_dominios = [url[4:-4] for url in urls]

print("dominios:", nomes_dominios)

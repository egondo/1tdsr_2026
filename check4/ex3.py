def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)

def organiza(lista: list, pos: int):
    aux = lista[pos]
    i = pos
    while i > 0 and lista[i-1]['ano'] > aux['ano']:
        lista[i] = lista[i-1]
        i = i - 1
    lista[i] = aux


livros = [
    {"autor": "Simon Singh", 
    "titulo": "O Último Teorema de Fermat",
    "ano": 1997},

    {"autor": "Simon Singh",
    "titulo": "O Livro dos Códigos",
    "ano": 1999},

    {"autor": "Elias Canetti",
    "titulo": "A Língua Absolvida",
    "ano": 1977},

    {"autor": "Marcelo Gleise",
    "titulo": "A Dança do Universo",
    "ano": 1997},

    {"autor": "Amyr Klink",
    "titulo": "Paratii - Entre dois Polos",
    "ano": 1992},

    {"autor": "Agatha Christie",
    "titulo": "Os crimes ABC",
    "ano": 1936},

    {"autor": "J. K. Rowling",
    "titulo": "Harry Potter e a Pedra Filosofal",
    "ano": 1998}
]

insertion_sort(livros)
for livro in livros:
    print(livro)
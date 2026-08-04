#Dicionario de listas

atores = {}

atores['Leonardo DiCaprio'] = ['Titanic', 'O Regresso', 'Lobo de Wall Street']
atores['Anne Hathaway'] = ['Diabo Veste Prada', 'Diabo Veste Prada 2']
atores['Alice Braga'] = ['Cidade de Deus', 'Eu sou a Lenda']

for chave in atores:
    print(f"Ator {chave}: ")
    for filme in atores[chave]:
        print(f"\t {filme}")


atores['Anne Hathaway'].append("Diário de uma Princesa")

print(atores['Anne Hathaway'])
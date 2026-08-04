ufs = {"RJ": "Rio de Janeiro", "BA": "Bahia"}

ufs['SP'] = "São Paulo"
ufs['MG'] = 'Minas Gerais'
ufs['SC'] = "Santa Catarina"
ufs['SE'] = 'Sergipe'

for sigla in ufs:
    print(sigla, ufs[sigla])

ufs.pop('SC')

print("___________________")

for sigla in ufs:
    print(sigla, ufs[sigla])


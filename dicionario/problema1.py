texto = input("Digite a frase: ")

contagem = {}

texto = texto.upper()

for letra in texto:
    #print(letra)
    if not letra in contagem:
        contagem[letra] = 1
    else:
        contagem[letra] = contagem[letra] + 1

for chave in contagem:
    print(chave, "=>", contagem[chave])


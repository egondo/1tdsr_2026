frase = input("Frase: ")
letras = input("Letras: ")

resp = ""

for c in frase:
    if c in letras:
        resp = resp + '*'
    else:
        resp = resp + c

print(resp)
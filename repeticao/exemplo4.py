nota = float(input("Digite uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    print('Nota invalida!')
    nota = float(input("Digite novamente: "))

print(nota)

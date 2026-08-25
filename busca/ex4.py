lista = [2, 5, -7, 9, 3, 10, 15, 6, 1]

soma = 11

#num = lista[0]
#for i in range(1, len(lista)):
#    if num + lista[i] == soma:
#        print(f"({num}, {lista[i]})")

#num = lista[1]
#for i in range(2, len(lista)):
#    if num + lista[i] == soma:
#        print(f"({num}, {lista[i]})")

for j in range(0, len(lista) - 1):
    num = lista[j]
    for i in range(j + 1, len(lista)):
        if num + lista[i] == soma:
            print(f"({num}, {lista[i]})")
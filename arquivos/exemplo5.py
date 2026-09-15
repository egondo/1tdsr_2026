lista = ["Maça\n", "Pêra\n", "Banana\n", "Caqui\n", "Manga\n", "Uva\n"]

with open("frutas.txt", mode="w") as arq:
    arq.writelines(lista)


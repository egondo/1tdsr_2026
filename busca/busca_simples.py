def busca(lista: list, elemento: str) -> int:
    i = 0
    while i < len(lista) and lista[i] != elemento:
        i = i + 1

    if i < len(lista):
        print("Parabéns, vc encontrou!")
        return i
    else:
        print("Vc não encontrou o elemento na lista")
        return -1

l = [343, 92,  234, 1000, 7, 19, 22, 72, 11, 15]
pos = busca(l, 19)
print(pos)

pos = busca(l, 192)
print(pos)


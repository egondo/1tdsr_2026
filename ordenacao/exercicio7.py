def particao(lista: list) -> int:
    #criando aux do mesmo tamanho de lista
    aux = [0] * len(lista)
    ini = 0
    fim = len(aux) - 1
    pivo = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < pivo:
            aux[ini] = lista[i]
            ini = ini + 1
        else:
            aux[fim] = lista[i]
            fim = fim - 1
        i = i + 1

    aux[ini] = pivo
    i = 0
    while i < len(lista):
        lista[i] = aux[i]
        i = i + 1
    return ini    

#conj = [10, 23, 7, 6, 4, 18]
conj = [15, 9, -10, 76, 5, 86, 23, 43, -7]
pos = particao(conj)
print("POS ", pos)
print(conj)
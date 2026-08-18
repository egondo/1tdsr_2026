def menor(v: list, pos: int) -> int:
    pos_menor = pos
    i = pos
    while i < len(v):
        if v[i] < v[pos_menor]:
            pos_menor = i
        i = i + 1
    return pos_menor

def selection_sort(lista: list):
    for i in range(len(lista)):
        resp = menor(conj, i)
        aux = lista[resp]
        lista[resp] = lista[i]
        lista[i] = aux


conj = [3, 0, 8, 10, 7, -1, 5, 6]
selection_sort(conj)
print(conj)
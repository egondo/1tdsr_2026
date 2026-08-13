def busca_binaria(lista: list, ini: int, fim: int, valor: str) -> int:
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] < valor:
            ini = meio + 1
        elif lista[meio] > valor:
            fim = meio - 1
        else:
            return meio
    return -1


lista = [2, 56, 78, 90, 100, 120, 156]
pos = busca_binaria(lista, 0, len(lista) - 1, 78)
print(pos)

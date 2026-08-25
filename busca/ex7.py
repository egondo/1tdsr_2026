def busca(valor, lista: list) -> list:
    retorno = []
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            retorno.append(i)
        i = i + 1
    
    return retorno


lista = [-4, 6, 9, 2, 7, 8, 10, 23, 76, 23, 21, 19, 18, 23, 19, -5]
ret = busca(18, lista)
print(ret)

ret = busca(23, lista)
print(ret)

ret = busca(0, lista)
print(ret)


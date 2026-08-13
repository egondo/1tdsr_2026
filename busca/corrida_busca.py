import time

def busca_binaria(lista: list, ini: int, fim: int, valor) -> int:
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] < valor:
            ini = meio + 1
        elif lista[meio] > valor:
            fim = meio - 1
        else:
            return meio
    return -1

def busca(lista: list, elemento) -> int:
    i = 0
    while i < len(lista) and lista[i] != elemento:
        i = i + 1

    if i < len(lista):
        return i
    else:
        return -1

dados = []
for num in range(200_000):
    dados.append(num)

ini = time.time()
for i in range(1000):
    busca(dados, -1)
fim = time.time()
print("Busca simples ", fim - ini, " segundos")

ini = time.time()
for i in range(1000):
    busca_binaria(dados, 0, len(dados) - 1, -1)
fim = time.time()
print("busca binaria ", fim - ini, " segundos")
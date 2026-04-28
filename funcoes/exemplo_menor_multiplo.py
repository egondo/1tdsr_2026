def mmc(a: int, b: int) -> int:
    valor = b
    while valor % a != 0 or valor % b != 0:
        valor = valor + 1
    return valor
        

res = mmc(8, 12)
print(res)


def soma(a: float, b: float) -> float:
    valor = a + b
    a = a + 1
    b = b + 1
    return valor
x = 7
y = 10
res = soma(x, y)
print(res)
print(x)
print(y)

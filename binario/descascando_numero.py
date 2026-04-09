cpf = int(input("CPF: "))
aux = cpf

while aux != 0:
    dig = aux % 10
    aux = aux // 10
    print(dig)




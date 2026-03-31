num_a = float(input("Informe 1 num: "))
op = input("Operador (+-*/): ")
num_b = float(input("Informe 2 num: "))

fez_conta = True

if op == "+":
    resultado = num_a + num_b
elif op == "-":
    resultado = num_a - num_b
elif op == "*":
    resultado = num_a * num_b
elif op == "/":
    if num_b != 0:
        resultado = num_a / num_b
    else:
        fez_conta = False
    

if fez_conta:
    print(f"{num_a} {op} {num_b} = {resultado}")
else:
    print(f"Não foi possivel realizar: {num_a} {op} {num_b}")
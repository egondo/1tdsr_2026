try:
    a = int(input("A: "))
    b = int(input("B: "))
    c = a / b
    
except ZeroDivisionError as erro:
    print(erro, "Divisao por zero")
else:
    print(f"Resultado {c}")

valor = float(input("Valor do produto: "))
desc  = float(input("Desconto em percentual: "))

valor_desconto = valor * desc / 100
valor_final = valor - valor_desconto

print("O desconto foi de ", valor_desconto)
print("Você irá pagar: ", valor_final)
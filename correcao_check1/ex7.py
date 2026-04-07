print("1 - Comum")
print("2 - VIP")
print("1 - Premium")
tipo = int(input("Tipo de fidelidade: "))

valor = float(input("Valor da compra: "))
desconto = 0

if valor > 100 and tipo == 2:
    desconto = valor * 0.05 
elif tipo == 3:
    if valor > 500:
        desconto = valor * 0.15
    else:
        desconto = valor * 0.1

frete = 0
if valor < 200:
    frete = 25

print(f"Valor do frete: {frete}")
print(f"Desconto: {desconto}")
print(f"Valor da compra: {valor - desconto + frete}")
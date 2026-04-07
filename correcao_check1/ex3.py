peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"IMC: {imc} - abaixo do peso")
elif imc <= 24.9:
    print(f"IMC: {imc} - peso normal")
elif imc <= 29.9:
    print(f"IMC: {imc} - sobrepeso")
else:
    print(f"IMC: {imc} - obesidade")



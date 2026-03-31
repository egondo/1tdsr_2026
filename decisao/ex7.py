import math

numero = float(input("Informe o número: "))
if numero >= 0:
    resultado = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {resultado}")
else:
    print(f"Impossível extrair raiz de número negativo: {numero}")
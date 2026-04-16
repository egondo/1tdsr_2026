num = int(input("Digite num: "))
div = 2
resto = num % div

while resto != 0:
    div = div + 1
    resto = num % div

if num > div:
    print(f"{num} não é primo")
else:
    print(f"{num} é primo")
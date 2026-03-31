soma = 0

num = int(input("Informe o numero da sequencia: "))
while num != 0:
    if num % 2 == 0:
        soma = soma + num

    num = int(input("Informe o numero da sequencia: "))

print(f"A soma vale {soma}")
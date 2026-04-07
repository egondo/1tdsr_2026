qtd_num = int(input("Informe a qtd de números: "))

contador = 0
conta_pares = 0
conta_impares = 0
while contador < qtd_num:
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        conta_pares = conta_pares + 1
        print(f"{num} é PAR")
    else:
        conta_impares = conta_impares + 1
        print(f"{num} é ÍMPAR")
    contador = contador + 1

print(f"A qtd de pares foi de {conta_pares}")
print(f"A qtd de ímpares foi de {conta_impares}")

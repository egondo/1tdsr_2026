n = int(input("Qtd de alunos/notas: "))

contador = 0
soma = 0

while contador < n:
    nota = float(input("Nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma / n

print(f"A média vale {media}")
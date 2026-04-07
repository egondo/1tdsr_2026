n = int(input("Qtd de alunos/notas: "))

contador = 0
soma = 0
qtd_alunos_bem = 0
qtd_alunos_mal = 0

while contador < n:
    nota = float(input("Nota: "))
    soma = soma + nota
    if nota >= 5:
        qtd_alunos_bem = qtd_alunos_bem + 1
    else:
        qtd_alunos_mal = qtd_alunos_mal + 1

    contador = contador + 1

media = soma / n

print(f"A média vale {media}")
print(f"A qtd de alunos que tirou 5 ou mais é {qtd_alunos_bem}")
print(f"A qtd de alunos que tiraram menos do que 5 é {qtd_alunos_mal}")
n = int(input("Quantidade alunos: "))

notas = []
soma = 0
i = 0

while i < n:
    nota = float(input("Nota: "))
    notas.append(nota)
    soma = soma + nota
    i = i + 1

print(f"Lista: {notas}")

media = soma / n
abaixo_media = 0
for nota in notas:
    if nota < media:
        abaixo_media = abaixo_media + 1

acima_media = n - abaixo_media        
print(f"A média da turma foi {media}")
print(f"{acima_media} tiraram acima ou igual da média da turma")
print(f"{abaixo_media} tiraram abaixo da média da turma")

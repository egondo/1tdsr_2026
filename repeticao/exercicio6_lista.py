nota = int(input("Nota: "))
maior = nota
menor = nota

conta_ate_20 = 0
conta_ate_50 = 0
conta_acima_50 = 0

if nota <= 20:
    conta_ate_20 = conta_ate_20 + 1
elif nota <= 50:
    conta_ate_50 = conta_ate_50 + 1
else:
    conta_acima_50 = conta_acima_50 + 1

contador = 0
while contador < 19:
    nota = int(input("Nota: "))

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

    if nota <= 20:
        conta_ate_20 = conta_ate_20 + 1
    elif nota <= 50:
        conta_ate_50 = conta_ate_50 + 1
    else:
        conta_acima_50 = conta_acima_50 + 1
    
    contador = contador + 1

print(f"A maior nota foi {maior}")
print(f"A menor nota foi {menor}")

perc_20 = (conta_ate_20 / 20) * 100.0
perc_50 = (conta_ate_50 / 20) * 100.0
perc_acima_50 = (conta_acima_50 / 20) * 100.0

print(f"percentual de candidatos com até 20 acertos: {perc_20}%")
print(f"percentual de candidatos de 21 até 50 acertos: {perc_50}%")
print(f"percentual com mais de 50 acertos: {perc_acima_50}%")
ms1 = float(input("Media 1º semestre: "))
ms2 = float(input("Media 2º semestre: "))

ministradas = int(input("Qtd aulas ministradas: "))
assistidas = int(input("Qtd aulas assistidas: "))

media_final = (4 * ms1 + 6 * ms2) / 10
presenca_percent = assistidas / ministradas

if presenca_percent >= 0.7:
    #nao reprovado por falta
    if media_final >= 6:
        print(f"Aprovado MF: {media_final}")
    elif media_final >= 4:
        print(f"Vc esta de Exame e precisa de: {12 - media_final}")
    else:
        print(f"Vc foi reprovado, média {media_final}")
else:
    print(f"Reprovado por falta {presenca_percent * 100}%")
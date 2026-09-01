def calcula_media(notas: dict):
    for chave in notas.keys():
        medias = notas[chave]
        media_final = (4 * medias[0] + 6 * medias[1]) / 10
        resultado = ""
        if media_final >= 6:
            resultado = "Aprovado"
        elif media_final >= 4:
            resultado = "Exame"
        else:
            resultado = "Retido"

        medias.append(media_final)   
        medias.append(resultado)

turma = {
    "Alexandre": [5.6, 7.0],
    "Bruna": [4.5, 3.8],
    "Carolina": [5.5, 4.8],
    "Douglas": [2.0, 8.5],
    "Evandro": [4.6, 6.1],
    "Fabio": [6.7, 9.0]
}

calcula_media(turma)

for aluno in turma:
    print(f"{aluno} => {turma[aluno]}")
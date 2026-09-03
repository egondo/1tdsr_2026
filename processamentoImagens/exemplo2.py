import Imagem

matriz = Imagem.getMatrizImagemCinza('domino.png')

lin = len(matriz)
col = len(matriz[0])

for i in range(lin):
    for j in range(col):
        matriz[i][j] = 255 - matriz[i][j]

Imagem.salvaImagemCinza('domino2.png', matriz)
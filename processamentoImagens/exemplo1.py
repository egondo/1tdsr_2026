import Imagem

tupla = Imagem.getMatrizImagemColorida('olhos.jpg')

matriz_r = tupla[0]
matriz_g = tupla[1]
matriz_b = tupla[2]

lin = len(matriz_r)
col = len(matriz_r[0])

print(f"olhos.jpg tem {col} X {lin}")

for i in range(lin):
    for j in range(col):
        matriz_r[i][j] = matriz_r[i][j] - 20

Imagem.salvaImagemCinza('olhos_escurecidos.jpg', matriz_r)
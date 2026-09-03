import Imagem

yao = Imagem.getMatrizImagemCinza('yao-ming.png')

lin = len(yao)
col = len(yao[0])

mat = []
for i in range(col):
    mat.append([0] * lin)

for i in range(lin):
    for j in range(col):
        mat[j][i] = yao[i][j]
Imagem.salvaImagemCinza('yao_transposto.png', mat)
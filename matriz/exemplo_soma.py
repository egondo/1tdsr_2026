def soma(matrizA: list, matrizB: list) -> list:

    #criar a matriz soma com as mesmas dimensões da matriz A ou B.

    #percorra a lista das matrizes A e B, somando os valores de cada posiçao
    #atribuo valor dessa soma na matriz que foi criada.

    lin = len(matrizA)
    col = len(matrizA[0])
    resp = []
    for l in range(lin):
        resp.append([0] * col)

    for i in range(lin):
        for j in range(col):
            resp[i][j] = matrizA[i][j] + matrizB[i][j]
    return resp  

    
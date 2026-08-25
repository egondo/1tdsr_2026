#criando a matriz 4x5
matriz = []
for i in range(4):
    matriz.append([0] * 5)


#populando a matriz
num = 1
for i in range(4):
    for j in range(5):
        matriz[i][j] = num
        num = num + 1

#imprimindo uma matriz
for lin in matriz:
    print(lin)
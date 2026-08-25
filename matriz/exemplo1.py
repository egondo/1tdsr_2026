#Criar uma matriz que representa um jogo da velha, ou seja, 3 linhas e 3 colunas

matriz = []
for i in range(3):
    matriz.append([''] * 3)

#matriz[0][0] = 'X'
#matriz[1][1] = 'O'
#matriz[2][2] = 'X'

matriz[0][2] = 'X'
matriz[1][0] = 'O'
matriz[1][1] = 'X'
matriz[2][0] = 'O'

#para imprimir
for lin in matriz:
    print(lin)

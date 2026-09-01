#Crie aqui as funcoes do Jogo da Velha

def tem_espaco(matriz: list) -> bool:
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == '' or matriz[i][j] == ' ':
                return True
    return False


def joga(matriz: list, lin: int, col: int, jogador: str) -> bool:
    if matriz[lin][col] == '' or matriz[lin][col] == ' ':
        matriz[lin][col] = jogador
        return True
    else:
        return False


def ha_ganhador(matriz: list) -> bool:
    for i in range(3):
        if matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][0] != '':
            return True

        if matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i] != '':
            return True
            
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] != '':
        return True
    if matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[0][2] != '':
        return True

    return False

def imprime(matriz: list):
    for lin in matriz:
        print(lin)

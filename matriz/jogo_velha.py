import velha

tab = []
for i in range(3):
    tab.append([''] * 3)

player = 'X'
while velha.tem_espaco(tab) and not velha.ha_ganhador(tab):
    velha.imprime(tab)

    lin = int(input("Lin: "))
    col = int(input("Col: "))

    resp = velha.joga(tab, lin, col, player)
    if resp:
        velha.troca_jogador(player)
    else:
        print("Jogada inválida!")
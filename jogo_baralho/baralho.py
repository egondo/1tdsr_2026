import random

def criar() -> list:
    monte = []
    for valor in range(1, 14):
        monte.append( (valor, '♥️') )
        monte.append( (valor, '♠️') )
        monte.append( (valor, '♦️') )
        monte.append( (valor, '♣️') )
    return monte

def comprar(monte: list) -> tuple:
    return monte.pop()

def distribuir(qtd: int, monte: list) -> list:
    resp = []
    while qtd > 0:
        resp.append(comprar(monte))
        qtd = qtd - 1
    return resp    

def embaralhar(monte: list):
    for vezes in range(200):
        x = random.randint(0, 51)
        y = random.randint(0, 51)
        aux = monte[x]
        monte[x] = monte[y]
        monte[y] = aux



bar = criar()
embaralhar(bar)
jogador1 = 0
jogador2 = 0

for i in range(26):
    c1 = comprar(bar)
    c2 = comprar(bar)

    if c1[0] < c2[0]:
        jogador2 = jogador2 + 1
    elif c1[0] > c2[0]:
        jogador1 = jogador1 + 1

if jogador1 > jogador2:
    print("Jogador 1 venceu")
elif jogador1 < jogador2:
    print("Jogador 2 venceu")
else:
    print("Empataram:")

#Faça um jogo onde cada jogador compra uma carta e aquele que
#tirar a carta maior vence a partida e ganha o ponto.
#Jogue até o baralho terminar e, aquele que tiver mais pontos, 
#vence o jogod
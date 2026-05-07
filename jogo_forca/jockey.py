import random

def lancar_dado() -> int:
    return random.randint(0, 6) + 1


def jogada(pos, jogador) -> int:
    valor = pos + jogador
    if valor == 18:
        print("Desviou do ostáculo, volte para 12")
        return 12
    elif valor == 31:
        print("Caveleiro derrubado!") 
        return 1
    elif valor == 44:
        print("Estou cavalgando bem, ascrecente o mesmo valor pos na jogada")
        return  44 + pts
    elif valor == 62:
        return 1
    elif valor > 72:
        print("Parabéns vc cruzou a linha de chegada.")


red = 1
blue = 1
while red < 72 and blue < 72:
    pts = lancar_dado()
    red = jogada(red, pts)

    pts = lancar_dado()
    azul = jogada(azul, pts)

if red >= 72:
    print("Vermelho foi vencedor!")
elif blue >= 72 :
    print("Azul foi vencedoir")

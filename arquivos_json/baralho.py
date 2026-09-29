import random

class Carta:

    def __init__(self, valor: int, naipe: str):
        self.valor = valor
        self.naipe = naipe

    def to_string(self) -> str:
        naipe = ''
        if self.naipe == 'PAUS':
            naipe = '♣'
        elif self.naipe == 'ESPADAS':
            naipe = '♠'
        elif self.naipe == 'OUROS':
            naipe = '♦'
        else:
            naipe = '♥'

        if self.valor == 1:
            return f"A {naipe}"    
        return f"{self.valor} {naipe}"


class Baralho:

    def __init__(self):
        self.monte = []
        self.topo = 0
        for i in range(1, 13):
            self.monte.append(Carta(i, 'PAUS'))
            self.monte.append(Carta(i, 'ESPADAS'))
            self.monte.append(Carta(i, 'COPAS'))
            self.monte.append(Carta(i, 'OUROS'))

    def embaralha(self):
        random.shuffle(self.monte)

    def compra(self) -> Carta:
        aux = self.topo
        self.topo = self.topo + 1
        return self.monte[aux]
    

if __name__ == "__main__":
    b = Baralho()
    for _ in range(10):
        c = b.compra()
        print(c.to_string())
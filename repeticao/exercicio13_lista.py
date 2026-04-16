import random

sorteado = random.randint(1, 1000)

chute = int(input("Tente acertar: "))
tentativas = 1

while chute != sorteado:

    if chute < sorteado:
        print("Tente um numero maior")
    elif chute > sorteado:
        print("Tente um numero menor")
    chute = int(input("Tente acertar: "))
    tentativas = tentativas + 1

print(f"Parabéns vc acertou em {tentativas} tentativas")


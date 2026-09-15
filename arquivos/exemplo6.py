lista = ["Melancia", "Jatobá", "Laranja", "Kiwi", "Limão"]
with open('frutas.txt', mode="a", encoding="UTF-8") as arq:
    for f in lista:
        arq.write(f + "\n")

print('Finalizei as frutas!')

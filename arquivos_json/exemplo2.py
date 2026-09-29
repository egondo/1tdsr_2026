import json

with open('biblioteca_jogos.json', mode="r") as arq:
    info = json.load(arq)


for dado in info:
    print(dado)
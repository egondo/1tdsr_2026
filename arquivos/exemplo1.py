#Lendo arquivo texto

with open('RemuneracaoAtivos.txt', mode="r") as arq:
    info = arq.read()


print(info)

#tam = len(info)
#print(tam)
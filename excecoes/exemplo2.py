lista = [x for x in range(100)]
try:
    pos = int(input("Digite uma posicao "))
    print(lista[pos])
except IndexError as erro:
    print(f"Indice {pos} invalido, tente um numero de 0 a 99!")
    #raise erro


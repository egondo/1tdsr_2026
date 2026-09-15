import datetime

ini = datetime.datetime.now()
print(ini)
#with open("Microdados_utf8.csv", mode="r") as file:
with open("Big_File.csv", mode="r") as file:
    lista = file.readlines()
    #info = file.read()


fim = datetime.datetime.now()
print(fim)
print(type(lista))

print(len(lista))

#print(type(info))

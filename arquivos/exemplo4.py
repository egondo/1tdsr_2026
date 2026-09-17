#Gravar um arquivo gigantesco
import datetime

ini = datetime.datetime.now()
print(ini)
arq_read = open("Microdados_utf8.csv", mode="r", encoding="UTF-8")
dados = arq_read.read()

arq_write = open("Big_File.csv", mode="w", encoding="UTF-8")


for i in range(30):
    arq_write.write(dados)

arq_read.close()
arq_write.close()

fim = datetime.datetime.now()
print(fim)
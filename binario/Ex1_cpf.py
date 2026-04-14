#Formatar o CPF que o usuário fornecer
#26790651843 => 267.906.528-43

cpf = int(input("Digite um CPF (somente os dígitos): "))

dc = cpf % 100
cpf = cpf // 100

parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

print(f"{cpf:03}.{parte2:03}.{parte3:03}-{dc:02}")
#Se nao existisse o recurso de formatação, implemente a solução usando ifs e talvez convertendo as partes do CPF para strings.
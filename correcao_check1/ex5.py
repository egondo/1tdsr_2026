votos_a = 0
votos_b = 0
votos_nulos = 0
votos_brancos = 0

print("0 - Encerra votação")
print("1 - Candidato A")
print("2 - Candidato B")
print("3 - Voto Nulo")
print("4 - Voto em Branco")
opcao = int(input("Opção: "))

while opcao != 0:
    if opcao == 1:
        votos_a = votos_a + 1
    elif opcao == 2:
        votos_b = votos_b + 1
    elif opcao == 3:
        votos_nulos = votos_nulos + 1
    elif opcao == 4:
        votos_brancos = votos_brancos + 1
    else:
        print("Opção inválida!")
    
    print("0 - Encerra votação")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Voto Nulo")
    print("4 - Voto em Branco")
    opcao = int(input("Opção: "))


print(f"Candidato A: {votos_a}")
print(f"Candidato B: {votos_b}")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos brancos: {votos_brancos}")
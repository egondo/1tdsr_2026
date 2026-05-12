'''Controle de Estoque
a) cadastro de produto com respectiva quantidade
b) consulta para reposição do estoque
c) venda'''

def menu() -> int:
    print("Controle de Estoque")
    print("1 - cadastro de produto")
    print("2 - consulta estoque baixo")
    print("3 - venda")
    print("4 - sair")
    return int(input("Opcao: "))


lista = []
opcao = menu()
while opcao != 4:
    if opcao == 1:
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        valor = float(input("Valor: "))
        qtd = int(input("Quantidade em estoque: "))
        estoque_minimo = int(input("Estoque mínimo: "))
        lista.append(nome)
        lista.append(categoria)
        lista.append(valor)
        lista.append(qtd)
        lista.append(estoque_minimo)

    opcao = menu()

print(lista)


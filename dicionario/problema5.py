def menu() -> int:
    print("Whats app")
    print("1 - cadastra")
    print("2 - consulta")
    print("3 - sair")
    resp = input("Escolha uma das opções")
    return int(resp)

def cadastra(repositorio: dict, msg: str, remetente: str):
    if remetente in repositorio:
        lista = repositorio[remetente]
        lista.insert(0, msg)
    else:
        repositorio[remetente] = [msg]

def consulta(repositorio: dict, remetente: str):
    lista = repositorio[remente]
    return lista


banco_dados = {}
op = menu()
while op != 3:
    tel = input("Informe o numero de telefone: ")
    if op == 1:
        msg = input("Informe a msg ")
        cadastra(banco_dados, msg, tel)
    elif op == 2:
        if tel in banco_dados:
            lista_msgs = banco_dados[tel]
            for itens in lista_msgs:
                print(itens)
    else:
        print("finalizando o programa")

    op = menu()


        


def menu() -> int:
    print('1 - cadastra médico')
    print('2 - cadastra paciente')
    print('3 - consulta médico')
    print('4 - consulta paciente')
    print('5 - altera médico')
    print('6 - altera paciente')
    print('7 - sair')
    opcao = int(input("Opcao: "))
    return opcao

def cadastra_medico():
    nome = input("Nome: ")
    crm = input("CRM: ")
    espec = input('Especialidades: ')
    email = input('Email: ')
    with open('hospital.txt', mode='a', encoding='UTF-8') as arq:
        arq.write(f"MED;{nome};{crm};{espec};{email}\n")


def cadastra_paciente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    tel = input('Telefone: ')
    email = input('Email: ')
    convenio = input('Convenio: ')
    with open('hospital.txt', mode='a', encoding='UTF-8') as arq:
        arq.write(f"PAC;{nome};{cpf};{tel};{email};{convenio}\n")


def consulta_medico():
    espec = input("Informe uma especialidade: ")
    resp = []
    with open('hospital.txt', mode="r", encoding="UTF-8") as arq:
        for registro in arq:
            if registro.startswith("MED"):
                if espec in registro:
                    resp.append(registro)
    
    for dados in resp:
        print(dados)

#program principal
op = menu()
while op != 7:
    if op == 1:
        cadastra_medico()
    elif op == 2:
        cadastra_paciente()
    elif op == 3:
        consulta_medico()
    elif op == 4:
        consulta_paciente()
    
    op = menu()

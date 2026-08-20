def menu() -> int:
    print("1 cadastra")
    print("2 altera")
    print("3 calcula média")
    print("4 exibe média")
    print("5 sair")
    opcao = int(input("Escolha: "))
    return opcao


def cadastra(repositorio: dict):
    rot = ["cp1", "cp2", "cp3", "sp1", "sp2", "gs"]
    rm = int(input("RM: "))
    notas = {}
    repositorio[rm] = notas 
    
    for info in rot:
        dado = float(input(f"{info}:"))
        notas[info] = dado
    
def calcula_media(notas: dict):
    cp1 = notas['cp1']
    cp2 = notas['cp2']
    cp3 = notas['cp3']
    
    if cp1 <= cp2 and cp1 <= cp3:
        media_cp = (cp2 + cp3)/2
    
    if cp2 <= cp1 and cp2 <= cp3:
        media_cp = (cp1 + cp3)/2    
    
    if cp3 <= cp1 and cp3 <= cp2:
        media_cp = (cp1 + cp2)/2

    media_sp = (notas['sp1'] + notas['sp2']) / 2
    ms = 0.2 * media_cp + 0.2 * media_sp + 0.6 * notas['gs']
    notas['ms'] = ms 

if __name__ == "__main__":
    turma = {}
    opcao = 0
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            cadastra(turma)
        elif opcao == 2:
            print("Em construcao")
        elif opcao == 3:
            for chave in turma:
                calcula_media(turma[chave])
        elif opcao == 4:
            print("Medias dos alunos")
            for chave in turma:
                boletim = turma[chave]
                print(f"RM {chave} => {boletim['ms']}")
import futebol_banco as bd

p = {
    "mandante": "Palmeiras",
    "gols_mandante": 3,
    "visitante": "Santos",
    "gols_visitante": 1
}

def atualiza_time(nome_time: str, vit: int, emp: int, derr: int) -> dict:
    time = bd.consulta_clube(nome_time)
    if time == None:
        time = {"nome": nome_time, "vitorias": vit, 
                "empates": emp, "derrotas": derr}
        bd.insert_clube(time)
    else:
        time['vitorias'] = time['vitorias'] + vit
        time['empates'] = time['empates'] + emp
        time['derrotas'] = time['derrotas'] + derr
        bd.update_clube(time)

    return time

def cadastra_partida(partida: dict):
    vit_mand = vit_visi = derr_mand = derr_visi = 0
    emp_mand = emp_visi = 0

    if partida['gols_mandante'] > partida['gols_visitante']:
        vit_mand = 1
        derr_visi = 1
    elif partida['gols_mandante'] < partida['gols_visitante']:
        vit_visi = 1
        derr_mand = 1
    else:
        emp_mand = 1
        emp_visi = 1

    time_mand = atualiza_time(partida['mandante'], vit_mand, emp_mand, derr_mand)

    time_visi = atualiza_time(partida['visitante'], vit_visi, emp_visi, derr_visi)

    match = {
        "id_visitante": time_visi['id'],
        "gols_visitante": partida['gols_visitante'],
        "id_mandante": time_mand['id'],
        "gols_mandante": partida['gols_mandante']
    }

    bd.insert_partida(match)


def recupera_tabela():
    lista_tupla = bd.consulta_tudo()
    #converter a lista de tuplas para uma lista de dicionario,
    #onde dicionario representa um time
    #depois retorno essa lsita de dicionario
    resp = []

    for reg in lista_tupla:
        time = {
            "nome": reg[0],
            "vitorias": reg[1],
            "empates": reg[2],
            "derrotas": reg[3],
            "pontos": reg[4],
            "jogos": reg[5]
        }
        resp.append(time)

    return resp



p1 = {"mandante": "Palmeiras", "visitante": "Santos", 
        "gols_visitante": 1, "gols_mandante": 3}

#cadastra_partida(p1)

p2 = {"mandante": "Palmeiras", "visitante": "Corinthians", 
        "gols_visitante": 1, "gols_mandante": 1}
#cadastra_partida(p2)

p3 = {"mandante": "Santos", "visitante": "Corinthians", 
        "gols_visitante": 2, "gols_mandante": 1}
#cadastra_partida(p3)


tabela = recupera_tabela()
for linha in tabela:
    print(linha)

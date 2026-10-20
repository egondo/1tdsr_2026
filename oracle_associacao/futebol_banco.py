import oracledb

'''
select * from clube

select m.nome, p.gols_mandante, v.nome, p.gols_visitante 
      from partida p join clube m on p.id_mandante=m.id 
                     join clube v on p.id_visitante=v.id
                     
                     
select nome, vitorias, empates, derrotas, vitorias * 3 + empates as pontos, 
vitorias + empates + derrotas as jogos from clube order by pontos desc
'''

def consulta_tudo():
    sql = '''select nome, vitorias, empates, derrotas, vitorias * 3 + empates as pontos, vitorias + empates + derrotas as jogos from clube order by pontos desc'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    


def get_conexao():
    return oracledb.connect(user="pf0313", password= "professor#23", dsn="oracle.fiap.com.br/orcl")



def consulta_clube(nome: str):
    sql = "SELECT id, nome, vitorias, empates, derrotas FROM clube WHERE nome like :nome"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"nome": nome})
            reg = cur.fetchone()

    if reg:
        clube = {
            "id": reg[0], "nome": reg[1], "vitorias": reg[2],
            "empates": reg[3], "derrotas": reg[4]
        }
    else:
        clube = None
    return clube


def insert_clube(clube: dict):
    sql = "INSERT INTO clube(nome, vitorias, empates, derrotas) VALUES(:nome, :vitorias, :empates, :derrotas) returning id INTO :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            var = cur.var(oracledb.NUMBER)
            clube['id'] = var
            cur.execute(sql, clube)
            clube['id'] = var.getvalue()[0]
        con.commit()


def update_clube(clube: dict):
    sql = "UPDATE clube set nome=:nome, vitorias=:vitorias, empates=:empates, derrotas=:derrotas WHERE id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, clube)
        con.commit()

def insert_partida(partida: dict):
    sql = "INSERT INTO partida(gols_visitante, gols_mandante, id_visitante, id_mandante) VALUES(:gols_visitante, :gols_mandante, :id_visitante, :id_mandante)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()


if __name__ == "__main__":
    tabela = consulta_tudo()
    for linha in tabela:
        print(linha)
import oracledb


def get_conexao():
    return oracledb.conect(user="pf0313", password= "professor#23", dsn="oracle.fiap.com.br/orcl")



def consulta_clube(nome: str):
    sql = "SELECT id, descricao, vitias, empates. derrotas FROM clube WHERE descricao like :nome"
    with get_conexao() as con:
        with con.cursor() as cur:

            cur.execute(sql, {"nome": nome})
            reg = cur.fetchone()
        con.close()
    return reg


def insert_clube(clube: dict):
    sql = "INSERT INTO clube(nome, vitorias, empates, derrotas) clube WHERE descricao(:nome, :vitorias, :empates. :derrotas) returning id INTO :id
    with get_conexao() as con:
        with con.cursor() as cur:
            var = cur.var("oracledb.NUMBER")
            clube['id'] = var
            cur.execute(sql, {"nome": nome})
            reg = cur.fetchone()
        con.close()
    return reg


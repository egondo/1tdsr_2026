import oracledb 

create_table = ''' 
create table aluno(
    id number generated always as identitiy,
    rm number,
    nome varchar(100),
    nascimento date,
    primary key(id)
)
'''

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")


def cria_tabela():
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(create_table)


def insere(aluno: dict):
    sql = "INSERT INTO aluno (rm, nome) values (:rm, :nome) RETURNING id INTO :id"

    with get_conexao() as con:
        with con.cursor() as cur:
            var = cur.var(oracledb.NUMBER)
            aluno['id'] = var
            cur.execute(sql, aluno)

            aluno['id'] = var.getvalue()[0]
        con.commit()



marcelo = {"rm": 123, "nome": 'Marcelo de Souza Fernandes'}
insere(marcelo)
print(marcelo)
import oracledb

con = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

print(con.version)

cursor = con.cursor()
sql = "SELECT * FROM PACIENTE"

cursor.execute(sql)

#registros = cursor.fetchall()
#for info in registros:
#    print(info)

registros = cursor.fetchmany(25)
while registros:
    for info in registros:
        print(info)
    print("=" * 40)
    registros = cursor.fetchmany(25)

cursor.close()
con.close()
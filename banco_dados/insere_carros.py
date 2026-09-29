import oracledb

veiculos = [
    ("Toyota", "Corolla", 2022, "ABC-1234", 200.00),
    ("Honda", "Civic", 2021, "DEF-5678", 180.00),
    ("Volkswagen", "Gol", 2019, "GHI-9012", 100.00),
    ("Chevrolet", "Onix", 2023, "JKL-3456", 130.00),
    ("Ford", "Ranger", 2020, "MNO-7890", 350.00),
    ("Hyundai", "HB20", 2022, "PQR-1234", 100.00),
    ("Jeep", "Compass", 2023, "STU-5678", 280.00),
    ("Fiat", "Argo", 2021, "VWX-9012", 165.00),
    ("Renault", "Kwid", 2023, "YZA-3456", 80.00),
    ("Nissan", "Kicks", 2022, "BCD-7890", 170.00),
    ("Peugeot", "208", 2023, "EFG-1234", 120.00),
    ("BMW", "X1", 2021, "HIJ-5678", 500.00),
    ("Audi", "Q3", 2022, "KLM-9012", 600.00),
    ("Mercedes-Benz", "C200", 2020, "NOP-3456", 400.00),
    ("Caoa Chery", "Tiggo 5X", 2023, "QRS-7890", 200.00)
]

sql = "INSERT INTO TR_VEICULO(marca, modelo, ano, placa, valor) VALUES(:marca, :modelo, :ano, :placa, :valor)"

with oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl") as con:
    with con.cursor() as cur:
        for tupla in veiculos:
            v = {
                "marca": tupla[0],
                "modelo": tupla[1],
                "ano": tupla[2],
                "placa": tupla[3],
                "valor": tupla[4]
            }
            cur.execute(sql, v)
    con.commit()

print("Registros incluidos com sucesso!") 
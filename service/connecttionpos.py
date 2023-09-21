import psycopg2


def connectdb():
    # connection = psycopg2.connect(
    #     host='localhost',
    #     user='postgres',
    #     password='1234',
    #     database='sampledb',
    #     port=5432
    # )

    connection = psycopg2.connect(
        host='dpg-ck5snnj6fquc739cp7c0-a.singapore-postgres.render.com',
        user='admin',
        password='ivEhQfBtO0Ht35vb15CloAp9smmbz1dM',
        database='sampledb_q4m3',
        port=5432
    )
    return connection


connectdb()

print(connectdb())

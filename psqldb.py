import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from psycopg2 import sql

dataBase = psycopg2.connect(
    # dbname='postgres',
    user="postgres",
    password="1",
    host="127.0.0.1",
    port="5432"
    )

dataBase.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

cursorObject = dataBase.cursor()

cursorObject.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier("test_db"))
    )
print("All Done")
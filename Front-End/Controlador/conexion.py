import psycopg2
from psycopg2 import sql

'''# Configura la conexión a PostgreSQL
def obtener_conexion():
    return psycopg2.connect(
        dbname="LifeLine",
        user="postgres",
        password="a",
        host="localhost",
        port="5432"
    )'''

# Configura la conexión a PostgreSQL
def obtener_conexion():
    return psycopg2.connect(
        dbname="LifeLine",
        user="LifeLine_owner",
        password="7enERyAU5IXt",
        host="ep-orange-tooth-a5s3opz2.us-east-2.aws.neon.tech",
        port="5432"
    )
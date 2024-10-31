import psycopg2
from psycopg2 import sql

# Configura la conexión a PostgreSQL
def obtener_conexion():
    return psycopg2.connect(
        dbname="LifeLine",
        user="postgres",
        password="a",
        host="localhost",
        port="5432"
    )
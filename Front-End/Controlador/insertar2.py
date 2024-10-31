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
    
    
def crear_campana(nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario):
    conn = None
    
    try:
        conn = obtener_conexion()
        
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("""
                    INSERT INTO campañas (nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """),
                (nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario)
            )  
            conn.commit() 
            print("Campaña insertada exitosamente.")
    except Exception as e:
        print(f"Error al insertar la campaña: {e}")
    finally:
        if conn:
            conn.close()  
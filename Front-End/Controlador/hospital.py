from conexion import obtener_conexion
from psycopg2 import sql

def crear_hospital(nombre, direccion, contacto, horario, estado):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("INSERT INTO hospital (nombre, direccion, contacto, horario, estado) VALUES (%s, %s, %s, %s, %s)"),
                (nombre, direccion, contacto, horario, estado)
            )
            conn.commit()
        return True, "Hospital agregado con éxito."
    except Exception as e:
        print(f"Error al agregar hospital: {e}")
        return False, "Error al agregar hospital."
    finally:
        conn.close()




def obtener_hospitales():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT id, nombre, direccion, contacto, horario, estado FROM hospital"))
            hospitales = cur.fetchall()
            return hospitales
    
    except Exception as e:
        print(f"Error al obtener hospitales: {e}")
        return []
    
    finally:
        conn.close()




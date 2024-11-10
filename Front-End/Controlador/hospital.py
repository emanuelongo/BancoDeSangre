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

        return True, "Hospital agregado con éxito."  # Devolver una tupla en caso de éxito
        
    except Exception as e:
        print(f"Error al agregar hospital: {e}")
        return False, "Error al agregar hospital."  # También es una tupla en caso de error
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


def obtener_hospital_por_id(hospital_id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("SELECT nombre, direccion, contacto, horario, estado FROM hospital WHERE id = %s"),
                (hospital_id,)
            )
            hospital = cur.fetchone()  # Devuelve solo un resultado
            if hospital:
                # Retorna el hospital como un diccionario
                return {
                    "Nombre": hospital[0],
                    "Direccion": hospital[1],
                    "Contacto": hospital[2],
                    "Horario": hospital[3],
                    "Estado": hospital[4],
                }
    except Exception as e:
        print(f"Error al obtener hospital: {e}")
        return None
    finally:
        conn.close()








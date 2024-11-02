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

def actualizar_hospital(hospital_id, nombre, direccion, contacto, horario, estado):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("""
                UPDATE hospital
                SET nombre = %s, direccion = %s, contacto = %s, horario = %s, estado = %s
                WHERE id = %s
            """), (nombre, direccion, contacto, horario, estado, hospital_id))
            conn.commit()
            return True, "Hospital actualizado exitosamente."
    
    except Exception as e:
        print(f"Error al actualizar el hospital: {e}")
        return False, "Error al actualizar el hospital."

    finally:
        conn.close()

def obtener_hospital_por_id(hospital_id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT * FROM hospital WHERE id = %s"), (hospital_id,))
            return cur.fetchone()  # Devuelve todos los campos del hospital.
    
    except Exception as e:
        print(f"Error al obtener el hospital: {e}")
        return None
    
    finally:
        conn.close()




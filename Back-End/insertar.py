from conexion import obtener_conexion
from psycopg2 import sql

def insertar_usuario(tipo_usuario, nombre, tipo_documento, fecha_nacimiento, email, password):
    try:
        # Crea una conexión
        conn = obtener_conexion()
        with conn.cursor() as cur:
            # Inserta los datos en la tabla 'usuarios'
            cur.execute(
                sql.SQL("INSERT INTO usuarios (tipo_usuario, nombre, tipo_documento, fecha_nacimiento, email, password) VALUES (%s, %s, %s, %s, %s, %s)"),
                (tipo_usuario, nombre, tipo_documento, fecha_nacimiento, email, password)
            )
            conn.commit()
        return True, "Inserción exitosa"
    except Exception as e:
        # Si ocurre un error, revierte y captura el mensaje
        conn.rollback()
        print(f"Error en la inserción: {e}")
        return False, str(e)
    finally:
        conn.close()

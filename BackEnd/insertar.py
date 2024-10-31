from conexion import obtener_conexion
from psycopg2 import sql

def insertar_usuario(tipo_usuario, nombre, tipo_documento, numero_documento, fecha_nacimiento, email, password):
    try:
        # Crea una conexión
        conn = obtener_conexion()
        with conn.cursor() as cur:
            # Inserta los datos en la tabla 'usuarios'
            cur.execute(
                sql.SQL("INSERT INTO usuarios (tipo_usuario, nombre, tipo_documento, numero_documento, fecha_nacimiento, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
                (tipo_usuario, nombre, tipo_documento, numero_documento, fecha_nacimiento, email, password)
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

    
def crear_camapaña(nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario):
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
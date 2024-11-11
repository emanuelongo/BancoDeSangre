from conexion import obtener_conexion
from psycopg2 import sql

def crear_solicitud(tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional):
    try:
        print(f"Datos recibidos: {tipo_sangre}, {cantidad_sangre}, {numero_contacto}, {fecha_solicitud}, {hora_solicitud}, {direccion}, {informacion_adicional}")
        
        conn = obtener_conexion()
        if not conn:
            return False, "No se pudo conectar a la base de datos."
        
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("INSERT INTO solicitud (tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
                (tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional)
            )
            conn.commit()
        
        return True, "Solicitud agregada con éxito."  # Devolver una tupla en caso de éxito
        
    except Exception as e:
        print(f"Error al agregar la solicitud: {e}")
        return False, "Error al agregar la solicitud."  # También es una tupla en caso de error
    finally:
        conn.close()

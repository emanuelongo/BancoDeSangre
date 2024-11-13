from conexion import obtener_conexion
from psycopg2 import sql

def crear_solicitud(tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional):
    conn = None
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
            
        
        return True, "Solicitud agregada con éxito."
        
    except Exception as e:
        print(f"Error al agregar la solicitud: {e}")
        return False, f"Error al agregar la solicitud: {e}"
        
    finally:
        if conn:
            conn.close()

def obtener_solicitudes():
    try:
        conn = obtener_conexion()  
        with conn.cursor() as cur:
            cur.execute("""
                SELECT ID, tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional FROM solicitud
            """)
            solicitudes = cur.fetchall() 
            
            if solicitudes:
                for solicitud in solicitudes:
                    print(f"ID:{solicitud[0]}, tipo_sangre: {solicitud[1]}, cantidad_sangre: {solicitud[2]}, "
                          f"numero_contacto: {solicitud[3]}, fecha_solicitud: {solicitud[4]}, "
                          f"hora_solicitud: {solicitud[5]}, direccion: {solicitud[6]}, "
                          f"informacion_adicional: {solicitud[7]}")
            else:
                print("No se encontraron solicitudes.")
            
            return solicitudes
        
    except Exception as e:
        print(f"Error al obtener las solicitudes: {e}")
        return [], f"Error al obtener las solicitudes: {e}"
    
    finally:
        if conn:
            conn.close()

            
def obtener_solicitud(id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT * FROM campaña WHERE id = %s"), (id,))
            return cur.fetchone() 
    
    except Exception as e:
        print(f"Error al obtener el campaña: {e}")
        return None
    
    finally:
        conn.close()
        


def cancelar_solicitud(id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("DELETE FROM solicitud WHERE id = %s"), (id,))
            conn.commit() 
        print(f"solicitud con id {id} eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar la solicitud: {e}")
    finally:
        if conn:
            conn.close()
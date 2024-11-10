import psycopg2
from psycopg2 import sql

def obtener_conexion():
    return psycopg2.connect(
        dbname="LifeLine",
        user="postgres",
        password="a",
        host="localhost",
        port="5432"
    )
    
def crear_campana(nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario, Realizada=False):
    conn = None
    
    try:
        conn = obtener_conexion()
        
        with conn.cursor() as cur:
            cur.execute(
                sql.SQL("""
                    INSERT INTO campañas (nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario, Realizada)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """),
                (nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario, Realizada)
            )  
            conn.commit() 
            print("Campaña insertada exitosamente.")
            
    except Exception as e:
        print(f"Error al insertar la campaña: {e}")
    finally:
        if conn:
            conn.close()  

def obtener_campañas():
    try:
        conn = obtener_conexion()  
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario, Realizada
                FROM campañas
            """)
            campañas = cur.fetchall() 
            
            # Imprimir las campañas obtenidas en la consola
            if campañas:
                for campana in campañas:
                    print(f"ID: {campana[0]}, Nombre: {campana[1]}, Campaña: {campana[2]}, "
                          f"Donantes: {campana[3]}, Objetivo: {campana[4]}, Contacto: {campana[5]}, "
                          f"Fecha: {campana[6]}, Dirección: {campana[7]}, Horario: {campana[8]}, Reallizada:{campana[9]}")
            else:
                print("No se encontraron campañas.")
            
            return campañas

    except Exception as e:
        print(f"Error al obtener campañas: {e}")
        return []  

    finally:
        if conn:
            conn.close()  
            
            
def obtener_campaña(id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT * FROM campañas WHERE id = %s"), (id,))
            return cur.fetchone() 
    
    except Exception as e:
        print(f"Error al obtener el campaña: {e}")
        return None
    
    finally:
        conn.close()
        
from psycopg2 import sql

def eliminar_campaña(id):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("DELETE FROM campañas WHERE id = %s"), (id,))
            conn.commit() 
        print(f"Campaña con id {id} eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar la campaña: {e}")
    finally:
        if conn:
            conn.close()




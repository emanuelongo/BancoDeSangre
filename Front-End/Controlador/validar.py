from conexion import obtener_conexion
from psycopg2 import sql

def validar_usuario(email, password):
    try:
        # Crea una conexión a la base de datos
        conn = obtener_conexion()
        with conn.cursor() as cur:
            # Consulta el usuario por su correo electrónico
            cur.execute(
                sql.SQL("SELECT password FROM usuarios WHERE email = %s"),
                (email,)
            )
            resultado = cur.fetchone()
        
        # Si no se encontró el usuario
        if resultado is None:
            return False, "Usuario no encontrado." 
        
        # Compara la contraseña proporcionada con la almacenada en la base de datos
        if resultado[0] == password:
            return True, "Inicio de sesión exitoso."
        else:
            return False, "Contraseña incorrecta."
    
    except Exception as e:
        print(f"Error al validar el usuario: {e}")
        return False, "Error en la validación."
    
    finally:
        conn.close()

from conexion import obtener_conexion
from psycopg2 import sql

def validar_usuario(email, password):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cur:
            # Consulta el usuario por su correo electrónico y tipo de usuario
            cur.execute(
                sql.SQL("SELECT password, tipo_usuario FROM usuarios WHERE email = %s"),
                (email,)
            )
            resultado = cur.fetchone()
        
        # Si no se encontró el usuario
        if resultado is None:
            return False, "Usuario no encontrado.", None 
        if resultado[0] == password:
            tipo_usuario = resultado[1]  # Obtenemos el tipo de usuario
            return True, "Inicio de sesión exitoso.", tipo_usuario
        else:
            return False, "Contraseña incorrecta.", None
    
    except Exception as e:
        print(f"Error al validar el usuario: {e}")
        return False, "Error en la validación.", None
    
    finally:
        conn.close()

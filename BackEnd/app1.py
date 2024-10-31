from flask import Flask, request, render_template
from insertar import insertar_usuario

app = Flask(__name__, template_folder='../Front-End/templates', static_folder='../Front-End/static')


@app.route('/')
def index():
    # Carga el archivo HTML de registro
    return render_template('Registrarse.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # Recibe los datos del formulario
    tipo_usuario = request.form['tipo_usuario']
    nombre = request.form['nombre']
    tipo_documento = request.form['tipo_documento']
    numero_documento = request.form['numero_documento']
    fecha_nacimiento = request.form['fecha_nacimiento']
    email = request.form['email']
    password = request.form['password']
    
    # Llama a la función de inserción
    exito, mensaje = insertar_usuario(tipo_usuario, nombre, tipo_documento, numero_documento, fecha_nacimiento, email, password)
    
    # Devuelve mensaje de éxito o error
    if exito:
        return "¡Registro exitoso!"
    else:
        return f"Error en el registro: {mensaje}"
    


    
    
    

if __name__ == '__main__':
    app.run(debug=True)

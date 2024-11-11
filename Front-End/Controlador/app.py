from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from campaña import crear_campana
from campaña import obtener_campañas, obtener_campaña, eliminar_campaña
 
from insertar import insertar_usuario
from validar import validar_usuario
from hospital import crear_hospital, obtener_hospitales,  obtener_hospital_por_id

from solicitudes import crear_solicitud, obtener_solicitud
from datetime import datetime



app = Flask(__name__, static_folder='../static', template_folder="../templates")
app.secret_key = 'clave'



@app.route("/")
def inicio():
    return render_template("IniciarSesion.html")

@app.route("/inicioSesion", methods=["POST"])
def inicio_sesion():
    correo = request.form.get("correo")
    contraseña = request.form.get("contraseña")
    
    # Validar que se llenaron los campos 
    if not correo or not contraseña:
        flash("Faltan campos por completar", "error")
        return redirect(url_for("inicio"))
    
    # Verificar si el correo es del administrador
    if correo.lower() == "admin@lifeline.com" and contraseña == "123":
        return redirect(url_for("menu_admin"))  
    
    # Para otros usuarios
    exito, mensaje, tipo_usuario = validar_usuario(correo, contraseña)
    
    if exito:
        if tipo_usuario == "solicitante":
            # Redirigir a la página de menú solicitante
            return redirect(url_for("menu_solicitante"))
        else:
            # Redirigir a la página de menú usuario (o cualquier otra según sea el caso)
            return redirect(url_for("menu_usuario"))
    else:
        # Mostrar el mensaje de error
        flash(f"Error en el registro: {mensaje}", "error")
        return redirect(url_for("inicio"))

@app.route("/menu_admin")
def menu_admin():
    return render_template("MenuAdmi.html")

@app.route("/menu_solicitante")
def menu_solicitante():
    return render_template("MenuSolicitante.html")

num_hospital=0

#los hospitales se agregan en una lista hospitales
hospitales=[] 


hospital1 = {   
    "id": num_hospital,
    "Nombre": "Hospital General de Medellín",
    "Direccion": "Cra. 48 #32-102, La Candelaria, Medellin",
    "Contacto": "324 789 253",  
    "Horario": "24 horas",
    "Estado": "habilitado"
}

    
@app.route('/agregar_hospital', methods=["GET", "POST"])
def agregar_hospital_route():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        contacto = request.form.get('contacto')
        horario = request.form.get('horario')
        estado = request.form.get('estado')
        
        exito, mensaje = crear_hospital(nombre, direccion, contacto, horario, estado)
        
        if exito:
            flash(mensaje, "success")
        else:
            flash(mensaje, "error")
        
        return redirect(url_for("catalogo_hospitales"))
    
    return render_template("AgregarHospital.html")


@app.route('/agregar_hospital')
def agregar_hospital():
    return render_template("AgregarHospital.html")
 # Muestra el formulario de agregar hospital

@app.route('/catalogo_hospitales')
def catalogo_hospitales():
    hospitales = obtener_hospitales()  
    return render_template('CatalogoHospitales.html', hospitales=hospitales)

@app.route('/gestionar_hospitales')
def gestionar_hospitales():
    return render_template("GestionHospitales.html") 



@app.route('/hospital/<int:hospital_id>')
def ver_hospital(hospital_id):
    hospital = obtener_hospital_por_id(hospital_id)
    if hospital:
        return render_template("verhospital2.html", hospital=hospital)
    else:
        flash("El hospital no existe", "error")
        return redirect(url_for("catalogo_hospitales")) 



from flask import Flask, request, redirect, url_for, flash, render_template

@app.route('/agregar_solicitud', methods=["GET", "POST"])
def agregar_solicitud_route():
    if request.method == "POST":
        tipo_sangre = request.form.get('tipo_sangre')
        cantidad_sangre = request.form.get('cantidad_sangre')
        numero_contacto = request.form.get('numero_contacto')
        fecha_solicitud = request.form.get('fecha_solicitud')
        hora_solicitud = request.form.get('hora_solicitud')
        direccion = request.form.get('direccion')
        informacion_adicional = request.form.get('informacion_adicional')

        exito, mensaje = crear_solicitud(tipo_sangre, cantidad_sangre, numero_contacto, fecha_solicitud, hora_solicitud, direccion, informacion_adicional)
        
        if exito:
            flash(mensaje, "success")
        else:
            flash(mensaje, "error")
        
        return redirect(url_for("solicitud"))
    
    return render_template("AgregarSolicitudes.html")



@app.route('/agregar_solicitudes')
def agregar_solicitud():
    return render_template("AgregarSolicitudes.html")







@app.route('/solicitudes')
def solicitud():
    solicitudes = obtener_solicitud()

    # Convertir las solicitudes a una lista de diccionarios más legibles
    solicitudes_formateadas = []

    for solicitud in solicitudes:
        # Obtener la fecha y la hora
        fecha = solicitud[3]
        hora = solicitud[4]

        try:
            # Verificar si la fecha es un objeto datetime.date
            if isinstance(fecha, datetime.date):
                fecha = fecha.strftime('%Y-%m-%d')  # Convertir a string
            else:
                print(f"Error: La fecha no es un objeto datetime.date. Es {type(fecha)}")
                fecha = str(fecha)  # Convertir a string de seguridad

            # Verificar si la hora es un objeto datetime.time
            if isinstance(hora, datetime.time):
                hora = hora.strftime('%H:%M')  # Convertir a string
            else:
                print(f"Error: La hora no es un objeto datetime.time. Es {type(hora)}")
                hora = str(hora)  # Convertir a string de seguridad

        except Exception as e:
            print(f"Error al procesar fecha y hora: {e}")
            fecha = str(fecha)
            hora = str(hora)

        # Crear el diccionario con los datos procesados
        solicitud_dict = {
            'tipo_sangre': solicitud[0],
            'cantidad': str(solicitud[1]),  # Convertir Decimal a string
            'contacto': solicitud[2],
            'fecha': fecha,
            'hora': hora,
            'direccion': solicitud[5],
            'informacion_adicional': solicitud[6]
        }
        solicitudes_formateadas.append(solicitud_dict)

    print("Solicitudes formateadas:", solicitudes_formateadas)  # Verificar los datos antes de enviarlos

    return render_template('solicitudes.html', solicitudes=solicitudes_formateadas)










 









#ELIMINAR HOSPITAL
#---------------------------
@app.route('/eliminar_hospital', methods=["GET", "POST"])
def eliminar_hospital():
    return render_template("EliminarHospitales.html") 
#--------------------



















@app.route('/editar_hospital', methods=["GET", "POST"])
def editar_hospital():
    hospital_a_editar = None  
    
    #for hospital in hospitales:
        #print(f"intentando editar hospital con id: {hospital_id}") 

        #if hospital['id'] == hospital_id:
            #hospital_a_editar = hospital 
            
    #print(hospital_a_editar.nombre)
            
    #if hospital_a_editar is None:
        #return "Hospital no encontrado", 404 

    #if request.method == "POST":
        #hospital_a_editar["Nombre"]= request.form.get("nombre")
        #hospital_a_editar["Direccion"]= request.form.get("direccion")
        #hospital_a_editar["Contacto"]= request.form.get("contacto")
        #hospital_a_editar["Horario"]= request.form.get("horario")

    
    return render_template("EditarHospitales.html")#, hospital= hospital_a_editar ) 





@app.route('/ver_campañas', methods=["GET"])
def ver_campañas():
    campañas_activas=[]
    campañas = obtener_campañas()
    
    for campaña in campañas:
        if campaña[9] == False:
            campañas_activas.append(campaña)
    
    campañasRealizadas= []
    for campaña in campañas:
        if campaña[9]==True:
            campañasRealizadas.append(campaña)
    print(campañasRealizadas)
    
    return render_template("VerCampañas.html", campañas_activas= campañas_activas, campañasRealizadas= campañasRealizadas) 



@app.route('/gestionar_campañas', methods=["GET"])
def gestionar_campañas():
    campañas=[]
    totalcampañas = obtener_campañas()
    
    for campaña in totalcampañas:
        if campaña[9] == False:
            campañas.append(campaña)
    
    
    return render_template("GestionCampañas.html", campañas = campañas) 


from flask import request, redirect, url_for, render_template
@app.route('/eliminar_campañas/<int:id>', methods=['GET', 'POST'])
def eliminar_campañas(id):
    try:
        campaña = obtener_campaña(id)
        if campaña is None:
            return redirect(url_for('gestionar_campañas')) 
        
        if request.method == 'POST':
            eliminar_campaña(id)
            return redirect(url_for('gestionar_campañas')) 
        
        return render_template("EliminarCampañas.html", campaña=campaña)
    
    except Exception as e:
        print(f"Error al eliminar la campaña: {e}")
        flash("Hubo un error al eliminar la campaña.", "error")
        return redirect(url_for('gestionar_campañas'))



@app.route('/editar_campañas', methods=["GET"])
def editar_campañas():
    return render_template("EditarCampañas.html")

@app.route('/ver_disponibilidad', methods=["GET"])
def ver_disponibilidad():
    return render_template("Disponibilidad.html")

@app.route('/agregar_campaña', methods=["GET", "POST"])
def agregar_campaña():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        nombre_campaña = request.form.get('nombre_campaña')
        cantidad_donantes = request.form.get('cantidad_donantes')
        objetivo = request.form.get('objetivo')
        contacto = request.form.get('contacto')
        fecha = request.form.get('fecha')
        direccion = request.form.get('direccion')
        horario = request.form.get('horario')
        
        crear_campana(nombre, nombre_campaña, cantidad_donantes, objetivo, contacto, fecha, direccion, horario)
        
        
        return redirect(url_for('gestionar_campañas'))  
  
    return render_template("AgregarCampaña.html")

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
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
    else:
        # Si es GET, muestra el formulario de registro
        return render_template('Registrarse.html')



if __name__ == "__main__":
    app.run(debug=True)

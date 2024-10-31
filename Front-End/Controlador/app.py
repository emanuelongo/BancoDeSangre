from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from insertar2 import crear_campana  


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
    

    if correo== "admin@lifeline.com" and contraseña== "123":
        return redirect(url_for("menu_admin"))
    
    else:
        flash("Correo o contraseña incorrectos", "error")
        return redirect(url_for("inicio"))
    
    

@app.route('/menu_admin')
def menu_admin():
    return render_template("MenuAdmi.html")

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

    
hospitales.append(hospital1)


@app.route('/agregar_hospital', methods=["GET", "POST"])
def agregar_hospital():
    global num_hospital
    
        
    if request.method == "POST": #cuando se pulsa el boton de agregar hospital
        
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        contacto = request.form.get('contacto')
        horario = request.form.get('horario')
        estado = request.form.get('estado')
        
        
        nuevo_hospital={
            "id": num_hospital, "Nombre": nombre, "Direccion": direccion, "Contacto": contacto, "Horario": horario, "Estado": estado
        }
        hospitales.append(nuevo_hospital)
        num_hospital += 1
        
        
        
        print(hospitales)  
    return render_template("AgregarHospital.html") 


@app.route('/ver_hospital2/<int:hospital_id>', methods=["GET"])
def ver_hospital2(hospital_id):
    # Buscar el hospital correspondiente por id
    hospital_encontrado = None  
    for hospital in hospitales:
        if hospital['id'] == hospital_id:
            hospital_encontrado = hospital  

    if hospital_encontrado is None:
        return "Hospital no encontrado", 404  

    return render_template("verhospital2.html", hospital=hospital_encontrado)


@app.route('/ver_hospital', methods=["GET"])
def ver_hospital():
    return render_template("VerHospital.html")


@app.route('/gestionar_hospitales', methods=["GET", "POST"])
def gestionar_hospitales():
    return render_template("GestionHospitales.html", hospitales =  hospitales) 


@app.route('/catalogo_hospitales', methods=["GET"])
def catalogo_hospitales():
    return render_template("CatalogoHospitales.html", hospitales= hospitales)


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


@app.route('/eliminar_hospital', methods=["GET", "POST"])
def eliminar_hospital():
    return render_template("EliminarHospitales.html") 

@app.route('/ver_campañas', methods=["GET"])
def ver_campañas():
    return render_template("VerCampañas.html") 



@app.route('/gestionar_campañas', methods=["GET"])
def gestionar_campañas():
    return render_template("GestionCampañas.html") 


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

if __name__ == "__main__":
    app.run(debug=True)

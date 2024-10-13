from flask import Flask, render_template, request, redirect, url_for, flash


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


@app.route('/catalogo_hospitales', methods=["GET"])
def catalogo_hospitales():
    return render_template("CatalogoHospitales.html")


@app.route('/ver_hospital', methods=["GET"])
def ver_hospital():
    return render_template("VerHospital.html") 

@app.route('/gestionar_hospitales', methods=["GET", "POST"])
def gestionar_hospitales():
    return render_template("GestionHospitales.html") 


@app.route('/ver_campañas', methods=["GET"])
def ver_campañas():
    return render_template("VerCampañas.html") 


#los hospitales se agregan en una lista hospitales
hospitales=[] 
@app.route('/agregar_hospital', methods=["GET", "POST"])
def agregar_hospital():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        contacto = request.form.get('contacto')
        horario = request.form.get('horario')
        estado = request.form.get('estado')
        
        
        nuevo_hodpital={
            "Nombre": nombre, "Direccion": direccion, "Contacto": contacto, "Horario": horario, "Estado": estado
        }
        
        hospitales.append(nuevo_hodpital)
        print(hospitales) #para probar que si se estan guardando
            
        
    return render_template("AgregarHospital.html") 





if __name__ == "__main__":
    app.run(debug=True)

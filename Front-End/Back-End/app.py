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


@app.route('/catalogo_hospitales', methods=['GET'])
def catalogo_hospitales():
    return render_template("CatalogoHospitales.html")


@app.route('/ver_hospital', methods=['GET'])
def ver_hospital():
    return render_template("VerHospital.html") 




if __name__ == "__main__":
    app.run(debug=True)

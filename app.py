from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from cs50 import SQL
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure applicatio
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///GreenHome.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        address = request.form["address"]
        phone = request.form["phone"]
        password = request.form["password"]
        confirmation_password = request.form["confirmation_password"]

        # Ensure field was submitted
        if not name or name == "":
            return jsonify({"error" : "Ingrese un nombre válido"})

        # Ensure field was submitted
        if not email or email == "":
            return jsonify({"error" : "Ingrese un email válido"})

        # Ensure field was submitted
        if not city or city == "":
            return jsonify({"error" : "Ingrese una ciudad válida"})

        # Ensure field was submitted
        if not address or address == "":
            return jsonify({"error" : "Ingrese una dirección válida"})

        # Ensure field was submitted
        if not phone or phone == "":
            return jsonify({"error" : "Ingrese un teléfono válido"})

        # Ensure field was submitted
        if not password or password == "":
            return jsonify({"error" : "Ingrese una contraseña válida"})

        # Ensure field was submitted
        if not confirmation_password or confirmation_password == "":
            return jsonify({"error" : "Ingrese su confirmación de contraseña"})

        # both passwords must be equal
        if password != confirmation_password:
            return jsonify({"error" : "Las contraseñas no coinciden"})

        # Hash password
        password_hash = generate_password_hash(password)

        try:
            new_user = db.execute('''
            INSERT INTO Registros(email, contrasena) VALUES(?, ?)
            ''', email, password_hash)
            print(new_user)
            db.execute('''
                INSERT INTO Usuarios(nombre_completo, telefono, id_registro, domicilio, codigo_ciudad)
            ''', name, phone, new_user, address, 1)
        except:
            return jsonify({"error" : "Este usuario ya existe en la plataforma."})

        # try:
        #     register_id = db.execute('''
        #     SELECT MAX(id_registro) FROM Registros
        #     ''')
        #     print("ultimo id: "+ register_id)
        # except:
        #     print('nel, esta malo')

        session['user_id'] = new_user

        # register = db.execute('''
        #     SELECT MAX(id_registro) FROM Registros
        # ''')
        return redirect("/")






@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/properties")
def properties():
    return render_template("properties.html")



@app.route("/enter_propertie")
def enter_propertie():
    return render_template("enter_propertie.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")






@app.route("/log_in", methods=["POST", "GET"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        email_s = request.form["email_s"]
        password_s = request.form["password_s"]

        if not email_s or email_s == "":
            return jsonify({"error" : "Ingrese un email válido"})
        
        if not password_s or password_s == "":
            return jsonify({"error" : "Ingrese una contraseña válida"})
    else:
        return render_template("log_in.html")

from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from cs50 import SQL

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
        country = request.form["country"]
        address = request.form["address"]
        phone = request.form["phone"]
        password = request.form["password"]

        if not name or name == "":
            return jsonify({"error" : "Ingrese un nombre"})

        if not email or email == "":
            print("Ingresar dato válido")

        if not country or country == "":
            print("Ingresar dato válido")

        if not address or address == "":
            print("Ingresar dato válido")

        if not phone or phone == "":
            print("Ingresar dato válido")

        if not password or password == "":
            print("Ingresar dato válido")


        try:
            new_user = db.execute('''
            INSERT INTO Registros(email, contrasena) VALUES(?, ?)
            ''', email, password)
            db.execute('''
                INSERT INTO Usuarios(nombre_completo, telefono, id_registro, domicilio, ciudad, codigo_pais)
            ''')
        except:
            print('Algo ha salido mal')

        try:
            register_id = db.execute('''
            SELECT MAX(id_registro) FROM Registros
            ''')
            print("ultimo id: "+ register_id)
        except:
            print('nel, esta malo')

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

@app.route("/log_in")
def log_in():
    return render_template("log_in.html")


@app.route("/enter_propertie")
def enter_propertie():
    return render_template("enter_propertie.html")

    
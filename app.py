from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for
from flask_session import Session
from cs50 import SQL
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import cloudinary
import cloudinary.uploader


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///GreenHome.db")

# Cloudinary for image storage
cloudinary.config( 
  cloud_name = "dfiqsvrpz", 
  api_key = "644192579483865", 
  api_secret = "6OVj6KW2_5qgzDdM6n6BzJChM8o" 
)

# Validation about user login.
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/log_in")
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route("/")
def index():
    properties = db.execute('''
        SELECT Propiedades.*, Tipo_Inmueble.descripcion AS tipoinmueble, t.descripcion AS tipotransaccion, Ciudad.nombre AS ciudad FROM Propiedades
        INNER JOIN Tipo_Inmueble ON Tipo_Inmueble.codigo_tipo = Propiedades.tipo_inmueble
        INNER JOIN Tipo_Transaccion AS t ON t.codigo_transaccion =  Propiedades.tipo_transaccion
        INNER JOIN Ciudad ON Ciudad.codigo_ciudad =  Propiedades.codigo_ciudad
        ORDER BY codigo_propiedad DESC LIMIT 6 
    ''')
    return render_template("index.html", properties = properties)

@app.route("/register", methods=["GET","POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = int(request.form["city"])
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

        # New user in the app
        new_user = db.execute('''
        INSERT INTO Registros(email, contrasena) VALUES(?, ?)
        ''', email, password_hash)
        
        db.execute('''
            INSERT INTO Usuarios(nombre_completo, telefono, id_registro, domicilio, codigo_ciudad) VALUES (?, ?, ?, ?, ?)
        ''', name, phone, new_user, address, city)

        # Redirect user to the Payment Plans
        session['user_id'] = new_user

        return jsonify({"correct" : "Proceso de registro ejecutado con éxito."})
    else:
        return render_template("log_in.html")

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

        rows = db.execute('''
            SELECT * FROM Registros WHERE email = ?
        ''', email_s)

        if len(rows) != 1 or not check_password_hash(rows[0]["contrasena"], password_s):
            return jsonify({"error" : "Nombre usuario y/o contraseña inválida"})

        # Remember which user has logged in
        session["user_id"] = rows[0]["id_registro"]

        flash("🏡🏡Bienvenido a Green Home Real State, sientete como en casa.🏡🏡")
        # Redirect user to home page
        return jsonify({"correct" : "Proceso de login ejecutado con éxito."})
    else:
        cities = db.execute('''
            SELECT * FROM Ciudad
        ''')
        return render_template("log_in.html", cities = cities)

@app.route("/payment", methods=["POST", "GET"])
@login_required
def payment():
    if request.method == "POST":
        plan = request.form.get("plan")

        if plan:
            db.execute('''
                INSERT INTO Usuarios_Suscripcion (id_registro, id_suscripcion) VALUES (?, ?)
            ''', session['user_id'], plan)

        flash("🏡🏡Bienvenido a Green Home Real State, sientete como en casa.🏡🏡")
        return redirect(url_for('index'))
    else:
        plans = db.execute('''
            SELECT * FROM Suscripcion
        ''')
        return render_template("payment.html", plans = plans)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for('index'))

@app.route("/properties")
@login_required
def properties():
    props = db.execute('''
        SELECT Propiedades.*, Tipo_Inmueble.descripcion AS tipoinmueble, t.descripcion AS tipotransaccion, Ciudad.nombre AS ciudad FROM Propiedades
        INNER JOIN Tipo_Inmueble ON Tipo_Inmueble.codigo_tipo = Propiedades.tipo_inmueble
        INNER JOIN Tipo_Transaccion AS t ON t.codigo_transaccion =  Propiedades.tipo_transaccion
        INNER JOIN Ciudad ON Ciudad.codigo_ciudad =  Propiedades.codigo_ciudad
        ORDER BY codigo_propiedad DESC 
    ''')
    props_type = db.execute('''
        SELECT * FROM Tipo_Inmueble
    ''')
    props_type1 = db.execute('''
        SELECT * FROM Tipo_Transaccion
    ''')
    print(props)
    return render_template("properties.html", props = props, props_type = props_type, props_type1 = props_type1)

@app.route("/enter_propertie", methods=["GET", "POST"])
@login_required
def enter_propertie():
    if request.method == "POST":
        
        inmueble = int(request.form.get("inmueble"))
        address = request.form.get("address")
        city = int(request.form.get("city"))
        phone = request.form.get("phone")
        price = request.form.get("price")
        moneda = request.form.get("moneda")
        images = request.files["images"]
        
        description = request.form.get("description")
        tipo_transaccion = int(request.form.get("tipo_transaccion"))
        img_db = cloudinary.uploader.upload(images)
        # print("---------------------------")
        # print(a)
        susc = db.execute('''
        SELECT id_usuario_suscripcion from Usuarios_Suscripcion where id_registro = :id''', 
        id=session['user_id'])[0]["id_usuario_suscripcion"]
        db.execute('''
            INSERT INTO Propiedades (direccion, precio, moneda, codigo_ciudad, tipo_inmueble, codigo_usuario_suscripcion, estado, imagen, descripcion, tipo_transaccion) VALUES (?, ?, ?, ?, ?, ?, 0, ?, ?, ?)
        ''', address, price, moneda, city, inmueble, susc, img_db["url"], description, tipo_transaccion)
        
        return redirect(url_for('index'))
    else:
        tipo_inmueble = db.execute('''
            SELECT * FROM Tipo_Inmueble
        ''')
        cities = db.execute('''
            SELECT * FROM Ciudad
        ''')
        tipo_trans = db.execute('''
            SELECT * FROM Tipo_Transaccion
        ''')

        return render_template("enter_propertie.html", tipo_inmueble = tipo_inmueble, cities = cities, tipo_trans = tipo_trans)

@app.route("/propertie_info/<int:codigo_propiedad>")
@login_required
def propertie_info(codigo_propiedad):
    prop_info = db.execute('''
        SELECT Propiedades.*, Tipo_Inmueble.descripcion AS tipoinmueble, t.descripcion AS tipotransaccion, Ciudad.nombre AS ciudad, Usuarios.*, r.* FROM Propiedades
        INNER JOIN Tipo_Inmueble ON Tipo_Inmueble.codigo_tipo = Propiedades.tipo_inmueble
        INNER JOIN Tipo_Transaccion AS t ON t.codigo_transaccion =  Propiedades.tipo_transaccion
        INNER JOIN Ciudad ON Ciudad.codigo_ciudad =  Propiedades.codigo_ciudad
        INNER JOIN Usuarios_Suscripcion AS u ON u.id_usuario_suscripcion = Propiedades.codigo_usuario_suscripcion
        INNER JOIN Usuarios ON u.id_usuario_suscripcion = Usuarios.codigo_usuario
        INNER JOIN Registros AS r ON r.id_registro = Usuarios.codigo_usuario
        WHERE Propiedades.codigo_propiedad = ?
    ''', codigo_propiedad)
    print(prop_info)
    return render_template("propertie_info.html", prop_info = prop_info)

@app.route("/profile")
@login_required
def profile():
    data_first = db.execute('''
        SELECT * FROM Usuarios WHERE codigo_usuario = ?
    ''', session["user_id"])
    data_second = db.execute('''
        SELECT * FROM Registros WHERE id_registro = ?
    ''', session["user_id"])
    data_third = db.execute('''
        SELECT nombre FROM Ciudad WHERE codigo_ciudad = ?
    ''', data_first[0]["codigo_ciudad"])
    data_props = db.execute('''
        SELECT COUNT(codigo_usuario_suscripcion) FROM Propiedades WHERE codigo_usuario_suscripcion = ?
    ''', session["user_id"])
    print(data_third)
    print(data_props)
    return render_template("profile.html", data_first = data_first, data_second = data_second, data_third = data_third, data_props = data_props)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html")
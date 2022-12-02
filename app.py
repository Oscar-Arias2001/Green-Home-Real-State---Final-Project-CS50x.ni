from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")

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

    
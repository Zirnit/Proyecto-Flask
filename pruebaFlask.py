from flask import Flask, request, url_for, redirect, abort, render_template
from mysqlpass import midb

cursor = midb.cursor(dictionary=True)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/post/<post_id>", methods=["GET", "POST"])
def lala(post_id):
    if request.method == "GET":
        return "El ID de este post es: " + post_id
    else:
        return "Este es otro método y no GET"

@app.route("/lele")
def lele():
    cursor.execute("select * from Usuario")
    usuarios = cursor.fetchall()
    # return redirect(url_for("lala", post_id=2))
    return render_template("lele.html", usuarios=usuarios)

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html', mensaje="Hola Mundo")

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for("lele"))
    return render_template("crear.html")

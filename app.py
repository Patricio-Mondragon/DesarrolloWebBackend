
import email
from http import client
from sqlite3 import dbapi2
from textwrap import indent
from urllib import request
from flask import Flask, render_template, request, session, redirect, url_for
import datetime
import pymongo

# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "Super secret key"
#############################################################

# MOngo db
#############################################################
mongodb_key = "mongodb+srv://DesarrolloWebUser:desarrollowebpassword@cluster0.siii8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongodb_key, tls = True, tlsAllowInvalidCertificates=True)
db = client.Escuela
cuentas = db.Alumno
#############################################################

#cursor = cuentas.find({})
#for doc in cursor:
    #print(doc)


@app.route('/')
def home():
    email = None
    if "email" in session:
        email = session["email"]
        return render_template('index.html', data = email)
    else : 
        return render_template('Login.html', data = email)




@app.route("/login", methods = ["GET"])
def login():
    email = None
    password = None
    if email in session:
        email = session['email']
        return render_template("index.html", data= session["email"])
    
    return render_template("Login.html", data = "email")


@app.route("/login", methods = ["POST"])
def login2Index():
    email = ""
    if email in session:
        return render_template("index.html", data= session["email"])
    
    email = request.form['email']
    password = request.form['password']
    session['email'] = email
    session['password'] = password

    return render_template("index.html", data = email)
 
@app.route('/logout')
def logout():
    if 'email' in session:
        email = session['email']
    session.clear()
    return redirect(url_for('home'))



@app.route("/singUp")
def singup():
    email = ""
    if "email" in session:
        return render_template("index.html", data = email)
    else: 
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        session['email'] = email
        session['password'] = password
        session['name'] = name
    return render_template("index.html" , data = email)



@app.route('/usuarios')
def usuarios():
    cursor = cuentas.find({})
    users = []
    for doc in cursor:
        users. append(doc)
    return render_template('usuarios.html', data = users)




@app.route('/prueba', methods=["GET"])
def prueba():
    nombres = []
    nombres.append({"nombre": "ruben",

    "Semestre01":[{
        "matematicas":"10",
        "español":"5"
        }],
    "Semestre02":[{
        "matematicas":"10",
        "español":"5"
        }]
        })

    nombres.append({"nombre": "sergio",

    "Semestre021":[{"matematicas":"8",
    "español":"6"
    }],
    "Semestre02":[{
        "matematicas":"4",
        "español":"9"
    }]
    })

    return render_template("home.html", data = nombres)


    

from datetime import date, datetime
import email
import re
from textwrap import indent
from urllib import request
from flask import Flask, render_template, request, session
import datetime

# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "Super secret key"
#############################################################

@app.route('/')
def home():
    email = None
    if "email" in session:
        email = session["email"]
        return render_template('index.html', data = email)
    else : 
        return render_template('Login.html', data = email)


@app.route("/singUp")
def singup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    return render_template("")


@app.route("/login", methods = ["GET", "POST"])
def login():
    email = None
    password = None
    if email in session:
        return render_template("index.html", data= session["email"])
    else: 
        if (request.method == "GET"):
            return render_template("Login.html", data = "email")
        else:
            email = request.form["email"]
            password = request.form["password"]
            session["email"] = email
            return render_template("index.html", data = email)



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

    

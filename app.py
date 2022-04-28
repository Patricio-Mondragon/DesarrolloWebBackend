import email
from urllib import request
from flask import Flask, render_template, request

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("Login.html", error = email)


@app.route("/loginuser", methods = ["POST"])
def loginuser():
    email = request.form["email"]
    password = request.form["password"]
    return render_template("index.html", error = email)

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

    

from flask import Flask, render_template

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prueba')
def prueba():
    return "Esta es una pagina prueba"


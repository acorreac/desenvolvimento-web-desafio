from fileinput import filename
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem-somos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
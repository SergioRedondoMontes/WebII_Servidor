from flask import Flask,render_template, current_app, g , request,  make_response, redirect, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola desde Flask"


@app.route('/<name>')
def nombre(name):
    return ("""
    <html>
        <head>
            <meta charset="utf-8">
            <title> Prog. Web Servidor </title>
        </head>
        <body>
            <h1> Curso de Programación Web Servidor  </h1>	
            <p> mi nombre es: {}</p>
        </body>
    </html>
    """).format(name)


@app.route('/ejemplo_css')
def ejemplo_css():
    resultado = render_template("ejemplo_css.html")
    print(resultado)
    return resultado

@app.route('/variables')
def variables():
    print('current_app.name = ', current_app.name)
    print("g = ", g)
    print("request = ", request)
    print("request.method = ", request.method)
    print("request.form = ", request.form)
    print("request.args = ", request.args)
    print("request.remote_addr = ", request.remote_addr)
    print("request.url = ", request.url)
    print("request.base_url = ", request.base_url)
    print("request.query_string = ", request.query_string)
    print("request.environ = ", request.environ)
    print("request.path = ", request.path)
    print("request.host = ", request.host)
    return ("Ok - variables")

import random
@app.route('/setCookie')
def setCookie():
    respuesta = make_response('<h1>Este doc contiene cookies</h1>')
    respuesta.set_cookie('id_usuario',str(int(random.random()*5000)))
    respuesta.set_cookie('color_ojos','verdes')
    return respuesta

@app.route('/redirect')
def redireccion():
    return redirect('https://google.es')

BLACK_LIST_IPS = {'127.0.0.1':1}
@app.route('/funcioncualquiera')
def funcioncualquiera():
    if request.remote_addr in BLACK_LIST_IPS:
        abort(404, 'NO TIENES ACCESO')
    return redirect('https://google.es')
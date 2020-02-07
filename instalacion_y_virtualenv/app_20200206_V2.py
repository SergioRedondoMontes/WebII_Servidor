# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    #AQUI YO DESCUBRI LA FORMULA DE LA COCA-COLA
    return('Hola Mundo - Flasky')

def hello_la_mejor_del_mundo():
    #AQUI YO DESCUBRI LA FORMULA DE LA COCA-COLA
    return('Hola Mundo - No Flasky')

app.add_url_rule('/noflask','noflask',hello_la_mejor_del_mundo)


@app.route('/nombre/<name>')
def nombre(name):
    return('Hola '+name)

@app.route('/cubode/<X>')
def cubode(X):
    try:
        X_cubo = int(X)**3
    except:
        return('Solo numeros!')        
    X_cubo_str = str(X_cubo)
    return('El cubo de '+ X +' es '+X_cubo_str)


@app.route('/cubodeV2/<int:X>')
def cubodeV2(X):
    return('El cubo de '+ str(X) +' es '+str(X**3))

@app.route('/tipos/<int:I>/<float:X>/<string:A>/<path:P>')
def tipos(I,X,A,P):
    print(I,type(I))
    print(X,type(X))
    print(A,type(A))
    print(P,type(P))
    return('tipos - OK')


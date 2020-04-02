# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:29:32 2020

@author: manoel.alonso
"""

from flask import Flask, render_template, request

app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('./database/company_balancesheet_database.db')

import pandas as pd

df = pd.read_sql("""
 SELECT *
    FROM cuentas_anuales
""", conn)

df.drop('id', inplace=True, axis=1)
df.columns = ['NIF', 'Nombre', 'CNAE',
              'Total Activos - 2017', 'Total Activos - 2016',
              'Total Activos - 2015', 'Recursos Propros - 2017', 'Recursos Propros - 2016',
              'Recursos Propros - 2015', 'Deuda a Corto - 2017',
              'Deuda a Corto - 2016', 'Deuda a Corto - 2015',
              'Deuda a Largo - 2017', 'Deuda a Largo - 2016',
              'Deuda a Largo - 2015', 'Ingresos - 2017',
              'Ingresos - 2016', 'Ingresos - 2015',
              'Amortizacion - 2017', 'Amortizacion - 2014',
              'Amortizacion - 2015', 'Beneficio - 2017', 'Beneficio - 2016',
              'Beneficio - 2015', 'Estado']


@app.route('/')
def index():
    return render_template("index.html")


pd.set_option('display.float_format', lambda x: '%.f' % x)


@app.route('/buscador', methods=["GET"])
def buscador():
    if request.method == "GET":
        if 'nif' not in request.args:
            return "GET mal formulado - ejemplo: /buscador?nif=A48010615&JSON=yes"
        data = df[df['NIF'] == request.args['nif']]
        if len(data) == 0:
            return render_template("index.html", df=df, ids=list(range(len(df))))
        if 'JSON' in request.full_path and request.args['JSON'] == 'yes':
            return data.to_json()
        else:
            data = data.T.to_html().replace('''<tr style="text-align: right;">''', '''<tr class="table-row">''')
            return render_template("index.html", df=df, ids=range(len(df)), data=data, result='1')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()

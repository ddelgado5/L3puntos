from flask import Flask, request

import sys

from flask.wrappers import Request
sys.path.append("..")  #subir de nivel en el path
from logica.servicios import *

#instancia de la clase Flask
app = Flask(__name__)

#rutas http para acceder desde un navegador web
@app.route('/')
def inicio():
    
    return '<B> Aplicación Web </B> con Python y Flask'

@app.route('/saludo/<nombre>')
def saludar(nombre):
    texto = f'''
    Hola <b>{nombre}</b>, Sea Bienvenido 
    '''
    return texto
    
@app.route('/saludo2/<nombre>,<deseo>')
def saludar2(nombre, deseo):
    texto = f'''
    Hola <b>{nombre}</b>, Sea Bienvenido <br>
    Mi deber es realizar tu deseo: <i>{deseo}</it> 
    '''
    return texto

@app.route('/calculardoble/<int:numero>')
def calcularDoble(numero):
    valorDoble = numero*2
    return f'El doble de {numero} es {valorDoble}!!!!'

@app.route('/calculardoble/<float:numero>')
def calcularDoble2(numero):
    valorDoble = numero*2
    return f'El doble de {numero} es {valorDoble}!!!!'

@app.route('/calculardoble/<string:numero>')
def calcularDobleString(numero):
    valorDoble = numero*2
    return f'El doble de {numero} es {valorDoble}!!!!'

@app.route('/argumentos/<string:parametros>')
def funcion_argumentos(parametros):
    texto1 = request.args.get('campo1','')
    texto2 = request.args.get('campo2','')
    texto3 = request.args.get('campo3','')

    texto = f'''
        Los argumentos que se toman son:<br>
        <ol start='1'>
            <li>campo 1: <b>{texto1}</b> </li>
            <li>campo 2: <b>{texto2}</b> </li>
            <li>campo 3: <b>{texto3}</b> </li>
        </ol> <br>
        Fin de la lista.
    '''
    return texto



#endpoint
@app.route('/crear/<basedatos>,<tipo>')
def inicioCrear(basedatos, tipo):
    #crearEstructura('../bd/jedi_API', 'domicilio')
    crearEstructura(basedatos, tipo)
    return '<B>Base de datos creada </B> con Python y Flask'

if __name__ == '__main__':
    app.run(debug=True)
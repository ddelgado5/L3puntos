import sys
sys.path.append("..")  #subir de nivel en el path
from logica.servicios import *

def inicio():
    crearEstructura('../bd/jedi_aplicacion', 'domicilio')


if __name__ == '__main__':
    inicio()


listaEstructuras = {}
listaEstructuras['mascota']='''
        CREATE TABLE IF NOT EXISTS mascota (
            nombre      TEXT NOT NULL,
            tipo        TEXT NOT NULL,
            edad        INTEGER,
            responsable TEXT,
            colorpelaje TEXT);
        '''
listaEstructuras['domicilio']='''
        CREATE TABLE IF NOT EXISTS domicilio (
            nombre      TEXT NOT NULL,
            tipo        TEXT NOT NULL,
            edad        INTEGER,
            responsable TEXT,
            colorpelaje TEXT);
        '''

listaComandos = {}
listaComandos['insertarMascota'] = ''' 
        INSERT INTO mascota(nombre, tipo, edad, responsable, colorpelaje)
        VALUES (?,?,?,?,?) '''
listaComandos['seleccionarMascota'] = '''  
        SELECT * FROM mascota  '''  

import sys
sys.path.append("..")  #subir de nivel en el path
from datos.dataclass import *

def crearEstructura(basedatos, tipo):
    miDB = SQL(basedatos)
    miDB.crearEstuctura(listaEstructuras[tipo])
    miDB.cerrarConexion()

def crearEstructuraMascota(basedatos):
    miDB = SQL(basedatos)
    miDB.crearEstuctura(listaEstructuras['mascota'])
    miDB.cerrarConexion()

def inscribirMascota(basedatos):
    miDB = SQL(basedatos)
    miDB.ejecutar_dml(listaComandos['insertarMascota'], valores)
    miDB.cerrarConexion()

def buscarMascota(basedatos, criterio, operador, valor):
    miDB = SQL(basedatos)
    comando = listaComandos['seleccionarMascota']
    comandoCompleto = f'{comando} WHERE {criterio} {operador} ?'
    data = miDB.ejecutar_dml(comandoCompleto, valor)
    miDB.cerrarConexion()
    return data

def listarMascotas(basedatos):
    miDB = SQL(basedatos)
    comando = listaComandos['seleccionarMascota']
    data = miDB.ejecutar_dml(comando)
    miDB.cerrarConexion()
    return data
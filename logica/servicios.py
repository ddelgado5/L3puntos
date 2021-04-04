

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

_DATABASE = "puntos"
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


def insertarPersona(nombre: str, documento: str, puntos: float, admin:int):
    '''
        metodo para insertar usuario
    '''
    miDB = SQL(_DATABASE)
    comando = ''' 
        INSERT INTO personas(nombre, documento, puntos, admin)
        VALUES (?,?,?,?)
    '''
    x = miDB.ejecutar_dml(comando,[nombre, documento, puntos, admin])
    print("se inserto desde el servicio --- " + x)
    miDB.cerrarConexion()

def insertarProducto(nombre:str, precio:float, puntos:float):
    '''
        metodo par insertar producto
    '''
    miDB = SQL(_DATABASE)
    comando = ''' 
        INSERT INTO productos(nombre, precio, puntos)
        VALUES (?,?,?)
    '''
    x = miDB.ejecutar_dml(comando,[nombre, precio, puntos])
    print("se inserto * PRODUCTO * desde el servicio --- " + x)

    miDB.cerrarConexion()

def buscarUsuarioByDocumento(documento):
    miDB = SQL(_DATABASE)
    comando = f'SELECTBYANY * FROM personas'
    com = f'{comando} WHERE documento = ?'
    user = miDB.ejecutar_dml(com, documento)
    miDB.cerrarConexion()
    return user
    

def getProducts():
    miDB = SQL(_DATABASE)
    comando = f'SELECT * FROM productos'
    producto = miDB.ejecutar_dml(comando)
    miDB.cerrarConexion()
    return producto

def findProductById(idProd):
    miDB = SQL(_DATABASE)
    comando = 'SELECTBYID * FROM productos'
    com = f'{comando} WHERE id = ?'
    producto = miDB.ejecutar_dml(com, idProd)
    miDB.cerrarConexion()
    return producto

def actualizarPersona(user):
    miDB = SQL(_DATABASE)
    comando = f'UPDATE personas SET puntos = ?'
    com = f'{comando} WHERE documento = ?'
    persona = miDB.ejecutar_dml(com, [user[3], user[2]])
    miDB.cerrarConexion()
    return persona

    
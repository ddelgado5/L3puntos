import sys
sys.path.append("..")  #subir de nivel en el path
from datos.dataclass import *

_DATABASE = "puntos"

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
    

def getProducts(params = None):
    miDB = SQL(_DATABASE)
    comando = f'SELECT * FROM productos'
    paramsAux = []  
    if params:
        comando = f'{comando} WHERE {params[0]} = ?'
        paramsAux=[params[1]]
             
    producto = miDB.ejecutar_dml(comando,paramsAux)

    miDB.cerrarConexion()
    return producto

def transaccionAllByUserService(params):
    miDB = SQL(_DATABASE)
    comando = f'SELECTBYID * FROM transacciones'
    comando = f'{comando} WHERE {params[0]} = ?'
    transaccion = miDB.ejecutar_dml(comando, params[1])
    miDB.cerrarConexion()
    return transaccion
    

def actualizarPersona(user):
    miDB = SQL(_DATABASE)
    comando = f'UPDATE personas SET puntos = ?'
    com = f'{comando} WHERE documento = ?'
    persona = miDB.ejecutar_dml(com, [user[3], user[2]])
    miDB.cerrarConexion()
    return persona

def llenarTablaTransacciones(idPersona: int, idProducto:int, tipo:str, puntosAntes:float, puntosDespues:float):
    miDB = SQL(_DATABASE)
    comando = '''
        INSERT INTO transacciones(idPersona, idProducto, tipo, puntosAntes, puntosDespues) VALUES(?,?,?,?,?)
    '''
    x = miDB.ejecutar_dml(comando,[idPersona, idProducto, tipo, puntosAntes, puntosDespues])
    print("se inserto * PRODUCTO * desde el servicio --- " + x)
    miDB.cerrarConexion()
    
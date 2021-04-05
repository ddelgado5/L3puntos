from datos.dataclass import *
from logica.servicios import insertarPersona, insertarProducto, buscarUsuarioByDocumento, getProducts, actualizarPersona, llenarTablaTransacciones, transaccionAllByUserService


#import sys
#sys.path.append('../')

def registrarPersona():
    nombre = input('Nombre: ')
    documento = float(input('Número de documento:  '))
    puntos = float(input('Puntos: '))
    

    persona = Personas(nombre, documento, puntos)
    print(persona.__dict__)
    return persona


def inicializarBD():
    crearTablaProductos = '''
        CREATE TABLE IF NOT EXISTS productos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT NOT NULL,
            precio      REAL DEFAULT 0,
            puntos      REAL DEFAULT 0
            );
        '''
    crearTablaPersonas = '''
        CREATE TABLE IF NOT EXISTS personas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT NOT NULL,
            documento   TEXT NOT NULL,
            puntos      REAL DEFAULT 0,
            admin       INTEGER DEFAULT 0
            );
    '''

    crearTablaTransacciones = '''
        CREATE TABLE IF NOT EXISTS transacciones (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            idPersona   INTEGER,
            idProducto   INTEGER,
            tipo         TEXT NOT NULL,
            puntosAntes  REAL NOT NULL,
            puntosDespues REAL NOT NULL,
            FOREIGN KEY (idPersona) REFERENCES personas(id),
            FOREIGN KEY (idProducto) REFERENCES productos(id)
            );
    '''
    
    miDB = SQL('puntos')
    miDB.crearEstuctura(crearTablaProductos)
    miDB.crearEstuctura(crearTablaPersonas)
    miDB.crearEstuctura(crearTablaTransacciones)

    # comandoDML = ''' 
    #     INSERT INTO productos(nombre, precio, puntos)
    #     VALUES (?,?,?)
    # '''
    # comandoDMLPersonas = ''' 
    #     INSERT INTO personas(nombre, documento, puntos, admin)
    #     VALUES (?,?,?,?)
    # '''
    comandoDMLTransacciones = ''' 
        INSERT INTO transacciones(idPersona, idProducto, tipo, puntosAntes, puntosDespues, )
        VALUES (?,?,?,?,?)
    '''

    # insertarPersona("Diana", "1010", 1000, 1)
    insertarPersona("CRIS", "1011", 10, 0)

    #miDB.cerrarConexion()
    insertarProducto("camara",200000, 20)
    insertarProducto("dvr",300000, 30)
    insertarProducto("cable",20000, 2)
    

def inicioApp():
    print(" ***      Bienvenido!     ***  \n")
    print(" Estas en el app de puntos que documento deseas consultar? \n ")
    cedula = input("# de documento:  ")
    user = buscarUsuarioByDocumento(cedula)
    if(user == None):
        print("\nUsuario no existe\n")
        return
    menu(user)

def getProductsAll():
    productosAll = getProducts()
    for item in productosAll:
        print(f'Producto: [ {item[0]} ] Nombre:  {item[1]}  Precio:  $ {item[2]}  puedes obtener {int(item[3])} puntos ')

def getTransaccionAll(user):
    transaccionAllByUser = transaccionAllByUserService(('idPersona',user[0]))
    print("|---------------------------------------------- Historial ----------------------------------------------|\n")
    for item in transaccionAllByUser:
        print(f' Codigo persona: [ {item[1]} ] Codigo Producto: [ {item[2]} ] Accion: {item[3]} Puntos anteriores: {item[4]} Puntos actuales {item[5]}')

def comprar(user):
    user = buscarUsuarioByDocumento(user[2])
    productoSeleccionado = int(input("seleccione el numero de producto: "))
    
    prod = getProducts(['id',productoSeleccionado])
    if(prod == None):
        print("--- Este producto no existe\n")
        print("--- Intentalo de nuevo\n")
        comprar(user)
        return
    
    sumaPuntos = user[3] + prod[0][3]
    transaccion = llenarTablaTransacciones(user[0], prod[0][0], 'compra', user[3], sumaPuntos)
    print(f'Total puntos: {type(sumaPuntos)}\n')
    actualpersona = actualizarPersona((user[0], user[1], user[2],sumaPuntos, user[4]))
    print("\nSe cargaron nuevos puntos!\n")
    return

def redimir(user):
    user = buscarUsuarioByDocumento(user[2])

    cuantos= int(input(f'Cuantos puntos vas a redimir? '))
    if(cuantos > user[3]):
        print(f'\nLo sentimos... No cuentas con {cuantos} puntos, sigue acumulando!\n')
        return
    resta = user[3]-cuantos
    transaccion = llenarTablaTransacciones(user[0], None, 'redimido', user[3], resta)
    actualpersona = actualizarPersona((user[0], user[1], user[2],resta, user[4]))
    print(f'\n Ahora tienes {resta} puntos! \n')
    return

def verPuntos(user):
    user = buscarUsuarioByDocumento(user[2])
    print(f'\n Tu acumulado de puntos es: {user[3]} \n')
    pass

def menu(user):
    print("\n|******************************* PUNTOS *************************************************************|\n")
    print("Que deseas hacer?\n")
    print("[ 0 ] Comprar: ")
    print("[ 1 ] Redimir: ")
    print("[ 2 ] Ver mis puntos: ")
    print("[ 3 ] Ver listado de productos: ")
    print("[ 4 ] Ver historial de movimientos: ")
    print("[ 5 ] Salir: \n")

    opcion = input("Elige una opcion: ")
    if(opcion == "0"):
        comprar(user)
        menu(user)
        return
    if(opcion =="1"):# redimir
        redimir(user)
        menu(user)
        return
    if(opcion == "2"):# ver puntos
        verPuntos(user)
        menu(user)
        return
    if(opcion == "3"): #listado de prod
        print("\n|-------------------------------------------------------------------------------------------|\n")
        getProductsAll()
        menu(user)
        return
    if(opcion == "4"): #historial 
        print("\n|-------------------------------------------------------------------------------------------|\n")
        getTransaccionAll(user)
        menu(user)
        return
    if(opcion == "5"):
        print("\n Adios! \n")
        exit()
        return
    else:
        print("------------------------------------")
        print("\nOpcion no valida \n")
        print("------------------------------------")
        menu(user)


if __name__ == '__main__':
    #inicializarBD()
    inicioApp()
    
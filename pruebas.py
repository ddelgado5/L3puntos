from datos.dataclass import *
from logica.servicios import *

#import sys
#sys.path.append('../')

def prueba1():
    nombre = input('Nombre de la mascota? ')
    tipo = input('Tipo de mascota (felino, canino)? ')
    edad = int(input('Edad de la mascota? '))
    responsable = input('Nombre del resposable de la mascota? ')
    colorPelaje = input('Color del pelaje? ')

    obj1 = Mascota(nombre, tipo, edad, responsable, colorPelaje)
    print(obj1.__dict__)


def prueba2():
    comandoCrearTabla = '''
        CREATE TABLE IF NOT EXISTS mascota (
            nombre      TEXT NOT NULL,
            tipo        TEXT NOT NULL,
            edad        INTEGER,
            responsable TEXT,
            colorpelaje TEXT);
        '''
    
    miDB = SQL('base01')
    miDB.crearEstuctura(comandoCrearTabla)

    comandoDML = ''' 
        INSERT INTO mascota(nombre, tipo, edad, responsable, colorpelaje)
        VALUES (?,?,?,?,?)
    '''
    xyz = miDB.ejecutar_dml(comandoDML,['Pepita Rose', 'Felino', 4, 'Edison', 'Amarillo'])
    print(xyz)
    miDB.cerrarConexion()


def prueba3():
    crearEstructura('jedidata', 'domicilio')
    print("se ejecuto prueba 3")

if __name__ == '__main__':
    prueba3()
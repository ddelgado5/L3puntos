import sqlite3 as sql

#===[Gestion DataBase]=========================================
class SQL:
    def __init__(self, nombreDB):
        self.db = sql.connect(f'{nombreDB}.db')
        self.cursor = self.db.cursor() #estructura de datos del DB
        
    def cerrarConexion(self):
        try:
            self.db.close()
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'
        
    def crearEstuctura(self, comandoSQL):
        self.ejecutar_ddl(comandoSQL)
    
    #DDL Lenguaje de Definición de datos (estructura)
    def ejecutar_ddl(self, comandoSQL):
        try:
            self.cursor.execute(comandoSQL)
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'

    #DML Lenguaje de manipulacion de datos (CRUD)
    def ejecutar_dml(self, comandoSQL, datos=None):
        #(C)insert, (R)select, (U)update, (D)delete
        tipoComando = comandoSQL.split()[0].upper()
        if tipoComando=='SELECT':
            return self.ejecutarSelect(comandoSQL)
        if tipoComando=='INSERT':
            return self.ejecutarInsert(comandoSQL, datos)
        if tipoComando=='UPDATE':
            return self.ejecutarUpdate(comandoSQL, datos)
        if tipoComando=='DELETE':
            return self.ejecutarDelete(comandoSQL, datos)

    def ejecutarSelect(self, comandoSQL):
        try:
            self.cursor.execute(comandoSQL)
            respuesta = self.cursor.fetchall()
            return respuesta
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'
    
    def ejecutarInsert(self, comandoSQL, datos):
        try:
            self.cursor.execute(comandoSQL,datos)
            self.db.commit()
            return 'Operacion INSERT Ok'
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'

    def ejecutarUpdate(self, comandoSQL, datos):
        try:
            self.cursor.execute(comandoSQL,datos)
            self.db.commit()
            return 'Operacion UPDATE Ok'
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'

    def ejecutarDelete(self, comandoSQL, datos):
        try:
            self.cursor.execute(comandoSQL,datos)
            self.db.commit()
            return 'Operacion DELETE Ok'
        except sql.OperationalError as errorSQL:
            return f'Error en el programo de Datos: {errorSQL}'


#===[DataClass]========================================

class Mascota:
    #constructor
    def __init__(self, nombre, tipo, edad, responsable, colorPelaje):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.responsable = responsable
        self.colorPelaje = colorPelaje

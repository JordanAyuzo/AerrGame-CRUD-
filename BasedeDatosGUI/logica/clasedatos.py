"""
Parte para colocar las funciones que agregan datos a la base según lo
que se necesite añadir
"""
import datetime
import psycopg2


class BaseDatos():
    """
        Esta clase tiene las funcionalidades de la base de datos, por este medio
        se pueden hacer los cambios a la base de datos, realizar consultas, modificaciones
        búsquedas.
    """
    def __init__(self):
        self.conexion = 0
        self.cursor = 0

    def connectDB(self):
        try:
            self.conexion = psycopg2.connect(database="gamesdb",
                                             user="regrob261",
                                             password="",
                                             host="127.0.0.1",
                                             port="5432")
            return self.conexion
        except:
            print("Datos inválidos para la conexión de la base")
            return -50

    def consultaDatos(self, tablaConsultar, claveDatoBusc,condicion, cursor):
        print(cursor)
        borrado = "DROP VIEW IF EXISTS consulta;"
        cursor.execute(borrado)
        vista = "CREATE VIEW consulta AS SELECT * FROM " + tablaConsultar
        print(vista)

        try:

            if claveDatoBusc == '*':
                sql = "SELECT * FROM " + 'consulta'
                borrado = "DROP VIEW " + "consulta"
                cursor.execute(vista)
                cursor.execute(sql)
                datos = cursor.fetchall()
                return datos

            else:
                sql = "SELECT * FROM " + 'consulta' + " WHERE " + condicion + " = '" + claveDatoBusc + "'"
                borrado = "DROP VIEW " + "consulta"
                print(sql)
                cursor.execute(vista)
                cursor.execute(sql)
                datos = cursor.fetchall()
            temp = list(datos[0])
            print(type(temp[1]))

            if isinstance(temp[1], datetime.date):
                temp[1] = str(temp[1])
                print(temp)
                datos[0] = temp
            if isinstance(temp[2], datetime.date):
                temp[2] = str(temp[2])
                print(temp)
                datos[0] = temp
            cursor.execute(borrado)
            print("retornado")
            datos = datos[0]
            #print(datos)
            return datos
        except:
            print("La consulta no pudo realizarse")
            return []

    def borrarColumna(self, clavePrimaria, tablaConsultar, condicion, cursor):
        sql = "DELETE FROM " + tablaConsultar + " WHERE " + condicion +" = '" + clavePrimaria + "'"
        print(sql)
        try:
            cursor.execute(sql)
            print("Borrado con éxito")
            return True
        except:
            return False





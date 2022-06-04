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

    def consultaDatos(self, tablaConsultar, claveDatoBusc, cursor):
        print(cursor)
        vista = "CREATE VIEW consulta AS SELECT * FROM " + tablaConsultar
        print(vista)

        try:
            sql = "SELECT * FROM " + 'consulta' + " WHERE nombre = " + "'" + claveDatoBusc + "'"
            borrado = "DROP VIEW " + "consulta"
            print(sql)
            cursor.execute(vista)
            cursor.execute(sql)
            datos = cursor.fetchall()
            cursor.execute(borrado)

            return datos
        except:
            print("La consulta no pudo realizarse")
            return []

    def borrarColumna(self, clavePrimaria,tablaConsultar, cursor):
        sql = "DELETE FROM " + tablaConsultar + " WHERE nombre = " + "'" + clavePrimaria + "'"
        print(sql)
        try:
            cursor.execute(sql)
            print("Borrado con éxito")
            return True
        except:
            return False





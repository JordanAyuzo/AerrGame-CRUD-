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

    def agregarJuego(self, nombreG, clasificacionG, descripcionG, generoG, cursor):
        if nombreG != None:

            """Línea de codigo que nos permite añadir los datos de un juego a la base de datos, considerando
                que la conexión fue correcta desde el inicio y que no falta ningún dato, solamente se 
                verifica si la clave primaria no es nula para poder añadir los datos"""

            if self.consultaDatos('juego', nombreG, cursor):
                print("El dato ya existe")
                return False
            else:
                cursor.execute("INSERT INTO juego(nombre,clasificacion, descripcion, genero) VALUES (%s,%s,%s,%s)",
                           (nombreG, clasificacionG, descripcionG, generoG))

            if cursor:
                print("Añadido con éxito")
                return True
            else:
                print("Error al añadir datos intente de nuevo")
                # Consulte tabla de errores
                return False
        else:
            print("Error, la clave primaria dada es null")
            # Consulte tabla de errores
            return False
        return True

    def agregarPlataforma(self, nombreG, anioG, modeloG, cursor):
        self.cursor = cursor

        if nombreG != None:
            """Línea de codigo que nos permite añadir los datos de una plataforma a la base de datos, considerando
                que la conexión fue correcta desde el inicio y que no falta ningún dato, solamente se
                verifica si la clave primaria no es nula para poder añadir los datos"""
            cursor.execute("""INSERT INTO plataforma(
                                nombre,anio, modelo)
                                VALUES (%s,%s,%s)""",
                               (nombreG, datetime.date(anioG[0], anioG[1], anioG[2]), modeloG))

            if cursor:
                print("Añadida plataforma con éxito")
            else:
                print("Error al añadir datos intente de nuevo")
                # Consulte tabla de errores
                return -1426
        else:
            print("Error, la clave primaria dada es null")
            # Consulte tabla de errores
            return -51
        return 1


    def agregarVersion(self, idG, requisitosG, anioG, plataformaFlag, juegoFlag, cursor):
        if idG != None:
            """Necesitamos hacer una consulta sobre la base de datos para saber si
                el juego dado y la plataforma existen dentro de la base de datos
                para evitar errores al añadir estos"""

            cursor.execute("""INSERT INTO version(
                                        id,requisitos, anio, plt_nombre, jgo_nombre)
                                        VALUES (%s,%s,%s)""",
                           idG, requisitosG, datetime.date(anioG[0], anioG[1], anioG[2]), plataformaFlag, juegoFlag)
            if cursor:
                print("Añadido con éxito")
            else:
                print("Error al añadir datos intente de nuevo")
                # Consulte tabla de errores
                return -1426
        else:
            print("Error, la clave primaria dada es null")
            # Consulte tabla de errores
            return -51

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


    def modificarJuego(self):



    def borrarColumna(self, clavePrimaria,tablaConsultar, cursor):
        sql = "DELETE FROM " + tablaConsultar + " WHERE nombre = " + "'" + clavePrimaria + "'"
        print(sql)
        try:
            cursor.execute(sql)
            print("Borrado con éxito")
            return True
        except:
            return False



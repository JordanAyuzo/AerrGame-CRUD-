from logica.clasedatos import *


class VersionBase(BaseDatos):


    def agregar(self, idG, requisitosG, anioG, plataformaFlag, juegoFlag, cursor):
        if idG != None:
            """Necesitamos hacer una consulta sobre la base de datos para saber si
                el juego dado y la plataforma existen dentro de la base de datos
                para evitar errores al añadir estos"""

            cursor.execute("""INSERT INTO version(
                                        id,requisitos, anio, plt_nombre, jgo_nombre)
                                        VALUES (%s,%s,%s,%s,%s)""",
                           (idG, requisitosG, anioG, plataformaFlag, juegoFlag))
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

    def consultaTodos(self, tablaConsultar, claveDatoBusc, cursor):
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
                i = 0
                for dato in datos:
                    temp = list(dato)
                    print(dato)
                    if isinstance(temp[2], datetime.date):
                        temp[2] = str(temp[2])
                        print(temp)
                        dato = temp
                        datos[i] = dato
                        print(datos)
                        i = i + 1
                cursor.execute(borrado)
                print("Consulta realizada")
                return datos

        except:
            print("Consulta no se pudo realizar")
            return []
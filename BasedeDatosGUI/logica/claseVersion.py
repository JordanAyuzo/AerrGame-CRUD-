from clasedatos import *


class Version(BaseDatos):


    def agregar(self, idG, requisitosG, anioG, plataformaFlag, juegoFlag, cursor):
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
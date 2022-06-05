from logica.clasedatos import *

class PlataformaBase(BaseDatos):

    def agregar(self, nombreG, anioG, modeloG, cursor):
        self.cursor = cursor
        if nombreG != None:
            """Línea de codigo que nos permite añadir los datos de una plataforma a la base de datos, considerando
                que la conexión fue correcta desde el inicio y que no falta ningún dato, solamente se
                verifica si la clave primaria no es nula para poder añadir los datos"""
            print("Hasta aquí")
            cursor.execute("""INSERT INTO plataforma(
                                   nombre,anio, modelo)
                                   VALUES (%s,%s,%s)""",
                           (nombreG, anioG, modeloG))

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


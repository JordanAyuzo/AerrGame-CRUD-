from logica.clasedatos import *

class JuegoBase(BaseDatos):

    def agregar(self, nombreG, clasificacionG, descripcionG, generoG, cursor):
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

    def actualizarDatos(self, listaDatosCanv, listaDatosAct, cursor):
        try:
            cursor.execute("""select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'public' and TABLE_NAME = 'juego'""")
            nameColumn = cursor.fetchall()
            i = 0

            for dato in listaDatosCanv:
                cursor.execute(
                    "UPDATE version SET " + nameColumn[i] + "=" + dato + "WHERE " + nameColumn[i] + "=" + listaDatosAct[i])
                i = i + 1

            print("datos actualizados")
            return True
        except:
            print("excepción")
            return False

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
        return True

    def modificarJuego(self,nombreK, nombreG, clasificacionG, descripcionG, generoG, cursor):
        try:
            datos = self.consultaDatos('juego', nombreK, cursor)
            if  datos != []:
                print(datos)
                return True
            else:
                print("Clave no existe")
                return False

        except:
            return False

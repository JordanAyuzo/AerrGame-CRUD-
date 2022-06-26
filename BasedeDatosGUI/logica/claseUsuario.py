from logica.clasedatos import *

class claseUsuario(BaseDatos):

    def agregar(self, nickname, nombre, fecha_vencimiento, correo, cursor):
        if nickname != None:
            """Necesitamos hacer una consulta sobre la base de datos para saber si
                el juego dado y la plataforma existen dentro de la base de datos
                para evitar errores al añadir estos"""
            try:
                cursor.execute("""INSERT INTO usuario(
                                             nickname, nombre, fecha_vencimiento, correo)
                                             VALUES (%s,%s,%s,%s)""",
                               (nickname, nombre, fecha_vencimiento, correo))
                if cursor:
                    print("Añadido con éxito")
                    return True
            except:
                print("Error al añadir datos intente de nuevo")
                # Consulte tabla de errores
                return False
        else:
            print("Error, la clave primaria dada es null")
            # Consulte tabla de errores
            return False

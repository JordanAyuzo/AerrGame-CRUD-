from logica.clasedatos import *


class UsuarioTarjetaBase(BaseDatos):
    def agregar(self, usr_nickname, trt_numero, cursor):
        #self.cursor = cursor
        if usr_nickname != None and trt_numero != None:
            try:
                cursor.execute("""INSERT INTO usuario_tarjeta( usr_nickname, trt_numero)
                                                      VALUES (%s,%s)""",
                               (usr_nickname, trt_numero))
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
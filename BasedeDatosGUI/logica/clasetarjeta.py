from logica.clasedatos import *


class TarjetaBase(BaseDatos):
    def agregar(self, numero, fecha_vencimiento, nombre, cursor):
        self.cursor = cursor
        if numero != None:
            try:
                cursor.execute("""INSERT INTO tarjeta(numero, fecha_vencimiento, nombre) VALUES (%s,%s,%s)""",
                               (numero, fecha_vencimiento, nombre))
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

    def actualizarDatos(self, listaDatosCanv, listaDatosAct, cursor):
        try:
            cursor.execute(
                """select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'public' and TABLE_NAME = 'tarjeta'""")
            nameColumn = cursor.fetchall()
            i = 0

            for dato in listaDatosCanv:
                a = str("'" + listaDatosAct[i] + "'")
                ext = nameColumn[i][0]
                cursor.execute(
                    "UPDATE plataforma SET " + nameColumn[i][0] + "= '" + dato + "' WHERE " + nameColumn[i][
                        0] + "= " + str(a))
                i = i + 1

            print("datos actualizados")
            return True
        except:
            print("excepción")
            return False
    def consultaDatos(self, tablaConsultar, claveDatoBusc,condicion, cursor):
        try:
            sql = "SELECT DISTINCT * FROM usuario_tarjeta JOIN tarjeta ON tarjeta.numero  = usuario_tarjeta.trt_numero and " \
                  "usuario_tarjeta.usr_nickname = " + "'" +claveDatoBusc + "'"
            cursor.execute(sql)
            datos = cursor.fetchall()
            i = 0
            for dato in datos:
                temp = list(dato)
                print(dato)

                if isinstance(temp[3], datetime.date):
                    temp[3] = str(temp[3])
                    print(temp)
                    dato = temp
                    datos[i] = dato
                    print(datos)
                    i = i + 1
            return datos
        except:
            print("La consulta no pudo realizarse")
            return []


    def consultaTodos(self, tablaConsultar, claveDatoBusc, cursor):

        try:
            if claveDatoBusc == '*':
                sql = "SELECT DISTINCT * FROM usuario_tarjeta JOIN tarjeta ON tarjeta.numero  = usuario_tarjeta.trt_numero "
                cursor.execute(sql)
                datos = cursor.fetchall()
                i = 0
                for dato in datos:
                    temp = list(dato)
                    print(dato)
                    if isinstance(temp[3], datetime.date):
                        temp[3] = str(temp[3])
                        print(temp)
                        dato = temp
                        datos[i] = dato
                        print(datos)
                        i = i + 1
                print("Consulta realizada")
                return datos

        except:
            print("Consulta no se pudo realizar")
            return []
import psycopg2

"""Función que se conecta a la base de datos según los parámetros que se le indiquen,
	para este caso se escriben dentro de la función de psycopg2.connect(parámetros)"""


def connectDB():
    try:
        con = psycopg2.connect(database="ubisoftdb",
                               user="regrob261",
                               password="EmmaRob261",
                               host="127.0.0.1",
                               port="5432")
        return con
    except:
        print("Datos inválidos para la conexión de la base")
        return -50

def consultaJuego(baseConsultar, cursor):
    sql = "SELECT * FROM " + baseConsultar
    try:
        cursor.execute(sql)
        print(cursor.fetchall())
    except:
        print("La consulta no pudo realizarse")
        return -52

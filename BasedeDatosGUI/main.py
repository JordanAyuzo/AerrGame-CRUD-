import sys
import time
from clasedatos import *
from menu import *
from game import *
from error401 import *
from error402 import *
from error403 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """     AQUI SE PUEDE INSTANCIAR LA CLASE PARA LA 
        CONEXION DE LA BASE DE DATOS
        ejemplo:self.nombredeinstancia = clase.metodo()
         """

        """Secuencias de conexión a la base de datos mediante la case BaseDatos.
            En dicha base se tienen ya registrados los datos para el inicio de sesión
            por lo que están ocultos para el usuario final."""




        """Finaliza secuencia de conexión"""

        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.bjuego.clicked.connect(self.abrirJuego)

    def abrirJuego(self):
        self.hide()
        self.ventana = Juego()
        self.ventana.show()


class Juego(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_game1()
        self.ui.setupUi(self)
        self.ui.bCode.clicked.connect(self.buscar)
        self.ui.bcrear.clicked.connect(self.crear)
        self.ui.bactualizar.clicked.connect(self.modificar)
        self.ui.bborrar.clicked.connect(self.borrar)
        self.ui.atras.clicked.connect(self.retroceder)
        self.ui.atras_2.clicked.connect(self.retroceder)
        self.ui.atras_3.clicked.connect(self.retroceder)
        self.ui.atras_4.clicked.connect(self.retroceder)

        self.principal = BaseDatos()
        self.con = self.principal.connectDB()
        self.con.autocommit = True
        self.cursor = self.con.cursor()

    def borrar(self):
        clav = self.ui.lcod_0.text()
        clave = str(clav)
        #########################
        """Llama al metodo de busqueda pasandole como parametro la clave primaria
        MANDA   en:clave <es la clave primaria>     ej:soft
        REGRESA en:datoB <Es una lista de 1 tupla>  ej:[(soft,dato2,dat3,dato4)](llega lista vacia 
        si no hay nada)
        datoB=self.clase.metodo_buscar(clave) """
        datoB = [('Minecraft', 'dat1', 'dat2', 'dat3')]



        #########################
        if datoB == []:
            self.error(2)
        else:
            #########################
            """ Llama al metodo de borrar pasandole la clave primaria
            MANDA   en:clave <es la clave primaria>     ej:soft
            REGRESA en:valor <boleano>                  ej:True
            valor=self.clase.metodo_borrar(clave) """

            valor = self.principal.borrarColumna(clave, 'juego', self.cursor)
            #########################
            if valor != True:
                self.ui.cargando_0.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.02)
                    self.ui.progressBar_0.setValue(i)
                self.ui.cargando_0.setText('')
                self.error(3)
                self.ui.progressBar_0.setValue(0)
            else:
                self.ui.cargando_0.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.02)
                    self.ui.progressBar_0.setValue(i)
                self.ui.cargando_0.setText('¡Operaciónn Exitosa!')

    def modificar(self):
        clav = self.ui.lcod_2.text()
        clave = str(clav)
        ########################
        """Llama al metodo de busqueda pasandole como parametro la clave primaria
        MANDA   en:clave <es la clave primaria>     ej:soft
        REGRESA en:datoB <Es una lista de 1 tupla>  ej:[](llega lista vacia si no hay nada)
        datoB=self.clase.metodo_buscar(clave) """
        datoB = []
        ########################
        if datoB == []:
            self.error(2)
        else:
            nom = self.ui.jnombre_2.text()
            nombre = str(nom)
            clas = self.ui.jclasif_2.text()
            clasificacion = str(clas)
            desc = self.ui.jdesc_2.text()
            descripcion = str(desc)
            gen = self.ui.jgene_2.text()
            genero = str(gen)
            if nombre == '':
                nombre = datoB[0][0]
            if clasificacion == '':
                clasificacion = datoB[0][1]
            if descripcion == '':
                descripcion = datoB[0][2]
            if genero == '':
                genero = datoB[0][3]
            ################################
            """Llama al metodo de actualizar pasandole como parametros:
                   el nombre,clasificacion,descripcion y el genero
            MANDA   en:nombre,clasificacion,descripcion,genero
            REGRESA en:valor true o false
            valor=self.clase.metodo_actualizar(nombre,clasificacion,descripcion,genero) """
            valor = True
            ###############################
            if valor != True:
                self.ui.cargando_2.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.02)
                    self.ui.progressBar_2.setValue(i)
                self.ui.cargando_2.setText('')
                self.error(3)
                self.ui.progressBar_2.setValue(0)
            else:
                self.ui.cargando_2.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.02)
                    self.ui.progressBar_2.setValue(i)
                self.ui.cargando_2.setText('¡Operaciónn Exitosa!')

    def crear(self):
        nom = self.ui.jnombre.text()
        nombre = str(nom)
        clas = self.ui.jclasif.text()
        clasificacion = str(clas)
        desc = self.ui.jdesc.text()
        descripcion = str(desc)
        gen = self.ui.jgene.text()
        genero = str(gen)
        if nombre == '' or clasificacion == '' or descripcion == '' or genero == '':
            self.error(1)
        else:
            ##########################
            """Llama al metodo de crear pasandole como parametros:
                el nombre,clasificacion,descripcion y el genero
            MANDA   en:nombre,clasificacion,descripcion,genero
            REGRESA en:true o false
            valor=self.clase.metodo_crear(nombre,clasificacion,descripcion,genero) """

            self.principal.agregarJuego(nombre, clasificacion, descripcion, genero, self.cursor)
            respuesta = True
            ######################
            if respuesta != True:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.02)
                    self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('')
                self.error(3)
                self.ui.progressBar_2.setValue(0)
            else:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.02)
                    self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('¡Operaciónn Exitosa!')

    def buscar(self):
        clav = self.ui.lcod.text()
        clave = str(clav)
        if clave == '':
            self.error(1)
        else:
            ##########################
            """Llama al metodo de busqueda pasandole como parametro la clave primaria
            MANDA   en:clave <es la clave primaria>     ej:soft
            REGRESA en:datoB <Es una lista de 1 tupla>  ej:[](llega lista vacia si no hay nada)
            datoB=self.clase.metodo_buscar(clave) """

            print(type(clave))
            datosB = self.principal.consultaDatos('juego', clave, self.cursor)

            #datosB = [('Minecraft', 'dat1', 'dat2', 'dat3'), ('Minecraft2', 'dat1', 'dat2', 'dat3')]
            ############################
            i = len(datosB)
            if i == 0:
                self.error(2)
            else:
                self.ui.tableWidget.setRowCount(i)
                tablerow = 0
                for row in datosB:
                    self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                    self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                    tablerow += 1

    ##NO TOCAR ESTOS ELEMENTOS##
    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()

    def error(self, x):
        if x == 1:
            self.ventana = error401()
            self.ventana.show()
        elif x == 2:
            self.ventana = error402()
            self.ventana.show()
        elif x == 3:
            self.ventana = error403()
            self.ventana.show()


class error401(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_error()
        self.ui.setupUi(self)


class error402(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_error2()
        self.ui.setupUi(self)


class error403(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_error3()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())

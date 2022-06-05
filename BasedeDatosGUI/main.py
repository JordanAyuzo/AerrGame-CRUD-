##
#rama nueva
##
import sys
import time

from PyQt5.QtCore import Qt

from logica.clasedatos import *
from logica.claseJuego import *
from logica.clasePlataforma import *

from grafica.menu import *
from grafica.game import *
from grafica.plataforma import *
from grafica.version import *
from grafica.error401 import *
from grafica.error402 import *
from grafica.error403 import *
from PyQt5.QtWidgets import *
class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.bjuego.clicked.connect(self.abrirJuego)
        self.ui.bplatform.clicked.connect(self.abrirPlataforma)
        self.ui.bversion.clicked.connect(self.abrirVersion)
    def abrirVersion(self):
        self.hide()
        self.ventana = Version()
        self.ventana.show()
    def abrirJuego(self):
        self.hide()
        self.ventana = Juego()
        self.ventana.show()
    def abrirPlataforma(self):
        self.hide()
        self.ventana2 = Plataforma()
        self.ventana2.show()
 ####
class Version(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_version()
        self.ui.setupUi(self)
        tuplasJuegos=[('hola','mundo','adios'),('hola2','mundo','adios'),('hola3','mundo','adios')]    #TODO mandas a traer en forma de lista de lista de tuplas a  todos los  juegos
                           #     el primer atributo será el "nombre"
        j=0
        for i in tuplasJuegos:
            juego1=tuplasJuegos[j][0]
            self.ui.combojuego.addItem(juego1)
            self.ui.combojuego2.addItem(juego1)
            j+=1
        tuplasPlataforma=[('hoola','mundo','adios'),('holaa2','mundo','adios'),('holla3','mundo','adios')]    #TODO mandas a traer en forma de lista de lista de tuplas a  todos las plataformas
                           #     el primer atributo será el "nombre"
        k=0
        for i in tuplasPlataforma:
            plataforma1=tuplasPlataforma[k][0]
            self.ui.comboplataforma.addItem(plataforma1)
            self.ui.comboplataforma2.addItem(plataforma1)
            k+=1
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.atras3.clicked.connect(self.retroceder)
        self.ui.atras4.clicked.connect(self.retroceder)
        self.ui.aceptar1.clicked.connect(self.crear)
        self.ui.aceptar2.clicked.connect(self.actualizar)
        self.ui.aceptar3.clicked.connect(self.borrar)
        self.ui.busca.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)
    def crear(self):
        jue=self.ui.combojuego.currentText()
        juego=str(jue)
        plata=self.ui.comboplataforma.currentText()
        plataforma=str(plata)
        nom = self.ui.textnombre.text()
        nombre = str(nom)
        fech = self.ui.textfecha.text()
        fecha = str(fech)
        req = self.ui.textrequisitos.text()
        requisitos = str(req)
        if plataforma == '' or juego == '' or nombre == '' or requisitos=='':
                        self.error(1)
        else:
            #TODO:se inserta la tupla
            valor=True#funcion(nombre,fecha,requisitos,juego,plataforma) nombre es nombre de la Version
            if valor != True:
                self.ui.cargando1.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando1.setText('')
                self.error(3)
                time.sleep(0.2)
                self.ui.progreso1.setValue(0)
                self.ui.textnombre.setText('')
                self.ui.textrequisitos.setText('')
                self.ui.combojuego.setCurrentIndex(0)
                self.ui.comboplataforma.setCurrentIndex(0)
            else:
                self.ui.cargando1.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando1.setText('¡Operación Exitosa!')
                self.ui.progreso1.setValue(0)
                self.ui.textnombre.setText('')
                self.ui.textrequisitos.setText('')
                self.ui.combojuego.setCurrentIndex(0)
                self.ui.comboplataforma.setCurrentIndex(0)
    def buscar(self):
        cod = self.ui.codigo1.text()
        codigo = str(cod)
        if codigo == '*':
            datosB=[]#TODO:llamada de base de datos regresa tuplas asi:(juego,plataforma,version,fecha, requsito)
                    #si llega de otra forma avisar
            i = len(datosB)
            if i == 0:
                self.error(2)
                self.ui.resultado.setRowCount(0)
            else:
                self.ui.resultado.setRowCount(i)
                tablerow = 0
                for row in datosB:
                    self.ui.resultado.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                    self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    self.ui.resultado.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                    self.ui.resultado.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                    tablerow += 1
                self.ui.codigo1.setText('')
        else:
            if codigo == '':
                self.error(1)
                self.ui.resultado.setRowCount(0)
            else:
                ##########################
                datosB = [('hola','mundo','cruel','es','feo')] #TODO:manda a llamar a la funcion buscar
                #parametro en : codigo
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(i)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.ui.resultado.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                        self.ui.resultado.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                        tablerow += 1
                    self.ui.codigo1.setText('')
    def actualizar(self):
        cod = self.ui.codigo2.text()
        codigo = str(cod)
        jue=self.ui.combojuego2.currentText()
        juego=str(jue)
        plata=self.ui.comboplataforma2.currentText()
        plataforma=str(plata)
        nom = self.ui.textnombre2.text()
        nombre = str(cod)
        fech = self.ui.textfecha2.text()
        fecha = str(fech)
        req = self.ui.textrequisitos2.text()
        requisitos = str(req)
        if codigo =="":
            self.error(1)
            self.ui.codigo2.setText('')
            self.ui.textnombre2.setText('')
            self.ui.textrequisitos2.setText('')
            self.ui.combojuego2.setCurrentIndex(0)
            self.ui.comboplataforma2.setCurrentIndex(0)
        else:
            ######
            #aqui hace una consulta y trae tupla del elemento a actualizar
            #parametro (codigo) regresa tupla
            datoB=[('dat1','dat2','dat3','dato4','dato5')]#TODO:se puede borrar despues de hacer la conexion
                                                            #el orden que lleva es (juego,plataforma,version,fecha, requsito) si es otra forma avisar
            if datoB==[]:
                self.ui.cargando2.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso2.setValue(i)
                self.ui.cargando2.setText('')
                self.error(2)
                time.sleep(0.3)
                self.ui.progreso2.setValue(0)
                self.ui.codigo2.setText('')
                self.ui.textnombre2.setText('')
                self.ui.textrequisitos2.setText('')
                self.ui.combojuego2.setCurrentIndex(0)
                self.ui.comboplataforma2.setCurrentIndex(0)
            else:
                if juego == '' :
                    juego = datoB[0][0]
                if plataforma == '':
                    plataforma =datoB[0][1]
                if nombre == '':
                    nombre = datoB[0][2]
                if fecha == '01/01/1900':
                    fecha = datoB[0][3]
                if requisitos == '':
                    requisitos=datoB[0][4]
                ########
                #TODO: se lleva los datos de la siguiente manera (nombre,fecha,requisitos,juego,plataforma)
                valor= True#se puede borrar cuando haga la conexion
                #######
                if valor !=True:
                    self.ui.cargando2.setText('Cargando...')
                    for i in range(0, 50):
                        time.sleep(0.01)
                        self.ui.progreso2.setValue(i)
                    self.ui.cargando2.setText('')
                    self.error(3)
                    time.sleep(0.3)
                    self.ui.progreso2.setValue(0)
                else:
                    self.ui.cargando2.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progreso2.setValue(i)
                    self.ui.cargando2.setText('Operación Exitosa')
                    time.sleep(0.3)
                    self.ui.progreso2.setValue(0)
                self.ui.codigo2.setText('')
                self.ui.progreso2.setValue(0)
                self.ui.textnombre2.setText('')
                self.ui.textrequisitos2.setText('')
                self.ui.combojuego2.setCurrentIndex(0)
                self.ui.comboplataforma2.setCurrentIndex(0)

    def borrar(self):
        cod = self.ui.codigo3.text()
        codigo=str(cod)
        if codigo=='':
            self.error(1)
        else:
            #TODO:hace consulta si existe el dato regresa true o false
            #### el dato se va en el parametro (codigo)
            valor=True #puede borrar el true cuando se haga la conexion de BD
            if valor !=True:
                self.ui.cargando3.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso3.setValue(i)
                self.ui.cargando3.setText('')
                self.error(2)
                time.sleep(0.3)
                self.ui.progreso3.setValue(0)
                self.ui.codigo3.setText('')
            else:
                #TODO: hace llamada de la funcion borrar elemento
                #el dato se va en el parametro (codigo)
                valor2=True #puede borrar el true cuando se haga la conexion de BD
                if valor2 !=True:
                    self.ui.cargando3.setText('Cargando...')
                    for i in range(0, 50):
                        time.sleep(0.01)
                        self.ui.progreso3.setValue(i)
                    self.ui.cargando3.setText('')
                    self.error(3)
                    time.sleep(0.3)
                    self.ui.progreso3.setValue(0)
                    self.ui.codigo3.setText('')
                else:
                    self.ui.cargando3.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progreso3.setValue(i)
                    self.ui.cargando3.setText('¡Operación Exitosa!')
                    time.sleep(0.3)
                    self.ui.progreso3.setValue(0)
                    self.ui.codigo3.setText('')
    def limpio(self):
        self.ui.codigo1.setText('')
        self.ui.resultado.setRowCount(0)
    def error(self,x):
        if x==1:
            self.ventana = error401()
            self.ventana.show()
        elif x==2:
            self.ventana = error402()
            self.ventana.show()
        elif x==3:
            self.ventana = error403()
            self.ventana.show()
    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()
####
class Plataforma(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_plataforma()
        self.ui.setupUi(self)
        self.ui.aceptar.clicked.connect(self.crear)
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.atras3.clicked.connect(self.retroceder)
        self.ui.atras4.clicked.connect(self.retroceder)
        self.ui.busca.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)
        self.ui.aceptar_3.clicked.connect(self.actualizar)
        self.ui.aceptar_4.clicked.connect(self.borrar)

        self.principal = PlataformaBase()
        self.con = self.principal.connectDB()
        self.con.autocommit = True
        self.cursor = self.con.cursor()

    def crear(self):
        nom = self.ui.nombre.text()
        nombre = str(nom)
        fech = self.ui.fecha.text()
        fecha = str(fech)
        model = self.ui.modelo.text()
        modelo = str(model)
        if nombre == '' or fecha == '' or modelo == '':
            self.error(1)
        else:
            #SE INSERTA LA TUPLA
            #valor=llamada(nombre,fecha,modelo)
            valor = self.principal.agregar(nombre, fecha, modelo, self.cursor)
            valor = True #TODO: borrar cuando se haga la union de la BDT
            ######
            if valor !=True:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando.setText('')
                self.error(3)
                time.sleep(0.2)
                self.ui.progreso1.setValue(0)
                self.ui.nombre.setText('')
                self.ui.modelo.setText('')
            else:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando.setText('¡Operación Exitosa!')
                self.ui.progreso1.setValue(0)
                self.ui.nombre.setText('')
                self.ui.modelo.setText('')
    def buscar(self):
        cod = self.ui.codigo.text()
        codigo = str(cod)
        if codigo == '*':
            ############################
            datosB=[]#llamada de base de datos
            ############################
            i = len(datosB)
            if i == 0:
                self.error(2)
                self.ui.resultado.setRowCount(0)
            else:
                self.ui.resultado.setRowCount(i)
                tablerow = 0
                for row in datosB:
                    self.ui.resultado.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                    self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    tablerow += 1
                self.ui.codigo.setText('')
        else:
            if codigo == '':
                self.error(1)
                self.ui.resultado.setRowCount(0)
            else:
                ##########################
                datosB = self.principal.consultaDatos('plataforma', codigo, self.cursor) #manda a llamar a la funcion buscar
                #parametro en : codigo
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(i)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                        self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        tablerow += 1
                    self.ui.codigo.setText('')
    def actualizar(self):
        cod = self.ui.codigo_2.text()
        codigo = str(cod)
        nom = self.ui.nombre_3.text()
        nombre = str(nom)
        fech = self.ui.fecha_3.text()
        fecha = str(fech)
        model = self.ui.modelo_3.text()
        modelo = str(model)
        if codigo =="":
            self.error(1)
            self.ui.nombre_3.setText('')
            self.ui.modelo_3.setText('')
        else:
            ######
            #aqui hace una consulta y trae tupla del elemento a actualizar
            #parametro (codigo) regresa tupla
            datoB=[('dat1','dat2','dat3')]#se puede borrar despues de hacer la conexion
            ######
            if datoB==[]:
                self.ui.cargando2.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso2.setValue(i)
                self.ui.cargando2.setText('')
                self.error(2)
                time.sleep(0.3)
                self.ui.progreso2.setValue(0)
                self.ui.codigo_2.setText('')
                self.ui.nombre_3.setText('')
                self.ui.modelo_3.setText('')
            else:
                if nombre== '':
                    nombre = datoB[0][0]
                if fecha == '01/01/1900':
                    fecha = datoB[0][1]
                if modelo== '':
                    modelo =datoB[0][2]
                ########

                print(nombre + fecha+modelo)
                #se llama a la funcion actualizar llevandose (nombre,fecha,modelo) y regresa un true o false
                valor= True#se puede borrar cuando haga la conexion
                #######
                if valor !=True:
                    self.ui.cargando2.setText('Cargando...')
                    for i in range(0, 50):
                        time.sleep(0.01)
                        self.ui.progreso2.setValue(i)
                    self.ui.cargando2.setText('')
                    self.error(3)
                    time.sleep(0.3)
                    self.ui.progreso2.setValue(0)
                else:
                    self.ui.cargando2.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progreso2.setValue(i)
                    self.ui.cargando2.setText('Operación Exitosa')
                    time.sleep(0.3)
                    self.ui.progreso2.setValue(0)
                self.ui.codigo_2.setText('')
                self.ui.nombre_3.setText('')
                self.ui.modelo_3.setText('')
    def borrar(self):
        cod = self.ui.codigo_3.text()
        codigo=str(cod)
        if codigo=='':
            self.error(1)
        else:
            #hace consulta si existe el dato regresa true o false
            #el dato se va en el parametro (codigo)
            valor=True #puede borrar el true cuando se haga la conexion de BD
            if valor !=True:
                self.ui.cargando3.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso3.setValue(i)
                self.ui.cargando3.setText('')
                self.error(2)
                time.sleep(0.3)
                self.ui.progreso3.setValue(0)
                self.ui.codigo_3.setText('')
            else:
                #hace llamada de la funcion borrar elemento
                #el dato se va en el parametro (codigo)
                valor2=True #puede borrar el true cuando se haga la conexion de BD
                if valor2 !=True:
                    self.ui.cargando3.setText('Cargando...')
                    for i in range(0, 50):
                        time.sleep(0.01)
                        self.ui.progreso3.setValue(i)
                    self.ui.cargando3.setText('')
                    self.error(3)
                    time.sleep(0.3)
                    self.ui.progreso3.setValue(0)
                    self.ui.codigo_3.setText('')
                else:
                    self.ui.cargando3.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progreso3.setValue(i)
                    self.ui.cargando3.setText('¡Operación Exitosa!')
                    time.sleep(0.3)
                    self.ui.progreso3.setValue(0)
                    self.ui.codigo_3.setText('')

    def limpio(self):
        self.ui.codigo.setText('')
        self.ui.resultado.setRowCount(0)
    def error(self,x):
        if x==1:
            self.ventana = error401()
            self.ventana.show()
        elif x==2:
            self.ventana = error402()
            self.ventana.show()
        elif x==3:
            self.ventana = error403()
            self.ventana.show()
    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()

class Juego(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_game1()
        self.ui.setupUi(self)
        self.ui.bCode.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)
        self.ui.bcrear.clicked.connect(self.crear)
        self.ui.bactualizar.clicked.connect(self.modificar)
        self.ui.bborrar.clicked.connect(self.borrar)
        self.ui.atras.clicked.connect(self.retroceder)
        self.ui.atras_2.clicked.connect(self.retroceder)
        self.ui.atras_3.clicked.connect(self.retroceder)
        self.ui.atras_4.clicked.connect(self.retroceder)

        self.principal = JuegoBase()
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

        datosB = self.principal.consultaDatos('juego', clave, self.cursor)
        #########################
        if datosB == []:
            self.error(2)
        if clave == '':
            self.error(1)
        else:
            #########################
            """Llama al metodo de busqueda pasandole como parametro la clave primaria
            MANDA   en:clave <es la clave primaria>     ej:soft
            REGRESA en:datoB <Es una lista de 1 tupla>  ej:[(soft,dato2,dat3,dato4)](llega lista vacia 
            si no hay nada)
            datoB=self.clase.metodo_buscar(clave) """

            #########################
            if datosB == []:
                self.ui.cargando_0.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progressBar_0.setValue(i)
                self.ui.cargando_0.setText('')
                self.error(2)
                time.sleep(0.3)
                self.ui.progressBar_0.setValue(0)
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
                        time.sleep(0.01)
                        self.ui.progressBar_0.setValue(i)
                    self.ui.cargando_0.setText('')
                    self.error(3)
                    time.sleep(0.2)
                    self.ui.progressBar_0.setValue(0)
                else:
                    self.ui.cargando_0.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progressBar_0.setValue(i)
                    self.ui.cargando_0.setText('¡Operación Exitosa!')
                    time.sleep(0.2)
                    self.ui.progressBar_0.setValue(0)
    def modificar(self):
        clav = self.ui.lcod_2.text()
        clave = str(clav)

        ########################
        """Llama al metodo de busqueda pasandole como parametro la clave primaria
        MANDA   en:clave <es la clave primaria>     ej:soft
        REGRESA en:datoB <Es una lista de 1 tupla>  ej:[](llega lista vacia si no hay nada)
        datoB=self.clase.metodo_buscar(clave) """
        datoB = self.principal.consultaDatos('juego', clave, self.cursor)


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

        if clave == '':
            self.error(1)
        else:
            ########################
            """Llama al metodo de busqueda pasandole como parametro la clave primaria
            MANDA   en:clave <es la clave primaria>     ej:soft
            REGRESA en:datoB <Es una lista de 1 tupla>  ej:[](llega lista vacia si no hay nada)
            datoB=self.clase.metodo_buscar(clave) """
            datoB = [('Minecraft', 'dat1', 'dat2', 'dat3')]  #cuando ya este enlazado borrar esto
            ########################
            if datoB == []:
                for i in range(0,   41):
                    time.sleep(0.01)

                    self.ui.progressBar_2.setValue(i)
                self.error(2)
                time.sleep(0.2)
                self.ui.progressBar_2.setValue(0)
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
                valor = True   #cuando ya estee enlazado borrar esto
                ###############################
                if valor != True:
                    self.ui.cargando_2.setText('Cargando...')
                    for i in range(0, 50):
                        time.sleep(0.02)
                        self.ui.progressBar_2.setValue(i)
                    self.ui.cargando_2.setText('')
                    self.error(3)
                    time.sleep(0.2)
                    self.ui.progressBar_2.setValue(0)
                else:
                    self.ui.cargando_2.setText('Cargando...')
                    for i in range(0, 101):
                        time.sleep(0.01)
                        self.ui.progressBar_2.setValue(i)
                    self.ui.cargando_2.setText('¡Operación Exitosa!')
                    time.sleep(0.2)
                    self.ui.progressBar_2.setValue(0)
                    self.ui.lcod_2.setText('')
                    self.ui.jnombre_2.setText('')
                    self.ui.jclasif_2.setText('')
                    self.ui.jdesc_2.setText('')
                    self.ui.jgene_2.setText('')
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

            respuesta = self.principal.agregar(nombre, clasificacion, descripcion, genero, self.cursor)
            ######################
            if respuesta != True:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('')
                self.error(3)
                time.sleep(0.2)
                self.ui.progressBar_2.setValue(0)
            else:
                self.ui.cargando.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.01)
                    self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('¡Operación Exitosa!')
                time.sleep(0.2)
                self.ui.progressBar_2.setValue(0)
                self.ui.jnombre.setText('')
                self.ui.jclasif.setText('')
                self.ui.jdesc.setText('')
                self.ui.jgene.setText('')
    def limpio(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.lcod.setText('')
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
                self.ui.lcod.setText('')
    ##NO TOCAR ESTOS ELEMENTOS##
    def retroceder(self):

        self.cursor.close()
        self.con.close()

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

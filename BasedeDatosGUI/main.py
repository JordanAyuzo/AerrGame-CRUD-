##
# rama nueva
##
import sys
import time

from PyQt5.QtCore import Qt

from logica.clasedatos import *
from logica.claseJuego import *
from logica.clasePlataforma import *
from logica.claseVersion import *
from logica.claseUsuario import *
from logica.clasetarjeta import *
from logica.claseTarjetaUsuario import *
from logica.claseInforme import *
from grafica.menu import *
from grafica.game import *
from grafica.plataforma import *
from grafica.usuario import *
from grafica.tarjeta import *
from grafica.version import *
from grafica.informe import *
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
        self.ui.busuario.clicked.connect(self.abrirUsuario)
        self.ui.btarjeta.clicked.connect(self.abrirTarjeta)
        self.ui.binforme.clicked.connect(self.abrirInforme)



    def abrirInforme(self):
        self.hide()
        self.ventana = Informe()
        self.ventana.show()

    def abrirTarjeta(self):
        self.hide()
        self.ventana = Tarjeta()
        self.ventana.show()

    def abrirUsuario(self):
        self.hide()
        self.ventana = Usuario()
        self.ventana.show()

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



class Informe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Informe()
        self.ui.setupUi(self)
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.limpiar1.clicked.connect(self.retroceder)
        self.ui.limpiar2.clicked.connect(self.retroceder)
        self.ui.actualizar1.clicked.connect(self.informe1)
        self.ui.actualizar2.clicked.connect(self.informe2)

        self.puente = informeBase()
        self.conUT = self.puente.connectDB()
        self.conUT.autocommit = True
        self.cursorUT = self.conUT.cursor()


    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()
    def limpio(self):
        self.ui.resultado1.setRowCount(0)
        self.ui.resultado2.setRowCount(0)
    def informe1(self):
        datosB = self.puente.informeUsuario(self.cursorUT) #se hace la consulta de algebra relacional
        i = len(datosB)
        if i == 0:
            self.error(2)
            self.ui.resultado1.setRowCount(0)
        else:
            self.ui.resultado1.setRowCount(i)
            tablerow = 0
            for row in datosB:
                self.ui.resultado1.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))#nickname
                self.ui.resultado1.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))#nombre
                self.ui.resultado1.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))#correo
                self.ui.resultado1.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))#monto
                tablerow+=1
    def informe2(self):
        datosB = datosB = self.puente.informeJuego(self.cursorUT)   #se hace la consulta de algebra relacional
        i = len(datosB)
        if i == 0:
            self.error(2)
            self.ui.resultado2.setRowCount(0)
        else:
            self.ui.resultado2.setRowCount(i)
            tablerow = 0
            for row in datosB:
                self.ui.resultado2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))#version
                self.ui.resultado2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))#juego
                self.ui.resultado2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))#plataforma
                self.ui.resultado2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))#modelo
                self.ui.resultado2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))#monto
                tablerow+=1
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

####
class Tarjeta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_tarjeta()
        self.ui.setupUi(self)

        self.principal = TarjetaBase()
        self.con = self.principal.connectDB()
        self.con.autocommit = True
        self.cursor = self.con.cursor()

        self.puente = UsuarioTarjetaBase()
        self.conUT = self.puente.connectDB()
        self.conUT.autocommit = True
        self.cursorUT = self.conUT.cursor()

        self.user = usuarioBase()
        self.conU = self.user.connectDB()
        self.conU.autocommit = True
        self.cursorU = self.conU.cursor()


        listausuario = self.user.consultaTodos('usuario', '*', self.cursorU)

        j = 0               #!TODO el primer dato no es el nombre, es el nickname del usuario.
                            #!Ojito con eso
        for i in listausuario:
            user = listausuario[j][0]
            self.ui.combousuario.addItem(user)
            j += 1
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.atras3.clicked.connect(self.retroceder)
        self.ui.atras4.clicked.connect(self.retroceder)

        self.ui.aceptar1.clicked.connect(self.crear)
        self.ui.acp.clicked.connect(self.carga_modificar)
        self.ui.act.clicked.connect(self.modificar)
        self.ui.aceptar_4.clicked.connect(self.borrar)
        self.ui.busca.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)

    def crear(self):
        user = self.ui.combousuario.currentText()
        usuario = str(user)
        nom = self.ui.textbanco1.text()
        nombre = str(nom)
        cla = self.ui.textclave1.text()
        clabe = int(cla)
        fech = self.ui.textfecha1.text()
        fecha = str(fech)
        fecha = fecha.split('/')
        fecha.reverse()
        fecha = '/'.join(fecha)

        print(self.principal)
        print(self.puente)
        if usuario == '' or nombre == '' or clabe == '':
            self.error(1)
        else:
            valorA = self.principal.agregar(clabe, fecha, nombre, self.cursor)
            valorB = self.puente.agregar(usuario, clabe, self.cursorUT) #funcion enlaceusuario-tarjeta(usuario,nombre,clave,fecha)
            if valorA != True or valorB!=True:
                self.ui.cargando1.setText('Cargando...')
                for i in range(0, 50):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando1.setText('')
                self.error(3)
                time.sleep(0.2)
                self.ui.progreso1.setValue(0)
                self.ui.textclave1.setText('')
                self.ui.textbanco1.setText('')
                self.ui.combousuario.setCurrentIndex(0)
            else:
                self.ui.cargando1.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando1.setText('¡Operación Exitosa!')
                self.ui.progreso1.setValue(0)
                self.ui.textclave1.setText('')
                self.ui.textbanco1.setText('')
                self.ui.combousuario.setCurrentIndex(0)

    def buscar(self):
        cod = self.ui.codigo1.text()
        codigo = str(cod)
        if codigo == '*':

            datosB = self.principal.consultaTodos('tarjeta', '*', self.cursor)#TODO lista de listas de consulta FROM usuario,tarjeta
                       #select usuario, tarjeta,banco,vencimiento
            i = len(datosB)
            if i == 0:
                self.error(2)
                self.ui.resultado.setRowCount(0)
            else:
                self.ui.resultado.setRowCount(i)
                tablerow = 0
                for row in datosB:
                    self.ui.resultado.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                    self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.ui.resultado.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow += 1
                self.ui.codigo1.setText('')
        else:
            if codigo == '':
                self.error(1)
                self.ui.resultado.setRowCount(0)
            else:
                ##########################
                datosB =self.principal.consultaDatos('tarjeta', codigo, 'usr_nickname', self.cursor) #TODO:funcion(codigo)
                # parametro en : codigo
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
                        self.ui.resultado.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.ui.resultado.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[4])))
                        self.ui.resultado.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        tablerow += 1
                    self.ui.codigo1.setText('')
    def carga_modificar(self):
        cod = self.ui.codigo2.text()
        clave = str(cod)
        if clave =='':
            self.error(1)
            self.ui.textclave2.setText('')
            self.ui.textbanco2.setText('')
            self.ui.textfecha2.setText('')
            ####
        else:
            datoB = ['numero','fecha','nombre']##self.principal.consultaDatos('juego', codigo, self.cursor)
            # SE REGRESA LOS DATOS DE LA SIGUIENTE MANERA: nombre,fecha, modelo
            ###
            if datoB == []:
                self.error(2)
                self.ui.codigo2.setText('')
                self.ui.textclave2.setText('')
                self.ui.textbanco2.setText('')
                self.ui.textfecha2.setText('')
            else:
                #caraga los datos en los textos
                self.ui.textclave2.setText(datoB[0])
                self.ui.textbanco2.setText(datoB[2])
                self.ui.textfecha2.setText(datoB[1])

    def modificar(self):
        num=self.ui.textclave2.text()
        numero=str(num)
        nom =self.ui.textbanco2.text()
        nombre = str(nom)
        fech = self.ui.textfecha2.text()
        fecha = str(fech)
        valor = True#TODO modificatarjeta(numero,nombre,fecha)
        if valor != True:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 50):
                time.sleep(0.02)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('')
            self.error(3)
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
        else:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 101):
                time.sleep(0.01)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('¡Operación Exitosa!')
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
            self.ui.codigo2.setText('')
            self.ui.textclave2.setText('')
            self.ui.textbanco2.setText('')
            self.ui.textfecha2.setText('')
    def borrar(self):
        cod = self.ui.codigo3.text()
        codigo = str(cod)
        if codigo == '':
            self.error(1)
        else:
            #### el dato se va en el parametro (codigo)
            valor = ['DATO'] #TODO:
            if valor == []:
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
                # el dato se va en el parametro (codigo)
                valor2 = True
                if valor2 != True:
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

    def retroceder(self):
        self.cursor.close()
        self.con.close()

        self.hide()
        self.ventana = MiApp()
        self.ventana.show()

####
class Usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_usuario()
        self.ui.setupUi(self)
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.atras3.clicked.connect(self.retroceder)
        self.ui.atras4.clicked.connect(self.retroceder)
        self.ui.aceptar1.clicked.connect(self.crear)
        self.ui.acp.clicked.connect(self.carga_modificar)
        self.ui.act.clicked.connect(self.modificar)
        self.ui.aceptar_4.clicked.connect(self.borrar)
        self.ui.busca.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)

        self.principal = usuarioBase()
        self.con = self.principal.connectDB()
        self.con.autocommit = True
        self.cursor = self.con.cursor()

    def borrar(self):
        cod = self.ui.codigo3.text()
        codigo = str(cod)
        if codigo == '':
            self.error(1)
        else:
            # hace consulta si existe el dato regresa true o false
            # el dato se va en el parametro (codigo)

            valor =  datosB = self.principal.consultaDatos('usuario', codigo, 'nickname', self.cursor)
            if valor == []:
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
                # hace llamada de la funcion borrar elemento
                # el dato se va en el parametro (codigo)

                valor2 = self.principal.borrarColumna(codigo, 'usuario', 'nickname', self.cursor)
                if valor2 != True:
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
    def modificar(self):
        datosCambiados = []
        nom = self.ui.textnombre_2.text()
        nombre = str(nom)
        al = self.ui.textalias_2.text()
        nickname = str(al)
        datosCambiados.append(nickname)
        datosCambiados.append(nombre)
        fech =  self.ui.textfecha_2.text()
        fecha = str(fech)
        datosCambiados.append(fecha)
        cor =  self.ui.textcorreo.text()
        correo = str(cor)
        datosCambiados.append(correo)

        datosActuales = self.principal.consultaDatos('usuario', nickname, 'nickname', self.cursor)  # TODO: trae funcion(nickname,nombre,fecha,correo)
        valor = self.principal.actualizarDatos(datosCambiados, datosActuales, self.cursor)    #TODO: trae funcion(nickname,nombre,fecha,correo)
        if valor != True:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 50):
                time.sleep(0.02)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('')
            self.error(3)
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
        else:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 101):
                time.sleep(0.01)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('¡Operación Exitosa!')
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
            self.ui.codigo_2.setText('')
            self.ui.textnombre_2.setText('')
            self.ui.textalias_2.setText('')
            self.ui.textfecha_2.setText('')
            self.ui.textcorreo.setText('')
    def carga_modificar(self):
        cod = self.ui.codigo_2.text()
        clave = str(cod)
        if clave =='':
            self.error(1)
            self.ui.textnombre_2.setText('')
            self.ui.textalias_2.setText('')
            self.ui.textfecha_2.setText('')
            self.ui.textcorreo.setText('')
            ####
        else:
            datoB = self.principal.consultaDatos('usuario', clave, 'nickname', self.cursor)  # TODO: trae funcion(nickname,nombre,fecha,correo)
            if datoB == []:
                self.error(2)
                self.ui.codigo_2.setText('')
                self.ui.textnombre_2.setText('')
                self.ui.textalias_2.setText('')
                self.ui.textfecha_2.setText('')
                self.ui.textcorreo.setText('')
            else:
                #caraga los datos en los textos
                self.ui.textnombre_2.setText(datoB[1])
                self.ui.textalias_2.setText(datoB[0])
                self.ui.textfecha_2.setText(datoB[2])
                self.ui.textcorreo.setText(datoB[3])
    def buscar(self):
        cod = self.ui.codigo.text()
        codigo = str(cod)


        if codigo == '*':
            datosB = self.principal.consultaTodos('usuario', codigo, self.cursor)
            # si llega de otra forma avisar
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
                    tablerow += 1
                self.ui.codigo.setText('')
        else:
            if codigo == '':
                self.error(1)
                self.ui.resultado.setRowCount(0)
            else:
                ##########################
                datosB = self.principal.consultaDatos('usuario', codigo, 'nickname', self.cursor)
                # parametro en : codigo
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(1)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(0, tablerow, QtWidgets.QTableWidgetItem(row))
                        tablerow += 1
                    self.ui.codigo.setText('')
    def crear(self):
        nom = self.ui.textnombre.text()
        nombre = str(nom)
        ali = self.ui.textalias.text()
        nickname = str(ali)
        fech = self.ui.textfecha.text()
        fecha = str(fech)
        fecha = fecha.split('/')
        fecha.reverse()
        fecha = '/'.join(fecha)
        cor = self.ui.textcorreo_2.text()
        correo = str(cor)
        if nombre == '' or nickname == '' or correo == '':
            self.error(1)
        else:
            valor =self.principal.agregar(nickname, nombre, fecha, correo, self.cursor) #TODO:fun(nickname,nombre,fecha,correo)
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
                self.ui.textalias.setText('')
                self.ui.textcorreo_2.setText('')
            else:
                self.ui.cargando1.setText('Cargando...')
                for i in range(0, 101):
                    time.sleep(0.01)
                    self.ui.progreso1.setValue(i)
                self.ui.cargando1.setText('¡Operación Exitosa!')
                self.ui.progreso1.setValue(0)
                self.ui.textnombre.setText('')
                self.ui.textalias.setText('')
                self.ui.textcorreo_2.setText('')
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

    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()
    def limpio(self):
        self.ui.codigo1.setText('')
        self.ui.resultado.setRowCount(0)





####
class Version(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_version()
        self.ui.setupUi(self)

        self.principalJue = JuegoBase()
        self.conJ = self.principalJue.connectDB()
        self.conJ.autocommit = True
        self.cursorJ = self.conJ.cursor()

        self.principalPla = PlataformaBase()
        self.conP = self.principalPla.connectDB()
        self.conP.autocommit = True
        self.cursorP = self.conP.cursor()

        self.principal = VersionBase()
        self.conV = self.principal.connectDB()
        self.conV.autocommit = True
        self.cursorV = self.conV.cursor()

        tuplasJuegos = self.principalJue.consultaDatos('juego', '*', 'nombre', self.cursorJ)
        #     el primer atributo será el "nombre"
        j = 0
        for i in tuplasJuegos:
            juego1 = tuplasJuegos[j][0]
            self.ui.combojuego.addItem(juego1)
            self.ui.combojuego2.addItem(juego1)
            j += 1
        tuplasPlataforma = self.principalPla.consultaTodos('plataforma', '*', self.cursorP)
        #     el primer atributo será el "nombre"
        k = 0
        for i in tuplasPlataforma:
            plataforma1 = tuplasPlataforma[k][0]
            self.ui.comboplataforma.addItem(plataforma1)
            self.ui.comboplataforma2.addItem(plataforma1)
            k += 1
        self.ui.atras1.clicked.connect(self.retroceder)
        self.ui.atras2.clicked.connect(self.retroceder)
        self.ui.atras3.clicked.connect(self.retroceder)
        self.ui.atras4.clicked.connect(self.retroceder)
        self.ui.aceptar1.clicked.connect(self.crear)
        self.ui.aceptar2.clicked.connect(self.carga_modificar)
        self.ui.actualizacion.clicked.connect(self.modificar)
        self.ui.aceptar3.clicked.connect(self.borrar)
        self.ui.busca.clicked.connect(self.buscar)
        self.ui.limpiar.clicked.connect(self.limpio)

    def crear(self):
        jue = self.ui.combojuego.currentText()
        juego = str(jue)
        plata = self.ui.comboplataforma.currentText()
        plataforma = str(plata)
        nom = self.ui.textnombre.text()
        nombre = str(nom)
        fech = self.ui.textfecha.text()
        fecha = str(fech)
        fecha = fecha.split('/')
        fecha.reverse()
        fecha = '/'.join(fecha)
        req = self.ui.textrequisitos.text()
        requisitos = str(req)
        if plataforma == '' or juego == '' or nombre == '' or requisitos == '':
            self.error(1)
        else:
            valor = self.principal.agregar(nombre, requisitos, fecha, plataforma, juego,
                                           self.cursorV)  # funcion(nombre,fecha,requisitos,juego,plataforma) nombre es nombre de la Version
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
            datosB = self.principal.consultaTodos('version', codigo, self.cursorV)
            # si llega de otra forma avisar
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
                datosB = self.principal.consultaDatos('version', codigo, 'id', self.cursorV)
                # parametro en : codigo
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(1)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(0, tablerow, QtWidgets.QTableWidgetItem(row))
                        tablerow += 1
                    self.ui.codigo1.setText('')

    #####
    def carga_modificar(self):
        cod = self.ui.codigo2.text()
        clave = str(cod)
        if clave =='':
            self.error(1)
            self.ui.textnombre2.setText('')
            self.ui.textrequisitos2.setText('')
            self.ui.textfecha2.setText('')
            self.ui.combojuego2.setCurrentIndex(0)
            self.ui.comboplataforma2.setCurrentIndex(0)
            ####
        else:
            datoB = self.principal.consultaDatos('version', clave, 'id', self.cursorV) ##self.principal.consultaDatos('juego', codigo, self.cursor)
            # SE REGRESA LOS DATOS DE LA SIGUIENTE MANERA: nombre,fecha, modelo
            ###
            if datoB == []:
                self.error(2)
                self.ui.codigo2.setText('')
                self.ui.textnombre2.setText('')
                self.ui.textrequisitos2.setText('')
                self.ui.textfecha2.setText('')
                self.ui.combojuego2.setCurrentIndex(0)
                self.ui.comboplataforma2.setCurrentIndex(0)
            else:
                #caraga los datos en los textos
                self.ui.textnombre2.setText(datoB[0])
                self.ui.textrequisitos2.setText(datoB[1])
                self.ui.textfecha2.setText(datoB[2])
                index = self.ui.combojuego2.findText(datoB[4])
                self.ui.combojuego2.setCurrentIndex(index)
                index = self.ui.comboplataforma2.findText(datoB[3])
                self.ui.comboplataforma2.setCurrentIndex(index)
    def modificar(self):
        datosCambiados = []

        nom = self.ui.textnombre2.text()
        nombre = str(nom)
        datosCambiados.append(nombre)

        req = self.ui.textrequisitos2.text()
        requisitos = str(req)
        datosCambiados.append(requisitos)

        fech = self.ui.textfecha2.text()
        fecha = str(fech)

        fecha = fecha.split('/')
        fecha.reverse()
        fecha = '/'.join(fecha)

        datosCambiados.append(fecha)

        plata=self.ui.comboplataforma2.currentText()
        plataforma=str(plata)
        datosCambiados.append(plataforma)

        jue = self.ui.combojuego2.currentText()
        juego = str(jue)
        datosCambiados.append(juego)


        datosActuales = self.principal.consultaDatos('version', nombre, 'id', self.cursorV)
        valor = self.principal.actualizarDatos(datosCambiados, datosActuales, self.cursorV)    #TODO: manda  a llamar actualizar(nombre,fecha,modelo)
                    #devuelve true o false
        if valor != True:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 50):
                time.sleep(0.02)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('')
            self.error(3)
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
        else:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 101):
                time.sleep(0.01)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('¡Operación Exitosa!')
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
            self.ui.codigo2.setText('')
            self.ui.textnombre2.setText('')
            self.ui.textrequisitos2.setText('')
            self.ui.textfecha2.setText('')
            self.ui.combojuego2.setCurrentIndex(0)
            self.ui.comboplataforma2.setCurrentIndex(0)

    ####
    def borrar(self):
        cod = self.ui.codigo3.text()
        codigo = str(cod)
        if codigo == '':
            self.error(1)
        else:
            #### el dato se va en el parametro (codigo)
            valor = self.principal.consultaDatos('version', codigo, 'id', self.cursorV)  # puede borrar el true cuando se haga la conexion de BD
            if valor == []:
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
                # el dato se va en el parametro (codigo)
                valor2 = self.principal.borrarColumna(codigo, 'version', 'id', self.cursorV)  # puede borrar el true cuando se haga la conexion de BD
                if valor2 != True:
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

    def retroceder(self):
        self.hide()
        self.ventana = MiApp()
        self.ventana.show()


####
def invertir_cadena(cadena):
    return cadena[::-1]

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
        self.ui.aceptar_3.clicked.connect(self.carga_modificar)
        self.ui.actualizacion.clicked.connect(self.modificar)
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
            # SE INSERTA LA TUPLA
            # valor=llamada(nombre,fecha,modelo)
            #fecha = invertir_cadena(fecha)

            fecha = fecha.split('/')
            fecha.reverse()
            fecha = '/'.join(fecha)
            valor = self.principal.agregar(nombre, fecha, modelo, self.cursor)
            ######
            if valor != True:
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
            datosB = self.principal.consultaTodos('plataforma', codigo, self.cursor)  # llamada de base de datos
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
                datosB = self.principal.consultaDatos('plataforma', codigo, 'nombre',
                                                      self.cursor)  # manda a llamar a la funcion buscar
                # parametro en : codigo
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(1)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(0, tablerow, QtWidgets.QTableWidgetItem(row))
                        tablerow += 1
                    self.ui.codigo.setText('')

    ####
    def modificar(self):
        datosCambiados = []
        nom = self.ui.nombre_3.text()
        nombre = str(nom)
        datosCambiados.append(nombre)
        fech = self.ui.fecha_3.text()
        fecha = str(fech)
        datosCambiados.append(fecha)
        model = self.ui.modelo_3.text()
        modelo = str(model)
        datosCambiados.append(modelo)

        datosActuales = self.principal.consultaDatos('plataforma', nombre, 'nombre', self.cursor)

        valor =  self.principal.actualizarDatos(datosCambiados, datosActuales, self.cursor) #TODO: manda  a llamar actualizar(nombre,fecha,modelo)
                    #devuelve true o false
        if valor != True:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 50):
                time.sleep(0.02)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('')
            self.error(3)
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
        else:
            self.ui.cargando2.setText('Cargando...')
            for i in range(0, 101):
                time.sleep(0.01)
                self.ui.progreso2.setValue(i)
            self.ui.cargando2.setText('¡Operación Exitosa!')
            time.sleep(0.2)
            self.ui.progreso2.setValue(0)
            self.ui.codigo_2.setText('')
            self.ui.nombre_3.setText('')
            self.ui.fecha_3.setText('')
            self.ui.modelo_3.setText('')

    def carga_modificar(self):
        cod = self.ui.codigo_2.text()
        clave = str(cod)
        if clave =='':
            self.error(1)
            self.ui.nombre_3.setText('')
            self.ui.fecha_3.setText('')
            self.ui.modelo_3.setText('')
            ####
        else:
            datoB = self.principal.consultaDatos('plataforma', clave, 'nombre', self.cursor) ##self.principal.consultaDatos('juego', codigo, self.cursor)
            # SE REGRESA LOS DATOS DE LA SIGUIENTE MANERA: nombre,fecha, modelo
            ###
            if datoB == []:
                self.error(2)
                self.ui.codigo_2.setText('')
                self.ui.nombre_3.setText('')
                self.ui.fecha_3.setText('')
                self.ui.modelo_3.setText('')
            else:
                #caraga los datos en los textos
                self.ui.nombre_3.setText(datoB[0])
                self.ui.fecha_3.setText(datoB[1])
                self.ui.modelo_3.setText(datoB[2])

    def borrar(self):
        cod = self.ui.codigo_3.text()
        codigo = str(cod)
        if codigo == '':
            self.error(1)
        else:
            # hace consulta si existe el dato regresa true o false
            # el dato se va en el parametro (codigo)

            valor = self.principal.consultaDatos('plataforma', codigo, 'nombre', self.cursor)  # puede borrar el true cuando se haga la conexion de BD
            if valor == []:
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
                # hace llamada de la funcion borrar elemento
                # el dato se va en el parametro (codigo)

                valor2 = self.principal.borrarColumna(codigo, 'plataforma', 'nombre', self.cursor)  # puede borrar el true cuando se haga la conexion de BD
                if valor2 != True:
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
        self.ui.bactualizar.clicked.connect(self.carga_modificar)
        self.ui.bactualizar2.clicked.connect(self.modificar)
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

        datosB = self.principal.consultaDatos('juego', clave, 'nombre', self.cursor)
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
                valor = self.principal.borrarColumna(clave, 'juego', 'nombre', self.cursor)
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

    def carga_modificar(self):
        clav = self.ui.lcod_2.text()
        clave = str(clav)
        if clave == '':
            self.error(1)
            self.ui.jnombre_2.setText('')
            self.ui.jclasif_2.setText('')
            self.ui.jdesc_2.setText('')
            self.ui.jgene_2.setText('')
            ####
        else:
            datosB = self.principal.consultaDatos('juego', clave, 'nombre', self.cursor)
            # SE REGRESA LOS DATOS DE LA SIGUIENTE MANERA: nombre,clasificacion descripcion genero
            ####
            if datosB == []:
                self.error(2)
                self.ui.jnombre_2.setText('')
                self.ui.jclasif_2.setText('')
                self.ui.jdesc_2.setText('')
                self.ui.jgene_2.setText('')
            else:
                # caraga los datos en los textos
                self.ui.jnombre_2.setText(datosB[0])
                self.ui.jclasif_2.setText(datosB[1])
                self.ui.jdesc_2.setText(datosB[2])
                self.ui.jgene_2.setText(datosB[3])
            # datos Cargados en los textos

    def modificar(self):
        datosCambiados = []

        nom = self.ui.jnombre_2.text()
        nombre = str(nom)
        datosCambiados.append(nombre)
        clas = self.ui.jclasif_2.text()
        clasificacion = str(clas)
        datosCambiados.append(clasificacion)

        desc = self.ui.jdesc_2.text()
        descripcion = str(desc)
        datosCambiados.append(descripcion)
        gen = self.ui.jgene_2.text()
        genero = str(gen)
        datosCambiados.append(genero)
        datosB = self.principal.consultaDatos('juego', nombre, 'nombre', self.cursor)
        print("lista actual", datosB)
        valor = self.principal.actualizarDatos(datosCambiados, datosB, self.cursor)  # TODO: manda  a llamar actualizar(nombre,clasificacion,descripcion,genero)
        # devuelve true o false
        if valor != True:
            self.ui.cargando_2.setText('Cargando...')
            i = 0
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
        self.ui.resultado.setRowCount(0)
        self.ui.lcod.setText('')

    def buscar(self):
        clav = self.ui.lcod.text()
        clave = str(clav)
        if clave == '*':
            ############################
            datosB =  self.principal.consultaDatos('juego', clave, 'nombre', self.cursor) # TODO aqui llega tu pinche lista de listas xD
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
                    tablerow += 1
                self.ui.lcod.setText('')
        else:
             if clave == '':
                self.error(1)
             else:
                ##########################
                """Llama al metodo de busqueda pasandole como parametro la clave primaria
                MANDA   en:clave <es la clave primaria>     ej:soft
                REGRESA en:datoB <Es una lista de 1 tupla>  ej:[](llega lista vacia si no hay nada)
                datoB=self.clase.metodo_buscar(clave) """
                datosB = self.principal.consultaDatos('juego', clave, 'nombre', self.cursor)
                # datosB = [te regresa una lista]
                ############################
                i = len(datosB)
                if i == 0:
                    self.error(2)
                    self.ui.resultado.setRowCount(0)
                else:
                    self.ui.resultado.setRowCount(1)
                    tablerow = 0
                    for row in datosB:
                        self.ui.resultado.setItem(0, tablerow, QtWidgets.QTableWidgetItem(row))
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

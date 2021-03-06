# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_usuario(object):
    def setupUi(self, usuario):
        usuario.setObjectName("usuario")
        usuario.resize(523, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurso/img/usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        usuario.setWindowIcon(icon)
        usuario.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(90, 0, 182, 255), stop:0.289216 rgba(150, 155, 255, 255), stop:0.921569 rgba(74, 206, 205, 255));")
        self.centralwidget = QtWidgets.QWidget(usuario)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 521))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color:rgb(255, 255, 255)")
        self.tabWidget.setObjectName("tabWidget")
        self.crear = QtWidgets.QWidget()
        self.crear.setObjectName("crear")
        self.logo_1 = QtWidgets.QLabel(self.crear)
        self.logo_1.setGeometry(QtCore.QRect(60, 20, 381, 51))
        self.logo_1.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"")
        self.logo_1.setObjectName("logo_1")
        self.nom = QtWidgets.QLabel(self.crear)
        self.nom.setGeometry(QtCore.QRect(90, 120, 71, 31))
        self.nom.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom.setObjectName("nom")
        self.model = QtWidgets.QLabel(self.crear)
        self.model.setGeometry(QtCore.QRect(70, 300, 91, 31))
        self.model.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);\n"
"")
        self.model.setObjectName("model")
        self.textnombre = QtWidgets.QLineEdit(self.crear)
        self.textnombre.setGeometry(QtCore.QRect(180, 120, 241, 31))
        self.textnombre.setAutoFillBackground(False)
        self.textnombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textnombre.setText("")
        self.textnombre.setPlaceholderText("")
        self.textnombre.setObjectName("textnombre")
        self.textcorreo_2 = QtWidgets.QLineEdit(self.crear)
        self.textcorreo_2.setGeometry(QtCore.QRect(180, 300, 241, 31))
        self.textcorreo_2.setAutoFillBackground(False)
        self.textcorreo_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textcorreo_2.setText("")
        self.textcorreo_2.setObjectName("textcorreo_2")
        self.fech = QtWidgets.QLabel(self.crear)
        self.fech.setGeometry(QtCore.QRect(110, 240, 51, 31))
        self.fech.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.fech.setObjectName("fech")
        self.textfecha = QtWidgets.QDateEdit(self.crear)
        self.textfecha.setGeometry(QtCore.QRect(180, 240, 241, 31))
        self.textfecha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"border: 1px solid #00007f;")
        self.textfecha.setCalendarPopup(True)
        self.textfecha.setObjectName("textfecha")
        self.progreso1 = QtWidgets.QProgressBar(self.crear)
        self.progreso1.setGeometry(QtCore.QRect(90, 430, 371, 23))
        self.progreso1.setAutoFillBackground(False)
        self.progreso1.setStyleSheet("")
        self.progreso1.setProperty("value", 0)
        self.progreso1.setInvertedAppearance(False)
        self.progreso1.setObjectName("progreso1")
        self.aceptar1 = QtWidgets.QPushButton(self.crear)
        self.aceptar1.setGeometry(QtCore.QRect(280, 360, 61, 61))
        self.aceptar1.setStyleSheet("image: url(:/recurso/img/elegir.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.aceptar1.setText("")
        self.aceptar1.setAutoDefault(True)
        self.aceptar1.setObjectName("aceptar1")
        self.atras1 = QtWidgets.QPushButton(self.crear)
        self.atras1.setGeometry(QtCore.QRect(180, 360, 61, 61))
        self.atras1.setStyleSheet("image: url(:/recurso/img/atras.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.atras1.setText("")
        self.atras1.setAutoDefault(True)
        self.atras1.setObjectName("atras1")
        self.cargando1 = QtWidgets.QLabel(self.crear)
        self.cargando1.setGeometry(QtCore.QRect(190, 450, 141, 20))
        self.cargando1.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.cargando1.setObjectName("cargando1")
        self.indicaciones_2 = QtWidgets.QLabel(self.crear)
        self.indicaciones_2.setEnabled(True)
        self.indicaciones_2.setGeometry(QtCore.QRect(0, 70, 511, 31))
        self.indicaciones_2.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.indicaciones_2.setObjectName("indicaciones_2")
        self.nom_15 = QtWidgets.QLabel(self.crear)
        self.nom_15.setGeometry(QtCore.QRect(90, 180, 71, 31))
        self.nom_15.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_15.setObjectName("nom_15")
        self.textalias = QtWidgets.QLineEdit(self.crear)
        self.textalias.setGeometry(QtCore.QRect(180, 180, 241, 31))
        self.textalias.setAutoFillBackground(False)
        self.textalias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textalias.setText("")
        self.textalias.setPlaceholderText("")
        self.textalias.setObjectName("textalias")
        self.tabWidget.addTab(self.crear, "")
        self.buscar = QtWidgets.QWidget()
        self.buscar.setObjectName("buscar")
        self.logo_2 = QtWidgets.QLabel(self.buscar)
        self.logo_2.setGeometry(QtCore.QRect(60, 20, 381, 51))
        self.logo_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"")
        self.logo_2.setObjectName("logo_2")
        self.resultado = QtWidgets.QTableWidget(self.buscar)
        self.resultado.setGeometry(QtCore.QRect(50, 210, 411, 261))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setStyleSheet("color:#000000;\n"
"background-color: rgb(255, 255, 255);\n"
"border :none;")
        self.resultado.setObjectName("resultado")
        self.resultado.setColumnCount(4)
        self.resultado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.resultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.resultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.resultado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.resultado.setHorizontalHeaderItem(3, item)
        self.atras2 = QtWidgets.QPushButton(self.buscar)
        self.atras2.setGeometry(QtCore.QRect(20, 20, 31, 41))
        self.atras2.setStyleSheet("image: url(:/recurso/img/atras.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.atras2.setText("")
        self.atras2.setAutoDefault(True)
        self.atras2.setObjectName("atras2")
        self.frame = QtWidgets.QLabel(self.buscar)
        self.frame.setGeometry(QtCore.QRect(-50, 30, 571, 481))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.frame.setObjectName("frame")
        self.codigo = QtWidgets.QLineEdit(self.buscar)
        self.codigo.setGeometry(QtCore.QRect(210, 100, 201, 31))
        self.codigo.setAutoFillBackground(False)
        self.codigo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.codigo.setText("")
        self.codigo.setObjectName("codigo")
        self.busca = QtWidgets.QPushButton(self.buscar)
        self.busca.setGeometry(QtCore.QRect(420, 90, 61, 51))
        self.busca.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"image: url(:/recurso/img/busqueda.png);")
        self.busca.setText("")
        self.busca.setAutoDefault(True)
        self.busca.setObjectName("busca")
        self.nom_2 = QtWidgets.QLabel(self.buscar)
        self.nom_2.setGeometry(QtCore.QRect(40, 100, 171, 31))
        self.nom_2.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_2.setObjectName("nom_2")
        self.limpiar = QtWidgets.QPushButton(self.buscar)
        self.limpiar.setGeometry(QtCore.QRect(410, 410, 71, 51))
        self.limpiar.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"image: url(:/recurso/img/limpiar.png)")
        self.limpiar.setText("")
        self.limpiar.setAutoDefault(True)
        self.limpiar.setObjectName("limpiar")
        self.frame.raise_()
        self.logo_2.raise_()
        self.resultado.raise_()
        self.atras2.raise_()
        self.codigo.raise_()
        self.busca.raise_()
        self.nom_2.raise_()
        self.limpiar.raise_()
        self.tabWidget.addTab(self.buscar, "")
        self.actualizar = QtWidgets.QWidget()
        self.actualizar.setObjectName("actualizar")
        self.logo_3 = QtWidgets.QLabel(self.actualizar)
        self.logo_3.setGeometry(QtCore.QRect(60, 20, 381, 51))
        self.logo_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"")
        self.logo_3.setObjectName("logo_3")
        self.codigo_2 = QtWidgets.QLineEdit(self.actualizar)
        self.codigo_2.setGeometry(QtCore.QRect(210, 90, 201, 31))
        self.codigo_2.setAutoFillBackground(False)
        self.codigo_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.codigo_2.setText("")
        self.codigo_2.setObjectName("codigo_2")
        self.nom_5 = QtWidgets.QLabel(self.actualizar)
        self.nom_5.setGeometry(QtCore.QRect(40, 90, 171, 31))
        self.nom_5.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_5.setObjectName("nom_5")
        self.nom_7 = QtWidgets.QLabel(self.actualizar)
        self.nom_7.setGeometry(QtCore.QRect(150, 130, 231, 31))
        self.nom_7.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_7.setObjectName("nom_7")
        self.progreso2 = QtWidgets.QProgressBar(self.actualizar)
        self.progreso2.setGeometry(QtCore.QRect(80, 430, 371, 23))
        self.progreso2.setAutoFillBackground(False)
        self.progreso2.setStyleSheet("")
        self.progreso2.setProperty("value", 0)
        self.progreso2.setInvertedAppearance(False)
        self.progreso2.setObjectName("progreso2")
        self.atras3 = QtWidgets.QPushButton(self.actualizar)
        self.atras3.setGeometry(QtCore.QRect(30, 20, 31, 41))
        self.atras3.setStyleSheet("image: url(:/recurso/img/atras.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.atras3.setText("")
        self.atras3.setAutoDefault(True)
        self.atras3.setObjectName("atras3")
        self.cargando2 = QtWidgets.QLabel(self.actualizar)
        self.cargando2.setGeometry(QtCore.QRect(180, 450, 141, 20))
        self.cargando2.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.cargando2.setObjectName("cargando2")
        self.nom_9 = QtWidgets.QLabel(self.actualizar)
        self.nom_9.setGeometry(QtCore.QRect(110, 180, 71, 31))
        self.nom_9.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_9.setObjectName("nom_9")
        self.textnombre_2 = QtWidgets.QLineEdit(self.actualizar)
        self.textnombre_2.setGeometry(QtCore.QRect(200, 180, 241, 31))
        self.textnombre_2.setAutoFillBackground(False)
        self.textnombre_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textnombre_2.setText("")
        self.textnombre_2.setPlaceholderText("")
        self.textnombre_2.setObjectName("textnombre_2")
        self.textcorreo = QtWidgets.QLineEdit(self.actualizar)
        self.textcorreo.setGeometry(QtCore.QRect(200, 330, 241, 31))
        self.textcorreo.setAutoFillBackground(False)
        self.textcorreo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textcorreo.setText("")
        self.textcorreo.setObjectName("textcorreo")
        self.fech_2 = QtWidgets.QLabel(self.actualizar)
        self.fech_2.setGeometry(QtCore.QRect(130, 280, 51, 31))
        self.fech_2.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.fech_2.setObjectName("fech_2")
        self.model_2 = QtWidgets.QLabel(self.actualizar)
        self.model_2.setGeometry(QtCore.QRect(90, 330, 91, 31))
        self.model_2.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);\n"
"")
        self.model_2.setObjectName("model_2")
        self.act = QtWidgets.QPushButton(self.actualizar)
        self.act.setGeometry(QtCore.QRect(220, 370, 61, 61))
        self.act.setStyleSheet("image:url(:/recurso/img/actualizar.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.act.setText("")
        self.act.setAutoDefault(True)
        self.act.setObjectName("act")
        self.acp = QtWidgets.QPushButton(self.actualizar)
        self.acp.setGeometry(QtCore.QRect(420, 80, 61, 61))
        self.acp.setStyleSheet("image: url(:/recurso/img/elegir.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.acp.setText("")
        self.acp.setAutoDefault(True)
        self.acp.setObjectName("acp")
        self.textfecha_2 = QtWidgets.QLineEdit(self.actualizar)
        self.textfecha_2.setGeometry(QtCore.QRect(200, 280, 241, 31))
        self.textfecha_2.setAutoFillBackground(False)
        self.textfecha_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textfecha_2.setText("")
        self.textfecha_2.setPlaceholderText("")
        self.textfecha_2.setObjectName("textfecha_2")
        self.nom_16 = QtWidgets.QLabel(self.actualizar)
        self.nom_16.setGeometry(QtCore.QRect(110, 230, 71, 31))
        self.nom_16.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.nom_16.setObjectName("nom_16")
        self.textalias_2 = QtWidgets.QLineEdit(self.actualizar)
        self.textalias_2.setGeometry(QtCore.QRect(200, 230, 241, 31))
        self.textalias_2.setAutoFillBackground(False)
        self.textalias_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.textalias_2.setText("")
        self.textalias_2.setPlaceholderText("")
        self.textalias_2.setObjectName("textalias_2")
        self.act.raise_()
        self.logo_3.raise_()
        self.codigo_2.raise_()
        self.nom_5.raise_()
        self.nom_7.raise_()
        self.progreso2.raise_()
        self.atras3.raise_()
        self.cargando2.raise_()
        self.nom_9.raise_()
        self.textnombre_2.raise_()
        self.textcorreo.raise_()
        self.fech_2.raise_()
        self.model_2.raise_()
        self.acp.raise_()
        self.textfecha_2.raise_()
        self.nom_16.raise_()
        self.textalias_2.raise_()
        self.tabWidget.addTab(self.actualizar, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.logo_4 = QtWidgets.QLabel(self.tab_4)
        self.logo_4.setGeometry(QtCore.QRect(60, 20, 381, 51))
        self.logo_4.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;\n"
"")
        self.logo_4.setObjectName("logo_4")
        self.aceptar_4 = QtWidgets.QPushButton(self.tab_4)
        self.aceptar_4.setGeometry(QtCore.QRect(390, 380, 61, 61))
        self.aceptar_4.setStyleSheet("image: url(:/recurso/img/elegir.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.aceptar_4.setText("")
        self.aceptar_4.setAutoDefault(True)
        self.aceptar_4.setObjectName("aceptar_4")
        self.codigo3 = QtWidgets.QLineEdit(self.tab_4)
        self.codigo3.setGeometry(QtCore.QRect(230, 130, 241, 31))
        self.codigo3.setAutoFillBackground(False)
        self.codigo3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"color:#000000;")
        self.codigo3.setText("")
        self.codigo3.setObjectName("codigo3")
        self.textnom = QtWidgets.QLabel(self.tab_4)
        self.textnom.setGeometry(QtCore.QRect(30, 130, 201, 31))
        self.textnom.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.textnom.setObjectName("textnom")
        self.progreso3 = QtWidgets.QProgressBar(self.tab_4)
        self.progreso3.setGeometry(QtCore.QRect(60, 400, 331, 23))
        self.progreso3.setAutoFillBackground(False)
        self.progreso3.setStyleSheet("")
        self.progreso3.setProperty("value", 0)
        self.progreso3.setInvertedAppearance(False)
        self.progreso3.setObjectName("progreso3")
        self.texto = QtWidgets.QLabel(self.tab_4)
        self.texto.setGeometry(QtCore.QRect(70, 240, 421, 101))
        self.texto.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.texto.setObjectName("texto")
        self.atras4 = QtWidgets.QPushButton(self.tab_4)
        self.atras4.setGeometry(QtCore.QRect(20, 20, 31, 41))
        self.atras4.setStyleSheet("image: url(:/recurso/img/atras.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.atras4.setText("")
        self.atras4.setAutoDefault(True)
        self.atras4.setObjectName("atras4")
        self.cargando3 = QtWidgets.QLabel(self.tab_4)
        self.cargando3.setGeometry(QtCore.QRect(130, 420, 141, 20))
        self.cargando3.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.cargando3.setObjectName("cargando3")
        self.checkBox = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(50, 220, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic Blk")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("font: 87 10pt \"Noto Sans Arabic Blk\";\n"
"background-color: rgba(0, 0, 0,0%);\n"
"color:rgb(170, 0, 0)")
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_4, "")
        usuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(usuario)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(usuario)

    def retranslateUi(self, usuario):
        _translate = QtCore.QCoreApplication.translate
        usuario.setWindowTitle(_translate("usuario", "Usuario"))
        self.logo_1.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><img src=\":/recurso/img/01title.png\"/></p></body></html>"))
        self.nom.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Nombre:</span></p></body></html>"))
        self.model.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Correo: </span></p></body></html>"))
        self.textnombre.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej:Juan Hernandez Ventura</span></p></body></html>"))
        self.textcorreo_2.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej: rgtling@hotmail.com</span></p></body></html>"))
        self.fech.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Fecha:</span></p></body></html>"))
        self.textfecha.setToolTip(_translate("usuario", "<html><head/><body><p><span style=\" color:#474747;\">Ej:02/09/2017</span></p></body></html>"))
        self.textfecha.setWhatsThis(_translate("usuario", "<html><head/><body><p><br/></p></body></html>"))
        self.textfecha.setDisplayFormat(_translate("usuario", "dd/MM/yyyy"))
        self.cargando1.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.indicaciones_2.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Ingrese Los Datos Del Usuario:</span></p></body></html>"))
        self.nom_15.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Alias:</span></p></body></html>"))
        self.textalias.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej:MasterCrack</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.crear), _translate("usuario", "Crear"))
        self.logo_2.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><img src=\":/recurso/img/01title.png\"/></p></body></html>"))
        item = self.resultado.horizontalHeaderItem(0)
        item.setText(_translate("usuario", "Alias"))
        item = self.resultado.horizontalHeaderItem(1)
        item.setText(_translate("usuario", "Nombre"))
        item = self.resultado.horizontalHeaderItem(2)
        item.setText(_translate("usuario", "Fecha"))
        item = self.resultado.horizontalHeaderItem(3)
        item.setText(_translate("usuario", "Correo"))
        self.frame.setText(_translate("usuario", "<html><head/><body><p><img src=\":/recurso/img/cuadro1.png\"/></p></body></html>"))
        self.codigo.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#747474;\">Ej:Juan</span></p></body></html>"))
        self.nom_2.setText(_translate("usuario", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nombre de la Usuario: </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.buscar), _translate("usuario", "Buscar"))
        self.logo_3.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><img src=\":/recurso/img/01title.png\"/></p></body></html>"))
        self.codigo_2.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#747474;\">Ej:Nintendo</span></p></body></html>"))
        self.nom_5.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Alias (Nickname):</span></p></body></html>"))
        self.nom_7.setText(_translate("usuario", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Ingrese Los Datos A Modificar:</span></p></body></html>"))
        self.cargando2.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.nom_9.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Nombre:</span></p></body></html>"))
        self.textnombre_2.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej:Juan Alberto</span></p></body></html>"))
        self.textcorreo.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej: nombre@dominio.com</span></p></body></html>"))
        self.fech_2.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Fecha:</span></p></body></html>"))
        self.model_2.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Correo: </span></p></body></html>"))
        self.textfecha_2.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej:05/05/05</span></p></body></html>"))
        self.nom_16.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Alias:</span></p></body></html>"))
        self.textalias_2.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#474747;\">Ej:Bobicraft</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actualizar), _translate("usuario", "Actualizar"))
        self.logo_4.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><img src=\":/recurso/img/01title.png\"/></p></body></html>"))
        self.codigo3.setToolTip(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#747474;\">Ej:Juan</span></p></body></html>"))
        self.textnom.setText(_translate("usuario", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600;\">Nombre Del Usuario: </span></p></body></html>"))
        self.texto.setText(_translate("usuario", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">En cuanto usted elimine el elemento nombrado, ??ste dejara de </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">existir y no habr?? forma de recuperarlo, si usted est?? seguro </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#aa0000;\">de esto continue.</span></p></body></html>"))
        self.cargando3.setText(_translate("usuario", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.checkBox.setText(_translate("usuario", "ADVERTENCIA:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("usuario", "Borrar"))
import recurso_rc

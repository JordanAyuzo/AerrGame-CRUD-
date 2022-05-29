# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurso/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.122549 rgba(109, 117, 255, 255), stop:0.921569 rgba(74, 206, 205, 255));\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(-1)
        self.frame.setObjectName("frame")
        self.bjuego = QtWidgets.QPushButton(self.frame)
        self.bjuego.setGeometry(QtCore.QRect(60, 100, 81, 71))
        self.bjuego.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"image: url(:/recurso/img/02button.png);\n"
"border:none;\n"
"")
        self.bjuego.setText("")
        self.bjuego.setObjectName("bjuego")
        self.ljuego = QtWidgets.QLabel(self.frame)
        self.ljuego.setGeometry(QtCore.QRect(70, 160, 61, 21))
        font = QtGui.QFont()
        font.setFamily("xos4 Terminus")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.ljuego.setFont(font)
        self.ljuego.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border :none;")
        self.ljuego.setObjectName("ljuego")
        self.bplatform = QtWidgets.QPushButton(self.frame)
        self.bplatform.setGeometry(QtCore.QRect(290, 100, 71, 61))
        self.bplatform.setStyleSheet("image: url(:/recurso/img/03plataform.png);\n"
"background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.bplatform.setText("")
        self.bplatform.setObjectName("bplatform")
        self.lplatform = QtWidgets.QLabel(self.frame)
        self.lplatform.setGeometry(QtCore.QRect(260, 160, 121, 21))
        font = QtGui.QFont()
        font.setFamily("xos4 Terminus")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lplatform.setFont(font)
        self.lplatform.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0,0%);")
        self.lplatform.setObjectName("lplatform")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 431, 61))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:none;")
        self.label.setObjectName("label")
        self.bexit = QtWidgets.QPushButton(self.frame)
        self.bexit.setGeometry(QtCore.QRect(170, 440, 81, 71))
        self.bexit.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"image: url(:/recurso/img/05exit.png);\n"
"border:none;\n"
"")
        self.bexit.setText("")
        self.bexit.setObjectName("bexit")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bexit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú"))
        self.ljuego.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">JUEGO</span></p></body></html>"))
        self.lplatform.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PLATAFORMA</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/recurso/img/01title.png\"/></p></body></html>"))
import recurso_rc

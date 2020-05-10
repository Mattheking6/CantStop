# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A_Propos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Propos(object):
    def setupUi(self, Propos):
        Propos.setObjectName("Propos")
        Propos.setWindowModality(QtCore.Qt.ApplicationModal)
        Propos.resize(271, 121)
        Propos.setAccessibleName("")
        self.aPropos = QtWidgets.QLabel(Propos)
        self.aPropos.setGeometry(QtCore.QRect(30, 20, 211, 71))
        self.aPropos.setTextFormat(QtCore.Qt.RichText)
        self.aPropos.setOpenExternalLinks(True)
        self.aPropos.setObjectName("aPropos")

        self.retranslateUi(Propos)
        QtCore.QMetaObject.connectSlotsByName(Propos)

    def retranslateUi(self, Propos):
        _translate = QtCore.QCoreApplication.translate
        Propos.setWindowTitle(_translate("Propos", "A propos..."))
        self.aPropos.setAccessibleName(_translate("Propos", "A propos"))
        self.aPropos.setText(_translate("Propos", "<html><head/><body><p align=\"center\">Application réalisée par <a href=\"mailto:mattheking6@hotmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Matthieu Mureau</span></a></p><p align=\"center\">Python 3.8 - Interface graphique QT5<br/><a href=\"https://github.com/Mattheking6/CantStop\"><span style=\" text-decoration: underline; color:#0000ff;\">Lien GitHub de l\'application.</span></a></p></body></html>"))

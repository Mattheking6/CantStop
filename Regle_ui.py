# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regle.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Regles(object):
    def setupUi(self, Regles):
        Regles.setObjectName("Regles")
        Regles.resize(739, 457)
        self.ReglesCantStop = QtWidgets.QLabel(Regles)
        self.ReglesCantStop.setGeometry(QtCore.QRect(20, 20, 691, 421))
        self.ReglesCantStop.setTextFormat(QtCore.Qt.RichText)
        self.ReglesCantStop.setWordWrap(True)
        self.ReglesCantStop.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.ReglesCantStop.setObjectName("ReglesCantStop")

        self.retranslateUi(Regles)
        QtCore.QMetaObject.connectSlotsByName(Regles)

    def retranslateUi(self, Regles):
        _translate = QtCore.QCoreApplication.translate
        Regles.setWindowTitle(_translate("Regles", "Règles du jeu"))
        self.ReglesCantStop.setText(_translate("Regles", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Règles du jeu Can’t Stop :</span></p><p><span style=\" font-size:10pt;\">Dans ce classique de Sid Sackson, les joueurs doivent tenter leur chance avec des dés et choisir des combinaisons tactiquement pour fermer </span><span style=\" font-size:10pt; font-weight:600;\">trois colonnes</span><span style=\" font-size:10pt;\">.</span></p><p><span style=\" font-size:10pt;\">Le tableau contient une colonne pour chaque total possible de deux dés à six faces, mais le nombre de cases de chaque colonne varie: plus un total est probable, plus il y a d\'espace dans la colonne et plus il faut rouler.</span></p><p><span style=\" font-size:10pt;\">À son tour, un joueur jette quatre dés et les range en duo, par exemple 1 4 5 6 peut devenir :</span></p><p><span style=\" font-size:10pt;\">- 1 + 4 et 5 + 6 pour 5 et 11</span></p><p><span style=\" font-size:10pt;\">- 1 + 5 et 4 + 6 pour 6 et 10</span></p><p><span style=\" font-size:10pt;\">- 1 + 6 et 4 + 5 pour 7 et 9</span></p><p><span style=\" font-size:10pt;\">Le joueur place ou avance les marqueurs de progression aux colonne(s) libre(s) associée(s) aux totaux choisis, puis choisit:</span></p><p><span style=\" font-size:10pt;\">- de rouler à nouveau</span></p><p><span style=\" font-size:10pt;\">- ou de terminer son tour et de remplacer les marqueurs de progression par des marqueurs de leur couleur.</span></p><p><span style=\" font-size:10pt;\">Un j</span><span style=\" font-size:10pt; text-decoration: underline;\">oueur ne peut avancer que de trois colonnes différentes dans un tour</span><span style=\" font-size:10pt;\"> et ne peut pas avancer de colonne que tout joueur a fermé en atteignant l’espace final.</span></p><p><span style=\" font-size:10pt;\">Si un résultat ne donne lieu à un </span><span style=\" font-size:10pt; text-decoration: underline;\">aucun jeu légal</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:10pt; text-decoration: underline;\">le tour se termine avec la perte de son progrès</span><span style=\" font-size:10pt;\">.</span></p></body></html>"))

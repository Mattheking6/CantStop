from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time

import css_ui


class Jeu(QMainWindow, css_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        systray_icon = QIcon("ressources\De5.png")
        systray = QSystemTrayIcon(systray_icon, self)

        menu = QMenu()
        restore = QAction("Restorer", self)
        close = QAction("Fermer", self)

        menu.addActions([restore, close])
        systray.setContextMenu(menu)

        systray.show()

        close.triggered.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jeu = Jeu()

    splash_image = QPixmap(r"ressources\De.png")
    splash = QSplashScreen()

    for x in range(1, 7):
        print(x)
        splash_image = QPixmap(r"ressources\De{}.png".format(x))
        splash = QSplashScreen(splash_image)
        splash.show()
        time.sleep(0.1)

    jeu.show()
    app.exec_()

    splash.finish(jeu)

    print("Bonjour Matthieu")

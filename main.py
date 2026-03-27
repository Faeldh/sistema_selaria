import sys
from PyQt5 import uic, QtWidgets



tela_menu = uic.loadUiType('TELAS/tela_menu.ui')[0]

from login import Login

class MainWindow(QtWidgets.QMainWindow, tela_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    



app = QtWidgets.QApplication(sys.argv)
janela = Login()
janela.show()


sys.exit(app.exec())

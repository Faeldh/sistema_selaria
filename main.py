import sys
from PyQt5 import uic, QtWidgets

tela_menu = uic.loadUiType('TEla/tela_menu.ui')

class MainWindow(QtWidgets.QMainWindow, tela_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
janela = MainWindow()
janela.show()


sys.exit(app.exec())

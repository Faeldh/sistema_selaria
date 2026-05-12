from PyQt5 import uic, QtWidgets

tela_menu = uic.loadUiType('TELAS/tela_menu.ui')[0]

class MainWindow(QtWidgets.QMainWindow, tela_menu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
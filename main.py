import sys
from PyQt5 import QtWidgets
from login import Login

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    janela = Login()
    janela.show()
    


    sys.exit(app.exec())

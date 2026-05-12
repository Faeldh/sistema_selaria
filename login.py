from PyQt5 import uic, QtWidgets
from conexao import conectar

tela_login = uic.loadUiType('TELAS/tela_login.ui')[0]

class Login(QtWidgets.QMainWindow, tela_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_conectar.clicked.connect(self.verificar_login)

    def verificar_login(self):
        nome = self.txt_nome.text()
        senha = self.txt_senha.text()

        conexao = conectar()
        cursor = conexao.cursor()

        comando = 'SELECT * FROM usuario WHERE nome=%s AND senha=%s'

        dados = (nome, senha)
        cursor.execute(comando, dados)
        resultado = cursor.fetchone()

        if resultado:
            print('login ok')
            #QtWidgets.QMessageBox.information(self, 'Login', 'Login realizado com sucesso')

            from menu import MainWindow

            self.janela = MainWindow()
            self.janela.show()

            self.close()
        
        else:
            QtWidgets.QMessageBox.warning(self, 'Erro', 'Usuário ou senha inválido')


        conexao.close()
        





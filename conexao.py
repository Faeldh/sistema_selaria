import pymysql


def conectar():
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'db_sistema'
    )

    return conexao
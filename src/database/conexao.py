import mysql.connector

class Conexao:
    def __init__(self):
        pass

    @staticmethod
    def conectar() -> list:

        try:
            # conectando ao banco de dados
            conexao = mysql.connector.connect(
                host= 'localhost',
                port='3306',
                user='root',
                password='root',
                database='financiaki'
            )

            cursor = conexao.cursor()

            return(conexao,cursor)
        
        except Exception as e:
            print(f'ERRO: {e}')
            return None, None
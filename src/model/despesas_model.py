from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    @staticmethod
    def adcionar (login:str, descricao:str, data:str, hora:str, valor:float) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False

        try:
            cursor.execute('''
                            INSERT INTO tb_despesas(login, descricao, data, hora, valor)
                            VALUES (%s, %s, %s, %s, %s)
                            ''',
                            [login, descricao, data, hora, valor])
            cod_despesas = cursor.lastrowid

            conexao.commit()
            conexao.close
            return cod_despesas

        except:
            return False
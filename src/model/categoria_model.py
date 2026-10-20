from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar (login:str, categoria:str) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False

        try:
            cursor.execute('''
                            INSERT INTO tb_categorias(login, categoria)
                            VALUES (%s, %s)
                            ''',
                            [login, categoria])
            conexao.commit()
            conexao.close()

            return True

        except:
            print('Não foi possível cadastrar esses valores!')
            return False

    @staticmethod
    def verificar(login:str, categoria:str) -> dict:
        conexao, cursor = Conexao().conectar()

        if conexao == None:
            print('Não existe essa categoria')
            return None

        cursor.execute('''
                        SELECT cod_categoria, login, categoria FROM tb_categorias
                        WHERE login = %s
                        AND categoria = %s
                        ''',
                        [login, categoria])

        resultado = cursor.fetchone()
        conexao.close()

        return resultado
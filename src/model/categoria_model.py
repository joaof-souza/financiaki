from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar (login:str, categoria:str) -> int:
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
            cod_categoria = cursor.lastrowid
            
            conexao.commit()
            conexao.close()
            return cod_categoria

        except:
            print('Não foi possível cadastrar esses valores!')
            return False


    @staticmethod
    def excluir (cod_categoria: int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False
        
        try:
            cursor.execute('''
                            DELETE FROM tb_categorias
                            WHERE cod_categoria = %s
                            ''',
                            [cod_categoria])

            conexao.commit()
            conexao.close()
            print(f'Categoria {cod_categoria} excluida!')
            return True

        except:
            print('Erro ao excluir categoria!')
            return False


    @staticmethod
    def recuperar(login:str) -> dict:
        conexao, cursor = Conexao().conectar()

        try:
            if conexao == None:
                print('Erro ao tentar conectar')
                return None

            cursor.execute('''
                            SELECT cod_categoria, categoria, login FROM tb_categorias
                            WHERE login = %s
                            ''',
                            [login])

            categorias = cursor.fetchall()
            conexao.close()
            print(categorias)

        except:
            print('Erro ao exibir categorias')
            return False
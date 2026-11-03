from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    @staticmethod
    def adcionar (login:str, descricao:str, data:str, valor:float, cod_categoria:int) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False

        try:
            cursor.execute('''
                            INSERT INTO tb_despesas(login, descricao, data, hora, valor)
                            VALUES (%s, %s, %s, %s, %s)
                            ''',
                            [login, descricao, data, valor, cod_categoria])
            cod_despesas = cursor.lastrowid

            conexao.commit()
            conexao.close
            return cod_despesas

        except Exception as erro:
            print(f'ERRO AO INSERIR {erro}')
            return False



    @staticmethod
    def recuperar(login:str) -> dict:
        conexao, cursor = Conexao().conectar()

        try:
            if conexao == None:
                print('Erro ao tentar conectar')
                return None

            cursor.execute('''
                            SELECT login, descricao, data, valor, id categoria login FROM tb_despesas
                            WHERE login = %s
                            ''',
                            [login])

            categorias = cursor.fetchall()
            conexao.close()
            print(categorias)

        except Exception as erro:
            print(f'ERRO AO INSERIR {erro}')
            return False



    @staticmethod
    def recuperar_por_categoria(login:str, cod_categoria:int) -> dict:
        conexao, cursor = Conexao().conectar()

        try:
            if conexao == None:
                print('Erro ao tentar conectar')
                return None

            cursor.execute('''
                            SELECT login, descricao, data, valor, id categoria login FROM tb_despesas
                            login = %s
                            cod_categoria = %s,
                            ''',
                            [login, cod_categoria])

            categorias = cursor.fetchall()
            conexao.close()
            print(categorias)

        except Exception as erro:
            print(f'ERRO AO INSERIR {erro}')
            return False



    @staticmethod
    def excluir (cod_despesa: int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False
        
        try:
            cursor.execute('''
                            DELETE FROM tb_despesas
                            WHERE cod_despesa = %s
                            ''',
                            [cod_despesa])

            conexao.commit()
            conexao.close()
            print(f'Categoria {cod_despesa} excluida!')
            return True

        except:
            print('Erro ao excluir categoria!')
            return False




    @staticmethod
    def alterar (cod_despesa:int, login:str, descricao:str, data:str, valor:float, cod_categoria:int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False

        try:
            cursor.execute('''
                            UPDATE tb_despesas SET
                                cod_categoria = %s,
                                descricao = %s,
                                valor = %s,
                                data = %s
                            WHERE
                                cod_despesa = %s
                                AND login = %s;
                            ''',
                            [cod_categoria, descricao, valor, data, cod_despesa, login])
            cod_despesas = cursor.lastrowid

            conexao.commit()
            conexao.close
            return cod_despesas

        except Exception as erro:
            print(f'ERRO AO INSERIR {erro}')
            return False
from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print('Erro ao tentar conectar!')
            return False

        try:
            cursor.execute('''
                            INSERT INTO tb_usuarios(login, senha)
                            VALUES (%s, %s)                     
                            ''',
                            [login, senha])
            conexao.commit()
            conexao.close()

            return True

        except:
            print('Ja existe esse usuário!')
            return False

    @staticmethod
    def verificar(login:str, senha:str) -> dict:
        conexao, cursor = Conexao().conectar()

        if conexao == None:
            print("Erro ao tentar conectar!")
            return None

        cursor.execute('''
                        SELECT login, senha FROM tb_usuarios
                        WHERE login = %s
                        AND senha = %s;                     
                        ''',
                        [login, senha])
        
        resultado = cursor.fetchone()
        conexao.close()

        return resultado
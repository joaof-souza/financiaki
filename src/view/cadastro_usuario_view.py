import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.bgcolor = '#fff'

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='Cadastro de Usuario')

        self.campo_usuario = ft.TextField(label='Usuário')
        self.campo_senha = ft.TextField(label='Senha',
                                   password=True,
                                   can_reveal_password=True)

        botao_cadastrar = ft.Button(content='CADASTRAR',
                                    on_click=self.cadastrar)
        
        botao_voltar = ft.Button(content='VOLTAR PARA O LOGIN')


        linha_botoes = ft.Row(controls=[botao_cadastrar,botao_voltar],
                             alignment='center')


        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         linha_botoes]


    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        Usuario().cadastrar(usuario,senha)
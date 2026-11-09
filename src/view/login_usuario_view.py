import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina =pagina

        self.route = '/login'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='Login')

        self.campo_usuario = ft.TextField(label='Usuário')
        self.campo_senha = ft.TextField(label='Senha',
                                   password=True,
                                   can_reveal_password=True)

        botao_login = ft.Button(content='LOGIN',
                                    on_click= self.login)
        
        botao_cadastrese = ft.Button(content='CADASTRE-SE',
                                     on_click=self.ir_para_cadastrar)


        linha_botoes = ft.Row(controls=[botao_login,botao_cadastrese],
                             alignment='center')


        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         linha_botoes]


    def login(self):

        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        if Usuario().verificar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Login efetuado com sucesso!",color="#69ec48")))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("O usuário ou senha estão incorretos.", color="#ce2222")))

    async def ir_para_cadastrar(self):
        await self.pagina.push_route('/cadastro')
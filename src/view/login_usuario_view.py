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

        self.campo_usuario = ft.TextField(label='Usuário',
                                          width=300)
        
        self.campo_senha = ft.TextField(label='Senha',
                                   password=True,
                                   can_reveal_password=True,
                                   width=300)

        botao_login = ft.OutlinedButton(content='LOGIN',
                                on_click= self.login,
                                width=300,
                                height=45,
                                style= ft.ButtonStyle(
                                                      color="#707070",
                                                      overlay_color="#E0E0E0",
                                                      shape=ft.RoundedRectangleBorder(radius=5),
                                                      side=ft.BorderSide(width=0.3, color="#000000"),
                                                      elevation=0)
                                )
        
        botao_cadastrese = ft.OutlinedButton(content='CADASTRE-SE',
                                    on_click=self.ir_para_cadastrar,
                                    width=300,
                                    height=45,
                                    style= ft.ButtonStyle(
                                                      color="#707070",
                                                      overlay_color="#E0E0E0",
                                                      shape=ft.RoundedRectangleBorder(radius=5),
                                                      side=ft.BorderSide(width=0.3, color="#000000"),
                                                      elevation=0)
                                )


        coluna_botoes = ft.Column(controls=[botao_login,botao_cadastrese],
                             alignment='center')


        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         coluna_botoes]


    def login(self):

        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        if Usuario().verificar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Login efetuado com sucesso!",
                                                                color="#ffffff", text_align='center'),
                                                                bgcolor="#8FBC8F"
                                                                ))
            self.pagina.navigate('/inicio')

            
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("O usuário ou senha estão incorretos.",
                                                        color="#ffffff", text_align='center'),
                                                        bgcolor='#E06666'
                                                        ))

    def ir_para_cadastrar(self):
        self.pagina.navigate('/cadastro')
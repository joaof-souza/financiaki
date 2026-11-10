import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina =pagina

        self.route = '/cadastro'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        logo = ft.Image(src='img/logo2.png',
                        width=500)

        titulo = ft.Text(value='CADASTRE UM NOVO USUÁRIO')

        self.campo_usuario = ft.TextField(label='Usuário',
                                          
                                          width=300)
        self.campo_senha = ft.TextField(label='Senha',
                                   password=True,
                                   can_reveal_password=True,
                                   
                                   width=300)

        botao_cadastrar = ft.OutlinedButton(content='CADASTRAR',
                                    on_click=self.cadastrar,
                                width=300,
                                height=45,
                                style= ft.ButtonStyle(
                                                      color="#707070",
                                                      overlay_color="#E0E0E0",
                                                      shape=ft.RoundedRectangleBorder(radius=5),
                                                      side=ft.BorderSide(width=0.3, color="#000000"),
                                                      elevation=0)
                                    )
        
        botao_voltar = ft.OutlinedButton(content='VOLTAR PARA O LOGIN',
                                on_click=self.ir_para_login,                                 
                                width=300,
                                height=45,
                                style= ft.ButtonStyle(
                                                      color="#707070",
                                                      overlay_color="#E0E0E0",
                                                      shape=ft.RoundedRectangleBorder(radius=5),
                                                      side=ft.BorderSide(width=0.3, color="#000000"),
                                                      elevation=0)
                                
                                
                                )



        coluna_botoes = ft.Column(controls=[botao_cadastrar,botao_voltar],
                             alignment='center')


        self.controls = [logo,
                         titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         coluna_botoes]


    def cadastrar(self):
        #verifica se existem valores nos campos
        if self.campo_usuario.value == "" or self.campo_senha.value == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Você não pode cadastrar campos sem valor!",
                                                                color="#FFFFFF", text_align='center'),
                                                                bgcolor='#E06666'
                                                                ))
            return False
        
        else:
            usuario = self.campo_usuario.value
            senha = self.campo_senha.value

        #snackbar de status do cadastro
        if Usuario().cadastrar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Usuário cadastrado com sucesso!",
                                                        color="#FFFFFF", text_align='center'),
                                                        bgcolor='#8FBC8F'
                                                        ))
            self.pagina.navigate('/inicio')


        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Esse nome de usuário já está sendo usado por outra pessoa. Tente uma combinação diferente.",
                                                        color="#FFFFFF", text_align='center'),
                                                        bgcolor='#E06666'
                                                        ))


    def ir_para_login(self):
        self.pagina.navigate('/login')
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

        titulo = ft.Text(value='Cadastro de Usuario')

        self.campo_usuario = ft.TextField(label='Usuário')
        self.campo_senha = ft.TextField(label='Senha',
                                   password=True,
                                   can_reveal_password=True)

        botao_cadastrar = ft.Button(content='CADASTRAR',
                                    on_click=self.cadastrar)
        
        botao_voltar = ft.Button(content='VOLTAR PARA O LOGIN',
                                 on_click=self.ir_para_login)


        linha_botoes = ft.Row(controls=[botao_cadastrar,botao_voltar],
                             alignment='center')


        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         linha_botoes]


    def cadastrar(self):
        #verifica se existem valores nos campos
        if self.campo_usuario.value == "" or self.campo_senha.value == "":
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Você não pode cadastrar campos sem valor!",color="#ce2222")))
            return False
        
        else:
            usuario = self.campo_usuario.value
            senha = self.campo_senha.value

        #snackbar de status do cadastro
        if Usuario().cadastrar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Usuário cadastrado com sucesso!",color="#69ec48")))


        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Esse nome de usuário já está sendo usado por outra pessoa. Tente uma combinação diferente.", color="#ce2222")))


    async def ir_para_login(self):
        await self.pagina.push_route('/login')
import flet as ft

class PaginaInicialView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina =pagina

        self.route = '/inicio'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='Pagina Inicial BB')

        dados_usuario = pagina.session.store.get('usuario_logado')

        if not dados_usuario:
            self.pagina.navigate('/login')
            return

        nome_usuario = dados_usuario["login"]
        self.pagina.show_dialog(ft.SnackBar(content=ft.Text(f"Login efetuado com sucesso. Seja bem vindo {nome_usuario}!",
                                                                color="#ffffff", text_align='center'),
                                                                bgcolor="#8FBC8F"
                                                                ))

        self.controls = [titulo]
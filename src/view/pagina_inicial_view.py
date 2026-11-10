import flet as ft
from src.model.usuario_model import Usuario

class PaginaInicialView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina =pagina

        self.route = '/inicio'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='Pagina Inicial BB')


        self.controls = [titulo]
import flet as ft
from src.model.categoria_model import Categoria

class CadastroCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = '/categoria'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='categorias')

        self.campo_categoria = ft.TextField(label='Nome da categoria',
                                            width=300)

        botao_cadastrar = ft.IconButton(icon=ft.Icons.ADD,
                                        tooltip='Cadastrar Categoria')
        
        linha_cadastrar = ft.Row(controls=[self.campo_categoria, botao_cadastrar],
                                 alignment='center')

        self.controls=[titulo,
                       linha_cadastrar]


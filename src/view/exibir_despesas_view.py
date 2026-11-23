import flet as ft
from src.model.despesa_model import Despesas


class ExibirDespesasView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = '/todas_despesas'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        titulo = ft.Text(value='TODAS AS SUAS CATEGORIAS')

        tabela = ft.DataTable(columns=[ft.DataColumn(label='ID DA CATEGORIA'),
                                       ft.DataColumn(label='DESCRICAO'),
                                       ft.DataColumn(label='CATEGORIA'),
                                       ft.DataColumn(label='VALOR'),
                                       ft.DataColumn(label='DATA'),],
                                       rows=[ft.DataRow()])

        self.controls=[titulo]
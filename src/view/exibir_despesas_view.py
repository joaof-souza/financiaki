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

        dados_usuario = pagina.session.store.get('usuario_logado')
        self.usuario = dados_usuario['login']

        titulo = ft.Text(value='TODAS AS SUAS CATEGORIAS')

        self.lista_despesas = []

        tabela = ft.DataTable(columns=[ft.DataColumn(label='ID DA CATEGORIA'),
                                       ft.DataColumn(label='DESCRICAO'),
                                       ft.DataColumn(label='CATEGORIA'),
                                       ft.DataColumn(label='VALOR'),
                                       ft.DataColumn(label='DATA'),],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()

        self.controls=[titulo, tabela]

    def atualizar_lista_despesas(self):
        despesas = Despesas().recuperar(self.usuario)

        for despesa in despesas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(despesa.get('cod_categoria')))),
                    ft.DataCell(ft.Text(str(despesa.get('descricao')))),
                    ft.DataCell(ft.Text(str(despesa.get('cod_categoria')))),
                    ft.DataCell(ft.Text(str(despesa.get('valor')))),
                    ft.DataCell(ft.Text(str(despesa.get('data')))),
                ]
            )

            self.lista_despesas.append(linha)

        self.pagina.update()
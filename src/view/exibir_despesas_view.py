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

        tabela = ft.DataTable(columns=[ft.DataColumn(label='ID DA DESPESA'),
                                       ft.DataColumn(label='DESCRICAO'),
                                       ft.DataColumn(label='CATEGORIA'),
                                       ft.DataColumn(label='VALOR'),
                                       ft.DataColumn(label='DATA'),
                                       ft.DataColumn(label='EXCLUIR')],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()

        self.controls=[titulo, tabela]

    def atualizar_lista_despesas(self):
        self.lista_despesas.clear()
        despesas = Despesas().recuperar(self.usuario)

        for despesa in despesas:
            id_despesa = str(despesa.get('cod_despesa'))

            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(id_despesa)),
                    ft.DataCell(ft.Text(str(despesa.get('descricao')))),
                    ft.DataCell(ft.Text(str(despesa.get('categoria')))),
                    ft.DataCell(ft.Text(str(despesa.get('valor')))),
                    ft.DataCell(ft.Text(str(despesa.get('data')))),
                    ft.DataCell(ft.IconButton(icon=ft.Icons.DELETE,
                                              key=id_despesa,
                                              on_click=self.excluir_despesa)) #id despesa aqui
                ]
            )

            self.lista_despesas.append(linha)

        self.pagina.update()


    def excluir_despesa(self,botao):
        id_despesa = botao.control.key
        Despesas().excluir(id_despesa)
        self.atualizar_lista_despesas()
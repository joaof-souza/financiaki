import flet as ft
from src.model.despesa_model import Despesas
from src.model.categoria_model import Categoria


class ExibirDespesasPorCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = '/despesa_p_categoria'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'

        dados_usuario = pagina.session.store.get('usuario_logado')
        self.usuario = dados_usuario['login']

        titulo = ft.Text(value='TODAS AS SUAS CATEGORIAS')

        opcoes_categoria = []

        categorias = Categoria().recuperar(self.usuario)

        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get('cod_categoria'),
                                            text=categoria.get('categoria'))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(options= opcoes_categoria,
                                      on_select=self.atualizar_lista_despesas)

        self.lista_despesas = []

        tabela = ft.DataTable(columns=[ft.DataColumn(label='ID DA DESPESA'),
                                       ft.DataColumn(label='DESCRICAO'),
                                       ft.DataColumn(label='CATEGORIA'),
                                       ft.DataColumn(label='VALOR'),
                                       ft.DataColumn(label='DATA'),
                                       ft.DataColumn(label='')],
                                       rows=self.lista_despesas)

        self.atualizar_lista_despesas()

        self.controls=[titulo,
                       self.campo_categoria,
                       tabela]

    def atualizar_lista_despesas(self):
        self.lista_despesas.clear()

        id_categoria = self.campo_categoria.value

        despesas = Despesas().recuperar_por_categoria(self.usuario,id_categoria)

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
import flet as ft
from src.model.despesa_model import Despesas
from src.model.categoria_model import Categoria

class CadastroDespesasView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = '/c_despesa'

        self.bgcolor = "#ECEDEF"

        self.vertical_alignment = 'CENTER'
        self.horizontal_alignment = 'CENTER'


        dados_usuario = pagina.session.store.get('usuario_logado')
        self.usuario = dados_usuario['login']
    

        titulo = ft.Text(value='DESPESAS')


        campo_descricao = ft.TextField(label='Descrição',
                                       width=300)

        campo_valor = ft.TextField(label='Valor',
                                   keyboard_type=ft.KeyboardType.NUMBER,
                                   width=300)

        campo_data = ft.TextField(label='Data',
                                  width=300)

        categorias = Categoria().recuperar(self.usuario)

        opcoes = []

        for categoria in categorias:
            opcoes.append(ft.DropdownOption(key=categoria.get('cod_categoria'),
                                            text=categoria.get('categoria')))

        campo_categoria = ft.Dropdown(options=opcoes)

        botao_adicionar = ft.IconButton(ft.Icons.ADD,
                                        tooltip='Cadastrar Despesa')

        self.controls=[titulo,
                       campo_descricao,
                       campo_valor,
                       campo_data,
                       campo_categoria,
                       botao_adicionar]
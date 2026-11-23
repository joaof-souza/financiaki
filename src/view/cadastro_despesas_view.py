import flet as ft
from src.model.despesa_model import Despesas

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
        
        categorias_salvas = pagina.session.store.get('categoria_salva')
        self.id_categoria = categorias_salvas['cod_categorias']

        titulo = ft.Text(value='DESPESAS')


        campo_descricao = ft.TextField(label='Descrição',
                                       width=300)

        campo_valor = ft.TextField(label='Valor',
                                   keyboard_type=ft.KeyboardType.NUMBER)

        campo_data = ft.DatePicker()




        self.controls=[titulo]
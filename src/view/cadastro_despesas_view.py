import flet as ft
from src.model.despesa_model import Despesas
from src.model.categoria_model import Categoria
from datetime import datetime

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


        self.campo_descricao = ft.TextField(label='Descrição',
                                       width=300)

        self.campo_valor = ft.TextField(label='Valor',
                                   keyboard_type=ft.KeyboardType.NUMBER,
                                   width=300)

        self.campo_data = ft.TextField(label='Data',
                                  width=300,
                                  hint_text='DD/MM/YYYY')

        self.categorias = Categoria().recuperar(self.usuario)

        opcoes = []

        for categoria in self.categorias:
            opcoes.append(ft.DropdownOption(key=categoria.get('cod_categoria'),
                                            text=categoria.get('categoria')))

        self.campo_categoria = ft.Dropdown(options=opcoes,
                                           width=300)

        botao_adicionar = ft.IconButton(ft.Icons.ADD,
                                        tooltip='Cadastrar Despesa',
                                        on_click=self.cadastrar_despesa)

        self.controls=[titulo,
                       self.campo_descricao,
                       self.campo_valor,
                       self.campo_data,
                       self.campo_categoria,
                       botao_adicionar]


    def cadastrar_despesa(self):
        categoria = self.campo_categoria.value
        descricao = self.campo_descricao.value
        valor = self.campo_valor.value
        texto_data = self.campo_data.value

        data = datetime.strptime(texto_data,'%d/%m/%Y').date()

        if self.campo_descricao.value == '' or self.campo_valor.value == '' or self.campo_data.value == '' or self.campo_categoria.value == '':
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Você não pode cadastrar campos sem valor.",
                                                                            color="#FFFFFF", text_align='center'),
                                                                            bgcolor='#E06666'
                                                                            ))
            return False

        resultado = Despesas.adcionar(self.usuario, descricao, data, valor, categoria)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(f"Cadastro realizado com sucesso!",
                                                        color="#ffffff", text_align='center'),
                                                        bgcolor="#8FBC8F"
                                                        ))
            self.campo_categoria.value=''
            self.campo_descricao.value=''
            self.campo_valor.value=''
            self.campo_data.value=''

            self.pagina.update()
            return True

        else:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Erro ao cadastrar.",
                                                                color="#FFFFFF", text_align='center'),
                                                                bgcolor='#E06666'
                                                        ))

            return False
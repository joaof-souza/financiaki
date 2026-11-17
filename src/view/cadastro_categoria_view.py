import flet as ft
from src.model.categoria_model import Categoria
from src.model.usuario_model import Usuario

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
                                        tooltip='Cadastrar Categoria',
                                        on_click=self.cadastrar)
        
        linha_cadastrar = ft.Row(controls=[self.campo_categoria, botao_cadastrar],
                                 alignment='center')

        self.controls=[titulo,
                       linha_cadastrar]

    def cadastrar(self):
        if self.campo_categoria.value == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Você não pode cadastrar campos sem valor!",
                                                                color="#FFFFFF", text_align='center'),
                                                                bgcolor='#E06666'
                                                                ))
            return False

        else:
            categoria = self.campo_categoria.value
            usuario = Usuario.login.value


        if Categoria().adicionar(usuario,categoria):
            print('oi')
            return True
        

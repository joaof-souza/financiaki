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

        dados_usuario = pagina.session.store.get('usuario_logado')
        self.usuario = dados_usuario['login']



        titulo = ft.Text(value='categorias')

        self.campo_categoria = ft.TextField(label='Nome da categoria',
                                            width=300)

        botao_cadastrar = ft.IconButton(icon=ft.Icons.ADD,
                                        tooltip='Cadastrar Categoria',
                                        on_click=self.cadastrar)
        

        titulo_lista = ft.Text(value='CATEGORIAS CADASTRADAS')

        self.lista_categorias = []

        coluna_lista_categorias = ft.Column(controls=self.lista_categorias)

        self.atualizar_lista_categorias()

        
        linha_cadastrar = ft.Row(controls=[self.campo_categoria, botao_cadastrar],
                                 alignment='center')

        self.controls=[titulo,
                       linha_cadastrar,
                       titulo_lista,
                       coluna_lista_categorias]




    def cadastrar(self): 
        if self.campo_categoria.value == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Você não pode cadastrar campos sem valor.",
                                                                color="#FFFFFF", text_align='center'),
                                                                bgcolor='#E06666'
                                                                ))
            return False


        resultado = Categoria.adicionar(self.usuario, self.campo_categoria.value)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(f"Cadastro realizado com sucesso!",
                                                        color="#ffffff", text_align='center'),
                                                        bgcolor="#8FBC8F"
                                                        ))
            

        else:
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text("Erro ao cadastrar.",
                                                                color="#FFFFFF", text_align='center'),
                                                                bgcolor='#E06666'
                                                        ))
        self.atualizar_lista_categorias()
            
    
    def atualizar_lista_categorias(self):
        categorias = Categoria().recuperar(self.usuario)
        self.lista_categorias.clear()

        if categorias:

            for categoria in categorias:
                nome_categoria = categoria.get('categoria')
                texto = ft.Text(value=nome_categoria)
                self.lista_categorias.append(texto)

        self.pagina.update()

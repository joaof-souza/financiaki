import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.pagina_inicial_view import PaginaInicialView

def main(pagina:ft.Page):

    def navegacao(component):
        item_clicado = component.control.selected_index
        if item_clicado == 0:
            pagina.navigate('/categoria')
        elif item_clicado == 1:
            pagina.navigate('/')
        elif item_clicado == 2:
            pagina.navigate('/')
        elif item_clicado == 3:
            pagina.navigate('/')
        elif item_clicado == 4:
            pagina.navigate('/login')

    barra_navegacao = ft.NavigationBar(destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.CIRCLE, label='Categoria'),
        ft.NavigationBarDestination(icon=ft.Icons.SIGNAL_CELLULAR_CONNECTED_NO_INTERNET_0_BAR_ROUNDED, label='Adicionar Despesa'),
        ft.NavigationBarDestination(icon=ft.Icons.TEXT_ROTATION_ANGLEDOWN_OUTLINED, label='Todas Despesas'),
        ft.NavigationBarDestination(icon=ft.Icons.DIRECTIONS_RAILWAY_FILLED_OUTLINED, label='Despesas por Categoria'),
        ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label='Sair')
                                                    ],
                                                    on_change=navegacao
    )

    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == '/cadastro':
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == '/login':
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_login_usuario)

        elif pagina.route == '/inicio':
            tela_inicial = PaginaInicialView(pagina)
            pagina.views.append(tela_inicial)
            tela_inicial.navigation_bar = barra_navegacao

        pagina.update()

    
    pagina.on_route_change = roteamento
    roteamento()

    #abrindo pagina inicial
    pagina.navigate('/login')
ft.run(main)
import flet as ft
from screens.login_screen import LoginScreen
from screens.produto_screen import ProdutoScreen
from screens.permissoes_screen import PermissoesScreen

def main(page: ft.Page):
    page.title = "Sistema Cafeteria"
    page.window_width = 500
    page.window_height = 600
    page.window_center()

    # Função para mudar de tela
    def mudar_tela(nome_tela):
        page.controls.clear()
        if nome_tela == "login":
            LoginScreen(page, mudar_tela)
        elif nome_tela == "home":
            HomeScreen(page, mudar_tela)
        elif nome_tela == "produto":
            ProdutoScreen(page, mudar_tela)
        elif nome_tela == "permissoes":
            PermissoesScreen(page, mudar_tela)
        elif nome_tela == "sucesso":
            SucessoScreen(page, mudar_tela)
        page.update()

    # Tela inicial
    mudar_tela("login")

# Rodar o app
ft.app(target=main)

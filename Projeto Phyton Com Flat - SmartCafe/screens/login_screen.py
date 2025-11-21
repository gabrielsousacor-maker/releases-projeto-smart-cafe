import flet as ft
from utils.json_loader import carregar_dados_usuario

def LoginScreen(page, mudar_tela):
    usuario = ft.TextField(label="Usuário", width=300)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    erro = ft.Text("", color="red", visible=False)

    def fazer_login(e):
        dados_usuario = carregar_dados_usuario()
        if usuario.value == dados_usuario["usuario"] and senha.value == dados_usuario["senha"]:
            erro.visible = False
            mudar_tela("home")
        else:
            erro.value = "Usuário ou senha incorretos!"
            erro.visible = True
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Image(src="assets/logo.png", width=160),
                ft.Text("ACESSO AO SISTEMA", size=24, weight="bold"),
                usuario,
                senha,
                erro,
                ft.ElevatedButton("Entrar", width=300, on_click=fazer_login)
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    )

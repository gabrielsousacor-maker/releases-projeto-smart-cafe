import flet as ft

def SucessoScreen(page, mudar_tela):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Ação realizada com sucesso!", size=24, weight="bold", color="green"),
                ft.ElevatedButton("Voltar ao Dashboard", width=300, on_click=lambda e: mudar_tela("home"))
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    )

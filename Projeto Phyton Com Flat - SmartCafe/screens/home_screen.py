import flet as ft

def HomeScreen(page, mudar_tela):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Dashboard", size=24, weight="bold"),
                ft.ElevatedButton("Produto", width=300, on_click=lambda e: mudar_tela("produto")),
                ft.ElevatedButton("Permissões", width=300, on_click=lambda e: mudar_tela("permissoes")),
                ft.ElevatedButton("Sucesso", width=300, on_click=lambda e: mudar_tela("sucesso")),
                ft.ElevatedButton("Sair", width=300, on_click=lambda e: mudar_tela("login"))
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    )

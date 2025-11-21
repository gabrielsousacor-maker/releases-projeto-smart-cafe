import flet as ft
from utils.json_loader import carregar_dados_usuario

def PermissoesScreen(page, mudar_tela):
    dados = carregar_dados_usuario()

    # Se "acoes" for string, transforma em lista separando por "|"
    acoes = dados["acoes"]
    if isinstance(acoes, str):
        acoes = [a.strip() for a in acoes.split("|")]

    page.add(
        ft.Column(
            controls=[
                ft.Text("Permissões do Usuário", size=24, weight="bold"),
                ft.Text(f"Nome: {dados['nome']}"),
                ft.Text(f"Nível: {dados['nivel']}"),
                ft.Text("Ações Permitidas:", weight="bold"),
                ft.Column([ft.Text(f"- {acao}") for acao in acoes]),
                ft.ElevatedButton("Voltar", on_click=lambda e: mudar_tela("home"))
            ],
            alignment="start",
            horizontal_alignment="center"
        )
    )

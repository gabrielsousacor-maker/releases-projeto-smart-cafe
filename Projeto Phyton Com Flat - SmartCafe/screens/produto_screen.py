import flet as ft
from utils.json_loader import carregar_dados_produto

def ProdutoScreen(page, mudar_tela):
    # Carrega os dados do produto do arquivo JSON
    produto = carregar_dados_produto()

    page.add(
        ft.Column(
            controls=[
                # Usa a imagem salva em static/cafeteria.jpg
                ft.Image(src="static/cafeteria.jpg", width=220),
                ft.Text(produto["nome"], size=24, weight="bold"),
                ft.Text(f"Código: {produto['codigo']}"),
                ft.Text(f"Preço: {produto['preco']}"),
                ft.Text("Descrição:", weight="bold"),
                ft.Text(produto["descricao"]),
                ft.Text("Características:", weight="bold"),
                ft.Column([ft.Text(f"- {c}") for c in produto["caracteristicas"]]),
                ft.ElevatedButton("Voltar", on_click=lambda e: mudar_tela("home"))
            ],
            alignment="start",
            horizontal_alignment="center"
        )
    )

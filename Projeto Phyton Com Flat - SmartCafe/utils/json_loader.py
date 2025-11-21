import json

def carregar_dados_produto():
    with open("data/produto.json", "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_dados_usuario():
    with open("data/usuario.json", "r", encoding="utf-8") as f:
        return json.load(f)

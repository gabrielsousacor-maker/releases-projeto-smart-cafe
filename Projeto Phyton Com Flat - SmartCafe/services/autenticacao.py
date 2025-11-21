from utils.json_loader import carregar_dados_usuario

def validar_login(usuario, senha):
    dados = carregar_dados_usuario()
    return usuario == dados["usuario"] and senha == dados["senha"]

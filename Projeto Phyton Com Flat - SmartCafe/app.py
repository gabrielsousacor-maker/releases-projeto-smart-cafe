import PySimpleGUI as sg
from utils.json_loader import carregar_dados_produto, carregar_dados_usuario
from services.autenticacao import validar_login

sg.theme("SystemDefault")

def tela_login():
    layout = [
        [sg.Text("LOGIN", font=("Arial", 20), justification="center", expand_x=True)],
        [sg.Text("Usuário:", font=("Arial", 12))],
        [sg.Input(key="usuario", font=("Arial", 12))],
        [sg.Text("Senha:", font=("Arial", 12))],
        [sg.Input(key="senha", password_char="*", font=("Arial", 12))],
        [sg.Button("Entrar", key="entrar", expand_x=True, button_color=("white", "#007BFF"))],
        [sg.Text("", key="erro", text_color="red")]
    ]
    return sg.Window("Login", layout, element_justification="center")

def tela_dashboard(usuario):
    layout = [
        [sg.Text(f"Bem-vindo, {usuario}!", font=("Arial", 18))],
        [sg.Button("Produto", expand_x=True)],
        [sg.Button("Permissões", expand_x=True)],
        [sg.Button("Sucesso", expand_x=True)],
        [sg.Button("Sair", button_color=("white", "#D9534F"), expand_x=True)],
    ]
    return sg.Window("Dashboard", layout)

def tela_produto():
    dados = carregar_dados_produto()
    layout = [
        [sg.Text("Produto", font=("Arial", 20))],
        [sg.Text(f"Nome: {dados['nome']}")],
        [sg.Text(f"Código: {dados['codigo']}")],
        [sg.Text(f"Preço: {dados['preco']}")],
        [sg.Text(f"Descrição: {dados['descricao']}")],
        [sg.Text(f"Características: {dados['caracteristicas']}")],
        [sg.Button("OK", expand_x=True)]
    ]
    return sg.Window("Produto", layout)

def tela_permissoes():
    dados = carregar_dados_usuario()
    layout = [
        [sg.Text("Permissões do Usuário", font=("Arial", 20))],
        [sg.Text(f"Nome: {dados['nome']}")],
        [sg.Text(f"Nível: {dados['nivel']}")],
        [sg.Text(f"Ações Permitidas: {', '.join(dados['acoes'])}")],
        [sg.Button("OK", expand_x=True)]
    ]
    return sg.Window("Permissões", layout)

def tela_sucesso():
    layout = [
        [sg.Text("Ação realizada com sucesso!", font=("Arial", 20), text_color="green")],
        [sg.Button("Voltar ao Dashboard", expand_x=True)]
    ]
    return sg.Window("Sucesso", layout)

# Execução principal
janela_login = tela_login()
janela_dashboard = None
janela_produto = None
janela_permissoes = None
janela_sucesso = None

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        window.close()
        if window == janela_login:
            break

    if window == janela_login and event == "entrar":
        usuario = values["usuario"]
        senha = values["senha"]
        if validar_login(usuario, senha):
            janela_dashboard = tela_dashboard(usuario)
            janela_login.close()
        else:
            janela_login["erro"].update("Usuário ou senha incorretos.")

    if window == janela_dashboard:
        if event == "Produto":
            janela_produto = tela_produto()
        elif event == "Permissões":
            janela_permissoes = tela_permissoes()
        elif event == "Sucesso":
            janela_sucesso = tela_sucesso()
        elif event == "Sair":
            janela_dashboard.close()
            janela_login = tela_login()

    if window == janela_produto and event == "OK":
        janela_produto.close()

    if window == janela_permissoes and event == "OK":
        janela_permissoes.close()

    if window == janela_sucesso and event == "Voltar ao Dashboard":
        janela_sucesso.close()

class Usuario:
    def __init__(self, usuario, senha, nome, nivel, acoes):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.nivel = nivel
        self.acoes = acoes

    def __str__(self):
        return f"{self.nome} - {self.nivel}"

class Produto:
    def __init__(self, nome, codigo, preco, descricao, caracteristicas):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.descricao = descricao
        self.caracteristicas = caracteristicas

    def __str__(self):
        return f"{self.nome} ({self.codigo}) - {self.preco}"

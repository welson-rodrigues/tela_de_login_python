class Usuario:
    proximo_codigo = 1

    def __init__(self, nome, senha):
        self.codigo = Usuario.proximo_codigo
        Usuario.proximo_codigo += 1
        self.nome = nome
        self.senha = senha

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Senha: {self.senha}"

# O usuarios.txt ficou na ordem codigo:usuario:senha

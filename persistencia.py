class Usuario:
    proximo_codigo = 1

    def __init__(self, codigo, nome, senha):
        self.codigo = codigo
        self.nome = nome
        self.senha = senha

def cadastrar_usuario(usuario, arquivo="usuarios.txt"):
    try:
        with open(arquivo, "a") as file:
            file.write(f"{usuario.codigo}:{usuario.nome}:{usuario.senha}\n")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False

def buscar_usuario(criterio, valor, arquivo="usuarios.txt"):
    try:
        with open(arquivo, "r") as file:
            for line in file:
                codigo, nome, senha = line.strip().split(":")
                if criterio == "codigo" and int(valor) == int(codigo):
                    return Usuario(int(codigo), nome, senha)
                elif criterio == "nome" and valor == nome:
                    return Usuario(int(codigo), nome, senha)
        return None
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None

def excluir_usuario(codigo, arquivo="usuarios.txt"):
    try:
        with open(arquivo, "r") as file:
            linhas = file.readlines()

        with open(arquivo, "w") as file:
            for linha in linhas:
                codigo_atual, _str_, _str_ = linha.strip().split(":")
                if int(codigo_atual) != int(codigo):
                    file.write(linha)

        return True
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
        return False

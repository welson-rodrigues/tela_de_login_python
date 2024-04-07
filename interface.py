from guizero import App, TextBox, PushButton, Text, Box, Window, error, info, Picture
from persistencia import Usuario, cadastrar_usuario, buscar_usuario, excluir_usuario

def criar_codigo_unico():
    return Usuario.proximo_codigo

def cadastrar_novo_usuario():
    novo_codigo = criar_codigo_unico()
    Usuario.proximo_codigo += 1
    novo_usuario = Usuario(novo_codigo, campo_novo_usuario.value, campo_nova_senha.value)
    if cadastrar_usuario(novo_usuario):
        info("Sucesso", "Usuário cadastrado com sucesso.")
    else:
        error("Erro", "Erro ao cadastrar usuário.")
def verificar_login():
    usuario = campo_usuario.value
    senha = campo_senha.value
    acesso_permitido = False

    with open("usuarios.txt", "r") as file:
        for line in file:
            proximo_codigo, user, senhas = line.strip().split(":")
            if usuario == user and senha == senhas:
                acesso_permitido = True
                break

    if acesso_permitido:
        abrir_janela_principal()
        tela_login.hide()
    else:
        app.warn("Atenção", "Acesso negado.")

def buscar_usuario_por_nome():
    nome_usuario = campo_buscar_nome.value
    usuario_encontrado = buscar_usuario("nome", nome_usuario)
    if usuario_encontrado:
        info("Sucesso", "Usuário encontrado com sucesso")
        print(f"Usuário encontrado: {usuario_encontrado.nome}")
    else:
        app.warn("Atenção", "Usuário não encontrado.")

def excluir_usuario_por_codigo():
    codigo_usuario = campo_excluir_codigo.value
    if excluir_usuario(codigo_usuario):
        info("Sucesso", "Usuário excluído com sucesso.")
    else:
        error("Error", "Erro ao excluir usuário.")

def abrir_janela_principal():
    janela_principal = Window(app, title="Janela", width=400, height=300)
    texto_principal = Text(janela_principal, text="Janela aberta. Dados validados com sucesso!", color="white")
    janela_principal.show()
    janela_principal.bg = "#008080"
    imagem_janela = Picture(janela_principal, image="ifrn.jpg", height=500,  width=500)

def botao_clicado():
    fechar = app.yesno("Atenção", "Tem certeza que deseja cancelar a Aplicação?")
    if fechar == True:
        app.info("Cancelada", "Aplicação cancelada.")
        app.destroy()
    else:
        app.info("Voltar", "Ok, voltando para a Aplicação")

def fechar_janela():
    info("Fechando", "Fechando a aplicação....")
    app.destroy()
    
app = App("Login", width=400, height=210)

box_usuario = Box(app, align="top")
imagem_usuario = Picture(box_usuario, image="usuario.png", align="left", height=11,  width=11)
texto_usuario = Text(box_usuario, text="Usuário:", align="left", color="white")
campo_usuario = TextBox(box_usuario, align="left")

box_senha = Box(app, align="top")
imagem_senha = Picture(box_senha, image="senha.png", align="left", height=11,  width=11)
texto_senha = Text(box_senha, text="Senha:", align="left", color="white")
campo_senha = TextBox(box_senha, align="left", hide_text=True)

box_novo_usuario = Box(app, align="top")
imagem_novo = Picture(box_novo_usuario, image="usuario.png", align="left", height=11,  width=11)
texto_novo_usuario = Text(box_novo_usuario, text="Novo Usuário:", align="left", color="white")
campo_novo_usuario = TextBox(box_novo_usuario, align="left")
imagem_nova_senha = Picture(box_novo_usuario, image="senha.png", align="left", height=11,  width=11)
texto_nova_senha = Text(box_novo_usuario, text="Nova Senha:", align="left", color="white")
campo_nova_senha = TextBox(box_novo_usuario, align="left", hide_text=True)

box_buscar_usuario = Box(app, align="top")
imagem_nome = Picture(box_buscar_usuario, image="nome.png", align="left", height=11,  width=11)
texto_buscar_nome = Text(box_buscar_usuario, text="Buscar por Nome:", align="left", color="white")
campo_buscar_nome = TextBox(box_buscar_usuario, align="left")
botao_buscar_nome = PushButton(box_buscar_usuario, text="Buscar", command=buscar_usuario_por_nome, align="left")

box_excluir_usuario = Box(app, align="top")
imagem_excluir = Picture(box_excluir_usuario, image="excluir.png", align="left", height=11,  width=11)
texto_excluir_codigo = Text(box_excluir_usuario, text="Excluír por Código:",align="left", color="white")
campo_excluir_codigo = TextBox(box_excluir_usuario, align="left")
botao_excluir_usuario = PushButton(box_excluir_usuario, text="Excluir", command=excluir_usuario_por_codigo, align="left")

box_botoes = Box(app, align="top")
botao_cancelar = PushButton(box_botoes, text="Cancelar", align="left", command=botao_clicado)
botao_logar = PushButton(box_botoes, text="Entrar", command=verificar_login, align="left")

botao_cadastrar_usuario = PushButton(box_botoes, text="Cadastrar Usuário", command=cadastrar_novo_usuario, align="left")

botao_logar.bg= "#708090"
botao_cancelar.bg= "#708090"
botao_cadastrar_usuario.bg="#708090"
botao_excluir_usuario.bg="#708090"
botao_buscar_nome.bg="#708090"
texto_novo_usuario.text_color="blue"
texto_usuario.text_color= "blue"
texto_senha.text_color="blue"
texto_nova_senha.text_color="blue"
texto_buscar_nome.text_color="blue"
texto_excluir_codigo.text_color="blue"

image = "usuario.png"

tela_login = app

app.when_closed = fechar_janela

app.display()

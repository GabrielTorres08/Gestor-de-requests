class templates():

    def corpo_mensagem_00(id, nome, email, idade, admin):
        mensagem = f"""
        <h1>Dados do seu cadastro:</h1>
        <hr>
        <p><str>ID:</str> {id}</p>
        <p><str>Nome:</str> {nome}</p>
        <p><str>E-mail:</str> {email}</p>
        <p><str>Idade:</str> {idade}</p>
        <p><str>Admin:</str> {"True" if admin == 1 else "False"}</p>
        """
        return mensagem
    
    def assunto_conversa00():
        return "Consulta de dados"
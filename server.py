from flask import Flask, jsonify, request
from rich import inspect
from enviar_email import enviar_email
from template_email import templates
from BD import DB_ADM

Banco_dados = DB_ADM()


app = Flask(__name__)

@app.route("/enviar_email")
def enviar_email_rota():
    id_user = request.args.get("id")
    existe = Banco_dados.existeBD(id_user)

    if existe:
        template = templates 
        dados = Banco_dados.pegarDados(id_user)
        enviar_email(destinatario=dados[2], corpo_mensagem=template.corpo_mensagem_00(dados[0],dados[1],dados[2],dados[3],dados[4]), assunto_conversa="Consulta de dados")
        return "Existe"
    else:
        return "Esse usuário não existe"


@app.route("/pegar_dados")
def pegar_dados():
    id_user = request.args.get("id")
    existe = Banco_dados.existeBD(id_user)

    if existe:
        dados_user = Banco_dados.pegarDados(id_user)
        json_infos = {
            "ID": f"{dados_user[0]}",
            "Nome": f"{dados_user[1]}",
            "Email": f"{dados_user[2]}",
            "Idade": f"{dados_user[3]}",
            "Admin": f"{True if dados_user[4] == 1 else False}"
        }
        return jsonify(json_infos)
    else: 
        json_infos = {"ID": None,
            "Nome": None,
            "Email": None,
            "Idade": None,
            "Admin": None}
        return jsonify(json_infos)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
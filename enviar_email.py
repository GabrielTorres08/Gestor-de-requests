import smtplib
import email.message
from dotenv import load_dotenv
import os
load_dotenv()

def enviar_email(destinatario=os.environ['EMAIL_PROVEDOR'], corpo_mensagem="<p>Nenhuma mensagem foi atribuíada a esse E-mail</p>", assunto_conversa="Conversa sem título"):

    try:
        corpo_email = corpo_mensagem

        msg = email.message.Message()
        msg['Subject'] = assunto_conversa
        msg['From'] = os.environ['EMAIL_PROVEDOR']
        msg['To'] = destinatario
        password = os.environ['SENHA']

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        # Login Credentials for sending the mail

        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    except smtplib.SMTPAuthenticationError:
        print("❌ Erro de autenticação (email ou senha inválidos)")

    except smtplib.SMTPRecipientsRefused:
        print("❌ Destinatário recusado (email inválido)")

    except smtplib.SMTPServerDisconnected:
        print("❌ Servidor desconectou")

    except smtplib.SMTPException as e:
        print(f"❌ Erro SMTP geral: {e}")

    except Exception as e:
        print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")


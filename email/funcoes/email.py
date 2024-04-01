import email.message
import getpass
import smtplib
import ssl


def set_servidor_usuario(pergunta):
    while True:
        dado = str(input(pergunta)).strip()
        if dado == "":
            print("Informação inválida")
        else:
            break
    return dado


def set_servidor_senha():
    while True:
        dado = getpass.getpass(prompt="Informe a senha do seu gmail: ")
        if dado == "":
            print("Informação inválida")
        else:
            break
    return dado


def envia_email(emails):
    try:
        gmail_login = set_servidor_usuario('Informe o seu login do gmail: ')
        gmail_senha = set_servidor_senha()
        gmail_assunto = set_servidor_usuario('Informe o assunto do e-mail: ')
        gmail_texto = set_servidor_usuario('Informe o texto do e-mail: ')

        context = ssl.create_default_context()

        mensagem = email.message.EmailMessage()
        mensagem["From"] = gmail_login
        mensagem["Subject"] = gmail_assunto
        mensagem["To"] = ','.join(emails)

        mensagem.add_header("Content-Type", "text/html")
        mensagem.set_payload(gmail_texto)

        servico = smtplib.SMTP(host="smtp.gmail.com", port=587)
        servico.starttls(context=context)
        servico.login(user=gmail_login, password=gmail_senha)
        servico.sendmail(mensagem["From"], mensagem["To"],
                         mensagem.as_string().encode("utf-8"))
    except smtplib.SMTPAuthenticationError as e:
        print("Erro ao tentar enviar e-mails com a autentificação fornecida.")
    finally:
        servico.quit()

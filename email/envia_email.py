from funcoes import mensagens, menu, valida_email, email as modulo_envia_email


if __name__ == "__main__":
    mensagens.mensagem_acesso_sistema()
    opcao = menu.opcaoes_menu()
    match opcao:
        case 1:
            lista_emais = list()
            while True:
                email = str(input("informe um e-mail: ")).strip().lower()
                if valida_email.email_valido(email):
                    lista_emais.append(email)
                    break
                else:
                    mensagens.email_invalido()

            while True:
                if mensagens.mensagem_adiciona_Email():
                    email = str(input("informe um e-mail: ")).strip().lower()
                    if valida_email.email_valido(email) and lista_emais.count(email) == 0:
                        lista_emais.append(email)
                    else:
                        print("E-mail inválido ou e-mail já informado")
                        if mensagens.ver_lista_email():
                            for count, email in enumerate(lista_emais):
                                print(f"{count + 1} - {email}")
                else:
                    modulo_envia_email.envia_email(lista_emais)
                    mensagens.mensagem_saida_sistema()
                    break
        case 2:
            mensagens.mensagem_saida_sistema()

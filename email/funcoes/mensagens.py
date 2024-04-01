def mensagem_acesso_sistema():
    print("-"*50)
    print("{:^50}".format("Bem vindo(a) ao sistema para enviar e-mails"))


def mensagem_saida_sistema():
    print("Obrigado por usar o sistema de envio de e-mail.\nVolte sempre!")


def email_invalido():
    print("\033[31mE-mail informado é inválido.\033[m")


def email_repetido():
    print("\033[31mE-mail já informado.\033[m")


def menu_opcao_invalida():
    print("\033[31mOpção inválida.\033[m")


def menu_campo_vazio():
    print("\033[31mCampo não pode ser vazio.\033[m")


def sair_do_sistema():
    bool_sair = False
    while True:
        sair = str(input("Deseja Sair do sistema [S/N]: ")).strip().upper()[0]
        if "S" in sair:
            bool_sair = True
            break
        elif "N" in sair:
            bool_sair = False
            break
        else:
            print("\033[31mDados informado inválido.\nInforme [S/N]\033[m")
    return bool_sair


def mensagem_adiciona_Email():
    bool_adiciona_email = True
    while True:
        adiciona = str(
            input("Deseja adicionar mais e-mail [S/N]: ")).strip().upper()[0]
        if "S" in adiciona:
            bool_adiciona_email = True
            break
        elif "N" in adiciona:
            bool_adiciona_email = False
            break
        else:
            print("\033[31mDados informado inválido.\nInforme [S/N]\033[m")
    return bool_adiciona_email


def ver_lista_email():
    boo_ver = False
    while True:
        ver = str(
            input("Deseja ver os e-mails informados [S/N]: ")).strip().upper()[0]
        if "S" in ver:
            boo_ver = True
            break
        elif "N" in ver:
            boo_ver = False
            break
        else:
            print("\033[31mDados informado inválido.\nInforme [S/N]\033[m")
    return boo_ver

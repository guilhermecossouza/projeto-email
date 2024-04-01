from funcoes import mensagens


def opcaoes_menu():
    lista_menu = ["Enviar e-mail", "Sair do programa"]
    print("-"*50)
    print("{:^50}".format("MENU"))
    for countador, opcao in enumerate(lista_menu):
        print(f"{countador + 1} - {opcao}")

    while True:
        try:
            numero_opcao = int(input("Qual a sua opção: "))
            if 0 < numero_opcao <= 2:
                break
            else:
                print("\033[31mOpção informada inválida.\033[m")
        except ValueError:
            print("\033[31mOpção informada inválida.\033[m")
    return numero_opcao

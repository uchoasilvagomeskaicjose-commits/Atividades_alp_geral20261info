#códigos sistema menu e login

while True:
    print("\n=== SISTEMA DE CADASTRO DE USUÁRIOS ===")
    usuario = input("Login: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("Login realizado com sucesso!")

        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("Usuário logado:", usuario)
            print("1 - Inserir usuário")
            print("2 - Pesquisar usuário")
            print("3 - Remover usuário")
            print("4 - Listar usuários")
            print("5 - Logout")
            print("6 - Encerrar")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 5:
                print("Logout realizado!")
                break

            elif opcao == 6:
                print("Programa encerrado!")
                exit()

            else:
                print("Essa opção ainda não funciona.")

    else:
        print("Login ou senha incorretos!")
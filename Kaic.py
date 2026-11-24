logado = False
usuario_logado = ""

# Lista para armazenar apenas os nomes dos usuários
usuarios = []

while True:
    print("\033c", end="")  # comando para limpar a tela
    print("#########################################")
    print("SISTEMA DE CADASTRO DE USUÁRIOS")
    print("#########################################\n")

    if not logado:
        print("===LOGIN===")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "admin" and senha == "123":
            print(f"Login realizado com sucesso! Bem-vindo, {login}!\n")
            input("ENTER para continuar...")
            logado = True
            usuario_logado = login
        else:
            input("\nLogin ou senha incorretos! ENTER para tentar novamente.")

    else:
        print("===MENU PRINCIPAL===")
        print(f"Usuário logado: {usuario_logado}")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n=== INSERIR USUÁRIO ===")
            novo_usuario = input("Digite o nome do novo usuário: ")
            
            if novo_usuario in usuarios:
                print("Este usuário já está cadastrado!")
            else:
                usuarios.append(novo_usuario)
                print(f"Usuário '{novo_usuario}' cadastrado com sucesso!")
            
            input("\nENTER para continuar...")

        elif opcao == "2":
            print("\n=== PESQUISAR USUÁRIO ===")
            pesquisa = input("Digite o nome do usuário que deseja pesquisar: ")
            
            if pesquisa in usuarios:
                print(f"O usuário '{pesquisa}' foi encontrado no sistema.")
            else:
                print("Usuário não encontrado.")
            
            input("\nENTER para continuar...")

        elif opcao == "3":
            print("\n=== REMOVER USUÁRIO ===")
            remover = input("Digite o nome do usuário que deseja remover: ")
            
            if remover in usuarios:
                usuarios.remove(remover)
                print(f"Usuário '{remover}' removido com sucesso!")
            else:
                print("Usuário não encontrado.")
            
            input("\nENTER para continuar...")

        elif opcao == "4":
            print("\n=== LISTAR TODOS OS USUÁRIOS ===")
            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado no momento.")
            else:
                for i, u in enumerate(usuarios, 1):
                    print(f"{i} - {u}")
            
            input("\nENTER para continuar...")

        elif opcao == "5":
            print("Fazendo logout...")
            input("ENTER para voltar para o login.")
            usuario_logado = ""
            logado = False

        elif opcao == "6":
            print("Encerrando o sistema... Até logo!")
            break

        else:
            input("Opção inválida! ENTER para continuar...")

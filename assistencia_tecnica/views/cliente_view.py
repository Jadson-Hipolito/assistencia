from controllers.cliente_controller import ClienteController

cliente_controller = ClienteController()

def menu_cliente():
    while True:
        print("\n--- Menu Cliente ---")
        print("1. Cadastrar Cliente")
        print("2. Consultar Cliente")
        print("3. Alterar Cliente")
        print("4. Excluir Cliente")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nasc = input("Data Nascimento (YYYY-MM-DD): ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            cliente = cliente_controller.cadastrar_cliente(nome, cpf, data_nasc, endereco, telefone)
            print(f"Cliente {cliente.nome} cadastrado com ID {cliente.id_cliente}")
        elif opcao == "2":
            id_cliente = int(input("ID do cliente: "))
            cliente = cliente_controller.consultar_cliente(id_cliente)
            if cliente:
                print(vars(cliente))
            else:
                print("Cliente não encontrado.")
        elif opcao == "3":
            id_cliente = int(input("ID do cliente: "))
            nome = input("Novo nome (enter para manter): ")
            endereco = input("Novo endereço (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")
            cliente_controller.alterar_cliente(id_cliente, nome=nome, endereco=endereco, telefone=telefone)
            print("Alteração realizada.")
        elif opcao == "4":
            id_cliente = int(input("ID do cliente: "))
            if cliente_controller.excluir_cliente(id_cliente):
                print("Cliente excluído.")
            else:
                print("Cliente não encontrado.")
        elif opcao == "5":
            break


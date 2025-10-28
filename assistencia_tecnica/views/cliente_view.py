from models.cliente import Cliente

def menu_cliente():
    while True:
        print("\n--- Menu Cliente ---")
        print("1. Cadastrar Cliente")
        print("2. Consultar Cliente")
        print("3. Alterar Cliente")
        print("4. Excluir Cliente")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            consultar_cliente()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_cliente():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    cpf = input("CPF: ")
    cliente = Cliente(nome=nome, endereco=endereco, contato=contato, cpf=cpf)
    cliente.salvar()
    print(f"Cliente cadastrado com sucesso! ID: {cliente.id_cliente}")

def consultar_cliente():
    id_cliente = int(input("ID do Cliente: "))
    cliente = Cliente.consultar(id_cliente)
    if cliente:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, Contato: {cliente.contato}, CPF: {cliente.cpf}")
    else:
        print("Cliente não encontrado.")

def alterar_cliente():
    id_cliente = int(input("ID do Cliente a alterar: "))
    cliente = Cliente.consultar(id_cliente)
    if not cliente:
        print("Cliente não encontrado.")
        return
    nome = input(f"Nome [{cliente.nome}]: ") or cliente.nome
    endereco = input(f"Endereço [{cliente.endereco}]: ") or cliente.endereco
    contato = input(f"Contato [{cliente.contato}]: ") or cliente.contato
    cpf = input(f"CPF [{cliente.cpf}]: ") or cliente.cpf
    cliente.nome = nome
    cliente.endereco = endereco
    cliente.contato = contato
    cliente.cpf = cpf
    cliente.salvar()
    print("Cliente alterado com sucesso!")

def excluir_cliente():
    id_cliente = int(input("ID do Cliente a excluir: "))
    Cliente.excluir(id_cliente)
    print("Cliente excluído com sucesso!")


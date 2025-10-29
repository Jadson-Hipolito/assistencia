from models.cliente import Cliente
from validadores import validar_nome, validar_endereco, validar_contato, validar_cpf

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
    if not validar_nome(nome):
        print("Nome inválido.")
        return

    endereco = input("Endereço: ")
    if not validar_endereco(endereco):
        print("Endereço inválido.")
        return

    contato = input("Contato: ")
    if not validar_contato(contato):
        print("Contato inválido. Use formato com DDD e número.")
        return

    cpf = input("CPF: ")
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return

    cliente = Cliente(nome=nome, endereco=endereco, contato=contato, cpf=cpf)
    cliente.salvar()
    print(f"Cliente cadastrado com sucesso! ID: {cliente.id_cliente}")

def consultar_cliente():
    try:
        id_cliente = int(input("ID do Cliente: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = Cliente.consultar(id_cliente)
    if cliente:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, Contato: {cliente.contato}, CPF: {cliente.cpf}")
    else:
        print("Cliente não encontrado.")

def alterar_cliente():
    try:
        id_cliente = int(input("ID do Cliente a alterar: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = Cliente.consultar(id_cliente)
    if not cliente:
        print("Cliente não encontrado.")
        return

    nome = input(f"Nome [{cliente.nome}]: ") or cliente.nome
    if not validar_nome(nome):
        print("Nome inválido.")
        return

    endereco = input(f"Endereço [{cliente.endereco}]: ") or cliente.endereco
    if not validar_endereco(endereco):
        print("Endereço inválido.")
        return

    contato = input(f"Contato [{cliente.contato}]: ") or cliente.contato
    if not validar_contato(contato):
        print("Contato inválido.")
        return

    cpf = input(f"CPF [{cliente.cpf}]: ") or cliente.cpf
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return

    cliente.nome = nome
    cliente.endereco = endereco
    cliente.contato = contato
    cliente.cpf = cpf
    cliente.salvar()
    print("Cliente alterado com sucesso!")

def excluir_cliente():
    try:
        id_cliente = int(input("ID do Cliente a excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    Cliente.excluir(id_cliente)
    print("Cliente excluído com sucesso!")

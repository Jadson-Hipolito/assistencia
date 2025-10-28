from models.equipamento import Equipamento

def menu_equipamentos():
    while True:
        print("\n--- Menu Equipamentos ---")
        print("1. Cadastrar Equipamento")
        print("2. Consultar Equipamento")
        print("3. Alterar Equipamento")
        print("4. Excluir Equipamento")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            consultar_equipamento()
        elif opcao == "3":
            alterar_equipamento()
        elif opcao == "4":
            excluir_equipamento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_equipamento():
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    numero_serie = input("Número de Série: ")
    id_cliente = int(input("ID do Cliente: "))
    equipamento = Equipamento(tipo=tipo, marca=marca, modelo=modelo, numero_serie=numero_serie, id_cliente=id_cliente)
    equipamento.salvar()
    print(f"Equipamento cadastrado com sucesso! ID: {equipamento.id_equipamento}")

def consultar_equipamento():
    id_equipamento = int(input("ID do Equipamento: "))
    equipamento = Equipamento.consultar(id_equipamento)
    if equipamento:
        print(f"ID: {equipamento.id_equipamento}, Tipo: {equipamento.tipo}, Marca: {equipamento.marca}, Modelo: {equipamento.modelo}, Número Série: {equipamento.numero_serie}, ID Cliente: {equipamento.id_cliente}")
    else:
        print("Equipamento não encontrado.")

def alterar_equipamento():
    id_equipamento = int(input("ID do Equipamento a alterar: "))
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        print("Equipamento não encontrado.")
        return
    equipamento.tipo = input(f"Tipo [{equipamento.tipo}]: ") or equipamento.tipo
    equipamento.marca = input(f"Marca [{equipamento.marca}]: ") or equipamento.marca
    equipamento.modelo = input(f"Modelo [{equipamento.modelo}]: ") or equipamento.modelo
    equipamento.numero_serie = input(f"Número Série [{equipamento.numero_serie}]: ") or equipamento.numero_serie
    cliente_input = input(f"ID Cliente [{equipamento.id_cliente}]: ") or equipamento.id_cliente
    equipamento.id_cliente = int(cliente_input)
    equipamento.salvar()
    print("Equipamento alterado com sucesso!")

def excluir_equipamento():
    id_equipamento = int(input("ID do Equipamento a excluir: "))
    Equipamento.excluir(id_equipamento)
    print("Equipamento excluído com sucesso!")


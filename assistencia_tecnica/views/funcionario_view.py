from models.funcionario import Funcionario

def menu_funcionarios():
    while True:
        print("\n--- Menu Funcionários ---")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Alterar Funcionário")
        print("4. Excluir Funcionário")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            consultar_funcionario()
        elif opcao == "3":
            alterar_funcionario()
        elif opcao == "4":
            excluir_funcionario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_funcionario():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    horario = input("Horário: ")
    salario = float(input("Salário: "))
    cnpj = input("CNPJ: ")
    funcionario = Funcionario(nome=nome, endereco=endereco, contato=contato, horario=horario, salario=salario, cnpj=cnpj)
    funcionario.salvar()
    print(f"Funcionário cadastrado com sucesso! ID: {funcionario.id_funcionario}")

def consultar_funcionario():
    id_funcionario = int(input("ID do Funcionário: "))
    funcionario = Funcionario.consultar(id_funcionario)
    if funcionario:
        print(f"ID: {funcionario.id_funcionario}, Nome: {funcionario.nome}, Endereço: {funcionario.endereco}, Contato: {funcionario.contato}, Horário: {funcionario.horario}, Salário: {funcionario.salario}, CNPJ: {funcionario.cnpj}, Ativo: {funcionario.ativo}")
    else:
        print("Funcionário não encontrado.")

def alterar_funcionario():
    id_funcionario = int(input("ID do Funcionário a alterar: "))
    funcionario = Funcionario.consultar(id_funcionario)
    if not funcionario:
        print("Funcionário não encontrado.")
        return
    funcionario.nome = input(f"Nome [{funcionario.nome}]: ") or funcionario.nome
    funcionario.endereco = input(f"Endereço [{funcionario.endereco}]: ") or funcionario.endereco
    funcionario.contato = input(f"Contato [{funcionario.contato}]: ") or funcionario.contato
    funcionario.horario = input(f"Horário [{funcionario.horario}]: ") or funcionario.horario
    funcionario.salario = input(f"Salário [{funcionario.salario}]: ") or funcionario.salario
    funcionario.cnpj = input(f"CNPJ [{funcionario.cnpj}]: ") or funcionario.cnpj
    ativo_input = input(f"Ativo [{funcionario.ativo}]: ")
    funcionario.ativo = bool(int(ativo_input)) if ativo_input else funcionario.ativo
    funcionario.salvar()
    print("Funcionário alterado com sucesso!")

def excluir_funcionario():
    id_funcionario = int(input("ID do Funcionário a excluir: "))
    Funcionario.excluir(id_funcionario)
    print("Funcionário excluído com sucesso!")


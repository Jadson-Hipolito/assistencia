from models.funcionario import Funcionario
from validadores import (
    validar_nome,
    validar_endereco,
    validar_contato,
    validar_horario,
    validar_salario,
    validar_cnpj,
    validar_id_funcionario
)
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
    if not validar_nome(nome):
        print("Nome inválido.")
        return

    endereco = input("Endereço: ")
    if not validar_endereco(endereco):
        print("Endereço inválido.")
        return

    contato = input("Contato: ")
    if not validar_contato(contato):
        print("Contato inválido.")
        return

    horario = input("Horário (ex: 08:00 - 17:00): ")
    if not validar_horario(horario):
        print("Horário inválido.")
        return

    try:
        salario = float(input("Salário: "))
        if not validar_salario(salario):
            print("Salário inválido.")
            return
    except ValueError:
        print("Salário deve ser numérico.")
        return

    cnpj = input("CNPJ: ")
    if not validar_cnpj(cnpj):
        print("CNPJ inválido.")
        return

    funcionario = Funcionario(
        nome=nome, endereco=endereco, contato=contato,
        horario=horario, salario=salario, cnpj=cnpj
    )
    funcionario.salvar()
    print(f"Funcionário cadastrado com sucesso! ID: {funcionario.id_funcionario}")

def consultar_funcionario():
    try:
        id_funcionario = int(input("ID do Funcionário: "))
        if not validar_id_funcionario(id_funcionario):
            print("ID inválido.")
            return
    except ValueError:
        print("ID deve ser um número inteiro.")
        return

    funcionario = Funcionario.consultar(id_funcionario)
    if funcionario:
        print(f"ID: {funcionario.id_funcionario}, Nome: {funcionario.nome}, Endereço: {funcionario.endereco}, Contato: {funcionario.contato}, Horário: {funcionario.horario}, Salário: {funcionario.salario}, CNPJ: {funcionario.cnpj}, Ativo: {funcionario.ativo}")
    else:
        print("Funcionário não encontrado.")

def alterar_funcionario():
    try:
        id_funcionario = int(input("ID do Funcionário a alterar: "))
        if not validar_id_funcionario(id_funcionario):
            print("ID inválido.")
            return
    except ValueError:
        print("ID deve ser um número inteiro.")
        return

    funcionario = Funcionario.consultar(id_funcionario)
    if not funcionario:
        print("Funcionário não encontrado.")
        return

    nome = input(f"Nome [{funcionario.nome}]: ") or funcionario.nome
    if not validar_nome(nome):
        print("Nome inválido.")
        return

    endereco = input(f"Endereço [{funcionario.endereco}]: ") or funcionario.endereco
    if not validar_endereco(endereco):
        print("Endereço inválido.")
        return

    contato = input(f"Contato [{funcionario.contato}]: ") or funcionario.contato
    if not validar_contato(contato):
        print("Contato inválido.")
        return

    horario = input(f"Horário [{funcionario.horario}]: ") or funcionario.horario
    if not validar_horario(horario):
        print("Horário inválido.")
        return

    salario_input = input(f"Salário [{funcionario.salario}]: ")
    try:
        salario = float(salario_input) if salario_input else funcionario.salario
        if not validar_salario(salario):
            print("Salário inválido.")
            return
    except ValueError:
        print("Salário deve ser numérico.")
        return

    cnpj = input(f"CNPJ [{funcionario.cnpj}]: ") or funcionario.cnpj
    if not validar_cnpj(cnpj):
        print("CNPJ inválido.")
        return

    ativo_input = input(f"Ativo [{funcionario.ativo}]: ")
    funcionario.ativo = bool(int(ativo_input)) if ativo_input else funcionario.ativo

    funcionario.nome = nome
    funcionario.endereco = endereco
    funcionario.contato = contato
    funcionario.horario = horario
    funcionario.salario = salario
    funcionario.cnpj = cnpj

    funcionario.salvar()
    print("Funcionário alterado com sucesso!")

def excluir_funcionario():
    try:
        id_funcionario = int(input("ID do Funcionário a excluir: "))
        if not validar_id_funcionario(id_funcionario):
            print("ID inválido.")
            return
    except ValueError:
        print("ID deve ser um número inteiro.")
        return

    Funcionario.excluir(id_funcionario)
    print("Funcionário excluído com sucesso!")
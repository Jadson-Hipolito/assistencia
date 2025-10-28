from models.conta import Conta

def menu_contas():
    while True:
        print("\n--- Menu Contas ---")
        print("1. Registrar Conta Receber")
        print("2. Pagar Conta")
        print("3. Consultar Conta")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_conta()
        elif opcao == "2":
            pagar_conta()
        elif opcao == "3":
            consultar_conta()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def registrar_conta():
    id_os = int(input("ID da Ordem de Serviço: "))
    valor = float(input("Valor da Conta: "))
    conta = Conta(id_os=id_os, valor=valor, tipo='Receber')
    conta.salvar()
    print(f"Conta registrada com sucesso! ID: {conta.id_conta}")

def pagar_conta():
    contas = Conta.listar_pendentes()
    if not contas:
        print("Não há contas pendentes.")
        return
    print("Contas Pendentes:")
    for c in contas:
        print(f"ID: {c.id_conta}, Valor: {c.valor}, ID OS: {c.id_os}")
    id_conta = int(input("ID da Conta a pagar: "))
    conta = Conta.consultar(id_conta)
    if conta:
        conta.pagar()
        print("Conta paga com sucesso!")
    else:
        print("Conta não encontrada.")

def consultar_conta():
    id_conta = int(input("ID da Conta: "))
    conta = Conta.consultar(id_conta)
    if conta:
        print(f"ID Conta: {conta.id_conta}, Valor: {conta.valor}, Status: {conta.status}, Tipo: {conta.tipo}, ID OS: {conta.id_os}")
    else:
        print("Conta não encontrada.")


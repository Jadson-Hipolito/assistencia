from models.cliente import Cliente
from models.funcionario import Funcionario
from models.equipamento import Equipamento
from models.ordem_servico import OrdemServico
from models.visita_tecnica import VisitaTecnica
from models.conta import Conta

def menu_principal():
    print("\n=== Sistema de Assistência Técnica ===")
    print("1. Clientes")
    print("2. Funcionários")
    print("3. Equipamentos")
    print("4. Ordens de Serviço")
    print("5. Visitas Técnicas")
    print("6. Contas")
    print("0. Sair")
    return input("Escolha uma opção: ")

# -----------------------------
# Menu Clientes
# -----------------------------
def menu_clientes():
    print("\n--- Menu Clientes ---")
    print("1. Cadastrar Cliente")
    print("2. Consultar Cliente")
    print("3. Alterar Cliente")
    print("4. Excluir Cliente")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def cadastrar_cliente():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    cpf = input("CPF: ")
    cliente = Cliente(nome=nome, endereco=endereco, contato=contato, cpf=cpf)
    cliente.salvar()
    print(f"Cliente {cliente.nome} cadastrado com sucesso! ID: {cliente.id_cliente}")

def consultar_cliente():
    id_cliente = int(input("ID do Cliente: "))
    cliente = Cliente.consultar(id_cliente)
    if cliente:
        print(cliente.__dict__)
    else:
        print("Cliente não encontrado.")

def alterar_cliente():
    id_cliente = int(input("ID do Cliente: "))
    cliente = Cliente.consultar(id_cliente)
    if not cliente:
        print("Cliente não encontrado.")
        return
    cliente.nome = input(f"Nome ({cliente.nome}): ") or cliente.nome
    cliente.endereco = input(f"Endereço ({cliente.endereco}): ") or cliente.endereco
    cliente.contato = input(f"Contato ({cliente.contato}): ") or cliente.contato
    cliente.cpf = input(f"CPF ({cliente.cpf}): ") or cliente.cpf
    cliente.salvar()
    print("Cliente atualizado com sucesso!")

def excluir_cliente():
    id_cliente = int(input("ID do Cliente: "))
    Cliente.excluir(id_cliente)
    print("Cliente excluído com sucesso!")

# -----------------------------
# Menu Funcionários
# -----------------------------
def menu_funcionarios():
    print("\n--- Menu Funcionários ---")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Alterar Funcionário")
    print("4. Excluir Funcionário")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def cadastrar_funcionario():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    horario = input("Horário: ")
    salario = float(input("Salário: "))
    cnpj = input("CNPJ: ")
    funcionario = Funcionario(nome=nome, endereco=endereco, contato=contato, horario=horario, salario=salario, cnpj=cnpj)
    funcionario.salvar()
    print(f"Funcionário {funcionario.nome} cadastrado com sucesso! ID: {funcionario.id_funcionario}")

# -----------------------------
# Menu Equipamentos
# -----------------------------
def menu_equipamentos():
    print("\n--- Menu Equipamentos ---")
    print("1. Cadastrar Equipamento")
    print("2. Consultar Equipamento")
    print("3. Alterar Equipamento")
    print("4. Excluir Equipamento")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def cadastrar_equipamento():
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    numero_serie = input("Número de Série: ")
    id_cliente = int(input("ID do Cliente: "))
    equipamento = Equipamento(tipo=tipo, marca=marca, modelo=modelo, numero_serie=numero_serie, id_cliente=id_cliente)
    equipamento.salvar()
    print(f"Equipamento {equipamento.marca} cadastrado com sucesso! ID: {equipamento.id_equipamento}")

# -----------------------------
# Menu Ordens de Serviço
# -----------------------------
def menu_ordens_servico():
    print("\n--- Menu Ordens de Serviço ---")
    print("1. Abrir Ordem de Serviço")
    print("2. Consultar Ordem de Serviço")
    print("3. Alterar Ordem de Serviço")
    print("4. Encerrar Ordem de Serviço")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def abrir_ordem_servico():
    id_cliente = int(input("ID do Cliente: "))
    descricao = input("Descrição do Problema: ")
    os = OrdemServico(id_cliente=id_cliente, descricao=descricao)
    os.salvar()
    print(f"Ordem de Serviço aberta com sucesso! ID: {os.id_os}")

# -----------------------------
# Menu Visitas Técnicas
# -----------------------------
def menu_visitas():
    print("\n--- Menu Visitas Técnicas ---")
    print("1. Agendar Visita Técnica")
    print("2. Consultar Visita Técnica")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def agendar_visita():
    id_os = int(input("ID da Ordem de Serviço: "))
    data = input("Data (AAAA-MM-DD): ")
    horario = input("Horário: ")
    tecnico = input("Técnico Responsável: ")
    visita = VisitaTecnica(id_os=id_os, data=data, horario=horario, tecnico=tecnico)
    visita.salvar()
    print(f"Visita Técnica agendada com sucesso! ID: {visita.id_visita}")

# -----------------------------
# Menu Contas
# -----------------------------
def menu_contas():
    print("\n--- Menu Contas ---")
    print("1. Registrar Conta a Receber")
    print("2. Pagar Conta")
    print("3. Consultar Conta")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def registrar_conta():
    id_os = int(input("ID da Ordem de Serviço: "))
    valor = float(input("Valor: "))
    conta = Conta(id_os=id_os, valor=valor)
    conta.salvar()
    print(f"Conta registrada com sucesso! ID: {conta.id_conta}")

def pagar_conta():
    id_conta = int(input("ID da Conta a Pagar: "))
    conta = Conta.consultar(id_conta)
    if not conta:
        print("Conta não encontrada.")
        return
    conta.status = "Pago"
    conta.salvar()
    print(f"Conta {conta.id_conta} paga com sucesso!")

# -----------------------------
# Loop Principal
# -----------------------------
def main():
    while True:
        print("\n=== Sistema Assistência Técnica ===")
        print("1. Clientes")
        print("2. Funcionários")
        print("3. Equipamentos")
        print("4. Ordens de Serviço")
        print("5. Visitas Técnicas")
        print("6. Contas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sub = menu_clientes()
            # Aqui você chamaria funções como cadastrar_cliente(), consultar_cliente()...
        elif opcao == "2":
            sub = menu_funcionarios()
            # Chamar funções de funcionário
        elif opcao == "3":
            sub = menu_equipamentos()
            # Chamar funções de equipamento
        elif opcao == "4":
            sub = menu_ordens_servico()
            # Chamar funções de OS
        elif opcao == "5":
            sub = menu_visitas()
            # Chamar funções de visita
        elif opcao == "6":
            sub = menu_contas()
            # Chamar funções de conta
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

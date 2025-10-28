from models.ordem_servico import OrdemServico

def menu_ordens_servico():
    while True:
        print("\n--- Menu Ordens de Serviço ---")
        print("1. Abrir Ordem de Serviço")
        print("2. Consultar Ordem de Serviço")
        print("3. Alterar Ordem de Serviço")
        print("4. Excluir Ordem de Serviço")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_ordem_servico()
        elif opcao == "2":
            consultar_ordem_servico()
        elif opcao == "3":
            alterar_ordem_servico()
        elif opcao == "4":
            excluir_ordem_servico()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def abrir_ordem_servico():
    id_cliente = int(input("ID do Cliente: "))
    descricao = input("Descrição do serviço: ")
    os_ = OrdemServico(id_cliente=id_cliente, descricao=descricao)
    os_.salvar()
    print(f"Ordem de Serviço aberta com sucesso! ID: {os_.id_os}")

def consultar_ordem_servico():
    id_os = int(input("ID da Ordem de Serviço: "))
    os_ = OrdemServico.consultar(id_os)
    if os_:
        print(f"ID OS: {os_.id_os}, ID Cliente: {os_.id_cliente}, Descrição: {os_.descricao}, Status: {os_.status}, Data Abertura: {os_.data_abertura}, Data Encerramento: {os_.data_encerramento}")
    else:
        print("Ordem de Serviço não encontrada.")

def alterar_ordem_servico():
    id_os = int(input("ID da Ordem de Serviço a alterar: "))
    os_ = OrdemServico.consultar(id_os)
    if not os_:
        print("Ordem de Serviço não encontrada.")
        return
    os_.descricao = input(f"Descrição [{os_.descricao}]: ") or os_.descricao
    os_.status = input(f"Status [{os_.status}]: ") or os_.status
    os_.salvar()
    print("Ordem de Serviço alterada com sucesso!")

def excluir_ordem_servico():
    id_os = int(input("ID da Ordem de Serviço a excluir: "))
    OrdemServico.excluir(id_os)
    print("Ordem de Serviço excluída com sucesso!")


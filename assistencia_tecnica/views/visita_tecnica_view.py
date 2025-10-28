from models.visita_tecnica import VisitaTecnica

def menu_visitas_tecnicas():
    while True:
        print("\n--- Menu Visitas Técnicas ---")
        print("1. Agendar Visita Técnica")
        print("2. Consultar Visita Técnica")
        print("3. Alterar Visita Técnica")
        print("4. Excluir Visita Técnica")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agendar_visita()
        elif opcao == "2":
            consultar_visita()
        elif opcao == "3":
            alterar_visita()
        elif opcao == "4":
            excluir_visita()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def agendar_visita():
    id_os = int(input("ID da Ordem de Serviço: "))
    data = input("Data (AAAA-MM-DD): ")
    horario = input("Horário (HH:MM): ")
    tecnico = input("Técnico responsável: ")
    visita = VisitaTecnica(id_os=id_os, data=data, horario=horario, tecnico=tecnico)
    visita.salvar()
    print(f"Visita técnica agendada com sucesso! ID: {visita.id_visita}")

def consultar_visita():
    id_visita = int(input("ID da Visita Técnica: "))
    visita = VisitaTecnica.consultar(id_visita)
    if visita:
        print(f"ID Visita: {visita.id_visita}, ID OS: {visita.id_os}, Data: {visita.data}, Horário: {visita.horario}, Técnico: {visita.tecnico}")
    else:
        print("Visita técnica não encontrada.")

def alterar_visita():
    id_visita = int(input("ID da Visita Técnica a alterar: "))
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        print("Visita técnica não encontrada.")
        return
    visita.data = input(f"Data [{visita.data}]: ") or visita.data
    visita.horario = input(f"Horário [{visita.horario}]: ") or visita.horario
    visita.tecnico = input(f"Técnico [{visita.tecnico}]: ") or visita.tecnico
    visita.salvar()
    print("Visita técnica alterada com sucesso!")

def excluir_visita():
    id_visita = int(input("ID da Visita Técnica a excluir: "))
    VisitaTecnica.excluir(id_visita)
    print("Visita técnica excluída com sucesso!")

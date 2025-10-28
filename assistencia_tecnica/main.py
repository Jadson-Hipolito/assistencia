from models.cliente import Cliente
from models.funcionario import Funcionario
from models.equipamento import Equipamento
from models.ordem_servico import OrdemServico
from models.visita_tecnica import VisitaTecnica
from models.conta import Conta

def menu_principal():
    while True:
        print("\n--- Sistema de Assistência Técnica ---")
        print("1. Clientes")
        print("2. Funcionários")
        print("3. Equipamentos")
        print("4. Ordens de Serviço")
        print("5. Visitas Técnicas")
        print("6. Contas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_funcionarios()
        elif opcao == "3":
            menu_equipamentos()
        elif opcao == "4":
            menu_ordens()
        elif opcao == "5":
            menu_visitas_tecnicas()
        elif opcao == "6":
            menu_contas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()

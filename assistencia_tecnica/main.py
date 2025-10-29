from views.cliente_view import menu_cliente
from views.funcionario_view import menu_funcionarios
from views.equipamento_view import menu_equipamentos
from views.ordem_servico_view import menu_ordens_servico
from views.visita_tecnica_view import menu_visitas_tecnicas
from views.conta_view import menu_contas

def main():
    while True:
        print("\n=== Sistema de Assistência Técnica ===")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Funcionários")
        print("3. Gerenciar Equipamentos")
        print("4. Gerenciar Ordens de Serviço")
        print("5. Gerenciar Visitas Técnicas")
        print("6. Gerenciar Contas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            menu_funcionarios()
        elif opcao == "3":
            menu_equipamentos()
        elif opcao == "4":
            menu_ordens_servico()
        elif opcao == "5":
            menu_visitas_tecnicas()
        elif opcao == "6":
            menu_contas()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

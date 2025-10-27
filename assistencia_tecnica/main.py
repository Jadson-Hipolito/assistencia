from views.cliente_view import menu_cliente
# As demais views serão importadas aqui

def main():
    while True:
        print("\n=== Sistema Assistência Técnica ===")
        print("1. Cliente")
        print("2. Funcionário")
        print("3. Ordem de Serviço")
        print("4. Equipamento")
        print("5. Contas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "6":
            break

if __name__ == "__main__":
    main()


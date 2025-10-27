from models.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, cpf, data_nascimento, endereco, telefone):
        id_cliente = len(self.clientes) + 1
        cliente = Cliente(id_cliente, nome, cpf, data_nascimento, endereco, telefone)
        self.clientes.append(cliente)
        return cliente

    def consultar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def alterar_cliente(self, id_cliente, **dados):
        cliente = self.consultar_cliente(id_cliente)
        if cliente:
            for key, value in dados.items():
                if hasattr(cliente, key) and value:
                    setattr(cliente, key, value)
            return cliente
        return None

    def excluir_cliente(self, id_cliente):
        cliente = self.consultar_cliente(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False


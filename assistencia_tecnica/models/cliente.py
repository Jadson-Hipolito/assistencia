class Cliente:
    def __init__(self, id_cliente, nome, cpf, data_nascimento, endereco, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.historico_servicos = []

    def adicionar_ordem_servico(self, ordem_servico):
        self.historico_servicos.append(ordem_servico)


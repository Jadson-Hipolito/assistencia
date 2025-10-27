from datetime import date

class OrdemServico:
    def __init__(self, id_os, cliente, funcionario, data_emissao=None, data_inicio=None):
        self.id_os = id_os
        self.cliente = cliente
        self.funcionario = funcionario
        self.data_emissao = data_emissao or date.today()
        self.data_inicio = data_inicio
        self.status = "Aberta"
        self.itens_os = []
        self.visita_tecnica = None

    def adicionar_item(self, item_os):
        self.itens_os.append(item_os)

    def agendar_visita(self, visita_tecnica):
        self.visita_tecnica = visita_tecnica

    def encerrar_os(self):
        self.status = "Encerrada"


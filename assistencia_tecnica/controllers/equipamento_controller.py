from models.equipamento import Equipamento

class EquipamentoController:
    def __init__(self):
        self.equipamentos = []

    def cadastrar_equipamento(self, tipo, marca, modelo, quantidade):
        id_equipamento = len(self.equipamentos) + 1
        equipamento = Equipamento(id_equipamento, tipo, marca, modelo, quantidade)
        self.equipamentos.append(equipamento)
        return equipamento

    def consultar_equipamento(self, id_equipamento):
        for eq in self.equipamentos:
            if eq.id_equipamento == id_equipamento:
                return eq
        return None

    def excluir_equipamento(self, id_equipamento):
        eq = self.consultar_equipamento(id_equipamento)
        if eq:
            self.equipamentos.remove(eq)
            return True
        return False


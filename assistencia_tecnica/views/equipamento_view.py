from assistencia_tecnica.models.equipamento import Equipamento

def listar_equipamentos():
    return [e.to_dict() for e in Equipamento.listar_todos()]

def obter_equipamento(id_equipamento: int):
    equipamento = Equipamento.consultar(id_equipamento)
    return equipamento.to_dict() if equipamento else None

def criar_equipamento(data: dict):
    equipamento = Equipamento(
        tipo=data.get("tipo"),
        marca=data.get("marca"),
        modelo=data.get("modelo"),
        numero_serie=data.get("numero_serie"),
        id_cliente=data.get("id_cliente")
    )
    equipamento.salvar()
    return equipamento.to_dict()

def atualizar_equipamento(id_equipamento: int, data: dict):
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        return None
    equipamento.tipo = data.get("tipo", equipamento.tipo)
    equipamento.marca = data.get("marca", equipamento.marca)
    equipamento.modelo = data.get("modelo", equipamento.modelo)
    equipamento.numero_serie = data.get("numero_serie", equipamento.numero_serie)
    equipamento.id_cliente = data.get("id_cliente", equipamento.id_cliente)
    equipamento.salvar()
    return equipamento.to_dict()

def deletar_equipamento(id_equipamento: int):
    equipamento = Equipamento.consultar(id_equipamento)
    if not equipamento:
        return None
    Equipamento.excluir(id_equipamento)
    return {"mensagem": "Equipamento excluído com sucesso"}
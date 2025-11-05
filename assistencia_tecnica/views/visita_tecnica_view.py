from assistencia_tecnica.models.visita_tecnica import VisitaTecnica

def listar_visitas():
    """Retorna todas as visitas como lista de dicionários"""
    return [v.to_dict() for v in VisitaTecnica.listar_todos()]

def obter_visita(id_visita: int):
    """Retorna uma visita específica"""
    visita = VisitaTecnica.consultar(id_visita)
    return visita.to_dict() if visita else None

def criar_visita(data: dict):
    """Cria uma nova visita"""
    visita = VisitaTecnica(
        id_os=data.get("id_os"),
        funcionario_id=data.get("funcionario_id"),
        data=data.get("data"),
        horario=data.get("horario"),
        observacoes=data.get("observacoes")
    )
    visita.salvar()
    return visita.to_dict()

def atualizar_visita(id_visita: int, data: dict):
    """Atualiza uma visita existente"""
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None
    visita.id_os = data.get("id_os", visita.id_os)
    visita.funcionario_id = data.get("funcionario_id", visita.funcionario_id)
    visita.data = data.get("data", visita.data)
    visita.horario = data.get("horario", visita.horario)
    visita.observacoes = data.get("observacoes", visita.observacoes)
    visita.salvar()
    return visita.to_dict()

def deletar_visita(id_visita: int):
    """Exclui uma visita"""
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None
    VisitaTecnica.excluir(id_visita)
    return {"mensagem": "Visita Técnica excluída com sucesso"}

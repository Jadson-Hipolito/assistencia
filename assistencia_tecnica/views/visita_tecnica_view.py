from assistencia_tecnica.models.visita_tecnica import VisitaTecnica

def listar_visitas():
    return [v.to_dict() for v in VisitaTecnica.listar_todos()]

def obter_visita(id_visita: int):
    visita = VisitaTecnica.consultar(id_visita)
    return visita.to_dict() if visita else None

def criar_visita(data: dict):
    visita = VisitaTecnica(
        id_os=data.get("id_os"),
        data=data.get("data"),
        horario=data.get("horario"),
        tecnico=data.get("tecnico")
    )
    visita.salvar()
    return visita.to_dict()

def atualizar_visita(id_visita: int, data: dict):
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None
    visita.id_os = data.get("id_os", visita.id_os)
    visita.data = data.get("data", visita.data)
    visita.horario = data.get("horario", visita.horario)
    visita.tecnico = data.get("tecnico", visita.tecnico)
    visita.salvar()
    return visita.to_dict()

def deletar_visita(id_visita: int):
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None
    VisitaTecnica.excluir(id_visita)
    return {"mensagem": "Visita Técnica excluída com sucesso"}
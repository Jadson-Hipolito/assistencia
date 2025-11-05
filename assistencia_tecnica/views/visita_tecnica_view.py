# assistencia_tecnica/views/visita_tecnica_view.py
from typing import Optional, List
from assistencia_tecnica.models.visita_tecnica import VisitaTecnica

def listar_visitas() -> List[dict]:
    return [v.to_dict() for v in VisitaTecnica.listar_todos()]

def obter_visita(id_visita: int) -> Optional[dict]:
    visita = VisitaTecnica.consultar(id_visita)
    return visita.to_dict() if visita else None

def criar_visita(data: dict) -> dict:
    # Converte valores vazios para None
    id_os = data.get("id_os")
    funcionario_id = data.get("funcionario_id")
    if id_os is None or funcionario_id is None:
        raise ValueError("Ordem de Serviço e Funcionário são obrigatórios")

    visita = VisitaTecnica(
        id_os=id_os,
        funcionario_id=funcionario_id,
        data=data.get("data"),
        horario=data.get("horario") or None,
        observacoes=data.get("observacoes") or None
    )
    visita.salvar()
    return visita.to_dict()

def atualizar_visita(id_visita: int, data: dict) -> Optional[dict]:
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None

    visita.id_os = data.get("id_os", visita.id_os)
    visita.funcionario_id = data.get("funcionario_id", visita.funcionario_id)
    visita.data = data.get("data", visita.data)
    visita.horario = data.get("horario") or visita.horario
    visita.observacoes = data.get("observacoes") or visita.observacoes
    visita.salvar()
    return visita.to_dict()

def deletar_visita(id_visita: int) -> Optional[dict]:
    visita = VisitaTecnica.consultar(id_visita)
    if not visita:
        return None
    VisitaTecnica.excluir(id_visita)
    return {"mensagem": "Visita Técnica excluída com sucesso"}

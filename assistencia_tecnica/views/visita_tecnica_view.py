# assistencia_tecnica/views/visita_tecnica_view.py
from typing import Optional, List
import sqlite3
from assistencia_tecnica.models.visita_tecnica import VisitaTecnica

DB_PATH = "data/assistencia_tecnica.db"

def registro_existe(tabela: str, coluna_id: str, valor: int) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM {tabela} WHERE {coluna_id} = ?", (valor,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def listar_visitas() -> List[dict]:
    return [v.to_dict() for v in VisitaTecnica.listar_todos()]

def obter_visita(id_visita: int) -> Optional[dict]:
    visita = VisitaTecnica.consultar(id_visita)
    return visita.to_dict() if visita else None

def criar_visita(data: dict) -> dict:
    id_os = data.get("id_os")
    tecnico = data.get("tecnico")

    if id_os is None or tecnico is None:
        raise ValueError("Ordem de Serviço e Técnico são obrigatórios")
    if not registro_existe("ordem_servico", "id_os", id_os):
        raise ValueError(f"Ordem de Serviço com id {id_os} não existe")
    if not registro_existe("funcionario", "id_funcionario", tecnico):
        raise ValueError(f"Técnico com id {tecnico} não existe")

    visita = VisitaTecnica(
        id_os=id_os,
        tecnico=tecnico,
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

    id_os = data.get("id_os", visita.id_os)
    tecnico = data.get("tecnico", visita.tecnico)

    if not registro_existe("ordem_servico", "id_os", id_os):
        raise ValueError(f"Ordem de Serviço com id {id_os} não existe")
    if not registro_existe("funcionario", "id_funcionario", tecnico):
        raise ValueError(f"Técnico com id {tecnico} não existe")

    visita.id_os = id_os
    visita.tecnico = tecnico
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

from fastapi import APIRouter, HTTPException
from assistencia_tecnica.views import visita_tecnica_view

router = APIRouter(prefix="/visitas", tags=["Visitas Técnicas"])

@router.get("/")
def listar_visitas():
    return visita_tecnica_view.listar_visitas()

@router.get("/{visita_id}")
def obter_visita(visita_id: int):
    visita = visita_tecnica_view.obter_visita(visita_id)
    if not visita:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return visita

@router.post("/")
def criar_visita(visita: dict):
    return visita_tecnica_view.criar_visita(visita)

@router.put("/{visita_id}")
def atualizar_visita(visita_id: int, visita: dict):
    atualizado = visita_tecnica_view.atualizar_visita(visita_id, visita)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return atualizado

@router.delete("/{visita_id}")
def deletar_visita(visita_id: int):
    deletado = visita_tecnica_view.deletar_visita(visita_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return deletado
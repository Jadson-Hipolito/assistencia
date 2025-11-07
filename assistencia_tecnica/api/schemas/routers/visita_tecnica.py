# assistencia_tecnica/api/schemas/routers/visita_tecnica.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from assistencia_tecnica.views import visita_tecnica_view

router = APIRouter(prefix="/visitas", tags=["Visitas Técnicas"])

class VisitaIn(BaseModel):
    id_os: int
    tecnico: int
    data: str
    horario: Optional[str] = None
    observacoes: Optional[str] = None

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
def criar_visita(visita: VisitaIn):
    try:
        return visita_tecnica_view.criar_visita(visita.dict())
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar visita: {e}")

@router.put("/{visita_id}")
def atualizar_visita(visita_id: int, visita: VisitaIn):
    try:
        atualizado = visita_tecnica_view.atualizar_visita(visita_id, visita.dict())
        if not atualizado:
            raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
        return atualizado
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar visita: {e}")

@router.delete("/{visita_id}")
def deletar_visita(visita_id: int):
    deletado = visita_tecnica_view.deletar_visita(visita_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return deletado

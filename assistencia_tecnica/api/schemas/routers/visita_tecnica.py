from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from assistencia_tecnica.views import visita_tecnica_view

router = APIRouter(prefix="/visitas", tags=["Visitas Técnicas"])

# --- Schemas Pydantic para validação ---
class VisitaIn(BaseModel):
    id_os: int
    funcionario_id: int
    data: str
    horario: Optional[str] = None
    observacoes: Optional[str] = None

# --- Endpoints ---
@router.get("/")
def listar_visitas():
    """Lista todas as visitas com informações da ordem e do funcionário."""
    return visita_tecnica_view.listar_visitas()

@router.get("/{visita_id}")
def obter_visita(visita_id: int):
    visita = visita_tecnica_view.obter_visita(visita_id)
    if not visita:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return visita

@router.post("/")
def criar_visita(visita: VisitaIn):
    """Cria uma nova visita técnica."""
    try:
        return visita_tecnica_view.criar_visita(visita.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar visita: {e}")

@router.put("/{visita_id}")
def atualizar_visita(visita_id: int, visita: VisitaIn):
    """Atualiza uma visita existente."""
    atualizado = visita_tecnica_view.atualizar_visita(visita_id, visita.dict())
    if not atualizado:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return atualizado

@router.delete("/{visita_id}")
def deletar_visita(visita_id: int):
    """Exclui uma visita técnica."""
    deletado = visita_tecnica_view.deletar_visita(visita_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Visita Técnica não encontrada")
    return deletado

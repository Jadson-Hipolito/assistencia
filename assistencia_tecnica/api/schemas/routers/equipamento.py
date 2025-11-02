from fastapi import APIRouter, HTTPException
from assistencia_tecnica.views import equipamento_view

router = APIRouter(prefix="/equipamentos", tags=["Equipamentos"])

@router.get("/")
def listar_equipamentos():
    return equipamento_view.listar_equipamentos()

@router.get("/{equipamento_id}")
def obter_equipamento(equipamento_id: int):
    equipamento = equipamento_view.obter_equipamento(equipamento_id)
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return equipamento

@router.post("/")
def criar_equipamento(equipamento: dict):
    return equipamento_view.criar_equipamento(equipamento)

@router.put("/{equipamento_id}")
def atualizar_equipamento(equipamento_id: int, equipamento: dict):
    atualizado = equipamento_view.atualizar_equipamento(equipamento_id, equipamento)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return atualizado

@router.delete("/{equipamento_id}")
def deletar_equipamento(equipamento_id: int):
    deletado = equipamento_view.deletar_equipamento(equipamento_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return deletado
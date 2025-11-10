from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from assistencia_tecnica.views import ordem_servico_view

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])

class OrdemCreateSchema(BaseModel):
    id_cliente: int
    equipamentos: list[int] = []
    descricao: str
    status: str = "Aberta"

@router.get("/")
def listar_ordens():
    return ordem_servico_view.listar_ordens()

@router.get("/{ordem_id}")
def obter_ordem(ordem_id: int):
    ordem = ordem_servico_view.obter_ordem(ordem_id)
    if not ordem:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem

@router.post("/")
def criar_ordem(ordem: OrdemCreateSchema):
    return ordem_servico_view.criar_ordem(ordem.dict())

@router.put("/{ordem_id}")
def atualizar_ordem(ordem_id: int, ordem: OrdemCreateSchema):
    atualizado = ordem_servico_view.atualizar_ordem(ordem_id, ordem.dict())
    if not atualizado:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return atualizado

@router.delete("/{ordem_id}")
def deletar_ordem(ordem_id: int):
    ordem_servico_view.deletar_ordem(ordem_id)
    return {"mensagem": "Ordem deletada com sucesso"}

from fastapi import APIRouter, HTTPException
from assistencia_tecnica.views import ordem_servico_view

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])

@router.get("/")
def listar_ordens():
    return ordem_servico_view.listar_ordens()

@router.get("/{ordem_id}")
def obter_ordem(ordem_id: int):
    ordem = ordem_servico_view.obter_ordem(ordem_id)
    if not ordem:
        raise HTTPException(status_code=404, detail="Ordem de Serviço não encontrada")
    return ordem

@router.post("/")
def criar_ordem(ordem: dict):
    return ordem_servico_view.criar_ordem(ordem)

@router.put("/{ordem_id}")
def atualizar_ordem(ordem_id: int, ordem: dict):
    atualizado = ordem_servico_view.atualizar_ordem(ordem_id, ordem)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Ordem de Serviço não encontrada")
    return atualizado

@router.delete("/{ordem_id}")
def deletar_ordem(ordem_id: int):
    deletado = ordem_servico_view.deletar_ordem(ordem_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Ordem de Serviço não encontrada")
    return deletado

@router.put("/{ordem_id}/fechar")
def fechar_ordem(ordem_id: int, data: dict):
    ordem = ordem_servico_view.fechar_ordem(ordem_id, data.get("data_encerramento"))
    if not ordem:
        raise HTTPException(status_code=404, detail="Ordem de Serviço não encontrada")
    return ordem
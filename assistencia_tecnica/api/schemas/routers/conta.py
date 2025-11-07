from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, condecimal
from typing import Optional
from assistencia_tecnica.views import conta_view

router = APIRouter(prefix="/contas", tags=["Contas"])

class ContaIn(BaseModel):
    id_os: int
    valor: condecimal(decimal_places=2, gt=0)
    tipo: Optional[str] = "Receber"

@router.get("/")
def listar_contas():
    return conta_view.listar_contas()

@router.get("/pendentes")
def listar_pendentes():
    return conta_view.listar_pendentes()

@router.get("/{conta_id}")
def obter_conta(conta_id: int):
    conta = conta_view.obter_conta(conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta

@router.post("/")
def criar_conta(conta: ContaIn):
    try:
        return conta_view.criar_conta(conta.dict())
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar conta: {e}")

@router.put("/{conta_id}/pagar")
def pagar_conta(conta_id: int):
    conta = conta_view.pagar_conta(conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return {"mensagem": "Conta paga com sucesso", "conta": conta}

@router.delete("/{conta_id}")
def deletar_conta(conta_id: int):
    deletado = conta_view.deletar_conta(conta_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return deletado

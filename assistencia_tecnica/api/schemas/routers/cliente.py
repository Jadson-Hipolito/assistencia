from fastapi import APIRouter, HTTPException
from assistencia_tecnica.views import cliente_view

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar_clientes():
    return cliente_view.listar_clientes()

@router.get("/{cliente_id}")
def obter_cliente(cliente_id: int):
    cliente = cliente_view.obter_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.post("/")
def criar_cliente(cliente: dict):
    try:
        return cliente_view.criar_cliente(cliente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: dict):
    try:
        atualizado = cliente_view.atualizar_cliente(cliente_id, cliente)
        if not atualizado:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return atualizado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int):
    deletado = cliente_view.deletar_cliente(cliente_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return deletado
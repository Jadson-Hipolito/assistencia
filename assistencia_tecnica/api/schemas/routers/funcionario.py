from fastapi import APIRouter, HTTPException
from assistencia_tecnica.views import funcionario_view

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.get("/")
def listar_funcionarios():
    return funcionario_view.listar_funcionarios()

@router.get("/{funcionario_id}")
def obter_funcionario(funcionario_id: int):
    funcionario = funcionario_view.obter_funcionario(funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.post("/")
def criar_funcionario(funcionario: dict):
    return funcionario_view.criar_funcionario(funcionario)

@router.put("/{funcionario_id}")
def atualizar_funcionario(funcionario_id: int, funcionario: dict):
    atualizado = funcionario_view.atualizar_funcionario(funcionario_id, funcionario)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return atualizado

@router.delete("/{funcionario_id}")
def deletar_funcionario(funcionario_id: int):
    deletado = funcionario_view.deletar_funcionario(funcionario_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return deletado
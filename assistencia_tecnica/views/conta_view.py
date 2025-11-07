from typing import Optional, List
from fastapi import HTTPException
from assistencia_tecnica.models.conta import Conta

def listar_contas() -> List[dict]:
    return Conta.listar_todos()

def listar_pendentes() -> List[dict]:
    return Conta.listar_pendentes()

def obter_conta(id_conta: int) -> Optional[dict]:
    conta = Conta.consultar(id_conta)
    return conta.to_dict() if conta else None

def criar_conta(data: dict) -> dict:
    id_os = data.get("id_os")
    valor = data.get("valor")
    tipo = data.get("tipo", "Receber")

    if id_os is None or valor is None:
        raise ValueError("id_os e valor são obrigatórios para criar uma conta")

    conta = Conta(id_os=id_os, valor=valor, tipo=tipo)
    conta.salvar()
    return conta.to_dict()

def pagar_conta(id_conta: int) -> Optional[dict]:
    conta = Conta.consultar(id_conta)
    if not conta:
        return None
    conta.pagar()
    return conta.to_dict()

def deletar_conta(id_conta: int) -> Optional[dict]:
    conta = Conta.consultar(id_conta)
    if not conta:
        return None
    Conta.excluir(id_conta)
    return {"mensagem": "Conta excluída com sucesso"}

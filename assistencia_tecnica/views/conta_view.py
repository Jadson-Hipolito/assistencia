from assistencia_tecnica.models.conta import Conta

def listar_contas():
    return [c.to_dict() for c in Conta.listar_todos()]

def listar_pendentes():
    return [c.to_dict() for c in Conta.listar_pendentes()]

def obter_conta(id_conta: int):
    conta = Conta.consultar(id_conta)
    return conta.to_dict() if conta else None

def criar_conta(data: dict):
    conta = Conta(
        id_os=data.get("id_os"),
        valor=data.get("valor"),
        tipo=data.get("tipo", "Receber")
    )
    conta.salvar()
    return conta.to_dict()

def pagar_conta(id_conta: int):
    conta = Conta.consultar(id_conta)
    if not conta:
        return None
    conta.pagar()
    return conta.to_dict()

def deletar_conta(id_conta: int):
    conta = Conta.consultar(id_conta)
    if not conta:
        return None
    Conta.excluir(id_conta)
    return {"mensagem": "Conta excluída com sucesso"}
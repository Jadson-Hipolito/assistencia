from assistencia_tecnica.models.ordem_servico import OrdemServico

def listar_ordens():
    return [o.to_dict() for o in OrdemServico.listar_todos()]

def obter_ordem(id_os: int):
    ordem = OrdemServico.consultar(id_os)
    return ordem.to_dict() if ordem else None

def criar_ordem(data: dict):
    ordem = OrdemServico(
        id_cliente=data.get("id_cliente"),
        equipamento_id=data.get("equipamento_id"),
        descricao=data.get("descricao"),
        status=data.get("status", "Aberta")
    )
    ordem.salvar()
    return ordem.to_dict()

def atualizar_ordem(id_os: int, data: dict):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.id_cliente = data.get("id_cliente", ordem.id_cliente)
    ordem.equipamento_id = data.get("equipamento_id", ordem.equipamento_id)
    ordem.descricao = data.get("descricao", ordem.descricao)
    ordem.status = data.get("status", ordem.status)
    ordem.salvar()
    return ordem.to_dict()

def deletar_ordem(id_os: int):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    OrdemServico.excluir(id_os)
    return {"mensagem": "Ordem de Serviço excluída com sucesso"}

def fechar_ordem(id_os: int, data_encerramento: str = None):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.fechar(data_encerramento)
    return ordem.to_dict()

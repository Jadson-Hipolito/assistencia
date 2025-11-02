from assistencia_tecnica.models.ordem_servico import OrdemServico

def listar_ordens():
    return [os.to_dict() for os in OrdemServico.listar_todos()]

def obter_ordem(id_os: int):
    ordem = OrdemServico.consultar(id_os)
    return ordem.to_dict() if ordem else None

def criar_ordem(data: dict):
    ordem = OrdemServico(
        id_cliente=data.get("id_cliente"),
        descricao=data.get("descricao"),
        status=data.get("status", "Aberta"),
        data_abertura=data.get("data_abertura"),
        data_encerramento=data.get("data_encerramento")
    )
    ordem.salvar()
    return ordem.to_dict()

def atualizar_ordem(id_os: int, data: dict):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.id_cliente = data.get("id_cliente", ordem.id_cliente)
    ordem.descricao = data.get("descricao", ordem.descricao)
    ordem.status = data.get("status", ordem.status)
    ordem.data_abertura = data.get("data_abertura", ordem.data_abertura)
    ordem.data_encerramento = data.get("data_encerramento", ordem.data_encerramento)
    ordem.salvar()
    return ordem.to_dict()

def deletar_ordem(id_os: int):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    OrdemServico.excluir(id_os)
    return {"mensagem": "Ordem de Serviço excluída com sucesso"}

def fechar_ordem(id_os: int, data_encerramento: str):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.fechar(data_encerramento)
    return ordem.to_dict()
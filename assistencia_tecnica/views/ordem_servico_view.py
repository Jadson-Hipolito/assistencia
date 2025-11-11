from assistencia_tecnica.models.ordem_servico import OrdemServico

def listar_ordens():
    return OrdemServico.listar_todos()

def obter_ordem(id_os):
    ordem = OrdemServico.consultar(id_os)
    return ordem.to_dict() if ordem else None

def criar_ordem(dados):
    ordem = OrdemServico(
        id_cliente=dados["id_cliente"],
        equipamentos=dados.get("equipamentos", []),
        descricao=dados["descricao"],
        status=dados.get("status", "Aberta"),
        data_encerramento=dados.get("data_encerramento")
    )
    ordem.salvar()
    return ordem.to_dict()

def atualizar_ordem(id_os, dados):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.id_cliente = dados["id_cliente"]
    ordem.equipamentos = dados.get("equipamentos", [])
    ordem.descricao = dados["descricao"]
    ordem.status = dados["status"]
    ordem.data_encerramento = dados.get("data_encerramento")
    ordem.salvar()
    return ordem.to_dict()

def deletar_ordem(id_os):
    OrdemServico.excluir(id_os)
    return True

def fechar_ordem(id_os, data_encerramento=None):
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None
    ordem.fechar(data_encerramento)
    return ordem.to_dict()

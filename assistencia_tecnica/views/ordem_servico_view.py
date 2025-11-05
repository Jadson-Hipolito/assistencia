from assistencia_tecnica.models.ordem_servico import OrdemServico
from typing import List, Optional


def listar_ordens() -> List[dict]:
    return OrdemServico.listar_todos()


def obter_ordem(id_os: int) -> Optional[dict]:
    ordem = OrdemServico.consultar(id_os)
    return ordem.to_dict() if ordem else None


def criar_ordem(data: dict) -> dict:
    # Verifica obrigatoriedade
    if "id_cliente" not in data or data["id_cliente"] is None:
        raise ValueError("id_cliente é obrigatório")
    if "descricao" not in data or not data["descricao"]:
        raise ValueError("descricao é obrigatória")

    ordem = OrdemServico(
        id_cliente=data["id_cliente"],
        equipamento_id=data.get("equipamento_id"),
        descricao=data["descricao"],
        status=data.get("status", "Aberta")
    )
    ordem.salvar()
    return ordem.to_dict()


def atualizar_ordem(id_os: int, data: dict) -> Optional[dict]:
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None

    ordem.id_cliente = data.get("id_cliente", ordem.id_cliente)
    ordem.equipamento_id = data.get("equipamento_id", ordem.equipamento_id)
    ordem.descricao = data.get("descricao", ordem.descricao)
    ordem.status = data.get("status", ordem.status)
    ordem.salvar()
    return ordem.to_dict()


def deletar_ordem(id_os: int) -> Optional[dict]:
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None

    OrdemServico.excluir(id_os)
    return {"mensagem": "Ordem de Serviço excluída com sucesso"}


def fechar_ordem(id_os: int, data_encerramento: str = None) -> Optional[dict]:
    ordem = OrdemServico.consultar(id_os)
    if not ordem:
        return None

    ordem.fechar(data_encerramento)
    return ordem.to_dict()

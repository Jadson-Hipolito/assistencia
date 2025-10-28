import json
from pathlib import Path

class Cliente:
    def __init__(self, id_cliente, nome, endereco, contato, cpf, historico_servicos=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.cpf = cpf
        self.historico_servicos = historico_servicos or []

    def adicionar_ordem_servico(self, ordem_servico):
        self.historico_servicos.append(ordem_servico)

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "endereco": self.endereco,
            "contato": self.contato,
            "cpf": self.cpf,
            "historico_servicos": self.historico_servicos,
        }

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nome={self.nome})"


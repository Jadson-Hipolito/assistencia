import json
from pathlib import Path

class Funcionario:
    def __init__(self, id_funcionario, nome, endereco, contato, horario, salario, cnpj, ativo=True):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.horario = horario
        self.salario = salario
        self.cnpj = cnpj
        self.ativo = ativo

    def to_dict(self):
        return {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "endereco": self.endereco,
            "contato": self.contato,
            "horario": self.horario,
            "salario": self.salario,
            "cnpj": self.cnpj,
            "ativo": self.ativo,
        }


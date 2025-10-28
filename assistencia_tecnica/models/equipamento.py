import json
from pathlib import Path

class Equipamento:
    def __init__(self, id_equipamento, tipo, marca, modelo, numero_serie, id_cliente):
        self.id_equipamento = id_equipamento
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.id_cliente = id_cliente

    def to_dict(self):
        return {
            "id_equipamento": self.id_equipamento,
            "tipo": self.tipo,
            "marca": self.marca,
            "modelo": self.modelo,
            "numero_serie": self.numero_serie,
            "id_cliente": self.id_cliente,
        }

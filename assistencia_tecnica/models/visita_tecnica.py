from datetime import datetime

class VisitaTecnica:
    def __init__(self, id_visita, os, endereco, data_hora):
        self.id_visita = id_visita
        self.os = os
        self.endereco = endereco
        self.data_hora = data_hora
        self.status = "Agendada"


import sqlite3

class VisitaTecnica:
    def __init__(self, id_visita=None, id_os=None, data=None, horario=None, tecnico=None):
        self.id_visita = id_visita
        self.id_os = id_os
        self.data = data
        self.horario = horario
        self.tecnico = tecnico

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        if self.id_visita is None:
            cursor.execute(
                "INSERT INTO visita_tecnica (id_os, data, horario, tecnico) VALUES (?, ?, ?, ?)",
                (self.id_os, self.data, self.horario, self.tecnico)
            )
            self.id_visita = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE visita_tecnica SET id_os=?, data=?, horario=?, tecnico=? WHERE id_visita=?",
                (self.id_os, self.data, self.horario, self.tecnico, self.id_visita)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(id_visita):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_visita, id_os, data, horario, tecnico FROM visita_tecnica WHERE id_visita=?",
            (id_visita,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return VisitaTecnica(*row)
        return None

    @staticmethod
    def excluir(id_visita):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM visita_tecnica WHERE id_visita=?", (id_visita,))
        conn.commit()
        conn.close()


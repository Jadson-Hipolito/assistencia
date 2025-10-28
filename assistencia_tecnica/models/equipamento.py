import sqlite3

class Equipamento:
    def __init__(self, id_equipamento=None, tipo=None, marca=None, modelo=None, numero_serie=None, id_cliente=None):
        self.id_equipamento = id_equipamento
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.id_cliente = id_cliente

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        if self.id_equipamento is None:
            cursor.execute(
                "INSERT INTO equipamento (tipo, marca, modelo, numero_serie, id_cliente) VALUES (?, ?, ?, ?, ?)",
                (self.tipo, self.marca, self.modelo, self.numero_serie, self.id_cliente)
            )
            self.id_equipamento = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE equipamento SET tipo=?, marca=?, modelo=?, numero_serie=?, id_cliente=? WHERE id_equipamento=?",
                (self.tipo, self.marca, self.modelo, self.numero_serie, self.id_cliente, self.id_equipamento)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(id_equipamento):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_equipamento, tipo, marca, modelo, numero_serie, id_cliente FROM equipamento WHERE id_equipamento=?",
            (id_equipamento,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Equipamento(*row)
        return None

    @staticmethod
    def excluir(id_equipamento):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipamento WHERE id_equipamento=?", (id_equipamento,))
        conn.commit()
        conn.close()

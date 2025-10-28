import sqlite3

class Conta:
    def __init__(self, id_conta=None, id_os=None, valor=0.0, status='Pendente', tipo='Receber'):
        self.id_conta = id_conta
        self.id_os = id_os
        self.valor = valor
        self.status = status
        self.tipo = tipo

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        if self.id_conta is None:
            cursor.execute(
                "INSERT INTO conta (id_os, valor, status, tipo) VALUES (?, ?, ?, ?)",
                (self.id_os, self.valor, self.status, self.tipo)
            )
            self.id_conta = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE conta SET id_os=?, valor=?, status=?, tipo=? WHERE id_conta=?",
                (self.id_os, self.valor, self.status, self.tipo, self.id_conta)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(id_conta):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_conta, id_os, valor, status, tipo FROM conta WHERE id_conta=?",
            (id_conta,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Conta(*row)
        return None

    @staticmethod
    def listar_pendentes():
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta, id_os, valor, status, tipo FROM conta WHERE status='Pendente'")
        rows = cursor.fetchall()
        conn.close()
        return [Conta(*row) for row in rows]

    def pagar(self):
        self.status = 'Pago'
        self.salvar()


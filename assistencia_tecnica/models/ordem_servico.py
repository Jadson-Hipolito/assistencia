import sqlite3

class OrdemServico:
    def __init__(self, id_os=None, id_cliente=None, descricao=None, status='Aberta', data_abertura=None, data_encerramento=None):
        self.id_os = id_os
        self.id_cliente = id_cliente
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura
        self.data_encerramento = data_encerramento

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        if self.id_os is None:
            cursor.execute(
                "INSERT INTO ordem_servico (id_cliente, descricao, status, data_abertura, data_encerramento) VALUES (?, ?, ?, ?, ?)",
                (self.id_cliente, self.descricao, self.status, self.data_abertura, self.data_encerramento)
            )
            self.id_os = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE ordem_servico SET id_cliente=?, descricao=?, status=?, data_abertura=?, data_encerramento=? WHERE id_os=?",
                (self.id_cliente, self.descricao, self.status, self.data_abertura, self.data_encerramento, self.id_os)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(id_os):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_os, id_cliente, descricao, status, data_abertura, data_encerramento FROM ordem_servico WHERE id_os=?",
            (id_os,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return OrdemServico(*row)
        return None

    @staticmethod
    def excluir(id_os):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ordem_servico WHERE id_os=?", (id_os,))
        conn.commit()
        conn.close()

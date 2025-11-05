import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class OrdemServico:
    def __init__(self, id_os=None, id_cliente=None, equipamento_id=None, descricao=None,
                 status='Aberta', data_abertura=None, data_encerramento=None,
                 cliente_nome=None, equipamento_nome=None):

        if id_cliente is None:
            raise ValueError("id_cliente é obrigatório")
        if descricao is None:
            raise ValueError("descricao é obrigatória")

        self.id_os = id_os
        self.id_cliente = id_cliente
        self.equipamento_id = equipamento_id
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura or datetime.now().strftime("%Y-%m-%d")
        self.data_encerramento = data_encerramento
        self.cliente_nome = cliente_nome
        self.equipamento_nome = equipamento_nome

    def salvar(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        try:
            if self.id_os is None:
                cursor.execute("""
                    INSERT INTO ordem_servico
                    (id_cliente, equipamento_id, descricao, status, data_abertura, data_encerramento)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (self.id_cliente, self.equipamento_id, self.descricao, self.status,
                      self.data_abertura, self.data_encerramento))
                self.id_os = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE ordem_servico
                    SET id_cliente=?, equipamento_id=?, descricao=?, status=?, data_abertura=?, data_encerramento=?
                    WHERE id_os=?
                """, (self.id_cliente, self.equipamento_id, self.descricao, self.status,
                      self.data_abertura, self.data_encerramento, self.id_os))
            conn.commit()
        finally:
            conn.close()

    def to_dict(self):
        return {
            "id_os": self.id_os,
            "id_cliente": self.id_cliente,
            "cliente_nome": self.cliente_nome or "Cliente inexistente",
            "equipamento_id": self.equipamento_id,
            "equipamento_nome": self.equipamento_nome or "Equipamento inexistente",
            "descricao": self.descricao,
            "status": self.status,
            "data_abertura": self.data_abertura,
            "data_encerramento": self.data_encerramento
        }

    @staticmethod
    def listar_todos():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT os.id_os, os.id_cliente, os.equipamento_id, os.descricao, os.status,
                   os.data_abertura, os.data_encerramento,
                   c.nome AS cliente_nome,
                   e.tipo || ' ' || e.modelo AS equipamento_nome
            FROM ordem_servico os
            LEFT JOIN cliente c ON os.id_cliente = c.id_cliente
            LEFT JOIN equipamento e ON os.equipamento_id = e.id_equipamento
        """)
        rows = cursor.fetchall()
        conn.close()
        return [OrdemServico(*row[:7], cliente_nome=row[7], equipamento_nome=row[8]) for row in rows]

    @staticmethod
    def consultar(id_os):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT os.id_os, os.id_cliente, os.equipamento_id, os.descricao, os.status,
                   os.data_abertura, os.data_encerramento,
                   c.nome AS cliente_nome,
                   e.tipo || ' ' || e.modelo AS equipamento_nome
            FROM ordem_servico os
            LEFT JOIN cliente c ON os.id_cliente = c.id_cliente
            LEFT JOIN equipamento e ON os.equipamento_id = e.id_equipamento
            WHERE os.id_os=?
        """, (id_os,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return OrdemServico(*row[:7], cliente_nome=row[7], equipamento_nome=row[8])
        return None

    @staticmethod
    def excluir(id_os):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ordem_servico WHERE id_os=?", (id_os,))
        conn.commit()
        conn.close()

    def fechar(self, data_encerramento=None):
        self.status = "Fechada"
        self.data_encerramento = data_encerramento or datetime.now().strftime("%Y-%m-%d")
        self.salvar()

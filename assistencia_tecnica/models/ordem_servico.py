import os
import sqlite3
from datetime import datetime
from fastapi import HTTPException

# Caminho para o mesmo banco de dados usado pelo modelo Cliente
DB_PATH = os.path.join("data", "assistencia_tecnica.db")


class OrdemServico:
    def __init__(self, id_os=None, id_cliente=None, equipamento_id=None, descricao=None,
                 status='Aberta', data_abertura=None, data_encerramento=None,
                 cliente_nome=None, equipamento_nome=None):

        # Só valida campos obrigatórios em criação manual, não em consultas do banco
        if id_os is None and id_cliente is None:
            raise ValueError("id_cliente é obrigatório ao criar nova ordem")
        if id_os is None and descricao is None:
            raise ValueError("descricao é obrigatória ao criar nova ordem")

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
        print(f"[DEBUG] Conectando ao banco: {DB_PATH}")
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
        except sqlite3.OperationalError as e:
            raise HTTPException(status_code=500, detail=f"Erro no banco: {str(e)}")
        finally:
            conn.close()

    def _atualizar_nomes(self):
        """Busca os nomes de cliente e equipamento no banco"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Cliente
        if self.cliente_nome is None and self.id_cliente is not None:
            cursor.execute("SELECT nome FROM cliente WHERE id_cliente=?", (self.id_cliente,))
            row = cursor.fetchone()
            self.cliente_nome = row[0] if row else "Cliente inexistente"

        # Equipamento
        if self.equipamento_id is not None and self.equipamento_nome is None:
            cursor.execute("SELECT tipo || ' ' || modelo FROM equipamento WHERE id_equipamento=?", (self.equipamento_id,))
            row = cursor.fetchone()
            self.equipamento_nome = row[0] if row else "Equipamento inexistente"

        conn.close()

    def to_dict(self):
        self._atualizar_nomes()
        return {
            "id_os": self.id_os,
            "id_cliente": self.id_cliente,
            "cliente_nome": self.cliente_nome,
            "equipamento_id": self.equipamento_id,
            "equipamento_nome": self.equipamento_nome,
            "descricao": self.descricao,
            "status": self.status,
            "data_abertura": self.data_abertura,
            "data_encerramento": self.data_encerramento
        }

    @staticmethod
    def listar_todos():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id_os FROM ordem_servico")
        ids = [row[0] for row in cursor.fetchall()]
        conn.close()

        ordens = []
        for id_os in ids:
            ordem = OrdemServico.consultar(id_os)
            if ordem:
                ordens.append(ordem.to_dict())
        return ordens

    @staticmethod
    def consultar(id_os):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_os, id_cliente, equipamento_id, descricao, status, data_abertura, data_encerramento
            FROM ordem_servico
            WHERE id_os=?
        """, (id_os,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return OrdemServico(*row)
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

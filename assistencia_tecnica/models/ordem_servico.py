# assistencia_tecnica/models/ordem_servico.py
import os
import sqlite3
from datetime import datetime
from fastapi import HTTPException

DB_PATH = os.path.join("data", "assistencia_tecnica.db")


class OrdemServico:
    def __init__(self, id_os=None, id_cliente=None, equipamentos=None,
                 descricao=None, status='Aberta', data_abertura=None,
                 data_encerramento=None, cliente_nome=None):
        self.id_os = id_os
        self.id_cliente = id_cliente
        self.equipamentos = equipamentos or []
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura or datetime.now().strftime("%Y-%m-%d")
        self.data_encerramento = data_encerramento
        self.cliente_nome = cliente_nome

    def salvar(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        try:
            if self.id_os is None:
                cursor.execute("""
                    INSERT INTO ordem_servico (id_cliente, descricao, status, data_abertura, data_encerramento)
                    VALUES (?, ?, ?, ?, ?)
                """, (self.id_cliente, self.descricao, self.status, self.data_abertura, self.data_encerramento))
                self.id_os = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE ordem_servico
                    SET id_cliente=?, descricao=?, status=?, data_abertura=?, data_encerramento=?
                    WHERE id_os=?
                """, (self.id_cliente, self.descricao, self.status, self.data_abertura, self.data_encerramento, self.id_os))
                cursor.execute("DELETE FROM ordem_servico_equipamento WHERE id_os=?", (self.id_os,))

            for eq_id in self.equipamentos:
                cursor.execute("""
                    INSERT INTO ordem_servico_equipamento (id_os, id_equipamento)
                    VALUES (?, ?)
                """, (self.id_os, eq_id))
            conn.commit()
        except sqlite3.OperationalError as e:
            raise HTTPException(status_code=500, detail=f"Erro no banco: {str(e)}")
        finally:
            conn.close()

    def _atualizar_nomes(self):
        if self.cliente_nome:
            return
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM cliente WHERE id_cliente=?", (self.id_cliente,))
        row = cursor.fetchone()
        self.cliente_nome = row[0] if row else "Cliente inexistente"
        conn.close()

    def _buscar_equipamentos(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id_equipamento, e.tipo || ' ' || e.modelo
            FROM equipamento e
            JOIN ordem_servico_equipamento oe ON oe.id_equipamento = e.id_equipamento
            WHERE oe.id_os = ?
        """, (self.id_os,))
        result = [{"id": r[0], "nome": r[1]} for r in cursor.fetchall()]
        conn.close()
        return result

    def to_dict(self):
        self._atualizar_nomes()
        return {
            "id_os": self.id_os,
            "id_cliente": self.id_cliente,
            "cliente_nome": self.cliente_nome,
            "equipamentos": self._buscar_equipamentos(),
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
        # montar lista com .consultar para garantir consistência
        ordens = []
        for i in ids:
            o = OrdemServico.consultar(i)
            if o:
                ordens.append(o.to_dict())
        return ordens

    @staticmethod
    def consultar(id_os):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_os, id_cliente, descricao, status, data_abertura, data_encerramento
            FROM ordem_servico WHERE id_os=?
        """, (id_os,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            return None

        # Mapear explicitamente para evitar deslocamento de campos
        id_os_val, id_cliente, descricao, status, data_abertura, data_encerramento = row

        ordem = OrdemServico(
            id_os=id_os_val,
            id_cliente=id_cliente,
            descricao=descricao,
            status=status,
            data_abertura=data_abertura,
            data_encerramento=data_encerramento
        )

        # popular lista de equipamentos (ids) para edição e to_dict
        ordem.equipamentos = [e["id"] for e in ordem._buscar_equipamentos()]
        return ordem

    @staticmethod
    def excluir(id_os):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ordem_servico_equipamento WHERE id_os=?", (id_os,))
        cursor.execute("DELETE FROM ordem_servico WHERE id_os=?", (id_os,))
        conn.commit()
        conn.close()

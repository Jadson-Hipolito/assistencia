import os
import sqlite3
from datetime import datetime
from fastapi import HTTPException
from assistencia_tecnica.models.ordem_servico import OrdemServico

DB_PATH = os.path.join("data", "assistencia_tecnica.db")

class Conta:
    def __init__(self, id_conta=None, id_os=None, valor=0.0, status='Pendente', tipo='Receber',
                 cliente_nome=None, os_descricao=None):
        if id_conta is None and id_os is None:
            raise ValueError("id_os é obrigatório ao criar nova conta")

        self.id_conta = id_conta
        self.id_os = id_os
        self.valor = valor
        self.status = status
        self.tipo = tipo
        self.cliente_nome = cliente_nome
        self.os_descricao = os_descricao

    def salvar(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            if self.id_conta is None:
                cursor.execute("""
                    INSERT INTO conta (id_os, valor, status, tipo)
                    VALUES (?, ?, ?, ?)
                """, (self.id_os, self.valor, self.status, self.tipo))
                self.id_conta = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE conta
                    SET id_os=?, valor=?, status=?, tipo=?
                    WHERE id_conta=?
                """, (self.id_os, self.valor, self.status, self.tipo, self.id_conta))
            conn.commit()
        except sqlite3.OperationalError as e:
            raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
        finally:
            conn.close()

    def _atualizar_nomes(self):
        """Busca nomes do cliente e da ordem de serviço"""
        if self.cliente_nome is not None and self.os_descricao is not None:
            return

        ordem = OrdemServico.consultar(self.id_os)
        if ordem:
            self.cliente_nome = ordem.cliente_nome
            self.os_descricao = ordem.descricao
        else:
            self.cliente_nome = "Cliente/OS inexistente"
            self.os_descricao = "OS inexistente"

    def to_dict(self):
        self._atualizar_nomes()
        return {
            "id_conta": self.id_conta,
            "id_os": self.id_os,
            "os_descricao": self.os_descricao,
            "cliente_nome": self.cliente_nome,
            "valor": self.valor,
            "status": self.status,
            "tipo": self.tipo
        }

    @staticmethod
    def consultar(id_conta):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_conta, id_os, valor, status, tipo
            FROM conta
            WHERE id_conta=?
        """, (id_conta,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Conta(*row)
        return None

    @staticmethod
    def listar_todos():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta FROM conta")
        ids = [row[0] for row in cursor.fetchall()]
        conn.close()

        contas = []
        for id_conta in ids:
            conta = Conta.consultar(id_conta)
            if conta:
                contas.append(conta.to_dict())
        return contas

    @staticmethod
    def listar_pendentes():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta FROM conta WHERE status='Pendente'")
        ids = [row[0] for row in cursor.fetchall()]
        conn.close()

        contas = []
        for id_conta in ids:
            conta = Conta.consultar(id_conta)
            if conta:
                contas.append(conta.to_dict())
        return contas

    @staticmethod
    def excluir(id_conta):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conta WHERE id_conta=?", (id_conta,))
        conn.commit()
        conn.close()

    def pagar(self):
        self.status = 'Pago'
        self.salvar()

    def cancelar(self):
        self.status = 'Cancelado'
        self.salvar()

import os
import sqlite3
from typing import Optional
from assistencia_tecnica.models.ordem_servico import OrdemServico

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class Conta:
    def __init__(
        self,
        id_conta: Optional[int] = None,
        id_os: Optional[int] = None,
        valor: float = 0.0,
        status: str = 'Pendente',
        tipo: str = 'Receber',
        cliente_nome: Optional[str] = None,
        os_descricao: Optional[str] = None
    ):
        # Quando construído a partir do SELECT (5 colunas), os argumentos batem
        # Para criação manual, garantimos id_os informado.
        if id_conta is None and id_os is None:
            raise ValueError("id_os é obrigatório ao criar nova conta")

        self.id_conta = id_conta
        self.id_os = id_os
        self.valor = float(valor) if valor is not None else 0.0
        self.status = status
        self.tipo = tipo
        self.cliente_nome = cliente_nome
        self.os_descricao = os_descricao

    def _ordem_existe(self) -> bool:
        ordem = OrdemServico.consultar(self.id_os)
        return ordem is not None

    def salvar(self):
        # validações de negócio
        if self.id_os is None:
            raise ValueError("id_os é obrigatório")
        if not isinstance(self.valor, (int, float)):
            raise ValueError("valor inválido")
        if self.valor <= 0:
            raise ValueError("valor deve ser maior que zero")
        if not self._ordem_existe():
            raise ValueError(f"Ordem de Serviço com id {self.id_os} não existe")

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            if self.id_conta is None:
                cursor.execute("""
                    INSERT INTO conta (id_os, valor, tipo, status)
                    VALUES (?, ?, ?, ?)
                """, (self.id_os, self.valor, self.tipo, self.status))
                self.id_conta = cursor.lastrowid
            else:
                cursor.execute("""
                    UPDATE conta
                    SET id_os=?, valor=?, tipo=?, status=?
                    WHERE id_conta=?
                """, (self.id_os, self.valor, self.tipo, self.status, self.id_conta))
            conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Erro de integridade ao salvar conta: {e}")
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro no banco ao salvar conta: {e}")
        finally:
            conn.close()

    def _atualizar_nomes(self):
        if self.cliente_nome is not None and self.os_descricao is not None:
            return
        ordem = OrdemServico.consultar(self.id_os)
        if ordem:
            self.cliente_nome = ordem.cliente_nome
            self.os_descricao = ordem.descricao
        else:
            self.cliente_nome = "Cliente/OS inexistente"
            self.os_descricao = "OS inexistente"

    def to_dict(self) -> dict:
        self._atualizar_nomes()
        return {
            "id_conta": self.id_conta,
            "id_os": self.id_os,
            "os_descricao": self.os_descricao,
            "cliente_nome": self.cliente_nome,
            "valor": float(self.valor),
            "status": self.status,
            "tipo": self.tipo
        }

    @staticmethod
    def consultar(id_conta: int) -> Optional["Conta"]:
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
            # row order matches __init__ parameters (id_conta, id_os, valor, status, tipo)
            return Conta(*row)
        return None

    @staticmethod
    def listar_todos() -> list:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta FROM conta")
        ids = [r[0] for r in cursor.fetchall()]
        conn.close()

        result = []
        for cid in ids:
            c = Conta.consultar(cid)
            if c:
                result.append(c.to_dict())
        return result

    @staticmethod
    def listar_pendentes() -> list:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id_conta FROM conta WHERE status='Pendente'")
        ids = [r[0] for r in cursor.fetchall()]
        conn.close()

        result = []
        for cid in ids:
            c = Conta.consultar(cid)
            if c:
                result.append(c.to_dict())
        return result

    @staticmethod
    def excluir(id_conta: int) -> None:
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

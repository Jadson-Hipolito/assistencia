import os
import sqlite3
from typing import List, Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class VisitaTecnica:
    DB_PATH = DB_PATH  # acesso como VisitaTecnica.DB_PATH

    def __init__(
        self,
        id_visita: Optional[int] = None,
        id_os: Optional[int] = None,
        funcionario_id: Optional[int] = None,
        data: Optional[str] = None,
        horario: Optional[str] = None,
        observacoes: Optional[str] = None
    ):
        self.id_visita = id_visita
        self.id_os = id_os
        self.funcionario_id = funcionario_id
        self.data = data
        self.horario = horario
        self.observacoes = observacoes
        self.ordem_nome: Optional[str] = None
        self.funcionario_nome: Optional[str] = None

    def salvar(self) -> None:
        """Insere ou atualiza a visita no banco de dados."""
        try:
            with sqlite3.connect(self.DB_PATH) as conn:
                cursor = conn.cursor()
                if self.id_visita is None:
                    cursor.execute(
                        """
                        INSERT INTO visita_tecnica 
                        (id_os, funcionario_id, data, horario, observacoes) 
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (self.id_os, self.funcionario_id, self.data, self.horario, self.observacoes)
                    )
                    self.id_visita = cursor.lastrowid
                else:
                    cursor.execute(
                        """
                        UPDATE visita_tecnica 
                        SET id_os=?, funcionario_id=?, data=?, horario=?, observacoes=? 
                        WHERE id_visita=?
                        """,
                        (self.id_os, self.funcionario_id, self.data, self.horario, self.observacoes, self.id_visita)
                    )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao salvar visita: {e}")
            raise

    @classmethod
    def consultar(cls, id_visita: int) -> Optional["VisitaTecnica"]:
        """Consulta uma visita pelo ID."""
        try:
            with sqlite3.connect(cls.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT id_visita, id_os, funcionario_id, data, horario, observacoes 
                    FROM visita_tecnica WHERE id_visita=?
                    """,
                    (id_visita,)
                )
                row = cursor.fetchone()
                if row:
                    return cls(*row)
        except sqlite3.Error as e:
            print(f"Erro ao consultar visita: {e}")
        return None

    @classmethod
    def listar_todos(cls) -> List["VisitaTecnica"]:
        """Retorna todas as visitas, incluindo nomes da ordem e do funcionário."""
        visitas: List[VisitaTecnica] = []
        try:
            with sqlite3.connect(cls.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT vt.id_visita, vt.id_os, vt.funcionario_id, vt.data, vt.horario, vt.observacoes,
                           o.descricao, f.nome
                    FROM visita_tecnica vt
                    LEFT JOIN ordem_servico o ON vt.id_os = o.id_os
                    LEFT JOIN funcionario f ON vt.funcionario_id = f.id_funcionario
                    """
                )
                rows = cursor.fetchall()
                for row in rows:
                    vt = cls(*row[:6])
                    vt.ordem_nome = row[6] or "Ordem inexistente"
                    vt.funcionario_nome = row[7] or "Funcionário inexistente"
                    visitas.append(vt)
        except sqlite3.Error as e:
            print(f"Erro ao listar visitas: {e}")
        return visitas

    @classmethod
    def excluir(cls, id_visita: int) -> None:
        """Exclui uma visita pelo ID."""
        try:
            with sqlite3.connect(cls.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM visita_tecnica WHERE id_visita=?", (id_visita,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao excluir visita: {e}")
            raise

    def to_dict(self) -> dict:
        """Retorna a visita como um dicionário."""
        return {
            "id_visita": self.id_visita,
            "id_os": self.id_os,
            "funcionario_id": self.funcionario_id,
            "data": self.data,
            "horario": self.horario,
            "observacoes": self.observacoes,
            "ordem_nome": self.ordem_nome or "Ordem inexistente",
            "funcionario_nome": self.funcionario_nome or "Funcionário inexistente"
        }

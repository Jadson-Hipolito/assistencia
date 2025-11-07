# assistencia_tecnica/models/visita_tecnica.py
import os
import sqlite3
from typing import Optional, List

# Caminho absoluto para o banco de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class VisitaTecnica:
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
        self.funcionario_id = funcionario_id  # ← será gravado como "tecnico" no banco
        self.data = data
        self.horario = horario
        self.observacoes = observacoes
        self.ordem_nome: Optional[str] = None
        self.funcionario_nome: Optional[str] = None

    def salvar(self) -> None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                if self.id_visita is None:
                    cursor.execute(
                        """
                        INSERT INTO visita_tecnica (id_os, data, horario, tecnico)
                        VALUES (?, ?, ?, ?)
                        """,
                        (self.id_os, self.data, self.horario, self.funcionario_id)
                    )
                    self.id_visita = cursor.lastrowid
                else:
                    cursor.execute(
                        """
                        UPDATE visita_tecnica
                        SET id_os=?, data=?, horario=?, tecnico=?
                        WHERE id_visita=?
                        """,
                        (self.id_os, self.data, self.horario, self.funcionario_id, self.id_visita)
                    )
                conn.commit()
        except sqlite3.Error as e:
            print(f"[ERRO] salvar visita: {e}")
            raise

    @staticmethod
    def consultar(id_visita: int) -> Optional["VisitaTecnica"]:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT id_visita, id_os, data, horario, tecnico
                    FROM visita_tecnica
                    WHERE id_visita=?
                    """,
                    (id_visita,)
                )
                row = cursor.fetchone()
                if row:
                    return VisitaTecnica(row[0], row[1], row[4], row[2], row[3])
        except sqlite3.Error as e:
            print(f"[ERRO] consultar visita: {e}")
        return None

    @staticmethod
    def listar_todos() -> List["VisitaTecnica"]:
        visitas: List[VisitaTecnica] = []
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vt.id_visita, vt.id_os, vt.data, vt.horario, vt.tecnico,
                           o.descricao AS ordem_nome
                    FROM visita_tecnica vt
                    LEFT JOIN ordem_servico o ON vt.id_os = o.id_os
                """)
                for row in cursor.fetchall():
                    vt = VisitaTecnica(row[0], row[1], row[4], row[2], row[3])
                    vt.ordem_nome = row[5] if row[5] else "Ordem inexistente"
                    visitas.append(vt)
        except sqlite3.Error as e:
            print(f"[ERRO] listar visitas: {e}")
        return visitas

    @staticmethod
    def excluir(id_visita: int) -> None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM visita_tecnica WHERE id_visita=?", (id_visita,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"[ERRO] excluir visita: {e}")
            raise

    def to_dict(self) -> dict:
        return {
            "id_visita": self.id_visita,
            "id_os": self.id_os,
            "funcionario_id": self.funcionario_id,
            "data": self.data,
            "horario": self.horario,
            "observacoes": self.observacoes,
            "ordem_nome": self.ordem_nome or "Ordem inexistente"
        }

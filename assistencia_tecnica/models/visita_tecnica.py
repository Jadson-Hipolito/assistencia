# assistencia_tecnica/models/visita_tecnica.py
import os
import sqlite3
from typing import Optional, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class VisitaTecnica:
    DB_PATH = DB_PATH

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
            print(f"[ERRO] salvar visita: {e}")
            raise

    @staticmethod
    def consultar(id_visita: int) -> Optional["VisitaTecnica"]:
        try:
            with sqlite3.connect(VisitaTecnica.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT id_visita, id_os, funcionario_id, data, horario, observacoes FROM visita_tecnica WHERE id_visita=?",
                    (id_visita,)
                )
                row = cursor.fetchone()
                if row:
                    return VisitaTecnica(*row)
        except sqlite3.Error as e:
            print(f"[ERRO] consultar visita: {e}")
        return None

    @staticmethod
    def listar_todos() -> List["VisitaTecnica"]:
        visitas: List[VisitaTecnica] = []
        try:
            with sqlite3.connect(VisitaTecnica.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vt.id_visita, vt.id_os, vt.funcionario_id, vt.data, vt.horario, vt.observacoes,
                           o.descricao AS ordem_nome, f.nome AS funcionario_nome
                    FROM visita_tecnica vt
                    LEFT JOIN ordem_servico o ON vt.id_os = o.id_os
                    LEFT JOIN funcionario f ON vt.funcionario_id = f.id_funcionario
                """)
                for row in cursor.fetchall():
                    vt = VisitaTecnica(*row[:6])
                    vt.ordem_nome = row[6] if row[6] else "Ordem inexistente"
                    vt.funcionario_nome = row[7] if row[7] else "Funcionário inexistente"
                    visitas.append(vt)
        except sqlite3.Error as e:
            print(f"[ERRO] listar visitas: {e}")
        return visitas

    @staticmethod
    def excluir(id_visita: int) -> None:
        try:
            with sqlite3.connect(VisitaTecnica.DB_PATH) as conn:
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
            "ordem_nome": self.ordem_nome or "Ordem inexistente",
            "funcionario_nome": self.funcionario_nome or "Funcionário inexistente"
        }

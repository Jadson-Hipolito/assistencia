# assistencia_tecnica/models/visita_tecnica.py
import os
import sqlite3
from typing import Optional, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "data", "assistencia_tecnica.db")

class VisitaTecnica:
    def __init__(
        self,
        id_visita: Optional[int] = None,
        id_os: Optional[int] = None,
        tecnico: Optional[int] = None,
        data: Optional[str] = None,
        horario: Optional[str] = None,
        observacoes: Optional[str] = None
    ):
        self.id_visita = id_visita
        self.id_os = id_os
        self.tecnico = tecnico
        self.data = data
        self.horario = horario
        self.observacoes = observacoes
        self.ordem_nome: Optional[str] = None
        self.funcionario_nome: Optional[str] = None

    @staticmethod
    def _existe_registro(tabela: str, coluna_id: str, valor: int) -> bool:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT 1 FROM {tabela} WHERE {coluna_id}=?", (valor,))
                return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"[ERRO] verificar existência em {tabela}: {e}")
            return False

    def salvar(self) -> None:
        if self.id_os is None or self.tecnico is None or self.data is None or self.horario is None:
            raise ValueError("Ordem de Serviço, Técnico, Data e Horário são obrigatórios")

        if not self._existe_registro("ordem_servico", "id_os", self.id_os):
            raise ValueError(f"Ordem de Serviço com id {self.id_os} não existe")
        if not self._existe_registro("funcionario", "id_funcionario", self.tecnico):
            raise ValueError(f"Técnico com id {self.tecnico} não existe")

        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                if self.id_visita is None:
                    cursor.execute(
                        "INSERT INTO visita_tecnica (id_os, data, horario, tecnico, observacoes) VALUES (?, ?, ?, ?, ?)",
                        (self.id_os, self.data, self.horario, self.tecnico, self.observacoes)
                    )
                    self.id_visita = cursor.lastrowid
                else:
                    cursor.execute(
                        "UPDATE visita_tecnica SET id_os=?, data=?, horario=?, tecnico=?, observacoes=? WHERE id_visita=?",
                        (self.id_os, self.data, self.horario, self.tecnico, self.observacoes, self.id_visita)
                    )
                conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Erro de integridade ao salvar visita: {e}")
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao salvar visita: {e}")

    @staticmethod
    def consultar(id_visita: int) -> Optional["VisitaTecnica"]:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vt.id_visita, vt.id_os, vt.data, vt.horario, vt.tecnico, vt.observacoes,
                           f.nome
                    FROM visita_tecnica vt
                    LEFT JOIN funcionario f ON vt.tecnico = f.id_funcionario
                    WHERE vt.id_visita=?""", (id_visita,))
                row = cursor.fetchone()
                if row:
                    vt = VisitaTecnica(
                        id_visita=row[0],
                        id_os=row[1],
                        tecnico=row[4],
                        data=row[2],
                        horario=row[3],
                        observacoes=row[5]
                    )
                    vt.funcionario_nome = row[6] or "Técnico desconhecido"
                    return vt
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
                    SELECT vt.id_visita, vt.id_os, vt.data, vt.horario, vt.tecnico, vt.observacoes,
                           o.descricao, f.nome
                    FROM visita_tecnica vt
                    LEFT JOIN ordem_servico o ON vt.id_os = o.id_os
                    LEFT JOIN funcionario f ON vt.tecnico = f.id_funcionario
                """)
                for row in cursor.fetchall():
                    vt = VisitaTecnica(
                        id_visita=row[0],
                        id_os=row[1],
                        tecnico=row[4],
                        data=row[2],
                        horario=row[3],
                        observacoes=row[5]
                    )
                    vt.ordem_nome = row[6] or "Ordem inexistente"
                    vt.funcionario_nome = row[7] or "Técnico desconhecido"
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
            "tecnico": self.tecnico,
            "funcionario_nome": self.funcionario_nome or "Técnico desconhecido",
            "data": self.data,
            "horario": self.horario,
            "observacoes": self.observacoes,
            "ordem_nome": self.ordem_nome or "Ordem inexistente"
        }

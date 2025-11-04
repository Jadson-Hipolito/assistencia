import sqlite3
from fastapi import HTTPException

DB_PATH = "data/assistencia_tecnica.db"


def _conn():
    """Cria e retorna uma conexão com o banco de dados SQLite, garantindo integridade referencial."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


class Equipamento:
    def __init__(self, id_equipamento=None, tipo=None, marca=None, modelo=None, numero_serie=None, id_cliente=None, nome_cliente=None):
        """
        Representa um equipamento vinculado a um cliente.

        :param id_equipamento: ID do equipamento (opcional)
        :param tipo: Tipo do equipamento (ex: Notebook, Impressora)
        :param marca: Marca do equipamento
        :param modelo: Modelo do equipamento
        :param numero_serie: Número de série
        :param id_cliente: ID do cliente proprietário
        :param nome_cliente: Nome do cliente (obtido via JOIN)
        """
        self.id_equipamento = id_equipamento
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente

    # ---------------------------------------------------------------------
    # MÉTODOS DE PERSISTÊNCIA
    # ---------------------------------------------------------------------

    def salvar(self):
        """Insere ou atualiza o equipamento no banco de dados."""
        with _conn() as conn:
            cursor = conn.cursor()
            try:
                # Verifica se o cliente existe
                cursor.execute("SELECT 1 FROM cliente WHERE id_cliente=?", (self.id_cliente,))
                if cursor.fetchone() is None:
                    raise HTTPException(status_code=404, detail="Cliente não encontrado")

                # Inserir novo equipamento
                if self.id_equipamento is None:
                    cursor.execute(
                        """
                        INSERT INTO equipamento (tipo, marca, modelo, numero_serie, id_cliente)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (self.tipo, self.marca, self.modelo, self.numero_serie, self.id_cliente)
                    )
                    self.id_equipamento = cursor.lastrowid

                # Atualizar equipamento existente
                else:
                    cursor.execute(
                        """
                        UPDATE equipamento
                        SET tipo=?, marca=?, modelo=?, numero_serie=?, id_cliente=?
                        WHERE id_equipamento=?
                        """,
                        (self.tipo, self.marca, self.modelo, self.numero_serie, self.id_cliente, self.id_equipamento)
                    )

                conn.commit()

            except sqlite3.IntegrityError as e:
                raise HTTPException(status_code=400, detail=f"Erro de integridade: {str(e)}")
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Erro ao salvar equipamento: {str(e)}")

    # ---------------------------------------------------------------------
    # MÉTODOS ESTÁTICOS DE CONSULTA / EXCLUSÃO
    # ---------------------------------------------------------------------

    @staticmethod
    def consultar(id_equipamento):
        """Retorna um equipamento pelo ID (incluindo nome do cliente)."""
        with _conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT 
                    e.id_equipamento, e.tipo, e.marca, e.modelo, e.numero_serie, 
                    e.id_cliente, c.nome AS nome_cliente
                FROM equipamento e
                LEFT JOIN cliente c ON e.id_cliente = c.id_cliente
                WHERE e.id_equipamento=?
                """,
                (id_equipamento,)
            )
            row = cursor.fetchone()
        return Equipamento(*row) if row else None

    @staticmethod
    def listar_todos():
        """Retorna uma lista com todos os equipamentos cadastrados (com nome e ID do cliente)."""
        with _conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT 
                    e.id_equipamento, e.tipo, e.marca, e.modelo, e.numero_serie, 
                    e.id_cliente, c.nome AS nome_cliente
                FROM equipamento e
                LEFT JOIN cliente c ON e.id_cliente = c.id_cliente
                ORDER BY e.id_equipamento DESC
                """
            )
            rows = cursor.fetchall()
        return [Equipamento(*row) for row in rows]

    @staticmethod
    def excluir(id_equipamento):
        """Exclui um equipamento do banco de dados pelo ID."""
        with _conn() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM equipamento WHERE id_equipamento=?", (id_equipamento,))
            conn.commit()
            return cursor.rowcount

    # ---------------------------------------------------------------------
    # REPRESENTAÇÃO
    # ---------------------------------------------------------------------

    def to_dict(self):
        """Retorna o equipamento como dicionário (inclui nome do cliente)."""
        return {
            "id_equipamento": self.id_equipamento,
            "tipo": self.tipo,
            "marca": self.marca,
            "modelo": self.modelo,
            "numero_serie": self.numero_serie,
            "id_cliente": self.id_cliente,
            "nome_cliente": self.nome_cliente
        }

    def __repr__(self):
        """Representação textual útil para logs e depuração."""
        return f"<Equipamento id={self.id_equipamento} tipo={self.tipo} cliente={self.nome_cliente}>"

import sqlite3

class Cliente:
    def __init__(self, id_cliente=None, nome=None, endereco=None, contato=None, cpf=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.cpf = cpf

    def to_dict(self):
        return {
            "id": self.id_cliente,
            "nome": self.nome,
            "endereco": self.endereco,
            "contato": self.contato,
            "cpf": self.cpf
        }

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        if self.id_cliente is None:
            cursor.execute(
                "INSERT INTO cliente (nome, endereco, contato, cpf) VALUES (?, ?, ?, ?)",
                (self.nome, self.endereco, self.contato, self.cpf)
            )
            self.id_cliente = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE cliente SET nome=?, endereco=?, contato=?, cpf=? WHERE id_cliente=?",
                (self.nome, self.endereco, self.contato, self.cpf, self.id_cliente)
            )
        conn.commit()
        conn.close()

    @staticmethod
    def consultar(id_cliente):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_cliente, nome, endereco, contato, cpf FROM cliente WHERE id_cliente=?", (id_cliente,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Cliente(*row)
        return None

    @staticmethod
    def listar_todos():
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_cliente, nome, endereco, contato, cpf FROM cliente")
        rows = cursor.fetchall()
        conn.close()
        return [Cliente(*row) for row in rows]

    @staticmethod
    def excluir(id_cliente):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente=?", (id_cliente,))
        conn.commit()
        conn.close()
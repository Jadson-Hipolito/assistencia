import sqlite3

class Funcionario:
    def __init__(self, id_funcionario=None, nome=None, endereco=None, contato=None,
                 horario=None, salario=None, cnpj=None, ativo=True):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.horario = horario
        self.salario = salario
        self.cnpj = cnpj
        self.ativo = ativo

    def salvar(self):
        with sqlite3.connect("data/assistencia_tecnica.db") as conn:
            cursor = conn.cursor()
            if self.id_funcionario is None:
                cursor.execute(
                    "INSERT INTO funcionario (nome, endereco, contato, horario, salario, cnpj, ativo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (self.nome, self.endereco, self.contato, self.horario, self.salario, self.cnpj, int(self.ativo))
                )
                self.id_funcionario = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE funcionario SET nome=?, endereco=?, contato=?, horario=?, salario=?, cnpj=?, ativo=? WHERE id_funcionario=?",
                    (self.nome, self.endereco, self.contato, self.horario, self.salario, self.cnpj, int(self.ativo), self.id_funcionario)
                )
            conn.commit()

    def to_dict(self):
        return {
            "id": self.id_funcionario,
            "nome": self.nome,
            "endereco": self.endereco,
            "contato": self.contato,
            "horario": self.horario,
            "salario": self.salario,
            "cnpj": self.cnpj,
            "ativo": self.ativo
        }

    @staticmethod
    def consultar(id_funcionario):
        with sqlite3.connect("data/assistencia_tecnica.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_funcionario, nome, endereco, contato, horario, salario, cnpj, ativo FROM funcionario WHERE id_funcionario=?",
                (id_funcionario,)
            )
            row = cursor.fetchone()
        return Funcionario(*row) if row else None

    @staticmethod
    def listar_todos():
        with sqlite3.connect("data/assistencia_tecnica.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_funcionario, nome, endereco, contato, horario, salario, cnpj, ativo FROM funcionario")
            rows = cursor.fetchall()
        return [Funcionario(*row) for row in rows]

    @staticmethod
    def excluir(id_funcionario):
        with sqlite3.connect("data/assistencia_tecnica.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM funcionario WHERE id_funcionario=?", (id_funcionario,))
            conn.commit()
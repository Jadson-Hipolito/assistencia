import sqlite3

class Funcionario:
    def __init__(self, id_funcionario=None, nome=None, endereco=None, contato=None, horario=None, salario=None, cnpj=None, ativo=True):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.horario = horario
        self.salario = salario
        self.cnpj = cnpj
        self.ativo = ativo

    def salvar(self):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
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
        conn.close()

    @staticmethod
    def consultar(id_funcionario):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_funcionario, nome, endereco, contato, horario, salario, cnpj, ativo FROM funcionario WHERE id_funcionario=?",
            (id_funcionario,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Funcionario(*row)
        return None

    @staticmethod
    def excluir(id_funcionario):
        conn = sqlite3.connect("data/assistencia_tecnica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionario WHERE id_funcionario=?", (id_funcionario,))
        conn.commit()
        conn.close()



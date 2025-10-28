import sqlite3
from pathlib import Path

# Cria diretório data caso não exista
Path("data").mkdir(exist_ok=True)

conn = sqlite3.connect("data/assistencia_tecnica.db")
cursor = conn.cursor()

# Tabela Cliente
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT,
    contato TEXT,
    cpf TEXT
)
""")

# Tabela Funcionário
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionario (
    id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT,
    contato TEXT,
    horario TEXT,
    salario REAL,
    cnpj TEXT,
    ativo INTEGER DEFAULT 1
)
""")

# Tabela Equipamento
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipamento (
    id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    marca TEXT,
    modelo TEXT,
    numero_serie TEXT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
)
""")

# Tabela Ordem de Serviço
cursor.execute("""
CREATE TABLE IF NOT EXISTS ordem_servico (
    id_os INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    descricao TEXT,
    status TEXT,
    data_abertura TEXT,
    data_encerramento TEXT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
)
""")

# Tabela Visita Técnica
cursor.execute("""
CREATE TABLE IF NOT EXISTS visita_tecnica (
    id_visita INTEGER PRIMARY KEY AUTOINCREMENT,
    id_os INTEGER,
    data TEXT,
    horario TEXT,
    tecnico TEXT,
    FOREIGN KEY (id_os) REFERENCES ordem_servico(id_os)
)
""")

# Tabela Conta
cursor.execute("""
CREATE TABLE IF NOT EXISTS conta (
    id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_os INTEGER,
    valor REAL,
    status TEXT,
    tipo TEXT,
    FOREIGN KEY (id_os) REFERENCES ordem_servico(id_os)
)
""")

conn.commit()
conn.close()
print("Tabelas criadas com sucesso!")

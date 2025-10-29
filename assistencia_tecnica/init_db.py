import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/assistencia_tecnica.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT,
    contato TEXT,
    cpf TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")
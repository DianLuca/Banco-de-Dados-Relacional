import sqlite3


conn = sqlite3.connect('C:\Repositorios\Banco de Dados Relacional\Banco-de-Dados-Relacional\BD_SQLite\meu_banco.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')


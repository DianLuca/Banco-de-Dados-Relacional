import sqlite3


conn = sqlite3.connect('..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\meu_banco.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')


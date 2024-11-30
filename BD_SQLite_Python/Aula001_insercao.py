import sqlite3


# Conexão com o BD
conn = sqlite3.connect('..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\meu_banco.db')

cursor = conn.cursor()

# Definição de uma tupla com os dados
dados_cliente = ('João Silva', 30)

# Placeholders (?, ?): Os pontos de interrogação são usados como
# "espaços reservados". Eles serão substituídos pelos valores dados_cliente
# tupla dados_cliente (ou seja, 'João Silva' e 30).
# Motivo: Usar placeholders é uma prática recomendada,
# pois previne ataques de injeção de SQL.

cursor.execute('INSERT INTO clientes (nome, idade) VALUES (?, ?)', dados_cliente)

conn.commit() # Salva a transação no banco de dados
conn.close() # Fecha conexão
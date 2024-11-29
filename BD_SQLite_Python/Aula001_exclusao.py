import os
import sqlite3


conn = sqlite3.connect('C:\Repositorios\Banco-de-Dados-Relacional\BD_SQLite_Python\meu_banco.db')

cursor = conn.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do usuário que você deseja excluir? ')

# Executa a exclusão com base no nome fornecido
cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome_cliente,))
conn.commit()

print('Cliente deletado com sucesso!')

conn.close()
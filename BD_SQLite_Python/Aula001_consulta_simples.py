import os
import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect('..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\meu_banco.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()

# Saída sem formatação
os.system('cls')
for row in resultados:
    print(row)

print('-' * 50 ,'\nSaída com formatação com prettytable\n')
# Saída com formatação com prettytable

tabela = PrettyTable()

colunas = [descricao[0] for descricao in cursor.description]

tabela.field_names = colunas

for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()


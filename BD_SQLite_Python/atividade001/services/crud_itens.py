# Manipulação dos itens dentro do banco de dados
import sqlite3


def funcao_teste_crud():
    print('módulo crud_itens.')


class Crud():
    def __init__(self, tabela):
        self.tabela = tabela

    def exibir(self, tabela):
        self.tabela = tabela
        print('OK!')

    def adicionar(self):
        pass

    def alterar(self):
        pass

    def apagar(self):
        pass


class Exibir(Crud):
    def exibir(self):
        conn = sqlite3.connect(
            '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\atividade001\\database\\airlines.db')

        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {self.tabela}')
        resultados = cursor.fetchall()

        return resultados


class Adicionar(Crud):
    def adicionar(self):
        conn = sqlite3.connect(
            '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\meu_banco.db')

        cursor = conn.cursor()

        aeroportos = [
            ("Hartsfield-Jackson Atlanta International Airport", "Estados Unidos"),
            ("Beijing Capital International Airport", "China"),
            ("Dubai International Airport", "Emirados Árabes Unidos"),
            ("Los Angeles International Airport", "Estados Unidos"),
            ("Tokyo Haneda Airport", "Japão"),
            ("O'Hare International Airport", "Estados Unidos"),
            ("Heathrow Airport", "Reino Unido"),
            ("Charles de Gaulle Airport", "França"),
            ("Frankfurt Airport", "Alemanha"),
            ("Singapore Changi Airport", "Singapura")
        ]

        cursor.executemany(
            f'INSERT INTO {self.tabela}(nome, pais) VALUES (?, ?)', aeroportos)
        conn.commit()
        conn.close()

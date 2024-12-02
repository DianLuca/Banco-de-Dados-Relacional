# Manipulação dos itens dentro do banco de dados
import sqlite3



# nome_colunas = []


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
        try:
            conn = sqlite3.connect(
                '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\atividade001\\database\\airlines.db')

            cursor = conn.cursor()

            # cursor.execute(f'PRAGMA table_info({self.tabela})')
            # colunas = cursor.fetchall()

            # # Trabalhando em uma forma que eu consiga manipular
            # # todas as tabelas com um unico comando
            # print(type(colunas))

            # for coluna in colunas:
            #     nome_colunas.append(coluna)

            itens = []

            cursor.executemany(

                f'INSERT INTO {self.tabela}(nome, pais) VALUES (?, ?)', itens)
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')

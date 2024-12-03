# Manipulação dos itens dentro do banco de dados
import sqlite3



# nome_colunas = []


class Crud():
    def __init__(self, tabela):
        self.tabela = tabela

    def exibir(self, tabela):
        self.tabela = tabela
        print('OK!')

    def adicionar(self, tabela):
        self.tabela = tabela
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
        
        if resultados:
            for k, v, p in resultados:
                print(k, end=' | ')
                print(v, end=' | ')
                print(p, end=' | ')
                print()
        else:
            print('Não há registros para exibir!')
            
        conn.close()


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
            
            if self.tabela == 'Aeroporto':
                print(f'Inserindo um novo item na tabela {self.tabela}:\n')
                nome = input(f'Adicione o nome do {self.tabela}: ')
                pais = input(f'Insira o país do deste {self.tabela}: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome, pais) VALUES (?, ?)', (nome, pais))
                conn.commit()
                conn.close()
                
                print('O item foi inserido com sucesso!')
            # if self.tabela == 'Passageiro':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            # if self.tabela == 'Passagem':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            # if self.tabela == 'Servico':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            # if self.tabela == 'Voo':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            # if self.tabela == 'Empresa':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            # if self.tabela == 'Gate':
            #     print(f'Inserindo um novo {self.tabela}:\n')
            #     cursor.executemany(
            #         f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', itens)
            
            # conn.commit()
            # conn.close()

        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')

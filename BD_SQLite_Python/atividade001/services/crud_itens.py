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

            while self.tabela == 'Aeroporto':
                print(f'Inserindo um novo item na tabela {self.tabela}:\n')
                nome = input(f'Adicione o nome do {self.tabela}: ')
                pais = input(f'Insira o país do deste {self.tabela}: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome, pais) VALUES (?, ?)', (nome, pais))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Empresa':
                print(f'Inserindo um novo {self.tabela}:\n')
                nome = input(f'Adicione o nome da {self.tabela} aérea: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome) VALUES (?)', (nome))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Gate':
                print(f'Inserindo um novo {self.tabela}:\n')
                identificador = input(f'Adicione o nome do {self.tabela}: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(identificador) VALUES (?, ?)', (identificador))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break
                
            while self.tabela == 'Passageiro':
                print(f'Inserindo um novo {self.tabela}:\n')
                nome = input(f'Adicione o nome do {self.tabela}: ')
                idade = int(input(f'Adicione a idade do {self.tabela}: '))
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', (nome, idade))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Passagem':  
                print(f'Inserindo um novo {self.tabela}:\n')
                id_passageiro = input('Insira o ID do passageiro: ')
                id_voo = input('Insira o ID do voo: ')
                id_empresa = input('Insira o ID da empresa aérea: ')
                id_gate = input('Insira o ID do gate: ')
                id_servico = input('Insira o ID do serviço: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(id_passageiro, id_voo, id_empresa, id_gate, id_servico) VALUES (?, ?)', (id_passageiro, id_voo, id_empresa, id_gate, id_servico))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Servico':
                print(f'Inserindo um novo {self.tabela}:\n')
                classe = input(f'Adicione o nome do {self.tabela}: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(classe) VALUES (?)', (classe))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Voo':
                print(f'Inserindo um novo {self.tabela}:\n')
                numero_voo = input(f'Adicione o número do {self.tabela}: ')
                id_origem = int(
                    input(f'Adicione o id da origem do {self.tabela}: '))
                id_destino = int(
                    input(f'Adicione o id do destino do {self.tabela}: '))
                data_ida = input(f'Adicione a data de ida do {self.tabela}: ')
                data_retorno = input(
                    f'Adicione a data de retorno do {self.tabela}: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(numero_voo, id_origem, id_destino, data_ida, data_retorno) VALUES (?, ?, ?, ?, ?)', (numero_voo, id_origem, id_destino, data_ida, data_retorno))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break


        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')
        except:
            print('Houve um erro ao inserir um dado. Tente novamente!')

# Manipulação dos itens dentro do banco de dados
import sqlite3
import os
from prettytable import PrettyTable


class Crud():
    def __init__(self, tabela):
        self.tabela = tabela

    def exibir(self, tabela, menu):
        self.tabela = tabela
        self.menu = menu
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

        if self.tabela == 'Passagem':
            cursor.execute('SELECT id_passagem AS ID, passageiro.nome as NOME, passageiro.idade AS IDADE, empresa.nome AS EMPRESA, '
                           + 'gate.identificador AS GATE, servico.classe AS CLASSE, voo.numero_voo AS VOO, origem.nome AS ORIGEM, '
                           + 'destino.nome AS DESTINO, preco AS PREÇO FROM passagem JOIN passageiro JOIN empresa JOIN gate JOIN servico JOIN voo JOIN aeroporto '
                           + 'AS origem ON voo.id_origem = origem.id_aeroporto JOIN aeroporto AS destino ON voo.id_destino = destino.id_aeroporto '
                           + 'WHERE passagem.id_passageiro = passageiro.id_passageiro AND passagem.id_empresa = empresa.id_empresa '
                           + 'AND passagem.id_gate = gate.id_gate AND passagem.id_servico = servico.id_servico AND passagem.id_voo = voo.id_voo;')
        else:
            cursor.execute(f'SELECT * FROM {self.tabela}')
        resultados = cursor.fetchall()

        if resultados:
            exibir_tabela = PrettyTable()

            colunas = [descricao[0] for descricao in cursor.description]

            exibir_tabela.field_names = colunas

            for row in resultados:
                exibir_tabela.add_row(row)

            print(exibir_tabela)
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
                nome = input(f'Adicione o nome do {self.tabela}: ').title()
                pais = input(f'Insira o país do deste {self.tabela}: ').title()
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome, pais) VALUES (?, ?)', (nome, pais,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Empresa':
                print(f'Inserindo um novo {self.tabela}:\n')
                nome = input(
                    f'Adicione o nome da {self.tabela} aérea: ').title()
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome) VALUES (?)', (nome,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Gate':
                print(f'Inserindo um novo {self.tabela}:\n')
                identificador = input(
                    f'Adicione o nome do {self.tabela}: ').title()
                cursor.execute(
                    f'INSERT INTO {self.tabela}(identificador) VALUES (?)', (identificador,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Passageiro':
                print(f'Inserindo um novo {self.tabela}:\n')
                nome = input(f'Adicione o nome do {self.tabela}: ').title()
                idade = int(input(f'Adicione a idade do {self.tabela}: '))
                cursor.execute(
                    f'INSERT INTO {self.tabela}(nome, idade) VALUES (?, ?)', (nome, idade,))
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
                preco = input('Insira o valor da sua passagem: ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(id_passageiro, id_voo, id_empresa, id_gate, id_servico) VALUES (?, ?, ?, ?, ?, ?)', (id_passageiro, id_voo, id_empresa, id_gate, id_servico, preco,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Servico':
                print(f'Inserindo um novo {self.tabela}:\n')
                classe = input(f'Adicione o nome do {self.tabela}: ').title()
                cursor.execute(
                    f'INSERT INTO {self.tabela}(classe) VALUES (?)', (classe,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

            while self.tabela == 'Voo':
                print(f'Inserindo um novo {self.tabela}:\n')
                numero_voo = input(
                    f'Adicione o número do {self.tabela}: ').capitalize()
                id_origem = int(
                    input(f'Adicione o id da origem do {self.tabela}: '))
                id_destino = int(
                    input(f'Adicione o id do destino do {self.tabela}: '))
                data_ida = input(
                    f'Adicione a data e a hora de ida do {self.tabela}(Ex: YYYY-MM-DD HH:MM): ')
                data_retorno = input(
                    f'Adicione a data e hora do retorno do {self.tabela}(Ex: YYYY-MM-DD HH:MM)(Este campo não é obrigátorio!): ')
                cursor.execute(
                    f'INSERT INTO {self.tabela}(numero_voo, id_origem, id_destino, data_ida, data_retorno) VALUES (?, ?, ?, ?, ?)', (numero_voo, id_origem, id_destino, data_ida, data_retorno,))
                conn.commit()

                print('O item foi inserido com sucesso!')

                sair = input(
                    'Deseja adicionar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')
            conn.close()
        except:
            print('Houve um erro ao inserir um dado. Tente novamente!')
            conn.close()


class Apagar(Crud):
    def apagar(self):
        try:
            conn = sqlite3.connect(
                '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\atividade001\\database\\airlines.db')

            cursor = conn.cursor()

            while self.tabela:
                os.system('cls')
                print(f'Apagando um item na tabela {self.tabela}:\n')
                exibir = Exibir(self.tabela)
                exibir.exibir()
                removido = input(
                    f'Qual item você deseja apagar na tabela {self.tabela}: ').title()

                cursor.execute(
                    f'select id_{self.tabela} from {self.tabela} WHERE nome LIKE ?', (f"%{(removido)}%",))
                resultado = cursor.fetchone()

                if removido == '':
                    print('Insira um valor para executar a operação!')
                else:
                    if resultado:
                        id_aeroporto = resultado[0]
                        # print(f'O ID do aeroporto é: {id_aeroporto}') para caso queria identificar o ID do elemento apagado
                        cursor.execute(
                            f'DELETE FROM {self.tabela} WHERE id_{self.tabela} = ?', (id_aeroporto,))
                        conn.commit()

                        print('O item foi removido com sucesso!')
                    else:
                        print('O item não está na lista ou não existe! ')

                sair = input(
                    'Deseja apagar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')
            conn.close()
        except:
            print('Houve um erro ao inserir um dado. Tente novamente!')
            conn.close()


class Alterar(Crud):
    def alterar(self):
        try:
            conn = sqlite3.connect(
                '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\atividade001\\database\\airlines.db')

            cursor = conn.cursor()

            while self.tabela:
                os.system('cls')
                print(f'Alterando um item na tabela {self.tabela}:\n')
                if self.tabela == 'Passagem':
                    cursor.execute(f'SELECT * FROM {self.tabela}')
                    resultados = cursor.fetchall()

                    if resultados:
                        exibir_tabela = PrettyTable()

                        colunas = [descricao[0]
                                   for descricao in cursor.description]

                        exibir_tabela.field_names = colunas

                        for row in resultados:
                            exibir_tabela.add_row(row)

                        print(exibir_tabela)
                    else:
                        print('Não há registros para exibir!')

                else:
                    exibir = Exibir(self.tabela)
                    exibir.exibir()

                alterando_item = input(
                    f'Qual item você deseja atualizar na tabela {self.tabela}: ')

                campo = input('Qual campo você deseja alterar? ').lower()

                if alterando_item:
                    cursor.execute(
                        f'select * from {self.tabela} WHERE {campo} LIKE ?', (f"%{(alterando_item)}%",))
                    resultado = cursor.fetchone()

                    if resultado:
                        colunas = [descricao[0]
                                   for descricao in cursor.description]

                        # Imprime o par nome-coluna e valor utilizando zip
                        for k, v in zip(colunas, resultado):
                            print(f"{k}: {v}", end=" | ")
                        print()

                        # campo = input('Qual campo você deseja alterar? ')
                        if campo == (f'id_{self.tabela}').lower():
                            print('NÃO É PERMITIDO ALTERAR O ID DO ELEMENTO!')
                        else:
                            novo_dado = input(
                                'Insira o valor para o qual o item será alterado: ')
                            cursor.execute(
                                f'UPDATE {self.tabela} SET {campo} = ? WHERE {campo} = ?', (novo_dado, alterando_item))
                            print(
                                f'O item {alterando_item} foi alterado para {novo_dado} com sucesso!')

                            conn.commit()

                    else:
                        print('O item selecionado não existe!')

                else:
                    print('Insira um valor para executar a operação!')
                sair = input(
                    'Deseja alterar mais algum item?(S - Sim) ').lower()
                if sair != 's':
                    conn.close()
                    break

        except sqlite3.Error as e:
            print(f'Aconteceu um erro ao inserir o dados: \n{e}')
            conn.close()
        except:
            print('Houve um erro ao inserir um dado. Tente novamente!')
            conn.close()

# Manipulação dos itens dentro do banco de dados
import sqlite3
import os
from prettytable import PrettyTable
import models.utils as utils


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

        with sqlite3.connect(
                '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                +'\\atividade001\\database\\airlines.db') as conn:

            cursor = conn.cursor()

            if self.tabela == 'Passagem':
                cursor.execute('SELECT id_passagem AS ID, passageiro.nome as NOME, passageiro.idade AS IDADE, empresa.nome AS EMPRESA, '
                               + 'gate.identificador AS GATE, servico.classe AS CLASSE, voo.numero_voo AS VOO, origem.nome AS ORIGEM, '
                               + 'destino.nome AS DESTINO, preco AS PREÇO_R$ FROM passagem JOIN passageiro JOIN empresa JOIN gate JOIN servico JOIN voo JOIN aeroporto '
                               + 'AS origem ON voo.id_origem = origem.id_aeroporto JOIN aeroporto AS destino ON voo.id_destino = destino.id_aeroporto '
                               + 'WHERE passagem.id_passageiro = passageiro.id_passageiro AND passagem.id_empresa = empresa.id_empresa '
                               + 'AND passagem.id_gate = gate.id_gate AND passagem.id_servico = servico.id_servico AND passagem.id_voo = voo.id_voo;')
            elif self.tabela == 'Voo':
                cursor.execute('SELECT id_voo, numero_voo, origem.nome as origem, destino.nome as destino, data_ida, data_retorno FROM voo JOIN aeroporto AS origem ON voo.id_origem = origem.id_aeroporto JOIN aeroporto AS destino ON voo.id_destino = destino.id_aeroporto;')
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


class Adicionar(Crud):
    def adicionar(self):
        try:
            # Abre e fecha a conexão com o banco quando a operação for realizada
            with sqlite3.connect(
                    '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                    + '\\atividade001\\database\\airlines.db') as conn:

                cursor = conn.cursor()

                cursor.execute(f'PRAGMA table_info({self.tabela})')
                colunas = cursor.fetchall()
                # Campos retorna a primeira coluna e ignora o id(auto_increment) das tabelas

                campos = [coluna[1] for coluna in colunas if coluna[1]
                          != f"id_{self.tabela.lower()}"]
                if not campos:
                    print(f'A tabela {self.tabela} '
                          +'não possui campos para inserção.')
                    return

                while True:
                    itens = []

                    print(f'Inserindo item na tabela {self.tabela}:')
                    if self.tabela ==  'Passagem' or self.tabela == 'Voo':
                        if self.tabela == 'Passagem':
                            cabecalho_tabela = ['Passageiro', 'Voo', 'Empresa', 'Gate', 'Servico']
                        if self.tabela == 'Voo':
                            cabecalho_tabela = ['Aeroporto']
                        for i in range(len(cabecalho_tabela)):
                            for campo in campos:
                                if campo == 'preco':
                                    item = input(f'Insira um valor para {campo} (S - Sair): ').strip()
                                    if item.upper() == 'S':
                                        break
                                    else:
                                        itens.append(item)
                                else:
                                    os.system('cls')
                                    exibir = Exibir(cabecalho_tabela[i])
                                    exibir.exibir()
                                    item = input(f'Insira um valor para {campo} (S - Sair): ').strip()
                                    if item.upper() == 'S':
                                        break
                                    else:
                                        itens.append(item)
                                    
                                    if self.tabela == 'Passagem':
                                        i+=1
                                    else:
                                        i == 0
                            break
                                    
                    else:
                        for campo in campos:
                            item = input(f'Insira um valor para {campo} (S - Sair): ').strip()
                            if item.upper() == 'S':
                                break
                            else:
                                itens.append(item)
                        
                            
                        
                    resposta = utils.validar(itens, self.tabela)
                    if resposta != False:

                        # Criando a inserção de forma dinâmica
                        # Une os campos da tabela
                        tabela_campos = ', '.join(campos)
                        # gera o placeholder de acordo com o número de campos
                        placeholders = ', '.join(["?"] * len(campos))
                        query = (f'INSERT INTO {self.tabela} '
                        f'({tabela_campos}) VALUES ({placeholders})')

                        cursor.execute(query, itens)
                        conn.commit()
                        print('O item foi inserido com sucesso!')

                    sair = input(
                        'Deseja adicionar mais algum '
                        +'item?(S - Sim) ').lower().strip()
                    if sair != 's':
                        break

        except Exception as e:
            print(f'ERRO! {e}')


class Apagar(Crud):
    def apagar(self):
        try:
            with sqlite3.connect(
                    '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                    +'\\atividade001\\database\\airlines.db') as conn:

                cursor = conn.cursor()

                while self.tabela:
                    os.system('cls')
                    print(f'Apagando um item na tabela {self.tabela}:\n')

                    exibir = Exibir(self.tabela)
                    exibir.exibir()

                    removido = input(
                        f'Pressione Enter para voltar ao menu ou digite o id '
                        +f'\ndo item você deseja apagar na tabela '
                        +f'{self.tabela}: ').strip()

                    if removido == '':
                        print('Insira um valor para executar a operação!')
                    else:
                        cursor.execute(
                            f'SELECT id_{self.tabela} FROM {self.tabela} '
                            f'WHERE id_{self.tabela} = ?', (removido,))
                        resultado = cursor.fetchone()
                        if resultado:
                            cursor.execute(
                                f'DELETE FROM {self.tabela} WHERE '
                                f'id_{self.tabela} = ?', (removido,))
                            conn.commit()

                            print('O item foi removido com sucesso!')
                        else:
                            print('O item não está na lista ou não existe! ')

                    sair = input(
                        'Deseja apagar mais algum item?(S - Sim) ').lower()
                    if sair != 's':
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
            with sqlite3.connect(
                    '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                    +'\\atividade001\\database\\airlines.db') as conn:

                cursor = conn.cursor()

                while self.tabela:
                    os.system('cls')
                    print(f'Alterando um item na tabela {self.tabela}:\n')
                    if self.tabela == 'Passagem' or self.tabela == 'Voo':
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

                    id_item = input(
                        f'Pressione Enter para voltar ao menu ou '
                        +f' digite o id_{(self.tabela.lower())} do item que você '
                        +'deseja alterar: ').strip()
                    
                    if id_item == '':
                        break

                    campo = input(
                        'Qual campo você deseja alterar? ').lower().strip()
                    resposta = utils.validar_campo(campo, self.tabela)
                    if id_item and resposta == True:
                        cursor.execute(
                            f'SELECT * FROM {self.tabela} '
                            f'WHERE id_{self.tabela.lower()} = ?', (id_item,))
                        resultado = cursor.fetchone()

                        if resultado:
                            colunas = [descricao[0]
                                       for descricao in cursor.description]

                            # Imprime o par nome-coluna e valor utilizando zip
                            for k, v in zip(colunas, resultado):
                                print(f"{k}: {v}", end=" | ")
                            print()
                            if campo == (f'id_{self.tabela}').lower():
                                print('NÃO É PERMITIDO ALTERAR O ID DO ELEMENTO!')
                            else:
                                novo_dado = input(
                                    f'Insira o valor para o qual o {campo} '
                                    +'será alterado: ')
                                # valida_novo_dado = utils.validar(
                                #     novo_dado, self.tabela) # Arrumar um método para validar a atualização de valores
                                if novo_dado:
                                    cursor.execute(
                                        f'UPDATE {self.tabela} SET {campo} = ?'
                                        f'WHERE id_{self.tabela} = ?', 
                                        (novo_dado, id_item))
                                    print(
                                        f'O item de ID: {id_item} foi alterado'
                                        f' para {novo_dado} com sucesso!')

                            conn.commit()

                        else:
                            print('O item selecionado não existe!')

                    else:
                        print('Insira um valor válido para executar a '
                              'operação!')
                    sair = input(
                        'Deseja alterar mais algum item?'
                        +'(S - Sim) ').lower().strip()
                    if sair != 's':
                        break

        except sqlite3.Error as e:
            print(f'Erro ao inserir o dados: \n{e}')
        except sqlite3.IntegrityError as e:
            print('Erro ao inserir um dado. Tente novamente!\n', e)
        except IndexError as e:
            print(f'Erro de índice ao manipular o campo {campo} '
                +f'ou os dados da tabela {self.tabela}:\n', e)

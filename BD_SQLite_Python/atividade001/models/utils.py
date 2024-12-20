# Módulo para validação de itens
import sqlite3


def validar(item, tabela):
    try:
        with sqlite3.connect('..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                             + '\\atividade001\\database\\airlines.db') as conn:

            cursor = conn.cursor()

            cursor.execute(f'PRAGMA table_info({tabela})')
            colunas = cursor.fetchall()

            campos = []
            campos_nulos = set()
            for coluna in colunas:
                if coluna[1] != f'id_{tabela.lower()}':
                    campos.append((coluna[1], coluna[2]))
                    if coluna[3] == 1:
                        campos_nulos.add(coluna[1])

            # List Comprehesion
            # campos = [(coluna[1], coluna[2]) for coluna in colunas if coluna[1] != f'id_{tabela}']
            # campos_nulos = {coluna[1] for coluna in colunas if coluna[3] == 1 and coluna[1] != "id"}

            if not campos:
                print(f'A tabela {tabela} não possuí nenhum campo.')

            for campo, tipo in campos:
                if tipo.upper() == 'INTEGER':
                    if item.isdigit():
                        # Se o item comprir as necessidades para a verificação, do contrário vai para a próxima checagem.
                        break
                    else:
                        print(
                            f'O campo {campo} requer um valor númerico inteiro!')

                elif tipo.upper() == 'REAL':
                    try:
                        break
                    except ValueError:
                        print(
                            f'O campo {campo} requer um valor númerico decimal!')

                else:
                    if item:
                        break
                    else:
                        print('O campo não pode estar vazio!')
                        break

                if campo in campos_nulos and not item:
                    print(f'Erro: o campo "{campo}" é obrigatório.')
                    return False

    except sqlite3.IntegrityError as e:
        print(f'Erro de integridade: {e}')
    except sqlite3.Error as e:
        print(f'Erro ao inserir os dados: {e}')


def validar_campo(campo, tabela):
    with sqlite3.connect('..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
                         + '\\atividade001\\database\\airlines.db') as conn:

        cursor = conn.cursor()

        cursor.execute(f'PRAGMA table_info({tabela})')
        colunas = cursor.fetchall()

        for coluna in colunas:
            if campo in coluna:
                return True
        else:
            print(f'O campo "{campo}" não existe nesta tabela.')
            return False


def validar_menu(menu):
    try:
        if menu and 1 <= int(menu) <= 7: 
            return True
    except ValueError:
        pass

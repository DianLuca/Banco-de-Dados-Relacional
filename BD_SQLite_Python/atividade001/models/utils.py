# Módulo para validação de itens
import sqlite3


def validar(itens, tabela):
    """
    Valida um ou mais itens para inserção em uma tabela do banco de dados.

    :param itens: lista de valores a serem validados.
    :param tabela: nome da tabela no banco de dados.
    :return: True se todos os itens forem válidos, False caso contrário.
    """
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
                
            for i, (campo, tipo) in enumerate(campos):
                valor = itens[i]
                # print(valor)
                print(valor)
                if campo in campos_nulos and (valor is None or valor == ''):
                    print(f'Erro: o campo "{campo}" é obrigatório.')
                    return False

                if tipo.upper() == 'INTEGER' and not str(valor).isdigit():
                    print(
                        f'O campo {campo} requer um valor númerico inteiro!')
                    return False

                elif tipo.upper() == 'REAL':
                    try:
                        float(valor)
                        break
                    except (ValueError, TypeError):
                        print(
                            f'O campo {campo} requer um valor númerico decimal!')
                        return False

                elif tipo.upper not in ['INTEGER', 'REAL'] and not valor:
                    print('O campo não pode estar vazio!')
                    return False

            return True

    except sqlite3.IntegrityError as e:
        print(f'Erro de integridade: {e}')
    except sqlite3.Error as e:
        print(f'Erro ao acessar o banco de dados: {e}')


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

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
            for coluna in colunas:
                if coluna[1] != f'id_{tabela}':
                    campos.append((coluna[1], coluna[2]))
            
            # List Comprehesion
            # campos = [(coluna[1], coluna[2]) for coluna in colunas if coluna[1] != f'id_{tabela}']
            
            if not campos:
                print(f'A tabela {tabela} não possuí nenhum campo.')
            
            for campo, tipo in campos:
                if tipo.upper() == 'INTEGER':
                    if item.isdigit():
                        # Se o item comprir as necessidades para a verificação, do contrário vai para a próxima checagem.
                        break
                    else:
                        print(f'O campo {campo} requer um valor númerico inteiro!')
                
                elif tipo.upper() == 'REAL':
                    try:
                        break
                    except ValueError:
                        print(f'O campo {campo} requer um valor númerico decimal!')
                
                else:
                    if item:
                        print('Isso é um texto!')
                        break
                    else:
                        print('O campo não pode estar vazio!')
                    
                        
                
    except:
        print('Ocorreu um erro na inserção dos itens')
        

# while True:
#     entrada = input('Insira valores aleatórios: ')
#     validar(entrada,'Gate')

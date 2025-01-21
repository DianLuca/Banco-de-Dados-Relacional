# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 02/12/2024

import os
from database.manipulacao_db import criar_db
from models.options import Option_Exibir
from models.options import Option_Adicionar
from models.options import Option_Alterar
from models.options import Option_Apagar


os.system('cls')
criar_db()

while True:
    os.system('cls')
    menu = input(
        '| 1 - Exibir | 2 - Adicionar | 3 - Atualizar | 4 - Apagar | 5 - Sair | \nQual a opção desejada: ').strip()
    if menu == '5':
        print('Parando!')
        break

# READ ----
    elif menu == '1':
        while True:
            os.system('cls')
            apresentar = Option_Exibir()
            apresentar.apresentar()
            input('\nVoltar ao menu: ')
            break

# CREATE ----
    elif menu == '2':
        while True:
            os.system('cls')
            inserir = Option_Adicionar()
            inserir.adicionar()
            input('\nVoltar ao menu principal: ')
            break

# UPDATE ----
    elif menu == '3':
        while True:
            os.system('cls')
            modificar = Option_Alterar()
            modificar.alterar()
            input('Voltar ao menu principal: ')
            break

# DELETE ----
    elif menu == '4':
        while True:
            os.system('cls')
            remover = Option_Apagar()
            remover.apagar()
            input('Voltar ao menu principal: ')
            break

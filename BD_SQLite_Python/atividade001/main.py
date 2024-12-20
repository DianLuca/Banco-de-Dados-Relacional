# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 02/12/2024

# A atividade proposta consiste em desenvolver um sistema de gerenciamento de
# passagens aéreas utilizando Python e o banco de dados SQLite3, aplicando o
# conceito de CRUD(Create, Read, Update e Delete) para manipulação dos dados.
# O sistema deve permitir o cadastro de informações essenciais, como nome do
# passageiro, número do voo, destino, data e hora da viagem, preço do bilhete,
# entre outros detalhes relevantes. Com a estrutura de CRUD, os usuários devem
# poder adicionar novos registros de passagens, visualizar a lista de passagens
# cadastradas, atualizar informações(por exemplo, ajustar horários ou destinos)
# e, quando necessário, excluir registros de passagens.
import os
from database.manipulacao_db import criar_db
from models.utils import validar_menu
from services.crud_itens import Exibir, Adicionar, Alterar, Apagar


sub_menu = {
    '1': 'Aeroporto',
    '2': 'Empresa',
    '3': 'Gate',
    '4': 'Passageiro',
    '5': 'Passagem',
    '6': 'Servico',
    '7': 'Voo'
}


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
            for k, v in sub_menu.items():
                print(f'{k} - {v}', end=' | ')
            menu_tabela = input(
                '\nQual tabela você deseja exibir: ').lower().strip()
            menu_selecionado = sub_menu.get(menu_tabela, 'Passagem')
            print(f'\nExibindo a tabela de {menu_selecionado}(s)')
            exibir = Exibir(menu_selecionado)
            exibir.exibir()
            input('\nVoltar ao menu: ')
            break
# Criando uma conexão com o banco de dados

# CREATE ----
    elif menu == '2':
        while True:
            os.system('cls')
            for k, v in sub_menu.items():
                print(f'{k} - {v}', end=' | ')
            menu_interno = input(
                '\nEm qual tabela você deseja adicionar um elemento: ').strip().lower()
            os.system('cls')
            resposta = validar_menu(menu_interno)
            if resposta == True:
                menu_selecionado = sub_menu.get(menu_interno)
                adicionando = Adicionar(menu_selecionado.title())
                adicionando.adicionar()
            else:
                print(
                    f'A opção "{menu_interno}" selecionada não existe, tente novamente.')

            input('\nVoltar ao menu principal: ')
            break

# UPDATE ----
    elif menu == '3':
        while True:
            os.system('cls')
            for k, v in sub_menu.items():
                print(f'{k} - {v}', end=' | ')
            menu_interno = input(
                '\nEm qual tabela você deseja atualizar um elemento: ').strip().lower()
            resposta = validar_menu(menu_interno)
            if resposta == True:
                menu_selecionado = sub_menu.get(menu_interno)
                alterando = Alterar(menu_selecionado.title())
                alterando.alterar()
            else:
                print(
                    f'A opção "{menu_interno}" selecionado não existe, tente novamente.')

            input('Voltar ao menu principal: ')
            break

# DELETE ----
    elif menu == '4':
        while True:
            os.system('cls')
            for k, v in sub_menu.items():
                print(f'{k} - {v}', end=' | ')
            menu_interno = input(
                '\nEm qual tabela você deseja apagar um elemento: ').strip().lower()
            os.system('cls')
            resposta = validar_menu(menu_interno)
            if resposta == True:
                menu_selecionado = sub_menu.get(menu_interno)
                apagando = Apagar(menu_selecionado)
                apagando.apagar()
            else:
                print(
                    f'A opção "{menu_interno}" selecionado não existe, tente novamente.')

            input('Voltar ao menu principal: ')
            break

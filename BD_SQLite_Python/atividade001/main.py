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
import sqlite3
from database.manipulacao_db import criar_db
from models.utils import funcao_teste_utils
from services.crud_itens import funcao_teste_crud, Exibir, Adicionar




while True:
    os.system('cls')
    menu = input(
        '| 1 - Exibir | 2 - Adicionar | 3 - Atualizar | 4 - Apagar | 5 - Sair | \nQual a opção desejada: ').strip()
    if menu == '5':
        print('Parando!')
        break


# READ ----
    elif menu == '1':
        exibe_tabela = input('Qual tabela você deseja exibir: ').lower().strip()
        exibir = Exibir(exibe_tabela)
        for k, v, p in exibir.exibir():
            print(k, end=' | ')
            print(v, end=' | ')
            print(p, end=' | ')
            print()
            
        input('Voltar ao menu: ')
# Criando uma conexão com o banco de dados

# CREATE ----
    elif menu == '2':
        Adicionar('Aeroporto')
        input('Adicionando: ')

# UPDATE ----
    elif menu == '3':
        input('Atualizando: ')

# DELETE ----
    elif menu == '4':
        input('Apagando: ')

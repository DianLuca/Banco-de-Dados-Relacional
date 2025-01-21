from services.crud_itens import Exibir
from services.crud_itens import Adicionar
from services.crud_itens import Alterar
from services.crud_itens import Apagar
from models.utils import validar_menu
import os


sub_menu = {
    '1': 'Aeroporto',
    '2': 'Empresa',
    '3': 'Gate',
    '4': 'Passageiro',
    '5': 'Passagem',
    '6': 'Servico',
    '7': 'Voo'
}


class Options():
    def __init__(self):
        pass

    def exibir(self):
        pass

    def adicionar(self):
        pass

    def alterar(self):
        pass

    def apagar(self):
        pass


class Option_Exibir():
    def apresentar(self):
        for k, v in sub_menu.items():
            print(f'{k} - {v}', end=' | ')
        menu_tabela = input(
            '\nQual tabela você deseja exibir: ').lower().strip()
        menu_selecionado = sub_menu.get(menu_tabela, 'Passagem')
        print(f'\nExibindo a tabela de {menu_selecionado}(s)')
        exibir = Exibir(menu_selecionado)
        exibir.exibir()


class Option_Adicionar():
    def adicionar(self):
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


class Option_Alterar():
    def alterar(self):
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


class Option_Apagar():
    def apagar(self):
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

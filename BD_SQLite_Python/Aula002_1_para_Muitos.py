import sqlite3
from prettytable import PrettyTable
from pathlib import Path
import os


os.system('cls')
# Conexão com o banco de dados (arquivo será criado se não existir)

# Caminho relativo
db_path = Path('BD_SQLite_Python') / 'bd_rel_1_n.db'
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()


# Criação da tabela de Clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, --ID único para o cliente
    nome TEXT NOT NULL,                           -- Nome do cliente
    email TEXT UNIQUE NOT NULL,                   -- Email único
    telefone TEXT,                                -- Telefone do cliente
    cidade TEXT                                   -- Cidade onde mora
)
''')

# Criação da tabela Pedidos (tabela relacionada)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos(
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, -- ID único para o pedido
    id_cliente INTEGER NOT NULL, --Relacionamento com a tabela Clientes
    produto TEXT NOT NULL, -- Nome do produto pedido
    quantidade INTEGER NOT NULL, -- Quantidade do produto
    data TEXT NOT NULL, -- Data do pedido
    valor_total REAL NOT NULL, -- Valor total do pedido
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente) -- Chave estrangeira
)
''')

# Função para verificar se um cliente existe no BD


def cliente_existe(id_cliente):
    cursor.execute(
        'SELECT 1 FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    # Retorna True se o cliente existir, False caso contrário
    return cursor.fetchone() is not None


# Função para inserir dados na tabela Clientes
def inserir_cliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    cidade = input('Digite o cidade do cliente: ')
    cursor.execute('''
        INSERT INTO Clientes (nome, email, telefone, cidade) VALUES (?, ?, ?, ?) ''', (nome, email, telefone, cidade))
    conn.commit()
    print('Cliente inserido com sucesso!')


# Função para inserir dados na tabela Pedidos
def inserir_pedido():
    # Listando os clientes
    cursor.execute('''
    SELECT * FROM Clientes               
    ''')
    
    resultados = cursor.fetchall()
    
    if not resultados:
        print('-' * 70)
        print('Nenhum cliente encontrado. Cadastre um cliente primeiro.')
        print('-' * 70)
        return
    
    tabela = PrettyTable(['id_cliente', 'Nome', 'Email', 'Telefone', 'Cidade'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)
    
    try:
        # Garantir que o ID seja um valor inteiro
        id_cliente = int(input('Digite o ID do cliente: '))
        
        # Verificar se o cliente existe antes de prosseguir 
        if not cliente_existe(id_cliente):
            print('-' * 70)
            print(f'Erro: Cliente com ID {id_cliente} não encontrado!')
            print('Por favor, cadastre o cliente primeiro.')
            print('-' * 70)
            # Returna ao menu se o cliente não existir
            return
        
        # Solicitar os dados do pedido
        produto = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade: '))
        # ISO 8601 (YYYY-MM-DD)
        data = input('Digite a data do pedido (YYYY-MM-DD): ')
        valor_total = float(input('Digite o valor total: '))
        
        # Inserir o pedido no BD
        cursor.execute('''
        INSERT INTO Pedidos (id_cliente, produto, quantidade, data, valor_total) VALUES (?, ?, ?, ?, ?) 
                       ''', (id_cliente, produto, quantidade, data, valor_total))
        conn.commit()
        
        print('Pedido inserido com  sucesso!')
    except ValueError:
        print('-' * 70)
        print('Erro: ID cliente deve ser um número inteiro.') # Observar a mensagem de  erro
        print('-' * 70)
        
        
# Função para realizar uma consulta com JOIN e exibir resultados
def consultar_pedidos():
    cursor.execute('''
    SELECT 
        Clientes.nome, Clientes.email, Clientes.cidade, 
        Pedidos.produto, Pedidos.quantidade, Pedidos.valor_total
    FROM Clientes
    JOIN Pedidos ON Clientes.id_cliente = Pedidos.id_cliente       
    ''')
    resultados = cursor.fetchall()
    
    tabela = PrettyTable(['Nome', 'Email', 'Cidade', 'Produto', 'Quantidade', 'Valor Total'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

    
# Função mpqara alterar Pedido
# Função para alterar um pedido existente
def alterar_pedido():
    try:
        # Solicitar o ID do pedido
        id_pedido = int(input('Digite o ID do pedido que deseja alterar: '))
        
        # Verifica se o pedido existe
        cursor.execute(
            'SELECT * FROM Pedidos WHERE id_pedido = ?', (id_pedido,)
        )
        pedido = cursor.fetchone()
        
        if not pedido:
            print('-' * 70)
            print(f'Erro: Pedido com ID {id_pedido} não encontrado!')
            print('-' * 70)
            return

        # Existir os dados atuais do pedido
        print('-' * 70)
        print('Dados atuais do pedido:')
        print(f'Produto: {pedido[2]}')
        print(f'Quantidade: {pedido[3]}')
        print(f'Data: {pedido[4]}')
        print(f'Valor Total: {pedido[5]}')
        print('-' * 70)
        
        produto = input('Digite o novo nome produto (ou pressione Enter para manter o atual): ') or pedido[2]
        quantidade = input('Digite a nova quantidade (ou pressione Enter para manter o atual): ') or pedido[3]
        data = input('Digite a nova data (YYYY-MM-DD) (ou pressione Enter para manter o atual): ') or pedido[4]
        valor_total = input('Digite o novo valor total (ou pressione Enter para manter o atual): ') or pedido[5]
        
        # Atualiza os dados do pedido
        cursor.execute('''
        UPDATE Pedidos SET produto = ?, quantidade = ?, data = ?, valor_total = ?
        WHERE id_pedido = ?
        ''', (produto, int(quantidade), data, float(valor_total), id_pedido,))
        conn.commit()
        print('Pedido alterado com sucesso!')
    except ValueError:
        print('-' * 70)
        print('Erro: Entrada inválida.')
        print('-' * 70)
        
while True:
    os.system('cls')
    print('\nMenu:')
    print('1 - Inserir Cliente \n2 - Inserir Pedido '
          '\n3 - Consultar Pedidos \n4 - Alterar Pedido \n5 - Sair')
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        os.system('cls')
        inserir_cliente()
        input('Pressione Enter para voltar ao menu: ')
    if opcao == '2':
        os.system('cls')
        inserir_pedido()
        input('Pressione Enter para voltar ao menu: ')
    if opcao == '3':
        os.system('cls')
        consultar_pedidos()
        input('Pressione Enter para voltar ao menu: ')
    if opcao == '4':
        os.system('cls')
        alterar_pedido()
        input('Pressione Enter para voltar ao menu: ')
    if opcao == '5':
        print('Saindo...')
        break
    else:
        print('-' * 70)
        print('Opção inválida. Tente novamente.')
        print('-' * 70)
        
# Fechando a conexão com o BD   
conn.close()
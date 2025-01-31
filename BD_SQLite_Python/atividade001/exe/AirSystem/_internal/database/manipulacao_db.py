# Para criação do banco de dados
import sqlite3
import time
import os


def conectar_bd():
    try:
        caminho_absoluto = os.path.dirname(os.path.abspath(__file__))
        
        caminho_banco = os.path.join(caminho_absoluto, 'airlines.db')

        conn = sqlite3.connect(caminho_banco)
    
        return conn
    
    except OSError as e:
        print('Não foi possível encontrar o caminho do arquivo!', e)


def criar_db():
    """_summary_
    Função para criar o banco de dados completo. O ideal é que cada comando do 
    banco seja executado separadamente, para evitar erros. Posteriormente é 
    colocado algumas exceções para evitar que o programa feche. 
    Atualizações ainda podem ser consideradas.
    """
    conn = None  # variável declarada anteriormente para o caso de o
    # banco não seja encontrado.
    try:
        # conn = sqlite3.connect('') # Para execução de testes.
        with conectar_bd() as conn:
            
        # with sqlite3.connect(
        #         '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python'
        #         +'\\atividade001\\database\\airlines.db') as conn:
            cursor = conn.cursor()

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Passageiro (
                id_passageiro INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
                );
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Aeroporto (
                id_aeroporto INTEGER PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                pais TEXT NOT NULL
                );        
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Empresa (
                id_empresa INTEGER PRIMARY KEY,
                nome TEXT NOT NULL
                ); 
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Gate (
                id_gate INTEGER PRIMARY KEY,
                identificador TEXT NOT NULL
                );    
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Servico (
                id_servico INTEGER PRIMARY KEY,
                classe TEXT NOT NULL
                );  
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Voo (
                id_voo INTEGER PRIMARY KEY,
                numero_voo TEXT NOT NULL UNIQUE,
                id_origem INTEGER NOT NULL,
                id_destino INTEGER NOT NULL,
                data_ida TEXT NOT NULL,
                data_retorno TEXT DEFAULT NULL
                );                    
            ''')

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Passagem (
                id_passagem INTEGER PRIMARY KEY,
                id_passageiro INTEGER NOT NULL,
                id_voo INTEGER NOT NULL,
                id_empresa INTEGER NOT NULL,
                id_gate INTEGER NOT NULL,
                id_servico INTEGER NOT NULL,
                preco REAL NOT NULL DEFAULT 0.0,
                FOREIGN KEY (id_passageiro) REFERENCES Passageiro(id_passageiro),
                FOREIGN KEY (id_voo) REFERENCES Voo(id_voo),
                FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa),
                FOREIGN KEY (id_gate) REFERENCES Gate(id_gate),
                FOREIGN KEY (id_servico) REFERENCES Servico(id_servico)
                );
            ''')

            conn.commit()

    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")
    except sqlite3.Error as e:
        print(f"Erro no SQLite: {e}")
        
    print(f'Programa iniciando aguarde! ')
    time.sleep(3)

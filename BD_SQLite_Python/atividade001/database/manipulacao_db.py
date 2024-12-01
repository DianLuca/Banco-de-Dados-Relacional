# Para criação do banco de dados
import sqlite3
import os

os.system('cls')


def criar_db():
    conn = None
    try:
        # conn = sqlite3.connect('') # Teste para o caso de algum erro
        conn = sqlite3.connect(
            '..\\Banco-de-Dados-Relacional\\BD_SQLite_Python\\atividade001\\database\\airlines.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Passageiro (
                id_passageiro INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            );
        ''')
        
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Aeroporto (
                id_aeroporto INTEGER PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                pais TEXT NOT NULL
            );        
        ''')
        
        
        cursor.execute('''    CREATE TABLE IF NOT EXISTS Empresa (
                id_empresa INTERGER PRIMARY KEY,
                nome TEXT NOT NULL
            ); 
        ''')
        
        
        cursor.execute('''    CREATE TABLE IF NOT EXISTS Gate (
                id_gate INTEGER PRIMARY KEY,
                identificador TEXT NOT NULL
            );    
        ''')
        
        
        cursor.execute('''    CREATE TABLE IF NOT EXISTS Servico (
                id_servico INTEGER PRIMARY KEY,
                classe TEXT NOT NULL
            );  
        ''')
        
        
        cursor.execute('''    CREATE TABLE IF NOT EXISTS Escala (
                id_escala INTEGER PRIMARY KEY,
                numero_escala TEXT NOT NULL UNIQUE
            );        
        ''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS Voo (
                id_voo INTEGER PRIMARY KEY,
                numero_voo TEXT NOT NULL UNIQUE,
                id_origem INTEGER NOT NULL,
                id_destino INTEGER NOT NULL,
                data_ida TEXT NOT NULL,
                data_retorno TEXT DEFAULT NULL
                
            );                    
        ''')
        
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Passagem (
                id_passagem INTEGER PRIMARY KEY,
                id_passageiro INTEGER NOT NULL,
                id_voo INTEGER NOT NULL,
                id_empresa INTEGER NOT NULL,
                id_gate INTEGER NOT NULL,
                id_servico INTEGER NOT NULL,
                id_numero_de_escala INTEGER DEFAULT 1,
                FOREIGN KEY (id_passageiro) REFERENCES Passageiro(id_passageiro),
                FOREIGN KEY (id_voo) REFERENCES Voo(id_voo),
                FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa),
                FOREIGN KEY (id_gate) REFERENCES Gate(id_gate),
                FOREIGN KEY (id_servico) REFERENCES Servico(id_servico),
                FOREIGN KEY (id_numero_de_escala) REFERENCES Escala(id_escala)
            );
        ''')


        conn.commit()

    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {e}")
    except sqlite3.Error as e:
        print(f"Erro no SQLite: {e}")
    finally:
        if conn:
            print('Banco de Dados foi fechado!')
            conn.close()


criar_db()

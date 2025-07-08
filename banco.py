import sqlite3
import json

# conecta e cria o banco bd 
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# apaga a tabela clientes se ja existir 
cursor.execute("DROP TABLE IF EXISTS CLIENTES")

# tabela com id nome email e telefone
cursor.execute('''
CREATE TABLE CLIENTES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT
)
''')

# inserção dos clientes 
cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Isabela Rodrigues', 'isabela.carvalho@email.com', '21999333666')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Maria Eduarda', 'mariaeduarda.silva@email.com', '21999888444')
''')
cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Iasmin Soares', 'iasmin.soares@email.com', '12666333999')
''')
cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Carla Gonçalves', 'carla.gonçalves@email.com', '12999456333')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Ana Paula', 'ana.paula@email.com', '21999887766')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('João Henrique', 'joao.henrique@email.com', '21988776655')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Mariana Costa', 'mariana.costa@email.com', '21977665544')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Ana Maria', 'ana.maria@email.com', '21966554433')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Carlos Eduardo', 'carlos.eduardo@email.com', '21955443322')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Maria Clara', 'maria.clara@email.com', '21944332211')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Fernanda Lima', 'fernanda.lima@email.com', '21933221100')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Joana Martins', 'joana.martins@email.com', '21922110099')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Bruno Ferreira', 'bruno.ferreira@email.com', '21911002233')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Letícia Andrade', 'leticia.andrade@email.com', '21922334455')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Gabriel Souza', 'gabriel.souza@email.com', '21933445566')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Tatiane Ribeiro', 'tatiane.ribeiro@email.com', '21944556677')
''')

cursor.execute('''
INSERT INTO CLIENTES (nome, email, telefone)
VALUES ('Amanda Soares', 'amanda.soares@email.com', '21955667788')
''')


# salva no banco
conexao.commit()

print("Banco de dados criado com sucesso.")

# lê todas as linhas da tabela (sem LIMIT, pega tudo)
cursor.execute("SELECT * FROM CLIENTES")   

linhas = cursor.fetchall()  # pega todas as linhas. Se não tiver nada retorna lista vazia

if linhas:   # se tem pelo menos uma linha
    colunas = [desc[0] for desc in cursor.description]    # cria uma lista com os nomes das colunas  
    
    # cria uma lista de dicionários, um pra cada linha,
    # juntando o nome da coluna com o valor daquela linha
    lista_clientes = [dict(zip(colunas, linha)) for linha in linhas]  

    # salva a lista toda num arquivo json bonitinho
    with open('clientes.json', 'w', encoding='utf-8') as arquivo_json:     
        json.dump(lista_clientes, arquivo_json, ensure_ascii=False, indent=4)

    print("Arquivo clientes.json criado com sucesso!")
else:
    print("Tabela clientes vazia ou inexistente.")

# fecha a conexao
conexao.close()

# import sqlite3

# # Conectar ao banco de dados (ou criar se não existir)
# conn = sqlite3.connect('meu_banco_de_dados.db')
# cursor = conn.cursor()

# # Criar uma tabela
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS usuarios (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         idade INTEGER NOT NULL
#     )
# ''')

# # Inserir dados na tabela
# cursor.execute('''
#     INSERT INTO usuarios (nome, idade)
#     VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)
# ''')

# # Salvar (commit) as mudanças
# conn.commit()

# # Fechar a conexão
# conn.close()

import requests

url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Concurso:", data["concurso"])
    print("Data:", data["data"])
    print("Dezenas sorteadas:", data["dezenas"])
else:
    print("Erro ao acessar a API:", response.status_code)



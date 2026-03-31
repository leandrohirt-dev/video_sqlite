import sqlite3

# 1. Conectando com o banco de dados (ou criando um novo)
conexao = sqlite3.connect("meu_banco.db")

# 2. Criando um cursor
cursor = conexao.cursor()

# 3. Escrevendo um comando SQL para criar uma tabela
comando_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""

# 4. Executando o comando SQL
cursor.execute(comando_sql)

# 5. Salvando alterações no banco de dados
conexao.commit()

# 6. Fechando a conexão com o banco de dados
conexao.close()

print("Banco de dados e tabela criados com sucesso!")
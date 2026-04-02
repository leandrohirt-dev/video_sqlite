import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

conexao.close()

print("Lista de usuários cadastrados:")
for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
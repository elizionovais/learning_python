
import sqlite3

con = sqlite3.connect('empresa.db')

# operações de banco de dados aqui
cursor = con.cursor()

# exp_sql = """
#     SELECT matricula, nome FROM funcionarios
#     WHERE salario > 2000
#     ORDER BY nome
# """

exp_sql = """
    SELECT matricula, nome FROM funcionarios
    WHERE nome LIKE :args
"""
nome = input('Digite o nome do funcionário: ')
args = (f'%{nome}%',)

cursor.execute(exp_sql, args)

data = cursor.fetchall()
for line in data:
    print(f'Matricula: {line[0]} - Nome: {line[1]}')
    
cursor.close()
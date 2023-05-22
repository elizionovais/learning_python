
import sqlite3

con = sqlite3.connect('empresa.db')

# operações de banco de dados aqui
cursor = con.cursor()

# exp_sql = 'INSERT INTO departamentos VALUES (?, ?)'

# registers = [
#     (1, 'Financeiro'),
#     (2, 'Marketing'),
#     (3, 'Tecnologia'),
#     (4, 'Recursos Humanos'),
#     (5, 'Comercial'),
#     (6, 'Logística'),]

# exp_sql = 'INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?, ?, ?, ?)'

# registers = [
#     (1001, 'João', 123456789, 'M', 1, 'Rua 1', 'São Paulo', 1000.00),
#     (1002, 'Maria', 987654321, 'F', 2, 'Rua 2', 'sorocaba', 2000.00),
#     (2003, 'José', 123456790, 'M', 3, 'Rua 3', 'campinas', 3000.00),
#     (1004, 'Ana', 987654320, 'F', 4, 'Rua 4', 'almenara', 4000.00),]

# exp_sql = 'INSERT INTO competencias (nome, area) values (?, ?)'

# registers = [
#     ('Python', 'Tecnologia'),
#     ('Java', 'Tecnologia'),
#     ('lideranca', 'Gestão'),
#     ('organizacao', 'Gestão'),
#     ('Vendas', 'Negócios'),]

exp_sql = 'INSERT INTO funcionarios_competencias VALUES (?, ?, ?)'

registers = [
    (1001, 1, '2020-01-01'),
    (1002, 2, '2020-05-01'),
    (2003, 3, '2021-01-01'),
    (1001, 4, '2022-01-01'),]

for register in registers:
    cursor.execute(exp_sql, register)
    
con.commit()
cursor.close()
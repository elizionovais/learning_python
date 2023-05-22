import os
os.remove('empresa.db') if os.path.exists('empresa.db') else None

import sqlite3

con = sqlite3.connect('empresa.db')

# operações de banco de dados aqui
cursor = con.cursor()

exp_sql = """
    CREATE TABLE departamentos (
        id  integer  NOT NULL PRIMARY KEY,
        nome  varchar(100)  NOT NULL
    )
"""
cursor.execute(exp_sql)

exp_sql = """
    CREATE TABLE funcionarios (
        matricula decimal(5) NOT NULL PRIMARY KEY,
        nome varchar(100) NOT NULL,
        rg decimal(9) NOT NULL UNIQUE,
        sexo char(1) CHECK (sexo IN ('M', 'F')),
        depto integer,
        endereco varchar(200),
        cidade varchar(100) DEFAULT 'São Paulo',
        salario decimal(10,2),
        FOREIGN KEY (depto) REFERENCES departamentos(id)
    )
"""
cursor.execute(exp_sql)

exp_sql = """
    CREATE TABLE IF NOT EXISTS competencias (
        id  integer  NOT NULL,
        nome  varchar(100)  NOT NULL,
        area varchar(100)  CHECK (area IN ('Tecnologia', 'Gestão', 'Negócios')),
        PRIMARY KEY (id AUTOINCREMENT)
    )
"""
cursor.execute(exp_sql)

exp_sql = """
    CREATE TABLE funcionarios_competencias (
        matricula decimal(5) REFERENCES funcionarios(matricula),
        id integer REFERENCES competencias(id),
        data DATE NOT NULL
    )
"""
cursor.execute(exp_sql)
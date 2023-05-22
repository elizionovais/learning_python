from mysql.connector import connect

con = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
)

# operações de banco de dados aqui


con.close()
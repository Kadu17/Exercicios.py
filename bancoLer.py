import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    database = 'netflix',
    user = 'root',
    password =''
)

if conexao.is_connected():
    print(f'conectou a {conexao.get_server_info()}')

def Read():
    cursor = conexao.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print(f'Banco => {linha[0]}')

    sql = 'select * from usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall()

    for i in linhas:
        print(i[0], end='\t')
        print(i[1], end='\t')
        print(i[2], end='\t')
        print(i[3], end='\t')
        print(i[4], end='\t')
        print(i[5])

    return linhas


import mysql.connector
conexao = cursor = 0

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        database = 'netflix',
        user = 'root',
        password =''
    )

    inserir_filmes = """INSERT INTO filmes(filme,plano,descricao,class)
    values
        ('Matrix', 'basic', 'hdskj', 12),
        ('Eu, eu mesmo e Irene', 'medium', 'hdskj', 0);"""
    cursor = conexao.cursor()
    cursor.execute(inserir_filmes)
    conexao.commit()

    sql = 'select * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()

    for i in linhas:
        print(i[0], end='\t')
        print(i[1], '' * (10 - len(i[1])), end='\t')
        print(i[2], '' * (20 - len(i[2])), end='\t')
        print(i[3], '' * (10 - len(i[3])), end='\t')
        print(i[4])




except ConnectionError as e:
    print(f'Erro: {e}')
finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close
        print('Fim da conexão')
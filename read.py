from conectar import cursor


def listar_usuarios():
    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    return cursor.fetchall()


def listar_filmes():
    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    return cursor.fetchall()


def procurar_usuario(user, email):
    sql = f"SELECT * from usuarios WHERE idUsuario = '{IdUser}'"
    cursor.execute(sql)
    return cursor.fetchall()


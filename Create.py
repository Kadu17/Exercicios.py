import mysql.connector

conexao = mysql.connector.connect(user='root', password='', host='localhost', database='netflix')
cursor = conexao.cursor()


class User:

    def add(self, usuario, email, plano, tipo, idade):
        cursor.execute(
            f'insert into usuarios(usuario, email, plano, tipo, idade) values ("{usuario}", "{email}", "{plano}", "{tipo}", "{idade}")')
        conexao.commit()

    def get_Users(self, usuario):
        cursor.execute(f'select * from usuarios where usuario = "{usuario}"')
        return cursor.fetchone()

    def get_User(self):
        pass


def Create_user():
    usuario = User()

    usuario.add(usuario=input("Digite o nome do usuario: "), email=input("Digite seu email: "),
                plano=input("Qual o seu plano: "), tipo=input("Qual o tipo do usuario:  "),
                idade=input("Digite sua idade: "))


class filme:

    def __add__(self, filme, plano, descrição, classificação):
        cursor.execute(
            f'insert into filme(filme, plano, descrição, classificação) values ("{filme}", "{plano}", "{descrição}", "{classificação}")')
        conexao.commit()

    def get_filme(self, filme):
        cursor.execute(f'select * from filmes where filme = "{filme}"')
        return  cursor.fetchone()


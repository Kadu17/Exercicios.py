from netflix import Cliente
from Create import Create_user
from bdLer import Read

usuario = []
usuarios = []
escolhido = ['Kadu', '', '', 'user']
planos = ['basic', 'medium', 'premium']
tipos = ['admin', 'user']

read = Read()
def menu():
    while True:
        print('---------------------\n'
              f'Usuário: {escolhido[0]}\n'
              f'Tipo: {escolhido[3]}\n'
              '[0] - Sair\n'
              '[1] - Cadastrar Usuário\n'
              '[2] - Cadastrar Filme\n'
              '[3] - Login\n'
              '[4] - Listar Filmes\n'
              '---------------------\n')
        op = int(input('Escolha a opção: '))
        if op == 0:
            break

        elif op == 1:
            usuario.clear()
            Read()
        elif op == 2:
            Create_user()



menu()
#             while True:
#                 plano = input('Plano: ')
#                 if plano in planos:
#                     usuario.append(plano)
#                     break
#                 else:
#                     print('Plano inválido')
#             while True:
#                 print('Tipos: | user | admin')
#                 tipo = input('Tipo: ')
#                 if tipo in tipos:
#                     usuario.append(tipo)
#                     break
#                 else:
#                     print('Tipo inválido')
#             usuarios.append(usuario[:])
#             usuario.clear()
#             print(usuarios)
#         elif op == 2:
#             pass
#
#         elif op == 3:
#             cliente = input('Nome: ')
#             for i in range(len(usuarios)):
#                 if cliente == usuarios[i][0]:
#                     escolhido.append(usuario[i][0])
#                     escolhido.append(usuario[i][1])
#                     escolhido.append(usuario[i][2])
#                     escolhido.append(usuario[i][3])
#
#             print(escolhido)
#
# menu()
# b1 = Cliente(escolhido[0], escolhido[1], escolhido[2], escolhido[3])

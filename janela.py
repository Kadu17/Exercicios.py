from tkinter import ttk
from tkinter import *
from create import inserir_filmes, inserir_usuarios
from read import listar_usuarios, procurar_usuario
from update import up_usuario
from delete import dt_usuario

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inserts()
        self.lista()
        self.select_list()
        janela.mainloop()

    def tela(self):
        self.janela.title("NETFLIX")
        self.janela.configure(background="cyan")
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=500)

    def frames(self):
        self.frame0 = Frame(self.janela, bg="black")
        self.frame0.place(relheight=0.11, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="black")
        self.frame1.place(relheight=0.25, relwidth=0.94, relx=0.03, rely=0.20)
        self.frame2 = Frame(self.janela, bg="black")
        self.frame2.place(relheight=0.45, relwidth=0.94, relx=0.03, rely=0.50)

    def botoes(self):
        self.btBuscar = Button(self.frame0, text='Buscar', bg="cyan", command=self.select_user)
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame0, text='Limpar', bg="cyan", command=self.limpar_tela)
        self.btLimpar.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btCreate = Button(self.frame0, text='Create', bg="cyan", command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame0, text='Read', bg="cyan", command=self.select_list)
        self.btRead.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btUpdate = Button(self.frame0, text='Update', bg="cyan", command=self.update_user)
        self.btUpdate.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame0, text='Delete', bg="cyan", command=self.delete_user)
        self.btDelete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.50)

    def labels(self):
        self.lbIDUsuario = Label(self.frame0, text="ID", background="cyan")
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)

        self.lbNome = Label(self.frame1, text="Nome", bg="cyan")
        self.lbNome.place(relx=0.005, rely=0.06, relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame1, text="Email", bg="cyan")
        self.lbEmail.place(relx=0.005, rely=0.37, relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame1, text="Plano", bg="cyan")
        self.lbPlano.place(relx=0.005, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame1, text="Tipo", bg="cyan")
        self.lbTipo.place(relx=0.32, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbIdade = Label(self.frame1, text="Idade", bg="cyan")
        self.lbIdade.place(relx=0.62, rely=0.69, relwidth=0.1, relheight=0.15)

    def inserts(self):
        self.insertIDUsuario = Entry(self.frame0, background="cyan")
        self.insertIDUsuario.place(relx=0.005, rely=0.40, relwidth=0.1, relheight=0.47)

        self.insertNome = Entry(self.frame1, bg="cyan")
        self.insertNome.place(relx=0.155, rely=0.05, relwidth=0.75, relheight=0.23)

        self.insertEmail = Entry(self.frame1, bg="cyan")
        self.insertEmail.place(relx=0.155, rely=0.37, relwidth=0.75, relheight=0.23)

        self.insertPlano = Entry(self.frame1, bg="cyan")
        self.insertPlano.place(relx=0.155, rely=0.69, relwidth=0.15, relheight=0.23)

        self.insertTipo = Entry(self.frame1, bg="cyan")
        self.insertTipo.place(relx=0.45, rely=0.69, relwidth=0.15, relheight=0.23)

        self.insertIdade = Entry(self.frame1, bg="cyan")
        self.insertIdade.place(relx=0.75, rely=0.69, relwidth=0.15, relheight=0.23)

    def lista(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Email')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Class')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=35)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=188)
        self.listaCli.column('#4', width=70)
        self.listaCli.column('#5', width=70)
        self.listaCli.column('#6', width=70)

        self.listaCli.place(relx=0.025, rely=0.075, relwidth=0.925, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.949, rely=0.079, relwidth=0.02, relheight=0.84)

    def insert_user(self):
        if self.insertNome.get()!='':
            inserir_usuarios(self.insertNome.get(), self.insertEmail.get(), self.insertPlano.get(),
                         self.insertTipo.get(), self.insertIdade.get())
            self.select_list()
            self.limpar_tela()

    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in listar_usuarios():
           self.listaCli.insert(parent='', index=0, values=i)

    def select_user(self):
        self.listaCli.delete(*self.listaCli.get_children())
        usuario = procurar_usuario(self.insertIDUsuario.get())
        self.listaCli.insert(parent='', index=0, values=usuario[0])
        self.insertNome.insert(0, usuario[0][1])
        self.insertEmail.insert(0, usuario[0][2])
        self.insertPlano.insert(0, usuario[0][3])
        self.insertTipo.insert(0, usuario[0][4])
        self.insertIdade.insert(0, usuario[0][5])

    def limpar_tela(self):
        self.insertIDUsuario.delete(0, end)
        self.insertNome.delete(0, end)
        self.insertPlano.delete(0, end)
        self.insertEmail.delete(0, end)
        self.insertTipo.delete(0, end)
        self.insertIdade.delete(0, end)
        self.select_list()

    def delete_user(self):
        dt_usuario(self.insertIDUsuario.get())
        self.select_list()
        self.limpar_tela()

    def update_user(self):
        if self.insertNome.get():
            self.insertIDUsuario.update()
            self.insertNome.update()
            self.insertPlano.update()
            self.insertEmail.update()
            self.insertTipo.update()
            self.insertIdade.update()
            up_usuario(self.insertIDUsuario.get(),
                       self.insertNome.get(),
                       self.insertEmail.get(),
                       self.insertPlano.get(),
                       self.insertTipo.get(),
                       self.insertIdade.get())
            self.limpar_tela()
            self.select_list()

from tkinter import *
class Cadus:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Cadastro de Usuários")
        self.master.geometry("400x400")

        # Frame principal
        self.cadus = Frame(master)
        self.cadus.pack(pady=20)


        self.label_titulo = Label(self.cadus, text='Informe os dados :', font=('Arial', 14, 'bold'))
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=10)


        self.label_id = Label(self.cadus, text='idUsuario:', font=('Arial', 12))
        self.label_id.grid(row=1, column=0, padx=0, pady=5, sticky=W)

        self.entry_id = Entry(self.cadus, font=('Arial', 12))
        self.entry_id.grid(row=1, column=1, padx=10, pady=5)

        self.botao_buscar = Button(self.cadus, text="Buscar", font=('Arial', 10))
        self.botao_buscar.grid(row=1, column=2, padx=10, pady=5)


        self.label_nome = Label(self.cadus, text='Nome:', font=('Arial', 12))
        self.label_nome.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.entry_nome = Entry(self.cadus, font=('Arial', 12))
        self.entry_nome.grid(row=2, column=1, columnspan=2, padx=10, pady=5)


        self.label_telefone = Label(self.cadus, text='Telefone:', font=('Arial', 12))
        self.label_telefone.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.entry_telefone = Entry(self.cadus, font=('Arial', 12))
        self.entry_telefone.grid(row=3, column=1, columnspan=2, padx=10, pady=5)


        self.label_email = Label(self.cadus, text='E-mail:', font=('Arial', 12))
        self.label_email.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        self.entry_email = Entry(self.cadus, font=('Arial', 12))
        self.entry_email.grid(row=4, column=1, columnspan=2, padx=10, pady=5)


        self.label_usuario = Label(self.cadus, text='Usuário:', font=('Arial', 12))
        self.label_usuario.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        self.entry_usuario = Entry(self.cadus, font=('Arial', 12))
        self.entry_usuario.grid(row=5, column=1, columnspan=2, padx=10, pady=5)


        self.label_senha = Label(self.cadus, text='Senha:', font=('Arial', 12))
        self.label_senha.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        self.entry_senha = Entry(self.cadus, font=('Arial', 12), show="*")
        self.entry_senha.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

        self.botao_inserir = Button(self.cadus, text="Inserir", font=('Arial', 12))
        self.botao_inserir.grid(row=7, column=0, padx=10, pady=20)

        self.botao_alterar = Button(self.cadus, text="Alterar", font=('Arial', 12))
        self.botao_alterar.grid(row=7, column=1, padx=10, pady=20)

        self.botao_excluir = Button(self.cadus, text="Excluir", font=('Arial', 12))
        self.botao_excluir.grid(row=7, column=2, padx=10, pady=20)


root = Tk()
Cadus(root)
root.mainloop()
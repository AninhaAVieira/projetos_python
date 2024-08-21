from tkinter import *

class FormularioCliente:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Cliente")
        self.master.geometry("400x300")

        self.form_frame = Frame(self.master)
        self.form_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        self.label_titulo = Label(self.form_frame, text="Informe os dados do cliente:", font=("Arial", 14, "bold"))
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=10)

        self.label_nome = Label(self.form_frame, text="Nome:", font=("Arial", 12))
        self.label_nome.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.entry_nome = Entry(self.form_frame, font=("Arial", 12))
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.label_cpf = Label(self.form_frame, text="CPF:", font=("Arial", 12))
        self.label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_cpf = Entry(self.form_frame, font=("Arial", 12))
        self.entry_cpf.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.label_data_nascimento = Label(self.form_frame, text="Data de Nascimento:", font=("Arial", 12))
        self.label_data_nascimento.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.entry_data_nascimento = Entry(self.form_frame, font=("Arial", 12))
        self.entry_data_nascimento.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.label_profissao = Label(self.form_frame, text="Profissão:", font=("Arial", 12))
        self.label_profissao.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.entry_profissao = Entry(self.form_frame, font=("Arial", 12))
        self.entry_profissao.grid(row=4, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.label_telefone = Label(self.form_frame, text="Telefone:", font=("Arial", 12))
        self.label_telefone.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        self.entry_telefone = Entry(self.form_frame, font=("Arial", 12))
        self.entry_telefone.grid(row=5, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.botao_inserir = Button(self.form_frame, text="Inserir", font=("Arial", 12))
        self.botao_inserir.grid(row=6, column=0, padx=10, pady=20, sticky=W)
        self.botao_alterar = Button(self.form_frame, text="Alterar", font=("Arial", 12))
        self.botao_alterar.grid(row=6, column=1, padx=10, pady=20)
        self.botao_excluir = Button(self.form_frame, text="Excluir", font=("Arial", 12))
        self.botao_excluir.grid(row=6, column=2, padx=10, pady=20, sticky=E)

        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=2)
        self.form_frame.grid_columnconfigure(2, weight=1)

root = Tk()
app = FormularioCliente(root)
root.mainloop()
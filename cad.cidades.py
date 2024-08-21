from tkinter import *
class FormularioCidade:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Cidade")
        self.master.geometry("400x300")

        self.form_frame = Frame(self.master)
        self.form_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        self.label_titulo = Label(self.form_frame, text="Informe os dados da cidade:", font=("Arial", 14, "bold"))
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=10)

        self.label_nome = Label(self.form_frame, text="Nome:", font=("Arial", 12))
        self.label_nome.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.entry_nome = Entry(self.form_frame, font=("Arial", 12))
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.label_uf = Label(self.form_frame, text="UF:", font=("Arial", 12))
        self.label_uf.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_uf = Entry(self.form_frame, font=("Arial", 12))
        self.entry_uf.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky=W+E)

        self.botao_inserir = Button(self.form_frame, text="Inserir", font=("Arial", 12), command=self.inserir)
        self.botao_inserir.grid(row=3, column=0, padx=10, pady=20, sticky=W)
        self.botao_alterar = Button(self.form_frame, text="Alterar", font=("Arial", 12), command=self.alterar)
        self.botao_alterar.grid(row=3, column=1, padx=10, pady=20)
        self.botao_excluir = Button(self.form_frame, text="Excluir", font=("Arial", 12), command=self.excluir)
        self.botao_excluir.grid(row=3, column=2, padx=10, pady=20, sticky=E)

        self.form_frame.grid_rowconfigure(0, weight=1)
        self.form_frame.grid_rowconfigure(1, weight=1)
        self.form_frame.grid_rowconfigure(2, weight=1)
        self.form_frame.grid_rowconfigure(3, weight=1)
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)
        self.form_frame.grid_columnconfigure(2, weight=1)

    def inserir(self):
        print("Inserir")

    def alterar(self):
        print("Alterar")

    def excluir(self):
        print("Excluir")

if __name__ == "__main__":
    root = Tk()
    app = FormularioCidade(root)
    root.mainloop()
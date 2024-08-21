from tkinter import *
class Projeto:

    def __init__(self, master=None):
        self.usuarios = Frame(master)
        self.usuarios.pack()

        self.fontePadrao = ('Arial', 12)

        self.usu = Button(self.usuarios, text='Usuários', font=self.fontePadrao)
        self.usu.pack(side=LEFT)

        self.cid = Button(self.usuarios, text='Cidades', font=self.fontePadrao)
        self.cid.pack(side=LEFT)

        self.cli = Button(self.usuarios, text='Clientes', font=self.fontePadrao)
        self.cli.pack(side=LEFT)

        self.fec = Button(self.usuarios, text='Fechar', font=self.fontePadrao)
        self.fec['command'] = self.usuarios.quit
        self.fec.pack(side=LEFT)


root = Tk()
Projeto(root)
root.mainloop()
from tkinter import*
from tkinter import ttk

class Menu_reall(Tk):
    def __init__(self):
        super().__init__()
        self.title('Menu')

        self.L1 = Label(self,text='Odaberite sport')

        self.photo1 = PhotoImage(file="slike/kosarka.png")
        self.B1 = Button(self, image = self.photo1, height=160, width=160 )
        self.photo2 = PhotoImage(file="slike/rukomet.png")
        self.B2 = Button(self, image=self.photo2, height=160, width=160)
        self.photo3 = PhotoImage(file="slike/odbojka.png")
        self.B3 = Button(self, image=self.photo3, height=160, width=160)
        self.photo4 = PhotoImage(file="slike/nogomet.png")
        self.B4 = Button(self, image=self.photo4, height=160, width=160)

        self.L1.grid(row=0, column=0)
        self.B1.grid(row=1, column=0)
        self.B2.grid(row=2, column=1)
        self.B3.grid(row=1, column=2)
        self.B4.grid(row=2, column=3)

        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(4):
            self.rowconfigure(0, weight=1)


a = Menu_reall()
a.mainloop()
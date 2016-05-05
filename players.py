from tkinter import*
import utils

class Players(Toplevel):
    def __init__(self):
        super().__init__()

        # postavke prozora
        self.resizable(0, 0)
        self.title('Semafor')
        self.geometry("275x350+480+200")
        self.home_names = utils.make_list('players_home.txt')
        self.guest_names = utils.make_list('players_guest.txt')

        # list boxovi
        self.l = []
        self.l += [Listbox(self, height = len(self.home_names))]#0
        self.l += [Listbox(self, height = len(self.guest_names))]#1
        self.l[0].place(x = 0, y = 0)
        self.l[1].place(x = 150, y = 0)
        for i in self.home_names:
            self.l[0].insert(END, i)
        for i in self.guest_names:
            self.l[1].insert(END, i)

        #gumbi
        self.b_names = ['Point', 'Foul', 'Rebound']
        self.b_home =[]
        self.b_guest =[]
        for i in self.b_names:
            self.b_home += [Button(self, text = i)]
            self.b_guest += [Button(self, text = i)]
        self.y = 240
        for i in self.b_home:
            i.place(x=20, y= self.y)
            self.y += 30
        self.y = 240
        for i in self.b_guest:
            i.place(x=170, y=self.y)
            self.y += 30



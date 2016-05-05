from semafor import*
from tkinter import*
import utils

class Meni(Tk):
    def __init__(self):
        super().__init__()
        self.title('Semafor')
        self.geometry("150x100+200+200")

        self.b = []
	    
        COORD = [(0, 0), (0, 25), (0, 50), (0, 75)]
        TEXT = ["Semafor", "Postavke", "Izlaz", "?"]
        CMD = [self.zapocni, self.postavke, self.destroy, self.informacije]

        x1 = 0
        for x,y in COORD:
            self.b += [Button(self, text = TEXT[x1], width=20, command  = CMD[x1])]
            self.b[x1].place(x=x, y=y)
            x1+=1

			
    def zapocni(self):
        s = Semafor(Sport(utils.make_list('players_home.txt')))

    def postavke(self):
        a=1
    def informacije(self):
        a=1



from tkinter import *
from tkinter import ttk

class Sport():

    def __init__(self, player_list):

        self.home_name='HOME'
        self.guest_name='GUEST'
        self.score_home=0
        self.score_guest=0

    def generateDisplay(self):
        root = Tk()

        self.labelfont = ('digital-7', 35 )

        lhome = ttk.Label(root, name='homename', text=self.home_name, background='black', foreground='white', font=self.labelfont)
        ltime = ttk.Label(root, name='time', text='00:00', background='black', foreground='yellow', font=self.labelfont)
        lguest = ttk.Label(root, name='guestname', text=self.guest_name,  background='black', foreground='white', font=self.labelfont)
        lscoreh = ttk.Label(root, name='score_home', text=str(self.score_home),  background='black', foreground='red', font=self.labelfont )
        lscoreg = ttk.Label(root, name='score_guest', text=str(self.score_guest), background='black', foreground='red',font=self.labelfont)

        lhome.grid(column=0, row=0, padx=3,pady=3)
        ltime.grid(column=1, row=0, padx=3,pady=3)
        lguest.grid(column=2, row=0, padx=3,pady=3)
        lscoreh.grid(column=0, row=1, padx=3, pady=3)
        lscoreg.grid(column=2, row=1, padx=3,pady=3)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)

        return root


class Player():

    def __init__(self, name, number=0):
        self.name = name
        self.number = number
        self.points = 0
        self.misses = 0
        self.height = 0
        self.weight = 0

    def score(self):
        self.points+=1

    def miss(self):
        self.miss+=1

class Kosarkas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)
        self.offensive_rebound = 0
        self.defensive_rebound = 0
        self.field_goal_attempts = [0, 0, 0]
        self.field_goal_made = [0, 0, 0]
        self.fauls = 0
        self.steals = 0

    def score(self, type=1):
        self.points += type
        self.field_goal_made[type] += 1


class Rukometas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)

class Odbojkas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)

class Nogometas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)

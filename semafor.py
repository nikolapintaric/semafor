import time
from form import*
from players import*
from sport import *


from xml.etree.ElementTree import XML

class Semafor(Toplevel):
    def __init__(self, sport):
        super().__init__()

        #postavke prozora
        self.resizable(1,1)
        self.title('Semafor')
        self.geometry("280x280+200+200" )
        self.configure(bg="black")

        #kordinate za widgete
        self.bcor = [(20,100),(20,130),(200,100),(200,130),(130,100),(130,130),(120,160)]
        self.lcor = [(20,50),(200,50),(100,20), (20,20), (200, 20)]
        self.ecor = [(124,190)]

        #lokalne varijable
        self.bool = False
        self.time_start = 0.00
        self.time_reall = 0.00
        self.time_store = 0.00
        self.time_decimal = 1
        self.time_refresh = 100
        self.time_min = 0
        self.time_print = Form(self.time_min, self.time_reall+self.time_store, self.time_decimal)
        self.v = StringVar()
        self.v.set(self.time_print.vrati())

        Display = sport.generateDisplay()

        Display.pack(self)

        # statistika
        self.a = Players()
        self.a.mainloop()


    def change_score(self,x, sport):
        if(x==0):
            sport.score_home += 1
            self.l[0].configure(text=str(self.score_home))
        if(x==1):
            if(sport.score_home!=0):
                sport.score_home -= 1
                self.l[0].configure(text=str(self.score_home))
        if(x==2):
            sport.score_guest += 1
            self.l[1].configure(text=str(self.score_guest))
        if(x==3):
            if(sport.score_guest!=0):
                sport.score_guest -= 1
                self.l[1].configure(text=str(self.score_guest))

    def start(self):
        if(self.bool != True):
            self.bool = True
            self.time_start = time.time()
            self.time()

    def stop(self):
        if self.bool != False:
            self.bool = False
            self.time_store += self.time_reall

    def time(self):
        if self.bool:
            self.time_reall = (time.time()-self.time_start)
            self.time_print = Form(self.time_min, self.time_reall+self.time_store, self.time_decimal)
            self.l[2].configure(text=self.time_print.vrati())
            if self.time_reall+self.time_store >= 60:
                self.time_min += 1
                self.time_reall = 0.00
                self.time_start = time.time()
                self.time_store = 0.00  
            self.after( self.time_refresh ,  self.time)

    def set(self):
        self.time_reall = 0.00
        self.time_start = time.time()
        a,b = self.v.get().split(':')
        self.time_min = int(a)
        self.time_store = float(b) 
        self.time_print = Form(self.time_min, self.time_reall+self.time_store, self.time_decimal)
        self.l[2].configure(text=self.time_print.vrati())
        


        
        

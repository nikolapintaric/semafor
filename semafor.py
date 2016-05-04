import time
from form import*
from players import*

class Semafor(Toplevel):
    def __init__(self, home_name = 'HOME', guest_name = 'GUEST', score_home = 0, score_guest = 0, time_decimal = 1, time_refresh = 1):
        super().__init__()

        #postavke prozora
        self.resizable(0,0)
        self.title('Semafor')
        self.geometry("280x280+200+200" )
        self.configure(bg="black")

        #kordinate za widgete
        self.bcor = [(20,100),(20,130),(200,100),(200,130),(130,100),(130,130),(120,160)]
        self.lcor = [(20,50),(200,50),(100,20), (20,20), (200, 20)]
        self.ecor = [(124,190)]
        
        #globalne varijable
        self.score_home = score_home
        self.score_guest = score_guest
        self.time_decimal = time_decimal
        self.time_refresh = time_refresh  # in ms
        self.home_name = home_name
        self.guest_name = guest_name

        #lokalne varijable
        self.bool = False
        self.time_start = 0.00
        self.time_reall = 0.00
        self.time_store = 0.00
        self.time_min = 0
        self.time_print = Form(self.time_min, self.time_reall+self.time_store, self.time_decimal)
        self.v = StringVar()
        self.v.set(self.time_print.vrati())

        #inicijalizacija
        self.e = []
        self.e += [Entry(self, textvariable=self.v, width=7 )] #0
        for i in range(len(self.e)):
            self.e[i].place(x=self.ecor[i][0], y=self.ecor[i][1])
        
        self.l = []
        self.l += [Label(self, text=str(self.score_home), font= ("Digital-7", 22), fg="red", bg="black")] #0
        self.l += [Label(self, text=str(self.score_guest), font= ("Digital-7", 22), fg="red", bg="black")] #1
        self.l += [Label(self, text=self.time_print.vrati(), font= ("Digital-7", 22), fg="yellow", bg="black")] #2
        self.l += [Label(self, text=self.home_name,  font=("Digital-7", 22), fg= "white", bg="black")]  # 4
        self.l += [Label(self, text=self.guest_name, font=("Digital-7", 22), fg= "white", bg="black")]  # 5
        for i in range(len(self.l)):
            self.l[i].place(x=self.lcor[i][0], y=self.lcor[i][1])
        
        self.b = []
        self.b += [Button(self, text="+", command=lambda: self.change_score(0))] #0
        self.b += [Button(self, text="-", command=lambda: self.change_score(1))] #1
        self.b += [Button(self, text="+", command=lambda: self.change_score(2))] #2
        self.b += [Button(self, text="-", command=lambda: self.change_score(3))] #3
        self.b += [Button(self, text="Start", command=self.start)] #4
        self.b += [Button(self, text="Stop", command=self.stop)] #5
        self.b += [Button(self, text="Set time", command=self.set)] #6
        for i in range(len(self.b)):
            self.b[i].place(x=self.bcor[i][0], y=self.bcor[i][1])

        # statistika
        self.a = Players()
        self.a.mainloop()


    def change_score(self,x):
        if(x==0):
            self.score_home += 1
            self.l[0].configure(text=str(self.score_home))
        if(x==1):
            if(self.score_home!=0):
                self.score_home -= 1
                self.l[0].configure(text=str(self.score_home))
        if(x==2):
            self.score_guest += 1
            self.l[1].configure(text=str(self.score_guest))
        if(x==3):
            if(self.score_guest!=0):
                self.score_guest -= 1
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
        


        
        

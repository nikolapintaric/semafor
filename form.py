
class Form():
    def __init__(self, minute=0, sekunde=0.0, preciznost=1):
        self.a = ''
        self.s = int(sekunde)
        self.s1 = sekunde-self.s
        self.a = "{:02d}:{:02d}".format(minute, self.s )

        if preciznost > 0:
            self.a += '.'
            self.s1 *= 10**preciznost
            self.s1 = int(self.s1)
            self.a += str(self.s1)
                  
    def vrati(self):
        return(self.a)


            
            

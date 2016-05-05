import tkinter

def realize(master, element):
    if element.tag == "form":
        frame = tkinter.Frame(master, **element.attrib)
        for subelement in element:
            widget = realize(frame, subelement)
            widget.pack()
        return frame
    else:
        options = element.attrib
        if element:
            options = options.copy()
            for subelement in element:
                options[subelement.tag] = subelement.text
        widget_factory = getattr(tkinter, element.tag.capitalize())
        return widget_factory(master, **options)

def make_list(a):
    file = open(a, "r")
    z = file.read()
    l = z.split("\n")
    file.close()
    return(l)


#class time
def start(self):
    if (self.bool != True):
        self.bool = True
        self.time_start = time.time()
        self.time()


def stop(self):
    if self.bool != False:
        self.bool = False
        self.time_store += self.time_reall


def time(self):
    if self.bool:
        self.time_reall = (time.time() - self.time_start)
        self.time_print = Form(self.time_min, self.time_reall + self.time_store, self.time_decimal)
        self.l[2].configure(text=self.time_print.vrati())
        if self.time_reall + self.time_store >= 60:
            self.time_min += 1
            self.time_reall = 0.00
            self.time_start = time.time()
            self.time_store = 0.00
        self.after(self.time_refresh, self.time)


def set(self):
    self.time_reall = 0.00
    self.time_start = time.time()
    a, b = self.v.get().split(':')
    self.time_min = int(a)
    self.time_store = float(b)
    self.time_print = Form(self.time_min, self.time_reall + self.time_store, self.time_decimal)
    self.l[2].configure(text=self.time_print.vrati())

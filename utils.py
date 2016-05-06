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



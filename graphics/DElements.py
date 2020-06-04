from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class DElement:

    def __init__(self, root, properties, fontsize):
        self.root = root
        self.x, self.y = properties[0], properties[1]
        self.w, self.h = properties[2], properties[3]
        self.stick = 'wns'
        self.state = NORMAL
        if fontsize != None: self.font = tkFont.Font(family="Times New Roman", size=fontsize)
    
    def clear(self):
        state = self.component.cget('state')
        self.component.config(state=NORMAL) 
        try:
            self.component.delete(0, 'end')
        except AttributeError as ae:
            try:
                self.component.set('')
            except AttributeError as ae:
                pass
        self.component.config(state=state)
    
    def get_text(self):
        return self.component.get()
    
class DLabel(DElement):
    def __init__(self, root, properties, fontsize, text):
        super().__init__(root, properties, fontsize)
        self.component = Label(root, text=text, font=self.font, justify=LEFT)

class DEntry(DElement):
    def __init__(self, root, properties, fontsize):
        super().__init__(root, properties, fontsize)
        self.component = Entry(root, font=self.font)

class DButton(DElement):
    def __init__(self, root, properties, fontsize, text, command, stick):
        super().__init__(root, properties, fontsize)
        self.stick = stick
        self.component = Button(root, text=text, command=command, font=self.font)

class DCombobox(DElement):
    def __init__(self, root, properties, fontsize, options):
        super().__init__(root, properties, fontsize)
        self.component = ttk.Combobox(root, font=self.font, state='readonly')
        self.stick = 'snwe'
        self.component['values'] = options
        root.option_add("*TCombobox*Listbox*Font", self.font)

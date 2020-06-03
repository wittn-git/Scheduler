from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class DComponent:
    def __init__(self, name, root, x_position, y_position, width, height, fontsize):
        self.root = root
        self.name = name
        self.x_position, self.y_position = x_position, y_position
        self.width, self.height = width, height
        self.stick = 'wns'
        self.pad_x, self.pad_y = 0, 0
        self.component = None
        if fontsize != None: self.font = tkFont.Font(family="Times New Roman", size=fontsize)
    
    def clear(self):
        if not type(self) == DCombobox and not type(self) == DEntry : return 0
        state = self.component.cget('state')
        self.component.config(state=NORMAL) 
        try:
            self.component.delete(0, 'end')
        except AttributeError as ae:
            self.component.set('')
        self.component.config(state=state)

class DPlaceHolder(DComponent):
    def __init__(self, root, x_position, y_position):
        super().__init__(root, None, x_position, y_position, 1, 1, None)
        self.component = Label(root, text='  ')

class DLabel(DComponent):
    def __init__(self, name, root, x_position, y_position, width, height, pad_x, pad_y, fontsize, text):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.pad_x, self.pad_y = pad_x, pad_y
        self.component = Label(root, text=text, font=self.font, justify=LEFT)

class DEntry(DComponent):
    def __init__(self, name,  root, x_position, y_position, width, height, fontsize, state):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.component = Entry(root, state = state, font=self.font)
    
    def get_text(self):
        return self.component.get()

class DButton(DComponent):
    def __init__(self, name, root, x_position, y_position, width, height, fontsize, text, command, stick):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.stick = stick
        self.component = Button(root, text=text, command=command, font=self.font)

class DCombobox(DComponent):
    def __init__(self, name, root, x_position, y_position, width, height, fontsize, state, options):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.component = ttk.Combobox(root, font=self.font, state=state) 
        self.stick = 'snwe'
        self.component['values'] = options
        root.option_add("*TCombobox*Listbox*Font", self.font)
    
    def get_text(self):
        return self.component.get()
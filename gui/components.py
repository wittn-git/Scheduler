from tkinter import *
import tkinter.font as tkFont

class DComponent:
    def __init__(self, name, root, x_position, y_position, width, height, fontsize):
        self.root = root
        self.name = name
        self.x_position, self.y_position = x_position, y_position
        self.width, self.height = width, height
        self.stick = 'wns'
        self.pad_x, self.pad_y = 0, 0
        if fontsize != None: self.font = tkFont.Font(family="Times New Roman", size=fontsize)

class DPlaceHolder(DComponent):
    def __init__(self, root, x_position, y_position):
        super().__init__(root, None, x_position, y_position, 1, 1, None)
        self.component = Label(root, text='test')

class DLabel(DComponent):
    def __init__(self, name, root, x_position, y_position, width, height, pad_x, pad_y, fontsize, text):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.pad_x, self.pad_y = pad_x, pad_y
        self.component = Label(root, text=text, font=self.font, justify=LEFT)

class DCanvas(DComponent):
    def __init__(self, name, root, width, height):
        super().__init__(name, root, 0, 0, width, height, 0, 0, None)
        self.component = Canvas(root, width=width, height=height)

class DEntry(DComponent):
    def __init__(self, name,  root, x_position, y_position, width, height, fontsize, state):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.component = Entry(root, state = state, font=self.font)

class DButton(DComponent):
    def __init__(self, name, root, x_position, y_position, width, height, fontsize, text, command, stick):
        super().__init__(name, root, x_position, y_position, width, height, fontsize)
        self.stick = stick
        self.component = Button(root, text=text, command=command, font=self.font)

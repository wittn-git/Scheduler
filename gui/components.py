from tkinter import *
import tkinter.font as tkFont

class DComponent:
    def __init__(self, root, name, x_position, y_position, width, height, pad_x, pad_y, fontsize):
        self.root = root
        self.name = name
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.pad_x = pad_x
        self.pad_y = pad_y
        if fontsize != None: self.font = tkFont.Font(family="Times New Roman", size=fontsize)

class DPlaceHolder(DComponent):
    def __init__(self, root, x_position, y_position):
        super().__init__(root, None, x_position, y_position, 1, 1, 0, 0, None)
        self.component = Label(root)

class DLabel(DComponent):
    def __init__(self, name, root, text, x_position, y_position, width, height, pad_x, pad_y, fontsize):
        super().__init__(root, name, x_position, y_position, width, height, pad_x, pad_y, fontsize)
        self.component = Label(root, text=text, font=self.font, justify=LEFT)

class DCanvas(DComponent):
    def __init__(self, name, root, width, height):
        super().__init__(root, name, 0, 0, width, height, 0, 0, None)
        self.component = Canvas(root, width=width, height=height)

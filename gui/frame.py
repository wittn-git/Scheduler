import tkinter 
from gui.components import DLabel, DCanvas, DPlaceHolder, DEntry, DButton
from tkinter import DISABLED, NORMAL

class DFrame:
    def __init__(self, title):
        self.root = tkinter.Tk()
        self.set_window(title)
        self.elements = self.get_elements(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
    
    def set_window(self, title):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.wm_title(title)
        self.root.geometry('%dx%d+0+0' % (w, h))

    def get_elements(self, w, h):
        elements = []

        #add placeholderrs
        for i in range(0, 50):
            #elements.append(DPlaceHolder(self.root, i, 0))
            #elements.append(DPlaceHolder(self.root, 0, i))
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)
    
        #add title and canvas
        #elements.append(DCanvas('canvas', self.root, w, h))
        elements.append(DLabel('title', self.root, 0, 0, 1, 1, 20, 20, 40, 'Scheduler'))

        #add task edit
        column, row = 40, 10
        
        fields = ['ID', 'Task', 'Day', 'From', 'To', 'Color']
        elements.append(DLabel('task_label', self.root, column, row-1, 1, 1, 0, 0, 28, 'Task'))
        for index, field in enumerate(fields):
            elements.append(DLabel('{}_label'.format(field.lower()), self.root, column, row+2*index, 1, 1, 0, 0, 22, field))
            elements.append(DEntry('{}_text'.format(field.lower()), self.root, column+1, row+2*index, 1, 1, 22, DISABLED if field == 'ID' else NORMAL))
        elements.append(DButton('add_button', self.root, column, row+1+len(fields)*2, 2,1, 22, 'Add', None, 'snwe'))
        elements.append(DButton('remove_button', self.root, column, row+3+len(fields)*2, 2,1, 22, 'Remove', None, 'snwe'))
        return elements
    
    def add_component(self, element):
        element.component.grid(column=element.x_position, 
                                row=element.y_position, 
                                columnspan=element.width,
                                rowspan=element.height,
                                padx=element.pad_x,
                                pady=element.pad_y,
                                sticky=element.stick)
        
    def show(self):
        for element in self.elements:
            self.add_component(element)
        self.root.mainloop()
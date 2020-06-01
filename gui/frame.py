import tkinter 
from gui.components import DLabel, DCanvas, DPlaceHolder

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
        for i in range(0, 15):
            elements.append(DPlaceHolder(self.root, i, 0))
            elements.append(DPlaceHolder(self.root, 0, i))
            self.root.grid_columnconfigure(i, weight=5)
            self.root.grid_rowconfigure(i, weight=2)

        #add title and canvas
        #elements.append(DCanvas('canvas', self.root, w, h))
        elements.append(DLabel('title', self.root, 'Scheduler', 0, 0, 1, 1, 20, 20, 40))

        #add task edit
        elements.append(DLabel('task_label', self.root, 'Task', 11, 1, 1, 1, 0, 0, 28))
        fields = ['ID', 'Task', 'Day', 'From', 'To', 'Color']
        for index, field in enumerate(fields):
            elements.append(DLabel('{}_label'.format(field.lower()), self.root, field, 11, 2+index, 1, 1, 0, 0, 22))

        return elements
    
    def add_component(self, element):
        element.component.grid(column=element.x_position, 
                                row=element.y_position, 
                                columnspan=element.width,
                                rowspan=element.height,
                                padx=element.pad_x,
                                pady=element.pad_y,
                                sticky='w')
        
    def show(self):
        for element in self.elements:
            self.add_component(element)
        self.root.mainloop()
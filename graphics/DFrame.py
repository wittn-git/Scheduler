import tkinter
from util.Objects import Schedule, Task
from graphics.Elements import *
from graphics.DCanvas import DCanvas
from util.Command_Handler import Command_Handler

class DFrame:
    
    def __init__(self, title):
        #set basic window
        self.root = self.create_window(title)
        #set empty schedule as schedule
        self.schedule = Schedule(self)
        #add the elements to the window
        self.elements = self.create_elements()

        self.schedule.add_task(Task('Test', 'Tuesday', 7, 14, 'Red'))
    
    def create_window(self, title):
        root = tkinter.Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.wm_title(title)
        root.geometry('%dx%d+0+0' % (w, h))
        return root

    def create_elements(self):
        for i in range(0, 50):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

        elements = {}

        #add title
        elements['title_label'] = DLabel(self.root, (5, 1, 1, 1), 44, 'Scheduler')

        #add file edit
        column, row = 5, 3
        elements['name_label'] = DLabel(self.root, (column, row-1, 1, 1), 22, 'Name')
        elements['name_text'] = DEntry(self.root, (column, row, 1, 1), 22)
        labels = ['Convert', 'Save', 'New', 'Open']
        command = [
                lambda: self.execute_command(2),
                lambda: self.execute_command(3),
                lambda: self.execute_command(4),
                lambda: self.execute_command(5)
            ]
        for index, label in enumerate(labels):
            elements['{}_button'.format(label.lower())] = DButton(self.root, (column+2*(index+1), row, 1, 1), 22, label, command[index], 'we')

        #add task edit
        column, row = 40, 15
        labels = ['Task', 'Day', 'From', 'To', 'Color']
        options =[None,
                    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
                    None,
                    None,
                    ('Blue', 'Red', 'Green')
                ]  
        for index, label in enumerate(labels):
            elements['{}_label'.format(label.lower())] = DLabel(self.root, (column, row+2*index, 1, 1), 22, label)
            if label == 'Color' or label == 'Day':
                elements['{}_combobox'.format(label.lower())] = DCombobox(self.root, (column+1, row+2*index, 1, 1), 22, options[index])
            else:
                elements['{}_text'.format(label.lower())] = DEntry(self.root, (column+1, row+2*index, 1, 1), 22)
        elements['add_button'] = DButton(self.root, (column, row+3+len(labels)*2, 2, 1), 22, 'Add', lambda: self.execute_command(0), 'snwe')
        elements['remove_button'] = DButton(self.root, (column, row+5+len(labels)*2, 2, 1), 22, 'Remove', lambda: self.execute_command(1), 'snwe')

        #add canvas
        elements['canvas'] = DCanvas(self.root)
        
        return elements

    def show(self):
        for key, element in self.elements.items():
            element.component.grid(column=element.x,
                                row=element.y, 
                                columnspan=element.w,
                                rowspan=element.h,
                                sticky=element.stick
                            )
            if key != 'canvas': element.component.lift()

        self.elements['canvas'].set_properties(self.elements)
        self.elements['canvas'].draw_schedule(self.schedule)
        self.root.mainloop()
    
    def execute_command(self, id, **kwargs):
        task = kwargs.get('task', None)
        self.schedule = Command_Handler().execute_command(id, self.elements, self.schedule, task)
        self.schedule.draw(self.elements['canvas'])
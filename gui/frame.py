import tkinter 
from gui.components import DLabel, DPlaceHolder, DEntry, DButton, DCombobox
from gui.dcanvas import DCanvas
from tkinter import DISABLED, NORMAL, filedialog
import util.schedule as sdl
from util.schedule import Schedule

class DFrame:
    def __init__(self, title):
        self.root = tkinter.Tk()
        self.get_elements(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.schedule = Schedule(None)
        self.schedule_name = None
    
    def set_window(self, title):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.wm_title(title)
        self.root.geometry('%dx%d+0+0' % (w, h))

    def get_elements(self, w, h):
        self.elements = []

        #add placeholders
        for i in range(0, 50):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)
        self.elements.append(DPlaceHolder(self.root, 0, 0))

        #add title and canvas
        self.elements.append(DLabel('title', self.root, 1, 0, 1, 1, 20, 20, 40, 'Scheduler'))
        self.canvas = DCanvas('canvas', self.root, w, h)
        self.elements.append(self.canvas)

        #add file edit
        column, row = 1, 2
        self.elements.append(DLabel('name_label', self.root, column, row-1, 1, 1, 0, 0, 22, 'Name'))
        self.elements.append(DEntry('name_text', self.root, column, row, 1, 1, 22, NORMAL))
        fields = ['Convert', 'Save', 'Delete', 'New', 'Open']
        commands = [lambda: sdl.convert_schedule(self.schedule),
                    lambda: sdl.save_schedule(self.schedule),
                    lambda: sdl.delete_schedule(self.schedule, self.schedule_name),
                    lambda: self.clear_frame(),
                    lambda: sdl.open_schedule(filedialog.askopenfilename(initialdir = 'data',title = "Select schedule",filetypes = (("json files","*.json"),)))]
        for index, field in enumerate(fields):
            self.elements.append(DButton(field.lower(), self.root, column+2*(index+1), row, 1, 1, 22, field, commands[index], 'we'))

        #add task edit
        column, row = 40, 10
        fields = ['ID', 'Task', 'Day', 'From', 'To', 'Color']
        options =[None, 
                    None,
                    ('Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'),
                    None,
                    None,
                    ('Blue', 'Red', 'Green')]   
        self.elements.append(DLabel('task_label', self.root, column, row-1, 1, 1, 0, 0, 28, 'Task'))
        for index, field in enumerate(fields):
            self.elements.append(DLabel('{}_label'.format(field.lower()), self.root, column, row+2*index, 1, 1, 0, 0, 22, field))
            if index == 2 or index == 5:
                self.elements.append(DCombobox('{}_text'.format(field.lower()), self.root, column+1, row+2*index, 1, 1, 22, 'readonly', options[index]))
            else:
                self.elements.append(DEntry('{}_text'.format(field.lower()), self.root, column+1, row+2*index, 1, 1, 22, 'readonly' if field == 'ID' else NORMAL))
        self.elements.append(DButton('add_button', self.root, column, row+3+len(fields)*2, 2,1, 22, 'Add', self.add_task, 'snwe'))
        self.elements.append(DButton('remove_button', self.root, column, row+5+len(fields)*2, 2,1, 22, 'Remove', None, 'snwe'))
        
    def add_task(self):
        task = self.schedule.add_task(
            self.get_element('day_text').get_text(),
            self.get_element('name_text').get_text(),
            self.get_element('from_text').get_text(),
            self.get_element('to_text').get_text(),
            self.get_element('color_text').get_text(),
        )
        self.canvas.add_task(task, self.get_element('day_text').get_text())

    def add_component(self, element):
        element.component.grid(column=element.x_position, 
                                row=element.y_position, 
                                columnspan=element.width,
                                rowspan=element.height,
                                padx=element.pad_x,
                                pady=element.pad_y,
                                sticky=element.stick
                            )
        if type(element) != DCanvas: element.component.lift()
        
    def clear_frame(self):
        for element in self.elements:
            element.clear()

    def show(self):
        for element in self.elements:
            self.add_component(element)
        self.canvas.set_properties((self.get_canvas_properties()))
        self.canvas.draw_baselines()
        self.canvas.draw_schedule(self.schedule)
        self.root.mainloop()
    
    def get_element(self, name):
        for element in self.elements:
            if element.name == name:
                return element
        return None
    
    def get_canvas_properties(self):
        padding = 35
        properties = [padding]
        
        name_text = self.get_element('name_text').component
        name_text.update()
        properties.append(name_text.winfo_rooty()+padding)
        
        task_label = self.get_element('task_label').component
        task_label.update()
        properties.append(task_label.winfo_rootx()-padding-properties[0])

        properties.append(self.root.winfo_screenheight()-properties[1]-padding*3)

        return properties
from graphics.DElements import DElement
from tkinter import Canvas

class DCanvas(DElement):
    
    def __init__(self, root):
        super().__init__(root, (0, 0, 50, 50), None)
        self.component = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        
    def set_properties(self, elements):
        padding = 25

        elements['name_text'].component.update()
        elements['task_label'].component.update()

        base_x = padding
        base_y = elements['name_text'].component.winfo_rooty()+padding

        self.w = elements['task_label'].component.winfo_rootx()-padding-base_x
        self.h = self.root.winfo_screenheight()-base_y-padding*3

        self.canvas = Canvas(self.component)
        self.canvas.place(x=base_x, y=base_y, width=self.w, height=self.h)

    def draw_schedule(self, schedule):
        self.canvas.delete('all')
        schedule.draw(self)
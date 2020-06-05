from graphics.DElements import DElement
from tkinter import Canvas

class DCanvas(DElement):
    
    def __init__(self, root):
        super().__init__(root, (0, 0, 50, 50), None)
        self.component = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        
    def set_properties(self, elements):
        padding = 35

        elements['name_text'].component.update()
        elements['task_label'].component.update()

        self.base_x = padding
        self.base_y = elements['name_text'].component.winfo_rooty()+padding
        self.max_w = elements['task_label'].component.winfo_rootx()-padding-self.base_x
        self.max_h = self.root.winfo_screenheight()-self.base_y-padding*3

    def point(self, x, y):
        return (self.base_x+x, self.base_y+y)

    def draw_schedule(self, schedule):
        self.component.delete('all')
        schedule.draw(self)
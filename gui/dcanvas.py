from gui.components import DComponent
from tkinter import *
from util.schedule import Schedule, Task
import tkinter.font as tkFont

class DCanvas(DComponent):
    def __init__(self, name, root, width, height):
        super().__init__(name, root, 0, 0, width, height, None)
        self.component = Canvas(root, width=width, height=height)

    def set_properties(self, properties):
        self.base_x = properties[0]
        self.base_y = properties[1]
        self.max_w = properties[2]
        self.max_h = properties[3]

    def point(self, x, y):
        return (self.base_x+x, self.base_y+y)

    def draw_schedule(self, schedule):
        self.task_objects = []
        for index, field in enumerate(schedule.days):
            for task in field:
                self.task_objects.append(Task_Object(Task(task, index), self))
        for task_object in self.task_objects:
            self.draw_task(task_object)

    def draw_baselines(self):
        self.component.create_rectangle(
            self.point(0, 0),
            self.point(self.max_w, self.max_h)
        )
        headlines = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        max = 8
        for i in range(max):
            self.component.create_text(self.point(i*self.max_w/max+5, 5), text=headlines[i], anchor='nw', font = tkFont.Font(family="Times New Roman", size=16))
            self.component.create_line(self.point(i*self.max_w/max, 0), self.point(i*self.max_w/max, self.max_h), width=3 if i==1 else 1)
        times = ['', '']
        for i in range(25):
            times.append('{}.00'.format(i))
        max = 27
        for i in range(max):
            self.component.create_text(self.point(5, i*self.max_h/max+2), text=times[i], anchor='nw', font = tkFont.Font(family="Times New Roman", size=8))
            if i != 1: self.component.create_line(self.point(0, i*self.max_h/max), self.point(self.max_w, i*self.max_h/max), width=3 if i==2 else 1)

    def add_task(self, task, day):
        task_object = Task_Object(Task(task, day), self)
        self.task_objects.append(task_object)
        self.draw_task(task_object)
    
    def draw_task(self, task_object):
        task_object.show()

    def remove_task(self, x, y):
        task_object = None #get task object from position
        task_object.remove()
        self.task_objects.remove(task_object)
        return task_object.task

    def clear(self):
        self.component.delete('all')

class Task_Object():
    def __init__(self, task, canvas):
        indexes = self.get_indexes(task.time_from, task.time_to)
        self.x = canvas.max_w/8 +canvas.max_w/8*task.day
        self.y = canvas.max_h/27*2 + canvas.max_h/27*indexes[0]
        self.w = canvas.max_w/8 
        self.h = canvas.max_h/27*(indexes[1]-indexes[0])
       
        self.task = task
        self.canvas = canvas
    
    def get_indexes(self, time_from, time_to):
        index_from, index_to = None, None

        for i in range(25):
            if '{}.00'.format(i) == time_from: index_from = i
            if '{}.00'.format(i) == time_to: index_to = i
            print('{}.00'.format(i), time_from)
        return (index_from, index_to)

    def show(self):
        self.object = self.canvas.component.create_rectangle(
            self.canvas.point(self.x, self.y),
            self.canvas.point(self.w, self.h), 
            fill='black'
        )

    def remove(self):
        self.canvas.component.remove(self.object)
    
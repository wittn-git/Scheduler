import tkinter.font as tkFont

day_list = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Schedule:
    def __init__(self, frame):
        self.days = {}
        for day in day_list:
            if day != '': self.days[day] = Day(day)
        self.frame = frame
    
    def add_task(self, task):
        self.days[task.day].add_task(task)
    
    def remove_task(self, task, canvas):
        self.days[task.day].remove_task(task, canvas)
    
    def draw(self, canvas):
        canvas.canvas.create_rectangle(1, 1, canvas.w-2, canvas.h-2)
        canvas.canvas.create_text((5, 5), text='Time', anchor='nw', font = tkFont.Font(family="Times New Roman", size=int((canvas.h/13)*0.6)))
        canvas.canvas.create_line((canvas.w/8+1, 0), (canvas.w/8+1, canvas.h), width=3)
        for i in range(1, 27):
            if i > 1 and i < 26: canvas.canvas.create_text((5, i*canvas.h/26+2), text='{}.00'.format(i-2), anchor='nw', font = tkFont.Font(family="Times New Roman", size=int((canvas.h/26)*0.575)))
            if i != 1: canvas.canvas.create_line((0, i*canvas.h/26), (canvas.w, i*canvas.h/26), width=3 if i==2 else 1)

        for key, day in self.days.items():
            day.draw(canvas, self.frame)

class Day:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.index = day_list.index(name)

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task, canvas):
        task.remove_task(canvas)
        self.tasks.remove(task)
    
    def draw(self, canvas, frame):
        canvas.canvas.create_text((canvas.w/8*self.index+5, 5), text=self.name, anchor='nw', font = tkFont.Font(family="Times New Roman", size=int((canvas.w/8)*0.16)))
        canvas.canvas.create_line((canvas.w/8*(self.index+1), 0), (canvas.w/8*(self.index+1), canvas.h), width=1)
        for task in self.tasks:
            task.draw(canvas, frame)

class Task:
    def __init__(self, name, day, time_from, time_to, color):
        self.name = name
        self.day = day
        self.time_from = time_from
        self.time_to = time_to
        self.color = color
        self.day_index = day_list.index(day)
        self.id = '{}-{}-{}-{}-{}'.format(name, day, time_from, time_to, color)
    
    def draw(self, canvas, frame):
        
        self.image = canvas.canvas.create_rectangle(
            canvas.w/8*(self.day_index)+1, canvas.h/26*(self.time_from+2),
            canvas.w/8*(self.day_index+1), canvas.h/26*(self.time_to+2),
            fill = self.color,
            tag = self.id
        )
        self.text = canvas.canvas.create_text(
            (canvas.w/8*(self.day_index)+5, canvas.h/26*(self.time_from+2)),
            anchor = 'nw',
            text = self.name,
            font = tkFont.Font(family="Times New Roman", size=int((canvas.h/26)*0.8))
        )
        canvas.canvas.tag_bind(self.id, '<Button-1>', lambda x: frame.execute_command(7, task=self))

    def remove_task(self, canvas):
        canvas.canvas.delete(self.image)
        canvas.canvas.delete(self.text)

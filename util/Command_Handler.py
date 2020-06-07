from util.Objects import Task, Schedule
import util.Morpher as Morpher
import sys
import os
from pathlib import Path
from tkinter import filedialog
from PIL import Image
import io
import cv2
import imutils

path = ''
if sys.platform.startswith('linux'): path = '{}/Documents/Scheduler/{}'.format(str(Path.home()), '{}/{}')
elif sys.platform.startswith('win'): path = '{}//Scheduler//{}'.format(str(Path.home()), '{}//{}')

class Command_Handler():

    def execute_command(self, id, frame, schedule, task):

        self.frame = frame
        self.elements = frame.elements
        self.schedule = schedule
        self.task = task

        commands = {
            0: self.add_task,
            1: self.remove_task,
            2: self.convert_schedule,
            3: self.save_schedule,
            4: self.new_schedule,
            5: self.open_schedule,
            6: self.delete_schedule,
            7: self.edit_task
        }

        return commands.get(id)()
    
    def add_task(self):
        try:
            task_name = self.elements['task_text'].get_text()
            day = self.elements['day_combobox'].get_text()
            time_from = int(self.elements['from_text'].get_text())
            time_to = int(self.elements['to_text'].get_text())
            color = self.elements['color_combobox'].get_text()

            for name, element in self.elements.items():
                if name != 'name_text': element.clear()
            task = Task(task_name, day, time_from, time_to, color)
            self.schedule.add_task(task)
        except:
            pass
        return self.schedule

    def remove_task(self):
        for name, element in self.elements.items():
            if name != 'name_text': element.clear()
        return self.schedule

    def convert_schedule(self):
        name = self.elements['name_text'].get_text()
        canvas = self.elements['canvas']

        canvas.canvas.postscript(file='data.ps', colormode='color')
        img = Image.open('data.ps')
        img.save('data.png', quality = 200)
        
        img = cv2.imread('data.png')
        img = imutils.rotate_bound(img, 90)
        cv2.imwrite('data.png', img)

        img = Image.open('data.png')
        img = img.convert('RGB')
        img.save(path.format('Schedules', name+'.pdf'))

        #os.remove('data.ps')
        #os.remove('data.jpg')
        return self.schedule
    
    def save_schedule(self):
        name = self.elements['name_text'].get_text()
        json_object = Morpher.schedule_to_json(self.schedule)
        schedule_file = open(path.format('data', name+'.json'), 'w')
        schedule_file.write(json_object)
        return self.schedule

    def new_schedule(self):
        for name, element in self.elements.items():
            element.clear()
        return Schedule(self.frame)

    def open_schedule(self):
        schedule_file = open(filedialog.askopenfilename(initialdir = path.format('data', ''),title = "Select schedule",filetypes = (("json files","*.json"),)))
        self.elements['name_text'].set_text(os.path.basename(schedule_file.name).replace('.json', ''))
        return Morpher.json_to_schedule(schedule_file, self.frame)
    
    def delete_schedule(self):
        name = self.elements['name_text'].get_text()
        try:
            os.remove(path.format('data', name+'.json'))
        except:
            pass
        return self.new_schedule()

    def edit_task(self):
        self.schedule.remove_task(self.task, self.elements['canvas'])

        self.elements['task_text'].set_text(self.task.name)
        self.elements['day_combobox'].set_text(self.task.day)
        self.elements['from_text'].set_text(self.task.time_from)
        self.elements['to_text'].set_text(self.task.time_to)
        self.elements['color_combobox'].set_text(self.task.color)

        return self.schedule
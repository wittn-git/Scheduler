import json
from util.messagebox import MessageDialog
import os

def get_json(path):
    file = open(path)
    file_content = file.read()
    return json.loads(file_content)

class Schedule:
    def __init__(self, path):
        if(path != None):
            self.days = get_json(path)
        else: self.days = {}
    
    def to_task(self, name, time_from, time_to, color):
        task = {
            'name': name,
            'time_from': time_from,
            'time_to': time_to,
            'color': color
        }
        return task

    def add_task(self, day, name, time_from, time_to, color):
        if day not in self.days: self.days[day] = []
        task = self.to_task(name, time_from, time_to, color)
        if task not in self.days[day]:
            self.days[day].append(task)
            MessageDialog().show_message('Task added.')
            return task
        else: 
            MessageDialog().show_message('Task already exists.')
        
def open_schedule(path):
    return Schedule(path)

def save_schedule(schedule, name):
    data = json.dumps(schedule.days, indent=2)
    file = open('../data/{}.json'.format(name), 'w')
    file.write(data)
    MessageDialog().show_message('Schedule saved.')

def delete_schedule(schedule, name):
    if MessageDialog().ask_message('Do you really want to delete this schedule?'):
        os.remove('../data/{}.json'.format(name))
        return Schedule(None)
    else: return schedule

def convert_schedule(schedule, name):
    pass
    #coming soon

class Task:

    def __init__(self, task, day):
        self.name = task['name']
        self.time_from = task['time_from']
        self.time_to = task['time_to']
        self.color = task['color']
        self.day = ('Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag').index(day)

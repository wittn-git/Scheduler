import json
from util.Objects import Task, Day, Schedule

def schedule_to_json(schedule):
    schedule_json = {}
    for name, day in schedule.days.items():
        schedule_json[name] = day_to_json(day)
    
    return json.dumps(schedule_json, indent=2)

def day_to_json(day):
    tasks_json = []
    for task in day.tasks:
        tasks_json.append(task_to_json(task))
    return tasks_json

def task_to_json(task):
    task_json = {
        'name': task.name,
        'day': task.day,
        'time_from': task.time_from,
        'time_to': task.time_to,
        'color': task.color
    }
    return task_json

def json_to_schedule(schedule_file, frame):
    object_json = json.loads(schedule_file.read())
    schedule = Schedule(frame)
    for name, day_json in object_json.items():
        for task_json in day_json:
            task = Task(
                task_json['name'],
                task_json['day'],
                task_json['time_from'],
                task_json['time_to'],
                task_json['color'])
            schedule.add_task(task)
    return schedule
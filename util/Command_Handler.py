from util.Objects import Task

class Command_Handler():

    def execute_command(self, id, elements, schedule, task):

        self.elements = elements
        self.schedule = schedule
        self.task = task

        commands = {
            0: self.add_task,
            1: self.remove_task,
            2: self.convert_schedule,
            3: self.save_schedule,
            4: self.new_schedule,
            5: self.open_schedule,
            6: self.edit_task
        }

        print(elements)
        return commands.get(id)()
    
    def add_task(self):
        name = self.elements['task_text'].get_text()
        day = self.elements['day_combobox'].get_text()
        time_from = int(self.elements['from_text'].get_text())
        time_to = int(self.elements['to_text'].get_text())
        color = self.elements['color_combobox'].get_text

        task = Task(name, day, time_from, time_to, color)
        self.schedule.add_task(task)
        return self.schedule

    def remove_task(self):
        for name, element in self.elements.items():
            if name != 'name_text': element.clear()
        return self.schedule

    def convert_schedule(self):
        pass

    def save_schedule(self):
        pass

    def new_schedule(self):
        pass

    def open_schedule(self):
        pass

    def edit_task(self):
        pass
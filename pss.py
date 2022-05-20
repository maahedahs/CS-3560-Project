from schedule import Schedule
from task import Task
import json

# PSS Class

class PSS:
    
    def __init__(self):
        schedule = Schedule()
        self.recurring_types = ['Class', 'Study', 'Sleep', 'Exercise', 'Work', 'Meal']
        self.transient_types = ['Visit', 'Shopping', 'Appointment']
        self.anti_types = ['Cancellation']

    def get_task(self):
        return schedule.list_of_tasks

    def add_task(self, task):
       schedule.add_task_to_schedule(task)
       print(schedule.list_of_tasks)
        
    def find_task(self,task_name):
        for task in schedule.list_of_tasks:
          if task.name.upper() == task_name.strip().upper():
                #print("Found")
                return task

    def remove_task(self, task):
        if (task in schedule.list_of_tasks):
            schedule.list_of_tasks.remove(task)
        #print(self._list_tasks)
        print("Task removed!")
    

    def edit_task(self, old_task, new_task):
        self.remove_task(old_task)
        self.add_task(new_task)

    def write_schedule_to_file(self, file):
        f = open(file, "w")
        for x in schedule.list_of_tasks:
            f.write(x)
        f.close()

    def read_schedule_from_file(self, file_name):
        file = open(file_name)
        file_data = json.load(file)
        for task in file_data:
            name = task['Name']
            type = task['Type']
            if type in self.recurring_types:
                start_date = task['StartDate']
                start_time = task['StartTime']
                duration = task['Duration']
                end_date = task['EndDate']
                frequency = task['Frequency']
                new_task = RecurringTask(name, type, start_date, start_time, duration, end_date, frequency)
            elif type in self.anti_types:
                start_date = task['Date']
                start_time = task['StartTime']
                duration = task['Duration']
                new_task = AntiTask(name, type, start_date, start_time, duration)
            elif type in self.transient_types:
                start_date = task['Date']
                start_time = task['StartTime']
                duration = task['Duration']
                new_task = TransientTask(name, type, start_date, start_time, duration)
            self.add_task(new_task)

    def view_one_day_schedule(self):
        pass

    def view_one_week_schedule(self):
        pass

    def view_one_month_schedule(self):
        pass

    

from schedule import Schedule
from task import Task
from task import RecurringTask
from task import AntiTask
from task import TransientTask
import json

# PSS Class

class PSS:
    
    def __init__(self):
        self.schedule = Schedule()
        self.recurring_types = ['Class', 'Study', 'Sleep', 'Exercise', 'Work', 'Meal']
        self.transient_types = ['Visit', 'Shopping', 'Appointment']
        self.anti_types = ['Cancellation']

    def get_task(self):
        return self.schedule.list_of_tasks

    def add_task(self, task):
        if isinstance(task, RecurringTask) and task.type not in self.recurring_types:
            print("Invalid type. Task not added.")
            return
        elif isinstance(task, AntiTask) and task.type not in self.anti_types:
            print("Invalid type. Task not added.")
            return
        elif isinstance(task, TransientTask) and task.type not in self.transient_types:
            print("Invalid type. Task not added.")
            return   
    self.schedule.add_task_to_schedule(task)
        
    def find_task(self,task_name):
        for task in self.schedule.list_of_tasks:
          if task.name.upper() == task_name.strip().upper():
                #print("Found")
                return task

    def remove_task(self, task):
        if (task in self.schedule.list_of_tasks):
            self.schedule.list_of_tasks.remove(task)
            print("Task removed!")
        #print(self._list_tasks)
            
    def view_task(self, task_name):
        for task in self.schedule.list_of_tasks:
            if task.name == task_name:
                task.view_task()
    
    def view_list_of_tasks(self, list_of_tasks):
        for task in list_of_tasks:
            task.view_task()

    def edit_task(self, old_task, new_task):
        self.remove_task(old_task)
        self.add_task(new_task)

    def write_schedule_to_file(self, file_name):
        file = open(file_name, 'w')
        json_list = []
        for task in self.schedule.list_of_tasks:
            json_dict = {}
            json_dict['Name'] = task.name
            json_dict['Type'] = task.type
            if isinstance(task, RecurringTask):
                json_dict['StartDate'] = task.start_date
                json_dict['StartTime'] = task.start_time
                json_dict['Duration'] = task.duration
                json_dict['EndDate'] = task.end_date
                json_dict['Frequency'] = task.frequency
            else:
                json_dict['Date'] = task.start_date
                json_dict['StartTime'] = task.start_time
                json_dict['Duration'] = task.duration
            json_list.append(json_dict)
        json.dump(json_list, file, indent=4)

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

    def view_one_day_schedule(self, start_date):
        one_day_schedule = []
        for task in self.schedule.list_of_tasks:
            if isinstance(task, RecurringTask):
                list_of_recurring_dates = self.schedule.get_list_of_recurring_dates(task)
                if task.start_date in list_of_recurring_dates:
                    one_day_schedule.append(task)
            if (start_date == task.start_date) and not isinstance(task, AntiTask):
                one_day_schedule.append(task)
        self.view_list_of_tasks(one_day_schedule)

    def view_one_week_schedule(self, start_date, end_date):
        one_week_schedule = []
        for task in self.schedule.list_of_tasks:
            if isinstance(task, RecurringTask):
                list_of_recurring_dates = self.schedule.get_list_of_recurring_dates(task)
                if task.start_date in list_of_recurring_dates:
                    one_week_schedule.append(task)
            if (start_date == task.start_date) and not isinstance(task, AntiTask):
                one_week_schedule.append(task)
        self.view_list_of_tasks(one_week_schedule)

    def view_one_month_schedule(self, start_date, end_date):
        one_month_schedule = []
        for task in self.schedule.list_of_tasks:
            if isinstance(task, RecurringTask):
                list_of_recurring_dates = self.schedule.get_list_of_recurring_dates(task)
                if task.start_date in list_of_recurring_dates:
                    one_month_schedule.append(task)
            if (start_date == task.start_date) and not isinstance(task, AntiTask):
                one_month_schedule.append(task)
        self.view_list_of_tasks(one_month_schedule)

    

from schedule import Schedule
from task import Task

# PSS Class

class PSS:
    
    def __init__(self):
        #self._list_tasks = []
        schedule = Schedule()

    def get_task(self):
        return schedule.list_of_tasks

    def add_task(self, task):
       #self._list_tasks.append(task)
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
    

    def edit_task(self, task):
        pass

    def write_schedule_to_file(self, file):
        f = open(file, "w")
        for x in schedule.list_of_tasks:
            f.write(x)
        f.close()

    def read_schedule_from_file(self, file):
        f = open(file, "r")
        for x in f:
            add_task(x)
            print(x)
        f.close()

    def view_one_day_schedule(self):
        pass

    def view_one_week_schedule(self):
        pass

    def view_one_month_schedule(self):
        pass

    

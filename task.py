
# Task Class

class Task:

    def __init__(self, name, type, start_date, start_time, duration):
        self.name = name
        self.type = type
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration

    def view_task(self):
        print("\nTask Name: ", self.name, "\nTask Type: ", self.type, "\nStart date: ",self.start_date, 
        "\nStart time: ", self.start_time, "\nDuration: ", self.duration)

class RecurringTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration, end_date, frequency):
        super().__init__(name, type, start_date, start_time, duration)
        self.end_date = end_date
        self.frequency = frequency
        self.list_of_anti_tasks = []

    # Inherited from the Task superclass and also prints end date and frequency
    def view_task(self):
        super().view_task()
        print("End date: ", self.end_date,  "\nFrequency: ", self.frequency)

class TransientTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration):
        super().__init__(name, type, start_date, start_time, duration)
       
class AntiTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration):
        super().__init__(name, type, start_date, start_time, duration)
        

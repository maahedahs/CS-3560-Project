
# Task Class

class Task:

    def __init__(self, name, type, start_date, start_time, duration):
        self.name = name
        self.type = type
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration

class RecurringTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration, end_date, frequency):
        super().__init__(name, type, start_date, start_time, duration, end_date, frequency)

class TransientTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration):
        super().__init__(name, type, start_date, start_time, duration)
       
class AntiTask(Task):
    
    def __init__(self, name, type, start_date, start_time, duration):
        super().__init__(name, type, start_date, start_time, duration)
        
    # I think cancel_recurring method can be implemented in remove task method in pss class, something like
    # when the remove task method gets called, the method checks if the task is recurring, transient, or anti task
    # and removes task accordingly
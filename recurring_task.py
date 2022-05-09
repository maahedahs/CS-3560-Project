
# Recurring Task Class

from task import Task

class RecurringTask(Task):

    def __init__(self, name, type, date, start_time, duration, frequency):
        self.name = name
        self.type = type
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.frequency = frequency

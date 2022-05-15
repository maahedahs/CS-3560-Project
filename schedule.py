
# Schedule Class

class Schedule:

    def __init__(self):
        self.list_of_tasks = []

    def __init__(self, list_of_tasks):
        self.list_of_tasks = []
        for i in list_of_tasks:
            unique_name = self.check_task_name(i.name)
            valid_date = self.check_valid_date(i.date)
            task_overlap = self.check_for_overlapping_tasks(i)
            if unique_name == True and valid_date == True and task_overlap == True:
                self.list_of_tasks.append(i)
            else:
                print("Error: Task not added to schedule", i.name)

    def check_for_overlapping_tasks(self, task):
        start_time = task.start_time
        end_time = start_time + task.duration
        anti_task = isinstance(task, AntiTask)

        # check that an anti task overlaps with a recurring task
        if anti_task == True:
            for i in self.list_of_tasks:
                if i.date != task.date:
                    continue
                check_start_time = i.start_time
                check_end_time = check_start_time + i.duration
                if start_time == check_start_time and end_time == check_end_time and isinstance(i, RecurringTask):
                    return True
            return False

        # check that recurring and transient tasks do not overlap with any other tasks
        else:
            for i in self.list_of_tasks:
                if i.date != task.date:
                    continue
                check_start_time = i.start_time
                check_end_time = check_start_time + i.duration
                # if task starts in the middle of another task
                if start_time < check_end_time and start_time > check_start_time:
                    return False
                # if task ends in the middle of another task
                elif end_time < check_end_time and end_time > check_start_time:
                    return False
                # if task starts and ends at the same time as another task
                elif end_time == check_end_time and start_time == check_start_time:
                    return False
            return True

    # returns True if name is a unique task name and False if not
    def check_task_name(self, name) -> bool:
        for i in self.list_of_tasks:
            if i.name == name:
                return False
        return True

    # returns True if date is valid and False if not
    def check_valid_date(self, date) -> bool:
        date = str(date)
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        if len(date) != 8:
            return False
        if day < 1:
            return False

        if month < 1 or month > 12:
            return False
        if month in months_31 and day > 31:
            return False
        elif month in months_30 and day > 30:
            return False
        else:
            if year % 4 == 0 and day > 29:
                return False
            elif day > 28:
                return False

        return True
